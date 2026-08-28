import json
from typing import Any
from .connect_socket import _send
from .errors import CommandError 
import os
import signal



async def _query_json(command: str) -> Any:
    response = await _send(f"j/{command}")
    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        raise CommandError(f"Invalid JSON response for '{command}': {e}") from e


async def get_activewindow() -> str:
    data = await _query_json("activewindow")
    if not data:
        return None
    return data["initialClass"]



async def get_all_app() -> list[str]:
    data = await _query_json("clients")

    return [
        app["initialClass"]
        for app in data
    ]
async def get_all_pid_app() -> dict:
    data = await _query_json("clients")

    return {
        client["initialClass"]: client["pid"]
        for client in data
    }

async def get_app_by_pid(initialClass):
    data = await get_all_pid_app()
    if not initialClass:
        return None
    return data.get(str(initialClass))



async def kill_by_pid(app: str) -> bool:
    pid = await get_app_by_pid(app)

    if pid is None:
        return False

    try:
        os.kill(pid, signal.SIGTERM)
        return True

    except ProcessLookupError:
        return f"Process {pid} not found"

    except PermissionError:
        return f"No permissions to terminate process {pid}"

