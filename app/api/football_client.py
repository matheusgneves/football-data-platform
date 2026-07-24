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
        """Retorna a lista de países ."""
        return self._get("countries")
    
    def get_leagues(self) -> dict:
        """Retorna as ligas disponíveis, opcionalmente filtradas por país."""
        return self._get("leagues")

    def get_league_seasons(self) -> dict:
        """Retorna todas as temporadas ."""
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
        """Retorna todos os times ."""
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
        """Retorna os países dos times ."""
        return self._get("teams/countries")

    def get_venues(
            self,
            venue_id: int | None = None,
            name: str  | None = None,
            city: str | None = None,
            country: str | None = None,
            search: str | None = None 
    ) -> dict:
        """Retorna as sedes ."""
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
        """Retorna as temporadas de um time ."""
        params = {
            "team": team_id,
        }
        return self._get("teams/seasons", params=params)

    def get_fixtures_rounds(
            self,
            league_id: int,
            season_id: int,
            current: bool = False,
            dates: bool = False,
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

    def get_fixtures(
            self,
            fixture_id: int | None = None,
            fixture_ids: str | None = None,
            live: str | None = None,
            date: str | None = None,
            league_id: int | None = None,
            season_id: int | None = None,
            team_id: int | None = None,
            last: int | None = None,
            _next: int | None = None,
            _from: str | None = None,
            to: str | None = None,
            _round: str | None = None,
            status: str | None = None,
            venue_id: int | None = None,
            timezone: str | None = None
    ) -> dict:
        """Retorna as partidas de uma liga e temporada."""
        params = {
            "id": fixture_id,
            "ids": fixture_ids,
            "live": live,
            "date": date,
            "league": league_id,
            "season": season_id,
            "team": team_id,
            "last": last,
            "next": _next,
            "from": _from,
            "to": to,
            "round": _round,
            "status": status,
            "venue": venue_id,
            "timezone": timezone
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("fixtures", params=params)

    def get_fixtures_h2h(
            self,
            h2h_team_ids: str,
            date: str | None = None,
            league_id: int | None = None,
            season_id: int | None = None,
            last: int | None = None,
            _next: int | None = None,
            _from: str | None = None,
            to: str | None = None,
            status: str | None = None,
            venue_id: int | None = None,
            timezone: str | None = None
    ) -> dict:
        """Retorna o confronto direto entre dois times."""
        params = {
            "h2h": h2h_team_ids,
            "date": date,
            "league": league_id,
            "season": season_id,
            "last": last,
            "next": _next,
            "from": _from,
            "to": to,
            "status": status,
            "venue": venue_id,
            "timezone": timezone
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("fixtures/headtohead", params=params)

    def get_fixtures_statistics(
            self,
            fixture_id: int,
            team_id: int | None = None,
            _type: str | None = None,
            half: bool = False,
    ) -> dict:
        """Retorna as estatísticas de uma partida."""
        params = {
            "fixture": fixture_id,
            "team": team_id,
            "type": _type,
            "half": half
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("fixtures/statistics", params=params)

    def get_fixtures_events(
            self,
            fixture_id: int,
            team_id: int | None = None,
            player_id: int | None = None,
            _type: str | None = None
    ) -> dict:
        """Retorna os eventos de uma partida."""
        params = {
            "fixture": fixture_id,
            "team": team_id,
            "player": player_id,
            "type": _type
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("fixtures/events", params=params)

    def get_fixtures_lineups(
            self,
            fixture_id: int,
            team_id: int | None = None,
            player_id: int | None = None,
            _type: str | None = None
    ) -> dict:
        """Retorna a escalação dos times de uma partida."""
        params = {
            "fixture": fixture_id,
            "team": team_id,
            "player": player_id,
            "type": _type
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("fixtures/lineups", params=params)

    def get_fixtures_players(
            self,
            fixture_id: int,
            team_id: int | None = None
    ) -> dict:
        """Retorna as estatisticas dos jogadores de uma partida."""
        params = {
            "fixture": fixture_id,
            "team": team_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("fixtures/players", params=params)

    def get_injuries(
            self,
            league_id: int | None = None,
            season_id: int | None = None,
            fixture_id: int | None = None,
            team_id: int | None = None,
            player_id: int | None = None,
            date: str | None = None,
            player_ids: str | None = None,
            fixture_ids: str | None = None,
            timezone: str | None = None
    ) -> dict:
        """Retorna o motivo e a lista de jogadores que não estão participando da partida."""
        params = {
            "league": league_id,
            "season": season_id,
            "fixture": fixture_id,
            "team": team_id,
            "player": player_id,
            "date": date,
            "ids": player_ids,
            "timezone": timezone
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("injuries", params=params)

    def get_predictions(self, fixture_id: int) -> dict:
        """Retorna as previsões (Time Vencedor, Under/Over, etc.) de uma partida."""
        params = {
            "fixture": fixture_id
        }
        return self._get("predictions", params=params)

    def get_coachs(
            self,
            coach_id: int | None = None,
            team_id: int | None = None,
            search: str | None = None
    ) -> dict:
        """Retorna as informações sobre os técnicos e suas carreiras."""
        params = {
            "id": coach_id,
            "team": team_id,
            "search": search
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("coachs", params=params)

    def get_players_seasons(self, player_id: int | None = None) -> dict:
        """Retorna todas as temporadas disponíveis para as estatísticas de jogador."""
        params = {
            "player": player_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players/seasons", params=params)

    def get_players_profiles(
            self,
            player_id: int | None = None,
            search: str | None = None,
            page: int = 1
    ) -> dict:
        """Retorna a lista de todos os jogadores."""
        params = {
            "player": player_id,
            "search": search,
            "page": page
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players/profiles", params=params)

    def get_players_statistics(
            self,
            player_id: int | None = None,
            team_id: int | None = None,
            league_id: int | None = None,
            season_id: int | None = None,
            search: str | None = None,
            page: int = 1
    ) -> dict:
        """Retorna as estatisticas dos jogadores."""
        params = {
            "id": player_id,
            "team": team_id,
            "league": league_id,
            "season": season_id,
            "search": search,
            "page": page
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players", params=params)

    def get_squads(
            self,
            team_id: int | None = None,
            player_id: int | None = None
    ) -> dict:
        """Retorna a escalação atual do time (caso o parâmetro team seja usado).
        Retorna os times associados ao jogador (caso o parâmetro player seja usado)."""
        params = {
            "team": team_id,
            "player": player_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players/squads", params=params)

    def get_player_teams(self, player_id: int) -> dict:
        """Retorna a lista de times e temporadas em que o jogador jogou durante a carreira."""
        params = {
            "player": player_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players/teams", params=params)

    def get_topscorers(
            self,
            league_id: int,
            season_id: int
    ) -> dict:
        """Retorna a lista dos 20 artilheiros de uma liga/copa por temporada."""
        params = {
            "league": league_id,
            "season": season_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players/topscorers", params=params)

    def get_topassists(
            self,
            league_id: int,
            season_id: int
    ) -> dict:
        """Retorna a lista dos 20 melhores assistentes de uma liga/copa por temporada."""
        params = {
            "league": league_id,
            "season": season_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players/topassists", params=params)
    
    def get_topyellowcards(
            self,
            league_id: int,
            season_id: int
    ) -> dict:
        """Retorna a lista dos 20 jogadores com mais cartões amarelos de uma liga/copa por temporada."""
        params = {
            "league": league_id,
            "season": season_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players/topyellowcards", params=params)

    def get_topredcards(
            self,
            league_id: int,
            season_id: int
    ) -> dict:
        """Retorna a lista dos 20 jogadores com mais cartões vermelhos de uma liga/copa por temporada."""
        params = {
            "league": league_id,
            "season": season_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("players/topredcards", params=params)

    def get_transfers(
            self,
            player_id: int | None = None,
            team_id: int | None = None
    ) -> dict:
        """Retorna a lista de transferências disponíveis por jogadores ou times."""
        params = {
            "player": player_id,
            "team": team_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("transfers", params=params)

    def get_trophies(
            self,
            player_id: int | None = None,
            players_id: str | None = None,
            coach_id: int | None = None,
            coachs_id: str | None = None
    ) -> dict:
        """Retorna a lista de troféus por jogadores ou técnicos."""
        params = {
            "player": player_id,
            "players": players_id,
            "coach": coach_id,
            "coachs": coachs_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("trophies", params=params)

    def get_sidelined(
            self,
            player_id: int | None = None,
            players_id: str | None = None,
            coach_id: int | None = None,
            coachs_id: str | None = None
    ) -> dict:
        """Retorna a lista de jogadores indisponíveis por jogador ou técnico."""
        params = {
            "player": player_id,
            "players": players_id,
            "coach": coach_id,
            "coachs": coachs_id   
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("sidelined", params=params)

    def get_odds_live(
            self,
            fixture_id: int | None = None,
            league_id: int | None = None,
            bet_id: int | None = None
    ) -> dict:
        """Retorna as odds de jogos ao vivo."""
        params = {
            "fixture": fixture_id,
            "league": league_id,
            "bet": bet_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("odds/live", params=params)

    def get_odds_live_bets(
            self,
            bet_id: int | None = None,
            search: str | None = None
    ) -> dict:
        """Retorna a lista de apostas disponíveis para jogos ao vivo."""
        params = {
            "id": bet_id,
            "search": search
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("odds/live/bets", params=params)

    def get_odds_prematch(
            self,
            fixture_id: int | None = None,
            league_id: int | None = None,
            season_id: int | None = None,
            date: str | None = None,
            timezone: str | None = None,
            page: int = 1,
            bookmaker_id: int | None = None,
            bet_id: int | None = None
    ) -> dict:
        """Retorna a lista de odds pré-jogo de partidas, ligas/copas ou datas."""
        params = {
            "fixture": fixture_id,
            "league": league_id,
            "season": season_id,
            "date": date,
            "timezone": timezone,
            "page": page,
            "bookmaker": bookmaker_id,
            "bet": bet_id
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("odds", params=params)

    def get_odds_mapping(self, page: int = 1) -> dict:
        """Retorna os ids de partidas disponíveis para o endpoint odds."""
        params = {
            "page": page
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("odds/mapping", params=params)

    def get_bookmakers(
            self,
            bookmaker_id: int | None = None,
            search: str | None = None
    ) -> dict:
        """Retorna a lista de todas as casas de apostas."""
        params = {
            "id": bookmaker_id,
            "search": search
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("odds/bookmakers", params=params)

    def get_bets(
            self,
            bet_id: int | None = None,
            search: str | None = None
    ) -> dict:
        """Retorna todas as apostas disponíveis para odds pré-jogo."""
        params = {
            "id": bet_id,
            "search": search
        }
        params = {key: value for key, value in params.items() if value is not None}
        return self._get("odds/bets", params=params)