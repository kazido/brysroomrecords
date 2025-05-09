import logging

from logging import handlers
from pathlib import Path
from discord.utils import setup_logging


root_log = logging.getLogger()


def setup():
    log_format = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    log_file = Path("logs", "bot.log")
    log_file.parent.mkdir(exist_ok=True)
    file_handler = handlers.RotatingFileHandler(
        log_file, maxBytes=5242880, backupCount=7, encoding="utf8"
    )
    file_handler.setFormatter(log_format)
    root_log.addHandler(file_handler)
    setup_logging(handler=file_handler, formatter=log_format)  # 2.1 Logging feature
