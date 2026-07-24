from app.api.football_client import FootballClient
from app.ingestion.runner import run_ingestion
from app.ingestion.config.leagues_config import LEAGUES

def ingest_fixtures() -> None:
    """Ingere as rodadas de todas as ligas configuradas."""
    client = FootballClient()

    for league in LEAGUES:
        run_ingestion(
            f"fixtures/league_{league['id']}",
            lambda league=league: client.get_fixtures(
                league_id=league["id"],
                season_id=league["season"],
            ),
        )

if __name__ == "__main__":
    ingest_fixtures()