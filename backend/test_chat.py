#!/usr/bin/env python3
"""
Script de teste interativo para o backend do Chatbot NFS-e.

Testa diretamente o endpoint /api/chat sem precisar do frontend.
O backend deve estar rodando (uvicorn backend.main:app).

Uso:
    python -m backend.test_chat                          # modo interativo
    python -m backend.test_chat "O que é o erro E0831?"  # pergunta única
    python -m backend.test_chat --all                    # roda todas as perguntas de teste
    python -m backend.test_chat --health                 # verifica health check
"""

import sys
import argparse
import requests

BASE_URL = "http://127.0.0.1:8000"

TEST_QUESTIONS = [
    "Como fazer o primeiro acesso ao Portal Nacional?",
    "O que é o erro E0831?",
    "Como funciona a retenção de PIS/COFINS/CSLL após a NT 007?",
    "Como migrar do emissor próprio para o nacional?",
    "Como cancelar uma NFS-e?",
]


def check_health() -> bool:
    try:
        r = requests.get(f"{BASE_URL}/health", timeout=5)
        if r.status_code == 200:
            print(f"[OK] Health check: {r.json()}")
            return True
        print(f"[ERRO] Health check retornou {r.status_code}: {r.text}")
        return False
    except requests.ConnectionError:
        print(f"[ERRO] Backend não está rodando em {BASE_URL}")
        print("       Execute: uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000")
        return False


def send_question(question: str, verbose: bool = True) -> str | None:
    if verbose:
        print(f"\n{'='*60}")
        print(f"Pergunta: {question}")
        print("-" * 60)

    try:
        r = requests.post(
            f"{BASE_URL}/api/chat",
            json={"messages": [{"role": "user", "content": question}]},
            stream=True,
            timeout=60,
        )

        if r.status_code != 200:
            print(f"[ERRO] Status {r.status_code}: {r.text}")
            return None

        full_response = ""
        for chunk in r.iter_content(chunk_size=None, decode_unicode=True):
            if chunk:
                full_response += chunk
                if verbose:
                    print(chunk, end="", flush=True)

        if verbose:
            print(f"\n{'='*60}")
            print(f"[OK] Resposta recebida ({len(full_response)} caracteres)")

        return full_response

    except requests.ConnectionError:
        print(f"[ERRO] Não foi possível conectar ao backend em {BASE_URL}")
        return None
    except requests.Timeout:
        print("[ERRO] Timeout aguardando resposta (60s)")
        return None


def run_all_tests():
    print("Executando todas as perguntas de teste...\n")

    if not check_health():
        return

    results = []
    for i, q in enumerate(TEST_QUESTIONS, 1):
        print(f"\n[{i}/{len(TEST_QUESTIONS)}]")
        response = send_question(q)
        success = response is not None and len(response) > 20
        results.append((q, success, len(response) if response else 0))

    print(f"\n\n{'='*60}")
    print("RESUMO DOS TESTES")
    print("=" * 60)
    passed = 0
    for q, success, length in results:
        status = "PASS" if success else "FAIL"
        if success:
            passed += 1
        print(f"  [{status}] {q[:50]}... ({length} chars)")

    print(f"\nResultado: {passed}/{len(results)} testes passaram")


def interactive_mode():
    print("Modo interativo - digite perguntas (Ctrl+C para sair)")
    print("Comandos especiais: /health, /test, /quit\n")

    if not check_health():
        return

    while True:
        try:
            question = input("\nVocê: ").strip()
            if not question:
                continue
            if question == "/quit":
                break
            if question == "/health":
                check_health()
                continue
            if question == "/test":
                run_all_tests()
                continue
            send_question(question)
        except (KeyboardInterrupt, EOFError):
            print("\nAté logo!")
            break


def main():
    global BASE_URL

    parser = argparse.ArgumentParser(description="Teste do backend Chatbot NFS-e")
    parser.add_argument("question", nargs="?", help="Pergunta para enviar")
    parser.add_argument("--all", action="store_true", help="Rodar todas as perguntas de teste")
    parser.add_argument("--health", action="store_true", help="Verificar health check")
    parser.add_argument("--url", default=BASE_URL, help=f"URL do backend (default: {BASE_URL})")
    args = parser.parse_args()

    BASE_URL = args.url

    if args.health:
        sys.exit(0 if check_health() else 1)

    if args.all:
        run_all_tests()
        return

    if args.question:
        result = send_question(args.question)
        sys.exit(0 if result else 1)

    interactive_mode()


if __name__ == "__main__":
    main()
