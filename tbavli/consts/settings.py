from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    server_address: str = "127.0.0.1"
    login_port: int = 8484
    channel_port: int = 8585

    class Config:
        env_file = ".env"