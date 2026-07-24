from app.api.football_client import FootballClient
from app.storage.s3 import save_raw


def ingest_countries() -> None:
    """Busca os países disponíveis na API-Football e salva o resultado bruto."""
    client = FootballClient()
    data = client.get_countries()

    file_path = save_raw(data, entity="countries")
    print(f"Países salvos em: {file_path}")


if __name__ == "__main__":
    ingest_countries()