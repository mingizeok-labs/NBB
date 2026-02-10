from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Set, List

class Settings(BaseSettings):
    ENV : str = 'local' # 실행환경 구분 (로컬, 테스트, 은양 베포 등 ...)

    SESSION_KEY : str
    SESSION_MAX_AGE: int
    ALLOWED_ORIGINS: str
    USE_HTTPS: bool

    ALLOWED_METHODS: str
    ALLOWED_HEADERS: str
    SESSION_SAMESITE: str
    SESSION_HTTPS_ONLY: bool

    model_config = SettingsConfigDict(
        env_file = '.env',
        env_parse_none_str=True, 
        extra="ignore",
        env_parse_delimiter=",",
    )

    def split(self, value: str) -> List[str]:
        return [v.strip() for v in value.split(",") if v.strip()]
    
settings = Settings()