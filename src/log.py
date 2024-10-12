import json
import logging
import logging.config
import os

default_handler = "rich"
which_handler = os.environ.get("USE_LOGGING_HANDLER", default_handler).lower()

available_handlers = ["rich", "aws"]
assert (
    which_handler in available_handlers
), f"Invalid handler: {which_handler}, must be one of {available_handlers}"
which_handler = which_handler + "_handler"

log_level = "INFO" if os.environ.get("DEPLOYMENT_MODE") == "LOCAL" else "DEBUG"


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(name)s:%(lineno)d|\t%(levelname)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(message)s",
        },
        "aws": {
            "()": "aws_lambda_powertools.logging.formatter.LambdaPowertoolsFormatter",
        },
    },
    "handlers": {
        "rich_handler": {
            "class": "rich.logging.RichHandler",
            "formatter": "default",
            "level": "INFO",
        },
        "aws_handler": {
            "()": logging.StreamHandler,
            "level": "DEBUG",
            "formatter": "aws",
        },
    },
    "loggers": {
        "": {
            "handlers": [which_handler],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "handlers": [which_handler],
        "level": "INFO",
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

log = logging.getLogger("anomaliser")


log.info("Starting Logger")


def log_useful_environment_vars():
    if os.environ.get("DEPLOYMENT_MODE") == "LAMBDA":
        log.info("Environment Variables:")
        log.info(json.dumps(dict(os.environ), indent=4))

    S3_MODEL_STORE = os.environ.get("S3_MODEL_STORE")
    log.info(f"S3_MODEL_STORE: {S3_MODEL_STORE}")

    DEPLOYMENT_MODE = os.environ.get("DEPLOYMENT_MODE")
    log.info(f"DEPLOYMENT_MODE: {DEPLOYMENT_MODE}")
