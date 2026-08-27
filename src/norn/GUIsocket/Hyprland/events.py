import asyncio
from collections.abc import AsyncIterator
from dataclasses import dataclass
from .connect_socket import _event_socket_path
from .errors import SocketError

@dataclass(frozen=True, slots=True)
class Event:
    name: str
    data: str


async def connect_event_socket(
    timeout: float | None = None,
) -> tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    try:
        if timeout is None:
            return await asyncio.open_unix_connection(
                _event_socket_path()
            )

        return await asyncio.wait_for(
            asyncio.open_unix_connection(
                _event_socket_path()
            ),
            timeout=timeout,
        )

    except (OSError, asyncio.TimeoutError) as e:
        raise SocketError(
            f"Cannot reach Hyprland event socket: {e}"
        ) from e


def parse_event_line(line: str) -> Event | None:
    line = line.strip()

    if not line:
        return None

    if ">>" in line:
        name, data = line.split(">>", 1)
        return Event(name=name, data=data)

    return Event(name=line, data="")


async def listen(
    timeout: float | None = None,
) -> AsyncIterator[Event]:
    reader, writer = await connect_event_socket(timeout)

    try:
        while True:
            try:
                if timeout is None:
                    line = await reader.readline()
                else:
                    line = await asyncio.wait_for(
                        reader.readline(),
                        timeout=timeout,
                    )

            except asyncio.TimeoutError:
                return

            if not line:
                return

            event = parse_event_line(
                line.decode("utf-8", errors="ignore")
            )

            if event is not None:
                yield event

    except OSError as e:
        raise SocketError(
            f"Hyprland event socket error: {e}"
        ) from e

    finally:
        writer.close()
        await writer.wait_closed()
