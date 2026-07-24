from app.api.football_client import FootballClient
from app.ingestion.runner import run_ingestion
from app.ingestion.config.leagues_config import LEAGUES

def ingest_standings() -> None:
    """Ingere a classificação de todas as ligas configuradas."""
    client = FootballClient()

    for league in LEAGUES:
        run_ingestion(
            f"standings/league_{league['id']}",
            lambda league=league: client.get_standings(
                league_id=league["id"],
                season_id=league["season"],
            ),
        )

if __name__ == "__main__":
    ingest_standings()