import json
from norn.GUIsocket.Hyprland.commands import get_activewindow
from .block_app import block_momental
from .block_app_interval import block_interval_momental
from norn.repository import app_time_update
from norn.utils.time_difference import time_difference
import norn.handlers.Hyprland.monitor_data as md
from norn.utils.send_socket import async_notify_daemon


async def handler_active_app():

    try:
        current_app = await get_activewindow() 
        await async_notify_daemon(f"app[{current_app}]")   

        if current_app != md.last_app:
            time_diff, new_time = await time_difference(md.timer) 
            await app_time_update(md.last_app, time_diff)
            await block_momental(current_app)
            await block_interval_momental(current_app)

            md.timer = new_time
            md.last_app = str(current_app)

    except json.JSONDecodeError:
        pass
    except Exception as e:
        print(f"Error retrieving window data: {e}")
