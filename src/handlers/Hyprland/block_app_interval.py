from datetime import datetime
from core.app_data import  data_active_app, data_block_app_interval
from GUIsocket.Hyprland.commands import kill_by_pid
from asyncio import sleep
from utils.send_messege import send_message


async def block_interval():
    now = datetime.now()
    current_time = now.hour * 60 + now.minute

    for app, interval in data_block_app_interval.items():
        try:
            if not interval:
                continue

            start = datetime.strptime(interval[0], "%H:%M")
            end = datetime.strptime(interval[1], "%H:%M")

            start_time = start.hour * 60 + start.minute
            end_time = end.hour * 60 + end.minute

            if app not in data_active_app:
                continue
            if start_time <= current_time <= end_time:
                kill = await kill_by_pid(app)
                if not kill:
                    continue

                await send_message(
                    f"{app} заблокирован с {interval[0]} до {interval[1]}"
                )

        except Exception as e:
            print(f"Error blocking {app}: {e}")


async def block_interval_momental(current_app):
    now = datetime.now()
    current_time = now.hour * 60 + now.minute

    for app, interval in data_block_app_interval.items():
        try:
            if not interval:
                continue

            start = datetime.strptime(interval[0], "%H:%M")
            end = datetime.strptime(interval[1], "%H:%M")

            start_time = start.hour * 60 + start.minute
            end_time = end.hour * 60 + end.minute

            if app == current_app:
                    
                if start_time <= current_time <= end_time:
                    await sleep(0.5)
                    kill = await kill_by_pid(current_app)
                    if not kill:
                        continue

                await send_message(
                    f"{app} заблокирован c {interval[0]} до {interval[1]}"
                )

        except Exception as e:
            print(f"Error blocking {app}: {e}")