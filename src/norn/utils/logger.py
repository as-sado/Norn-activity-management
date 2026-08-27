import logging
from pathlib import Path


LOG_DIR = Path.home() / ".local" / "share" / "norn"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "norn.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
    ],
)


logger = logging.getLogger("norn")