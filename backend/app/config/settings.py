from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Contact Center Agent"
    environment: str = "development"

    class Config:
        env_file = ".env"
