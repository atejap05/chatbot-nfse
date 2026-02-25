"""
Servidor FastAPI para o Chatbot RAG NFS-e.

Expõe a rota POST /api/chat que recebe mensagens e retorna stream de texto
compatível com o Vercel AI SDK (Text Stream Protocol).
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from backend.rag_engine import stream_generator

app = FastAPI(
    title="Chatbot NFS-e RAG API",
    description="API de chat especializada em Nota Fiscal de Serviços Eletrônica",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]


@app.get("/health")
async def health():
    """Verificação de saúde da API."""
    return {"status": "ok"}


@app.post("/api/chat")
async def chat(request: ChatRequest):
    """
    Processa a pergunta do usuário e retorna stream de resposta.

    O payload deve conter {"messages": [{"role": "user", "content": "..."}]}.
    Extrai a última mensagem do usuário para a consulta RAG.
    Retorna StreamingResponse com chunks de texto (Text Stream Protocol).
    """
    messages = request.messages
    if not messages:
        raise HTTPException(status_code=400, detail="Nenhuma mensagem enviada")

    # Extrair última mensagem do usuário
    user_messages = [m for m in messages if m.role == "user"]
    if not user_messages:
        raise HTTPException(status_code=400, detail="Nenhuma mensagem do usuário encontrada")

    user_query = user_messages[-1].content.strip()
    if not user_query:
        raise HTTPException(status_code=400, detail="Mensagem vazia")

    async def generate():
        async for chunk in stream_generator(user_query):
            yield chunk

    return StreamingResponse(
        generate(),
        media_type="text/plain; charset=utf-8",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
