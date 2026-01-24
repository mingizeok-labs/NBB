from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ENV : str = 'local' # 실행환경 구분 (로컬, 테스트, 은양 베포 등 ...)

    SESSION_KEY : str

    model_config = SettingsConfigDict(
        env_file = '.env'
    )
settings = Settings()