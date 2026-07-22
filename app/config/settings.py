from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações da aplicação, carregadas a partir de variáveis de ambiente."""

    api_football_key: str
    api_football_base_url: str = "https://v3.football.api-sports.io"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()