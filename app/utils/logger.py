from logging import config

debug_logger_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "[%(levelname)s] %(asctime)s - %(filename)s:%(lineno)ss  - %(message)s"
        }
    },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "gohan_map": {
            "level": "DEBUG",
            "handlers": ["consoleHandler"],
            "propagate": False,
        },
    },
    "root": {"level": "INFO", "handlers": []},
}


def init_logger() -> None:
    config.dictConfig(debug_logger_config)
