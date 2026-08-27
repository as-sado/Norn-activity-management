import asyncio
from pathlib import Path
import tomllib


CONFIG_PATH = Path(__file__).parent / "config.toml"


async def load_config():
    def read():
        with CONFIG_PATH.open("rb") as f:
            return tomllib.load(f)

    return await asyncio.to_thread(read)


PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATABASE_SQL_PATH = PROJECT_ROOT / "norn.db"
STATE_SQL_PATH = PROJECT_ROOT / "src" / "norn" / "core" / "state.json"