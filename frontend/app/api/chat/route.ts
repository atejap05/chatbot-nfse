/**
 * Proxy para o backend FastAPI.
 * Recebe requisições do useChat e repassa para o FastAPI.
 * Transforma o stream de texto puro no formato Data Stream Protocol do Vercel AI SDK.
 */

const BACKEND_URL = process.env.BACKEND_URL || "http://127.0.0.1:8000";

type MessageLike = { content?: string; parts?: Array<{ type?: string; text?: string }> };

function extractContent(msg: MessageLike): string {
  if (typeof msg.content === "string") return msg.content;
  if (Array.isArray(msg.parts)) {
    const textPart = msg.parts.find((p) => p.type === "text" || "text" in p);
    return textPart?.text ?? "";
  }
  return "";
}

function createId() {
  return `msg_${Date.now().toString(36)}_${Math.random().toString(36).slice(2)}`;
}

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const messages = body.messages ?? [];

    const formattedMessages = messages.map(
      (m: { role?: string; content?: string; parts?: Array<{ type?: string; text?: string }> }) => ({
        role: m.role || "user",
        content: extractContent(m),
      })
    );

    const response = await fetch(`${BACKEND_URL}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: formattedMessages }),
    });

    if (!response.ok) {
      const err = await response.text();
      return new Response(err, { status: response.status });
    }

    const reader = response.body?.getReader();
    if (!reader) {
      return new Response("No stream", { status: 500 });
    }

    const textId = createId();
    const encoder = new TextEncoder();

    const stream = new ReadableStream({
      async start(controller) {
        try {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: "start", messageId: textId })}\n\n`));
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: "text-start", id: textId })}\n\n`));

          const decoder = new TextDecoder();
          while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            const chunk = decoder.decode(value, { stream: true });
            if (chunk) {
              controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: "text-delta", id: textId, delta: chunk })}\n\n`));
            }
          }

          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: "text-end", id: textId })}\n\n`));
          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: "finish" })}\n\n`));
          controller.enqueue(encoder.encode("data: [DONE]\n\n"));
        } finally {
          controller.close();
        }
      },
    });

    return new Response(stream, {
      headers: {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
        "x-vercel-ai-ui-message-stream": "v1",
      },
    });
  } catch (error) {
    console.error("Proxy error:", error);
    return new Response(
      JSON.stringify({ error: "Erro ao conectar ao backend" }),
      { status: 500, headers: { "Content-Type": "application/json" } }
    );
  }
}
