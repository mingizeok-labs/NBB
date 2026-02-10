from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Set, List

class Settings(BaseSettings):
    ENV : str = 'local' # 실행환경 구분 (로컬, 테스트, 은양 베포 등 ...)

    SESSION_KEY : str
    SESSION_MAX_AGE: int
    ALLOWED_ORIGINS: Set[str]
    USE_HTTPS: bool

    ALLOWED_METHODS: List[str]
    ALLOWED_HEADERS: List[str]

    model_config = SettingsConfigDict(
        env_file = '.env',
        env_parse_none_str=True, 
        extra="ignore",
    )
settings = Settings()