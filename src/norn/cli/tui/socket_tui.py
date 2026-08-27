import asyncio
import norn.cli.tui.data as db

SOCKET_PATH = "/tmp/norn.sock"


async def socket_server_tui():
    while True:
        try:
            reader, writer = await asyncio.open_unix_connection(SOCKET_PATH)

            try:
                while True:
                    data = await reader.readline()

                    if not data:
                        break

                    command = data.decode().strip()

                    if not command:
                        continue

                    if command.startswith("app[") and command.endswith("]"):
                        app_name = command[4:-1].strip('"')
                        db.set_current_app(app_name)

                    elif command == "refresh[block]":
                        await db.transfer_from_block_app()

                    elif command == "refresh[interval]":
                        await db.transfer_from_block_app_interval()

            finally:
                writer.close()

                try:
                    await writer.wait_closed()
                except ConnectionError:
                    pass

        except (FileNotFoundError, ConnectionRefusedError, ConnectionResetError):
            await asyncio.sleep(1)