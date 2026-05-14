from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    ollama_model: str = "llama3.2:3b"

    elbow_angle_full_extension: float = 155.0
    elbow_angle_full_flexion: float = 40.0     
    shoulder_drift_threshold: float = 25.0     
    torso_lean_threshold: float = 10.0  

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()