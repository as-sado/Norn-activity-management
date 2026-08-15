import asyncio
import functools
import os
from pathlib import Path
from .errors import SocketError


@functools.cache
def _hypr_dir() -> Path:
    sig = os.environ.get("HYPRLAND_INSTANCE_SIGNATURE")

    if not sig:
        raise SocketError(
            "HYPRLAND_INSTANCE_SIGNATURE is not set — is Hyprland running?"
        )

    runtime = os.environ.get(
        "XDG_RUNTIME_DIR",
        f"/run/user/{os.getuid()}",
    )

    return Path(runtime) / "hypr" / sig

def _socket_path() -> str:
    return str(_hypr_dir() / ".socket.sock")

def _event_socket_path() -> str:
    return str(_hypr_dir() / ".socket2.sock")

async def _send(command: str, timeout: float = 2.0) -> str:
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_unix_connection(_socket_path()),
            timeout=timeout,
        )

        try:
            writer.write(command.encode())
            await writer.drain()

            chunks = []

            while True:
                chunk = await asyncio.wait_for(
                    reader.read(8192),
                    timeout=timeout,
                )

                if not chunk:
                    break

                chunks.append(chunk)

            return b"".join(chunks).decode()

        finally:
            writer.close()
            await writer.wait_closed()

    except (OSError, UnicodeDecodeError, asyncio.TimeoutError) as e:
        raise SocketError(
            f"Cannot reach Hyprland socket: {e}"
        ) from e




