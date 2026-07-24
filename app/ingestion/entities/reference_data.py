from app.api.football_client import FootballClient
from app.ingestion.runner import run_ingestion

def ingest_reference_data() -> None:
    """Ingere os dados de referência da API-Football (baixa frequência de mudança)."""
    client = FootballClient()

    run_ingestion("timezone", client.get_timezone)
    run_ingestion("countries", client.get_countries)
    run_ingestion("leagues", client.get_leagues)
    run_ingestion("league_seasons", client.get_league_seasons)
    run_ingestion("trophies", client.get_trophies)
    run_ingestion("bookmakers", client.get_bookmakers)

if __name__ == "__main__":
    ingest_reference_data()