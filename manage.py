#!/usr/bin/env python
import os
import sys
from decouple import Config, RepositoryEnv

def main():
    # Decide env file
    DJANGO_ENV = os.environ.get("DJANGO_ENV", "local")

    if DJANGO_ENV == "docker":
        env_config = Config(RepositoryEnv(".env.docker"))
    else:
        env_config = Config(RepositoryEnv(".env.local"))

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        env_config("DJANGO_SETTINGS_MODULE")
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
