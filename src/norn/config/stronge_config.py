import tomllib
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent.parent

CONFIG_PATH = Path(__file__).parent / "config.toml"

with CONFIG_PATH.open("rb") as f:
    CONFIG = tomllib.load(f)

DATABASE_SQL_PATH = Path.home() / ".local" / "share" / "norn" / CONFIG["database"]["path_sql"]
STATE_SQL_PATH = PACKAGE_ROOT / CONFIG["database"]["path_state_json"]

SOCKET_PATH = Path(CONFIG["socket"]["path_socket"])