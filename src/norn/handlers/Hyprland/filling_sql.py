from norn.core.app_data import data_active_app
from norn.repository import get_data, update_data, add_data


async def fill_sql():
    try:
        for app, time in list(data_active_app.items()):

            res = await get_data.get_app_by_name(app)
            if not res:
                await add_data.add_app(app, time)
            else:
                await update_data.set_time_app(app, time)
        return True
    except:
        return False