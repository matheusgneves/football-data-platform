from app.api.football_client import FootballClient
from app.ingestion.runner import run_ingestion

BRASILEIRAO_LEAGUE_ID = 71
SEASON = 2024  # ajuste conforme o que você confirmar no league_seasons.json


def ingest_brasileirao_teams() -> None:
    """Ingere os times do Brasileirão Série A na temporada configurada."""
    client = FootballClient()

    run_ingestion(
        "teams",
        lambda: client.get_teams_information(
            league_id=BRASILEIRAO_LEAGUE_ID,
            season_id=SEASON,
        ),
    )


if __name__ == "__main__":
    ingest_brasileirao_teams()