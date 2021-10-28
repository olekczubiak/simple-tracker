from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "API for the live monitoring and analyzing"
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()