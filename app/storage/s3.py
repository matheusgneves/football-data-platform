import json
import os
from datetime import datetime, timezone


def save_raw(data: dict, entity: str) -> str:
    """Salva o payload bruto retornado pela API em um arquivo JSON local.

    Por enquanto grava em disco; a assinatura já está pensada para,
    no futuro, ser trocada por um upload real ao S3 sem impactar
    quem chama essa função.
    """
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    directory = f"data/raw/{entity}"
    os.makedirs(directory, exist_ok=True)

    file_path = f"{directory}/{timestamp}.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    return file_path