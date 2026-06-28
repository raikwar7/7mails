from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BACKEND_URL: str
    WEB_URL: str

    ANDROID_REDIRECT: str
    IOS_REDIRECT: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str

    WEB_SUCCESS_URL: str

    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int

    SESSION_SECRET: str

    GROQ_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()