from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Technical Test API"
    API_V1_STR: str = "/api/v1"
    
    # Base de datos [cite: 20]
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "technical_test"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    
    # JWT Auth [cite: 32]
    SECRET_KEY: str = "CHANGE_THIS_TO_A_SECURE_SECRET_KEY" 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"

settings = Settings()