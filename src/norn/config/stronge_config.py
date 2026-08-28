import tomllib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]

CONFIG_PATH = Path(__file__).parent / "config.toml"

with CONFIG_PATH.open("rb") as f:
    CONFIG = tomllib.load(f)

DATABASE_SQL_PATH = PROJECT_ROOT / CONFIG["database"]["path_sql"]
STATE_SQL_PATH = PROJECT_ROOT / CONFIG["database"]["path_state_json"]

SOCKET_PATH = Path(CONFIG["socket"]["path_socket"])