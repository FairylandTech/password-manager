# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-14 23:19:47 UTC+8
"""

import os
from typing import Any, Dict, List

import yaml
from dotenv import load_dotenv
from fairylandfuture.utils.journal import journal
from fairylandfuture.constants.enums import EncodingEnum

from utils.exceptions import DataSourceError, CacheError


class ProjectConfig:

    def __init__(self, _env):
        self.__env = _env
        load_dotenv(self.__env)
        journal.info(f"Project configuration initialized with environment: {_env}")

    @property
    def environment(self) -> str:
        journal.info("Loading environment from environment variable.")
        if os.getenv("ENVIRONMENT").capitalize() == "Product":
            journal.warning("Running in product environment.")
            return "product"
        else:
            journal.warning("Running in develop environment.")
            return "develop"

    @property
    def debug(self) -> bool:
        journal.info("Loading debug mode from environment variable.")
        if os.getenv("DEBUG").capitalize() == "True":
            return True
        else:
            return False

    @property
    def allowed_hosts(self) -> List[str]:
        journal.info("Loading allowed hosts from environment variable.")
        allowed_hosts = os.getenv("ALLOWED_HOSTS")
        if allowed_hosts:
            allowed_hosts_list = [item for item in allowed_hosts.split(",")]
            return allowed_hosts_list
        else:
            return list()

    @property
    def datasource_engine(self) -> str:
        journal.info("Loading data source engine from environment variable.")
        return os.getenv("DATASOURCE_ENGINE").lower()

    @property
    def cache_engine(self) -> str:
        journal.info("Loading cache engine from environment variable.")
        return os.getenv("CACHE_ENGINE").lower()

    @property
    def language_code(self) -> str:
        journal.info("Loading language code from environment variable.")
        return os.getenv("LANGUAGE_CODE")

    @property
    def time_zone(self) -> str:
        journal.info("Loading time zone from environment variable.")
        return os.getenv("TIME_ZONE")

    @property
    def log_level(self) -> str:
        journal.info("Loading log level from environment variable.")
        return os.getenv("LOG_LEVEL")


class BaseConfig:

    def __init__(self, _env: str, config_dir: str):
        if _env == "product":
            self.file_name = "application.yaml"
        else:
            self.file_name = "dev-application.yaml"
        self.config_dir = config_dir

    def load_config(self) -> Dict[str, Any]:
        with open(os.path.join(self.config_dir, self.file_name), "r", encoding=EncodingEnum.UTF_8.value) as stream:
            config_data = yaml.safe_load(stream)
        return config_data


class DataSourceConfig(BaseConfig):

    def __init__(self, engine: str, _env: str, config_dir: str):
        engines = ("mysql", "postgresql")
        if engine.lower() not in engines:
            raise DataSourceError("Unsupported data source engine.")
        self.engine = engine.lower()

        super().__init__(_env, config_dir)

        journal.info(f"Loading {self.engine} data source configuration.")
        self.config: Dict[str, Any] = self.load_config().get("datasource").get(self.engine)


class CacheConfig(BaseConfig):

    def __init__(self, engine: str, _env: str, config_dir: str):
        engines = ("redis",)
        if engine.lower() not in engines:
            raise CacheError("Unsupported redis engine.")
        self.engine = engine.lower()

        super().__init__(_env, config_dir)

        journal.info(f"Loading {self.engine} redis configuration.")
        self.config: Dict[str, Any] = self.load_config().get("cache").get(self.engine)

    @property
    def redis_url(self) -> str:
        return f"redis://{self.config.get('host')}:{self.config.get('port')}/{self.config.get('database')}"
