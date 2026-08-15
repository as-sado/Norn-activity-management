from repository import transfer_from_block_app, transfer_from_daily_storage, transfer_from_block_app_interval
from utils.change_data_for_date import data_migration
from utils.getCurrenGUI import get_current_GUI
from models.createTable import DataBaseTables
import asyncio

grafInterface = get_current_GUI() 

async def main():
    db = DataBaseTables()
    await db.connect()
    await db.create_tables()

  
    await data_migration()

    await transfer_from_daily_storage()
    await transfer_from_block_app() 
    await transfer_from_block_app_interval()



    task = asyncio.create_task(grafInterface.run_monitor()) 
    await task


if __name__ == "__main__":
    asyncio.run(main())


    
