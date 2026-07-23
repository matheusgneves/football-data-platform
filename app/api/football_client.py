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

    def get_timezone(self) -> dict:
        """Retorna a lista de timezones"""
        return self._get("timezone")
    
    def get_countries(self) -> dict:
        """Retorna a lista de países disponíveis na API-Football."""
        return self._get("countries")
    
    def get_leagues(self) -> dict:
        """Retorna as ligas disponíveis, opcionalmente filtradas por país."""
        return self._get("leagues")

    def get_league_seasons(self) -> dict:
        """Retorna todas as temporadas disponíveis na API-Football."""
        return self._get("leagues/seasons")

    def get_teams_information(
            self,
            team_id: int | None = None,
            name: str | None = None ,
            league_id: int | None = None,
            season_id: int | None = None,
            country: str | None = None,
            code: str | None = None,
            venue_id: int | None = None,
            search: str | None = None
        ) -> dict:
        """Retorna todos os times disponíveis na API-Football."""
        params = {
            "id": team_id,
            "name": name,
            "league": league_id,
            "season": season_id,
            "country": country,
            "code": code,
            "venue": venue_id,
            "search": search
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("teams", params=params)

    def get_teams_statistics(
            self,
            league_id: int,
            season_id: int,
            team_id: int,
            date: str | None = None 
        ) -> dict:
        """Retorna as estatísticas de um time específico em uma liga e temporada."""
        params = {
            "league": league_id,
            "season": season_id,
            "team": team_id,
            "date": date
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("teams/statistics", params=params)

    def get_teams_countries(self) -> dict:
        """Retorna os países dos times disponíveis na API-Football."""
        return self._get("teams/countries")

    def get_venues(
            self,
            venue_id: int | None = None,
            name: str  | None = None,
            city: str | None = None,
            country: str | None = None,
            search: str | None = None 
        ) -> dict:
        """Retorna as sedes disponíveis na API-Football."""
        params = {
            "id": venue_id,
            "name": name,
            "city": city,
            "country": country,
            "search": search
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("venues", params=params)

    def get_standings(
            self,
            season_id: int,
            league_id: int | None = None,
            team_id: int | None = None  
        ) -> dict:
        """Retorna a classificação de uma temporada, opcionalmente filtrada por liga ou time."""
        params = {
            "season": season_id,
            "league": league_id,
            "team": team_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("standings", params=params)

    def get_teams_seasons(self, team_id: int) -> dict:
        """Retorna as temporadas de um time disponíveis na API-Football."""
        params = {
            "team": team_id,
        }
        return self._get("teams/seasons", params=params)

    def get_fixtures_rounds(
            self,
            league_id: int,
            season_id: int,
            current: bool | None = None,
            dates: bool | None = None ,
            timezone: str | None = None 
        ) -> dict:
        """Retorna as rodadas de uma liga em uma temporada específica."""
        params = {
            "league": league_id,
            "season": season_id,
            "current": current,
            "dates": dates,
            "timezone": timezone
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("fixtures/rounds", params=params)