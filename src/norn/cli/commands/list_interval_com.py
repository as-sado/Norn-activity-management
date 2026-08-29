from norn.repository import get_data
from asyncio import run
from norn.utils.check_daemon import check_daemon
from .start_com import start

def list_interval(args):
    if check_daemon(None):
        print("norn-daemon is not running; run: norn start") 
        return None
    res = run(get_data.get_all_data_block_interval())
    for i in res: 
        print(f"{i[1]}   {i[2]} {i[3]}")

    print(" ")