from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str

    class Config:
        env_file = ".env"
        extra = "ignore"  # 추가 입력 허용


class JWTSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    class Config:
        env_file = ".env"
        extra = "ignore"  # 추가 입력 허용


class CORSSettings(BaseSettings):
    ALLOW_ORIGIN: str

    class Config:
        env_file = ".env"
        extra = "ignore"


class AppSettings:
    def __init__(self):
        self._db_settings = None
        self._jwt_settings = None
        self._cors_settings = None

    @property
    def db(self):
        if not self._db_settings:
            self._db_settings = DBSettings()
        return self._db_settings

    @property
    def jwt(self):
        if not self._jwt_settings:
            self._jwt_settings = JWTSettings()
        return self._jwt_settings

    @property
    def cors(self):
        if not self._cors_settings:
            self._cors_settings = CORSSettings()
        return self._cors_settings


# 전역 설정 인스턴스 생성
settings = AppSettings()
