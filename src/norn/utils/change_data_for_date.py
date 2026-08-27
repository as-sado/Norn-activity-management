import json
from datetime import date
from norn.repository import add_data, delete_data, check_data
from norn.core.app_data import data_active_app
from norn.config import STATE_SQL_PATH

async def change_data(yesterday):
    if await check_data.check_date_permament(yesterday) is None:
        await add_data.transfer_daily_to_permanent(yesterday)
        await delete_data.delete_daily_data()
        data_active_app.clear() 


async def data_migration():
    with open(str(STATE_SQL_PATH), "r") as file:
        data = json.load(file)

    today = date.today().isoformat()
    saved_date = data.get("date")

    if saved_date == today:
        return False

    data["date"] = today
    await change_data(saved_date)
    with open(str(STATE_SQL_PATH), "w") as file:
        json.dump(data, file, indent=4)

    



