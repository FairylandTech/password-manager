"""
Django settings for managers project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

import pymysql
from fairylandfuture.utils.journal import journal

from utils.config import DataSourceConfig, ProjectConfig
from utils.exceptions import DataSourceError

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG = ProjectConfig(os.path.join(BASE_DIR, ".env"))
DATA_SOURCE_CONFIG = DataSourceConfig(CONFIG.datasource_engine, CONFIG.env, os.path.join(BASE_DIR, "conf")).config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6wkly!xq*o@gnmo_mmw@3fb7u3ejqqb*a9@+w9yd@$$vg&q%h="

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = CONFIG.debug

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = CONFIG.allowed_hosts

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    "apps.accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "managers.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "managers.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

if CONFIG.datasource_engine == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": DATA_SOURCE_CONFIG.get("host"),
            "PORT": DATA_SOURCE_CONFIG.get("port"),
            "USER": DATA_SOURCE_CONFIG.get("username"),
            "PASSWORD": DATA_SOURCE_CONFIG.get("password"),
            "NAME": DATA_SOURCE_CONFIG.get("database"),
            "CHARSET": DATA_SOURCE_CONFIG.get("charset"),
        }
    }
    db_settings = DATABASES["default"]
    db_name = db_settings["NAME"]
    conn = pymysql.connect(
        host=db_settings["HOST"],
        user=db_settings["USER"],
        password=db_settings["PASSWORD"],
        port=int(db_settings["PORT"]),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    finally:
        conn.close()
else:
    raise DataSourceError("Unsupported datasource engine")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = CONFIG.language_code

# TIME_ZONE = "UTC"
TIME_ZONE = CONFIG.time_zone

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "journal": {
            "level": CONFIG.log_level,
            "class": "utils.journal.JournalHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["journal"],
            "level": CONFIG.log_level,
            "propagate": True,
        },
    },
}