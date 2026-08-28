import asyncio
import os
from norn.repository.data_transfer_from_sql import transfer_from_block_app,transfer_from_block_app_interval
from norn.config.stronge_config import SOCKET_PATH




clients: set[asyncio.StreamWriter] = set()


async def broadcast(message: str):
    dead_clients = set()

    for writer in clients:
        try:
            writer.write(f"{message}\n".encode())
            await writer.drain()

        except (ConnectionResetError, BrokenPipeError):
            dead_clients.add(writer)

    for writer in dead_clients:
        clients.discard(writer)


async def handle_command(command: str):
    if command.startswith("app[") and command.endswith("]"):
        await broadcast(command)
        return

    if command == "block":
        await transfer_from_block_app()
        await broadcast("refresh[block]")
        return

    if command == "interval":
        await transfer_from_block_app_interval()
        await broadcast("refresh[interval]")
        return

    if command.startswith("command[") and command.endswith("]"):
        command_text = command[8:-1]
        return


async def handle_client(reader: asyncio.StreamReader,   writer: asyncio.StreamWriter):
    clients.add(writer)
    try:
        while True:
            data = await reader.readline()
            if not data:
                break

            command = data.decode().strip()
            if not command:
                continue

            await handle_command(command)

    except ( ConnectionResetError,BrokenPipeError,):
        pass

    finally:
        clients.discard(writer)
        writer.close()
        try:
            await writer.wait_closed()
        except ConnectionError:
            pass


async def socket_server():

    if os.path.exists(SOCKET_PATH):
        os.unlink(SOCKET_PATH)

    server = await asyncio.start_unix_server(handle_client,SOCKET_PATH)
    async with server:
        await server.serve_forever()