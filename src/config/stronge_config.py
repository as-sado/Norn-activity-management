import tomllib

with open("config/config.toml", "rb") as f:
    config = tomllib.load(f)

DATABASE_SQL_PATH = config["database"]["path_sql"]
STATE_SQL_PATH = config["database"]["path_state_json"]
