import logging
from .config import settings

logger = logging.getLogger("middleware_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(settings.log_file)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
