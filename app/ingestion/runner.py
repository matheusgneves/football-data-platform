from typing import Callable
from app.storage.s3 import save_raw

def run_ingestion(entity: str, fetch_fn: Callable[[], dict]) -> None:
    """Executa uma ingestão genérica: busca dados via fetch_fn e salva como raw."""
    print(f"Iniciando ingestão de {entity}...")
    data = fetch_fn()
    file_path = save_raw(data, entity=entity)
    print(f"{entity} salvo em: {file_path}")