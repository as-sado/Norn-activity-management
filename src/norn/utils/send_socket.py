import asyncio


async def send_socket(command):

    reader, writer = await asyncio.open_unix_connection(
        "/tmp/norn.sock"
    )

    writer.write(f"{command}\n".encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()


def notify_daemon(command):
    asyncio.run(send_socket(command))


async def async_notify_daemon(command):
    await send_socket(command)