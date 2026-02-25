"use client";

import { useState } from "react";
import { useChat } from "@ai-sdk/react";
import ReactMarkdown from "react-markdown";

function getMessageContent(m: { content?: string; parts?: Array<{ type?: string; text?: string }> }): string {
  if (typeof m.content === "string") return m.content;
  if (Array.isArray(m.parts)) {
    const textPart = m.parts.find((p) => p.type === "text" || "text" in p);
    return textPart?.text ?? "";
  }
  return "";
}

const SUGGESTED_QUESTIONS = [
  "Como fazer o primeiro acesso ao Portal Nacional?",
  "O que é o erro E0831?",
  "Como funciona a retenção de PIS/COFINS/CSLL após a NT 007?",
  "Como migrar do emissor próprio para o nacional?",
  "Como cancelar uma NFS-e?",
];

export default function ChatPage() {
  const [input, setInput] = useState("");
  const { messages, sendMessage, status } = useChat({
    api: "/api/chat",
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const text = input.trim();
    if (text && status !== "streaming") {
      sendMessage({ text });
      setInput("");
    }
  };

  return (
    <div className="flex flex-col h-screen bg-slate-50">
      <header className="shrink-0 border-b border-slate-200 bg-white px-4 py-3">
        <h1 className="text-xl font-semibold text-slate-800">
          Assistente NFS-e
        </h1>
        <p className="text-sm text-slate-500">
          Especialista em Nota Fiscal de Serviços Eletrônica
        </p>
      </header>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <div className="max-w-2xl mx-auto pt-8">
            <p className="text-slate-600 text-center mb-6">
              Faça uma pergunta sobre NFS-e. Exemplos:
            </p>
            <div className="flex flex-wrap gap-2 justify-center">
              {SUGGESTED_QUESTIONS.map((q) => (
                <button
                  key={q}
                  type="button"
                  onClick={() => sendMessage({ text: q })}
                  disabled={status === "streaming"}
                  className="px-4 py-2 text-sm rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition-colors disabled:opacity-50"
                >
                  {q}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((m) => (
          <div
            key={m.id}
            className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[85%] rounded-2xl px-4 py-3 ${
                m.role === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-white border border-slate-200 text-slate-800 shadow-sm"
              }`}
            >
              {m.role === "user" ? (
                <p className="whitespace-pre-wrap">{getMessageContent(m)}</p>
              ) : (
                <div className="prose prose-slate prose-sm max-w-none">
                  <ReactMarkdown>{getMessageContent(m)}</ReactMarkdown>
                </div>
              )}
            </div>
          </div>
        ))}

        {status === "streaming" && (
          <div className="flex justify-start">
            <div className="px-4 py-2 rounded-full bg-slate-200 text-slate-500 text-sm animate-pulse">
              Digitando...
            </div>
          </div>
        )}
      </div>

      <form
        onSubmit={handleSubmit}
        className="shrink-0 border-t border-slate-200 bg-white p-4"
      >
        <div className="flex gap-2 max-w-3xl mx-auto">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Digite sua pergunta sobre NFS-e..."
            className="flex-1 px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={status === "streaming"}
          />
          <button
            type="submit"
            disabled={status === "streaming" || !input.trim()}
            className="px-6 py-3 rounded-xl bg-blue-600 text-white font-medium hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            Enviar
          </button>
        </div>
      </form>
    </div>
  );
}
