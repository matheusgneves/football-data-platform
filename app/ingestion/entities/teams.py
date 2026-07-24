from app.api.football_client import FootballClient
from app.ingestion.runner import run_ingestion
from app.ingestion.config.leagues_config import LEAGUES

def ingest_teams() -> None:
    """Ingere os times de todas as ligas configuradas."""
    client = FootballClient()

    for league in LEAGUES:
        run_ingestion(
            f"teams/league_{league['id']}",
            lambda league=league: client.get_teams_information(
                league_id=league["id"],
                season_id=league["season"],
            ),
        )

if __name__ == "__main__":
    ingest_teams()