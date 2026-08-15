from .update_data import UpdateData
from .get_data import getData
from .add_data import AddData
from .delete_data import DeleteData
from .update_ram_data import app_time_update
from .check_data import CheckData
from .data_transfer_from_sql import transfer_from_block_app_interval, transfer_from_block_app,transfer_from_daily_storage

update_data = UpdateData()
get_data = getData()
add_data = AddData()
delete_data = DeleteData()
check_data = CheckData()
get_lock_data = getData()

__all__= [
    "update_data",
    "get_data",
    "time_update",
    "add_data",
    "delete_data",
    "check_data",
    "get_lock_data"
]