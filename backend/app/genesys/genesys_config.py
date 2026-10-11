from pydantic_settings import BaseSettings

class GenesysConfig(BaseSettings):
    region_wss: str
    deployment_id: str

    class Config:
        env_file = ".env"
