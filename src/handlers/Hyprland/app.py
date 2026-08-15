import json
from GUIsocket.Hyprland.commands import get_activewindow
from .block_app import block_momental
from .block_app_interval import block_interval_momental
from repository import app_time_update
from utils.time_difference import time_difference
from .monitor_data import  timer, current_app, time_diff, last_app


async def handler_active_app():
    global last_app, timer, current_app, time_diff
    try:
        current_app = await get_activewindow() 
        if current_app == None:
            return None

        if current_app != last_app:
            time_diff, new_time = await time_difference(timer) 
            await app_time_update(last_app, time_diff)
            await block_momental(current_app)
            await block_interval_momental(current_app)

            timer = new_time
            last_app = str(current_app)


    except json.JSONDecodeError:
        pass
    except Exception as e:
        print(f"Error retrieving window data: {e}")
