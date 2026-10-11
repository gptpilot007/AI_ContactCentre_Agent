from fastapi import FastAPI
from app.config.settings import Settings
from app.utils.logger import get_logger

settings = Settings()
logger = get_logger(__name__)

app = FastAPI(title="AI Contact Center Agent")

@app.get("/health")
def health_check():
    logger.info("Health check OK")
    return {"status": "ok"}
