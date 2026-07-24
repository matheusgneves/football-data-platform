from app.ingestion.entities.reference_data import ingest_reference_data
from app.ingestion.entities.teams import ingest_teams
from app.ingestion.entities.standings import ingest_standings
from app.ingestion.entities.fixtures import ingest_fixtures

def run_full_pipeline() -> None:
    """Executa a ingestão completa de todas as entidades configuradas."""
    ingest_reference_data()
    ingest_teams()
    ingest_standings()
    ingest_fixtures()
    # próximas entidades entram aqui conforme forem criadas: standings, fixtures, odds...

if __name__ == "__main__":
    run_full_pipeline()