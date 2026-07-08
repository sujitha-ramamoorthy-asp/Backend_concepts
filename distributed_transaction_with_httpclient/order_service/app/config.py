from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int

    DB_USER: str
    DB_PASSWORD: str

    DB_NAME: str

    PAYMENT_SERVICE: str
    INVENTORY_SERVICE: str

    class Config:
        env_file = ".env"


settings = Settings()