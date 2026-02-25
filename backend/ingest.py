"""
Script de indexação dos documentos FAQ da NFS-e no Qdrant.

Este script:
1. Carrega os arquivos Markdown da pasta data/ (faq-*.md)
2. Aplica o MarkdownNodeParser para chunking por seções H2 (cada "Dúvida NNN" vira um chunk)
3. Enriquece metadados com category, source_file
4. Gera embeddings com HuggingFace (paraphrase-multilingual-MiniLM-L12-v2)
5. Armazena no Qdrant (collection: nfse_faq)

Execute após subir o Qdrant: docker-compose up -d qdrant
Depois: python -m backend.ingest (ou python backend/ingest.py)
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Carregar .env do diretório backend
_env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(_env_path)

# Mapeamento de arquivos FAQ para categorias legíveis
FAQ_CATEGORIES = {
    "faq-01-painel-municipal-gestao.md": "Painel Municipal e Gestão",
    "faq-02-cadastro-contribuintes-cnc.md": "Cadastro CNC",
    "faq-03-emissao-nfse-portal.md": "Emissão no Portal",
    "faq-04-cancelamento-substituicao.md": "Cancelamento e Substituição",
    "faq-05-tributacao-iss-issqn.md": "Tributação ISS/ISSQN",
    "faq-06-tributos-federais-pcc-nt007.md": "Tributos Federais",
    "faq-07-reforma-tributaria-ibs-cbs.md": "Reforma Tributária",
    "faq-08-integracao-api-webservice.md": "Integração API",
}


def get_data_path() -> Path:
    """Retorna o caminho absoluto da pasta data."""
    backend_dir = Path(__file__).resolve().parent
    project_root = backend_dir.parent
    return project_root / "data"


def main() -> None:
    from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
    from llama_index.core.node_parser import MarkdownNodeParser
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.vector_stores.qdrant import QdrantVectorStore
    from qdrant_client import QdrantClient

    data_path = get_data_path()
    if not data_path.exists():
        raise FileNotFoundError(f"Pasta data não encontrada: {data_path}")

    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    collection_name = "nfse_faq"

    print(f"Carregando documentos de {data_path}...")
    reader = SimpleDirectoryReader(
        input_dir=str(data_path),
        required_exts=[".md"],
        recursive=False,
    )
    # Filtrar apenas arquivos faq-*.md
    all_docs = reader.load_data()
    documents = [d for d in all_docs if "faq-" in (d.metadata.get("file_name") or "")]
    print(f"Encontrados {len(documents)} documentos FAQ.")

    if not documents:
        raise ValueError("Nenhum documento FAQ encontrado. Verifique se existem arquivos faq-*.md em data/")

    # Parser Markdown: divide por H2 (## Dúvida NNN)
    print("Aplicando MarkdownNodeParser...")
    node_parser = MarkdownNodeParser.from_defaults(
        include_metadata=True,
        include_prev_next_rel=True,
    )
    nodes = node_parser.get_nodes_from_documents(documents)

    # Enriquecer metadados de cada node com category e source_file
    for node in nodes:
        file_name = node.metadata.get("file_name") or ""
        node.metadata["source_file"] = file_name
        node.metadata["category"] = FAQ_CATEGORIES.get(file_name, "FAQ NFS-e")

    print(f"Gerados {len(nodes)} nodes.")

    # Embedding model multilingue (português)
    print("Configurando embeddings HuggingFace...")
    embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    )

    # Configurar Qdrant
    print(f"Conectando ao Qdrant em {qdrant_url}...")
    client = QdrantClient(url=qdrant_url)
    # Recriar collection para reindexação limpa
    try:
        client.delete_collection(collection_name)
        print(f"Collection '{collection_name}' existente removida.")
    except Exception:
        pass
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
    )

    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Criar índice e indexar
    print("Indexando documentos no Qdrant...")
    VectorStoreIndex.from_nodes(
        nodes,
        storage_context=storage_context,
        embed_model=embed_model,
    )

    print(f"Indexação concluída. Collection '{collection_name}' pronta no Qdrant.")


if __name__ == "__main__":
    main()
