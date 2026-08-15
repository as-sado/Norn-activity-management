from asyncio import create_subprocess_exec

async def send_message(message):
    process = await create_subprocess_exec(
        "notify-send",
        "Norn",
        message
    )

    await process.wait()