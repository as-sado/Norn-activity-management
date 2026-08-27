import norn.handlers.Hyprland.monitor_data as md
from time import perf_counter
from norn.repository.update_ram_data import app_time_update
from norn.GUIsocket.Hyprland.commands import get_activewindow

async def update_actual_time():
    time_now = round(perf_counter(),1)
    try:
        time_diff = time_now - md.timer
        if time_diff >= 15:
            current_app = await get_activewindow()
            await app_time_update(current_app, time_diff)
            md.timer = time_now
            
    except:
        pass  

