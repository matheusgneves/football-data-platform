import requests
from app.config.settings import settings


class FootballClient:
    """Cliente responsável por toda comunicação com a API-Football."""

    def __init__(self) -> None:
        self.base_url = settings.api_football_base_url
        self.headers = {"x-apisports-key": settings.api_football_key}

    def _get(self, endpoint: str, params: dict | None = None) -> dict:
        """Executa uma requisição GET genérica para um endpoint da API-Football.

        Levanta uma exceção clara caso a requisição falhe.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params, timeout=10)

        if response.status_code != 200:
            raise RuntimeError(
                f"Erro ao chamar {endpoint}: status {response.status_code} - {response.text}"
            )

        return response.json()

    def get_countries(self) -> dict:
        """Retorna a lista de países disponíveis na API-Football."""
        return self._get("countries")

    def get_fixtures(self, league_id: int, season: int) -> dict:
        """Retorna as partidas de uma liga em uma temporada específica."""
        params = {"league": league_id, "season": season}
        return self._get("fixtures", params=params)