"""
RAG Engine para o Chatbot NFS-e.

Utiliza LlamaIndex com:
- Anthropic Claude (configurável via ANTHROPIC_MODEL) para geração de respostas
- Qdrant como vector store (collection nfse_faq)
- HuggingFace embeddings (paraphrase-multilingual-MiniLM-L12-v2)
- Streaming no formato Vercel AI SDK (0:"texto"\n)
"""

import os
from typing import AsyncGenerator

from pathlib import Path

from dotenv import load_dotenv

# Carregar .env do diretório backend
_env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(_env_path)

# System prompt baseado nas instruções do agente (INSTRUCOES-COPILOT-STUDIO.md)
SYSTEM_PROMPT = """Você é um assistente especializado no Sistema Nacional de NFS-e (Nota Fiscal de Serviços Eletrônica).

Responda dúvidas de contribuintes, gestores municipais e desenvolvedores sobre:
- Emissão, cancelamento e substituição de NFS-e
- Parametrização do Painel Administrativo Municipal
- Cadastro Nacional Complementar (CNC) e primeiro acesso
- Integração via API com o ADN (Ambiente de Dados Nacional)
- Tributos: ISS, PIS, COFINS, CSLL, IBS e CBS (Reforma Tributária)

Sempre baseie suas respostas nas fontes de conhecimento disponíveis.
Se a dúvida envolver erro técnico específico (ex: E0831, E1282), cite o código e explique a causa.
Responda sempre em português do Brasil. Seja objetivo e técnico."""


def _get_query_engine():
    """Cria e retorna o QueryEngine configurado para RAG com streaming."""
    from llama_index.core import VectorStoreIndex, Settings, get_response_synthesizer
    from llama_index.core.query_engine import RetrieverQueryEngine
    from llama_index.core.retrievers import VectorIndexRetriever
    from llama_index.core.prompts import PromptTemplate
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.llms.anthropic import Anthropic
    from llama_index.vector_stores.qdrant import QdrantVectorStore
    from qdrant_client import QdrantClient

    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    if not anthropic_key:
        raise ValueError("ANTHROPIC_API_KEY não configurada no .env")

    model_name = os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
    llm = Anthropic(
        model=model_name,
        api_key=anthropic_key,
        temperature=0.1,
    )

    # Embeddings (mesmo modelo usado na ingestion)
    embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    )

    Settings.llm = llm
    Settings.embed_model = embed_model

    # Conectar ao Qdrant e carregar índice
    client = QdrantClient(url=qdrant_url)
    vector_store = QdrantVectorStore(
        client=client,
        collection_name="nfse_faq",
    )

    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)

    # Retriever com top-k
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=5,
    )

    # Prompt customizado com instruções do especialista NFS-e
    qa_prompt = PromptTemplate(
        f"{SYSTEM_PROMPT}\n\n"
        "Com base no contexto abaixo, responda à pergunta do usuário. "
        "Seja objetivo e cite códigos de erro quando relevante.\n\n"
        "Contexto:\n{context_str}\n\n"
        "Pergunta: {query_str}\n\n"
        "Resposta:"
    )

    response_synthesizer = get_response_synthesizer(
        streaming=True,
        text_qa_template=qa_prompt,
    )

    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer,
    )

    return query_engine


async def stream_generator(user_query: str) -> AsyncGenerator[str, None]:
    """
    Gera chunks de texto para streaming.

    Compatível com Text Stream Protocol do Vercel AI SDK:
    chunks de texto puro são concatenados no frontend.
    """
    query_engine = _get_query_engine()

    response = query_engine.query(user_query)

    if hasattr(response, "response_gen") and response.response_gen:
        for text in response.response_gen:
            yield text
    else:
        yield str(response)


def get_query_engine():
    """Retorna o query engine (para uso síncrono se necessário)."""
    return _get_query_engine()
