current_app = None
from norn.core.app_data import  data_active_app, data_block_app, data_block_app_interval
from time import perf_counter

apps_time = data_active_app


def set_current_app(app_name):
    global current_app

    if app_name is None:
            return
    current_app = app_name
    

    if app_name not in apps_time:
        apps_time[app_name] = 0


def update_current_app(last_time):
    if current_app is None:
        return

    if current_app not in apps_time:
        apps_time[current_app] = 0
    try: 
        apps_time[current_app] += (perf_counter() - last_time)
    except:
        apps_time[current_app] += 1
    return perf_counter()