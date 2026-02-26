"""Testes do endpoint /api/chat (validação de input, sem chamar a LLM)."""

import pytest
from unittest.mock import patch, AsyncMock


def test_chat_rejects_empty_messages(client):
    response = client.post("/api/chat", json={"messages": []})
    assert response.status_code == 400
    assert "Nenhuma mensagem" in response.json()["detail"]


def test_chat_rejects_no_user_message(client):
    response = client.post(
        "/api/chat",
        json={"messages": [{"role": "assistant", "content": "oi"}]},
    )
    assert response.status_code == 400
    assert "usuário" in response.json()["detail"]


def test_chat_rejects_empty_content(client):
    response = client.post(
        "/api/chat",
        json={"messages": [{"role": "user", "content": "   "}]},
    )
    assert response.status_code == 400
    assert "vazia" in response.json()["detail"]


def test_chat_rejects_invalid_payload(client):
    response = client.post("/api/chat", json={"wrong": "field"})
    assert response.status_code == 422


async def _mock_stream(query: str):
    for word in ["Olá", ", ", "esta ", "é ", "uma ", "resposta."]:
        yield word


@patch("backend.main.stream_generator", side_effect=_mock_stream)
def test_chat_streams_response(mock_gen, client):
    response = client.post(
        "/api/chat",
        json={"messages": [{"role": "user", "content": "teste"}]},
    )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")
    body = response.text
    assert "Olá" in body
    assert "resposta." in body


@patch("backend.main.stream_generator", side_effect=_mock_stream)
def test_chat_uses_last_user_message(mock_gen, client):
    response = client.post(
        "/api/chat",
        json={
            "messages": [
                {"role": "user", "content": "primeira pergunta"},
                {"role": "assistant", "content": "resposta"},
                {"role": "user", "content": "segunda pergunta"},
            ]
        },
    )
    assert response.status_code == 200
    mock_gen.assert_called_once_with("segunda pergunta")
