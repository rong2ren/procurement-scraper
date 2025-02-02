from pydantic_settings import BaseSettings #Provides a base class for settings with environment variable support
from functools import lru_cache
from pathlib import Path

class Settings(BaseSettings):
    # Base paths
    BASE_DIR: Path = Path(__file__).parent.parent #2 levels up
    
    # API Keys
    openai_api_key: str
    
    # Database
    database_url: str
    
    # Scraping
    max_retries: int = 3
    scrape_delay: int = 2

    # Logging
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        extra = "allow" 

#Decorated with @lru_cache() to cache the settings instance
@lru_cache()
def get_settings():
    return Settings()