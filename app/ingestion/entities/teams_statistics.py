from app.api.football_client import FootballClient
from app.ingestion.runner import run_ingestion
from app.ingestion.config.leagues_config import LEAGUES


def ingest_teams_statistics() -> None:
    """Ingere as estatísticas de cada time, para cada liga configurada."""
    client = FootballClient()

    for league in LEAGUES:
        teams_response = client.get_teams_information(
            league_id=league["id"],
            season_id=league["season"],
        )
        team_ids = [team["team"]["id"] for team in teams_response["response"]]

        for team_id in team_ids:
            run_ingestion(
                f"teams_statistics/league_{league['id']}/team_{team_id}",
                lambda league=league, team_id=team_id: client.get_teams_statistics(
                    league_id=league["id"],
                    season_id=league["season"],
                    team_id=team_id,
                ),
            )


if __name__ == "__main__":
    ingest_teams_statistics()