from core.app_data import data_active_app


async def app_time_update(window, time):

    if str(window) in data_active_app:
        data_active_app[str(window)] += round(time, 1)
    elif window is None:
        pass
    else:
        data_active_app[str(window)] = round(time,)