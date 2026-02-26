/**
 * Proxy para o backend FastAPI.
 * Recebe requisições do useChat e repassa para o FastAPI.
 * Repassa stream de texto puro (streamProtocol: "text").
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

    if (!response.body) {
      return new Response("No stream", { status: 500 });
    }
    return new Response(response.body, {
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
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
