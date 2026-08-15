from core.app_data import data_block_app, data_active_app
from GUIsocket.Hyprland.commands import kill_by_pid
from asyncio import sleep
from utils.send_messege import send_message


async def block():
    try:
        for block_app, block_time in data_block_app.items():
            for app, time in data_active_app.items():
                if block_app == app and block_time <= time:
                        kill = await kill_by_pid(app)
                        if not kill:
                            continue
                        await send_message(
                            f"{block_app}, заблокирован по причине превышения времени: "
                            f"ограничение не более {block_time}"
            )
    except:
        pass


async def block_momental(current_app):

    for block_app, block_time in data_block_app.items():
        if block_app != current_app:
            continue

        current_time = data_active_app.get(current_app, 0)
        if current_time >= block_time:
            await sleep(0.5)

            kill = await kill_by_pid(current_app)

            if not kill:
                return

            await send_message(
                f"{current_app}, заблокирован по причине превышения времени: "
                f"ограничение не более {block_time}"
            )

