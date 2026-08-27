from norn.utils import grafInterface
from norn.repository import transfer_from_block_app, transfer_from_daily_storage, transfer_from_block_app_interval
from norn.utils.change_data_for_date import data_migration
from norn.models import dbcon
from norn.repository import add_data, delete_data
import asyncio

async def create_app():
    await dbcon.connect()
    await dbcon.create_tables()
    await dbcon.close()

    await data_migration()

    await transfer_from_daily_storage()
    await transfer_from_block_app() 
    await transfer_from_block_app_interval()



async def app():
    await create_app()
    await grafInterface.run_monitor()

def run_app():
    asyncio.run(app())

run_app()
    