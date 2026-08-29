from norn.repository import get_data
from asyncio import run
from norn.utils.time_convert import time_convenrot
from norn.utils.check_daemon import check_daemon
from .start_com import start

def list(args):
    if check_daemon():
        print("norn-daemon is not running; run: norn start") 
        return None
    res = run(get_data.get_all_data_day())
    res.sort(key= lambda item: item[2], reverse=True)
    for i in res:
        time = time_convenrot(i[2])
        print(f"{time} {i[1]}")

    print("  ")
