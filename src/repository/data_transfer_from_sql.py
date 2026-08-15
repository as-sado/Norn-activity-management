from .get_data import getData 
from core.app_data import data_active_app, data_block_app, data_block_app_interval

get_data = getData()

async def transfer_from_daily_storage():

    rows = await get_data.get_all_data_day()

    data_active_app.clear()

    for row in rows:
        data_active_app[row[1]] = row[2]



async def transfer_from_block_app():

    rows = await get_data.get_all_block_app()

    data_block_app.clear()

    for row in rows:
        data_block_app[row[1]] = row[2]


async def transfer_from_block_app_interval():

    rows = await get_data.get_all_data_block_interval()

    data_block_app_interval.clear()

    for row in rows:
        data_block_app_interval[row[1]] = [
            row[2],
            row[3]
        ]

    
