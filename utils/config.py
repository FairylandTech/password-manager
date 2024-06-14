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

from utils.exceptions import DataSourceError


class ProjectConfig:

    def __init__(self, _env):
        self.env = _env
        load_dotenv(self.env)
        journal.info(f"Project configuration initialized with environment: {_env}.")

    @property
    def environment(self) -> str:
        journal.info(f"Loading environment from environment variable.")
        if os.getenv("ENVIRONMENT").capitalize() == "Product":
            return "product"
        else:
            return "develop"

    @property
    def debug(self) -> bool:
        journal.info(f"Loading debug mode from environment variable.")
        if os.getenv("DEBUG").capitalize() == "True":
            return True
        else:
            return False

    @property
    def allowed_hosts(self) -> List[str]:
        journal.info(f"Loading allowed hosts from environment variable.")
        allowed_hosts = os.getenv("ALLOWED_HOSTS")
        if allowed_hosts:
            allowed_hosts_list = [item for item in allowed_hosts.split(",")]
            return allowed_hosts_list
        else:
            return list()

    @property
    def datasource_engine(self) -> str:
        journal.info(f"Loading data source engine from environment variable.")
        return os.getenv("DATASOURCE_ENGINE").lower()

    @property
    def language_code(self) -> str:
        journal.info(f"Loading language code from environment variable.")
        return os.getenv("LANGUAGE_CODE")

    @property
    def time_zone(self) -> str:
        journal.info(f"Loading time zone from environment variable.")
        return os.getenv("TIME_ZONE")

    @property
    def log_level(self) -> str:
        journal.info(f"Loading log level from environment variable.")
        return os.getenv("LOG_LEVEL")


class DataSourceConfig:

    def __init__(self, engine: str, _env: str, config_dir: str):
        engines = ("mysql",)
        if engine.lower() not in engines:
            raise DataSourceError("Unsupported data source engine.")
        if _env == "product":
            self.file_name = "application.yaml"
        else:
            self.file_name = "dev-application.yaml"
        self.engine = engine.lower()
        self.config_dir = config_dir

    def __load_config(self) -> Dict[str, Any]:
        with open(os.path.join(self.config_dir, self.file_name), "r", encoding="utf-8") as stream:
            config_data = yaml.safe_load(stream)
        journal.info(f"Data source configuration loaded from {self.file_name}.")
        return config_data

    @property
    def config(self) -> Dict[str, Any]:
        journal.info(f"Loading {self.engine} data source configuration.")
        return self.__load_config().get("datasource").get(self.engine)
