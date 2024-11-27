from pydantic_settings import BaseSettings
import json

class Settings(BaseSettings):
    clients: dict
    ip: str
    log_file: str

    @classmethod
    def load_settings(cls):
        with open("config/settings.json", "r") as f:
            data = json.load(f)
            return cls(**data)

settings = Settings.load_settings()
