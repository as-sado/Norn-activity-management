from datetime import datetime
from norn.core.app_data import data_block_app_interval
from norn.GUIsocket.Hyprland.commands import kill_by_pid, get_all_app
from asyncio import sleep
from norn.utils.send_messege import send_message
from datetime import datetime


async def block_interval():
    now = datetime.now()
    current_time = now.hour * 60 + now.minute

    for app, intervals in data_block_app_interval.items():
        try:
            if not intervals:
                continue

            data_active_app = await get_all_app()

            if app not in data_active_app:
                continue

            for interval in intervals:
                start = datetime.strptime(interval[0], "%H:%M")

                end = datetime.strptime(interval[1], "%H:%M")

                start_time = start.hour * 60 + start.minute
                end_time = end.hour * 60 + end.minute

                if start_time <= end_time:
                    is_blocked = (start_time <= current_time <= end_time)

                else:
                    is_blocked = (current_time >= start_time or current_time <= end_time)

                if not is_blocked:
                    continue

                kill = await kill_by_pid(app)

                if not kill:
                    continue

                await send_message(
                    f"{app} blocked from {interval[0]} to {interval[1]}")

        except Exception as e:
            print(
                f"Error blocking {app}: {e}"
            )


async def block_interval_momental(current_app):
    now = datetime.now()
    current_time = now.hour * 60 + now.minute

    if current_app not in data_block_app_interval:
        return

    intervals = data_block_app_interval[current_app]

    for interval in intervals:
        try:
            start = datetime.strptime(interval[0], "%H:%M")
            end = datetime.strptime(interval[1],"%H:%M")

            start_time = start.hour * 60 + start.minute
            end_time = end.hour * 60 + end.minute

            if start_time <= end_time:
                is_blocked = (start_time <= current_time <= end_time)
            else:
                is_blocked = (current_time >= start_time or current_time <= end_time)

            if not is_blocked:
                continue

            await sleep(1)

            kill = await kill_by_pid(current_app)

            if not kill:
                continue

            await send_message(
                f"{current_app} blocked from {interval[0]} to {interval[1]}")

            break

        except Exception as e:
            print(
                f"Error blocking {current_app}: {e}"
            )
