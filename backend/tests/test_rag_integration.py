"""
Testes de integração do RAG (requerem Qdrant rodando + API key Anthropic).

Rodar com: pytest backend/tests/test_rag_integration.py -v -s
Marcar como integração: esses testes são mais lentos e dependem de serviços externos.
"""

import os
import pytest

requires_services = pytest.mark.skipif(
    not os.getenv("ANTHROPIC_API_KEY"),
    reason="ANTHROPIC_API_KEY não configurada",
)


@requires_services
def test_rag_stream_produces_output(client):
    """Testa que o endpoint /api/chat retorna conteúdo com streaming real."""
    response = client.post(
        "/api/chat",
        json={"messages": [{"role": "user", "content": "Como cancelar uma NFS-e?"}]},
    )
    assert response.status_code == 200
    body = response.text
    assert len(body) > 50, f"Resposta muito curta: {body[:100]}"


@requires_services
def test_rag_stream_handles_technical_question(client):
    """Testa pergunta técnica sobre código de erro."""
    response = client.post(
        "/api/chat",
        json={"messages": [{"role": "user", "content": "O que é o erro E0831?"}]},
    )
    assert response.status_code == 200
    body = response.text
    assert len(body) > 50


@requires_services
def test_rag_retrieves_relevant_context(client):
    """Verifica se a resposta contém termos relacionados à pergunta."""
    response = client.post(
        "/api/chat",
        json={
            "messages": [
                {"role": "user", "content": "Como fazer o primeiro acesso ao Portal Nacional?"}
            ]
        },
    )
    assert response.status_code == 200
    body = response.text.lower()
    assert any(
        term in body for term in ["portal", "acesso", "cadastro", "cnpj", "gov.br"]
    ), f"Resposta não parece relevante: {body[:200]}"
