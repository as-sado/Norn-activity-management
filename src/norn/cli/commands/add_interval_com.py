from norn.repository import add_data
from asyncio import run
from norn.utils.time_convert import normalize_time
from norn.utils.send_socket import notify_daemon
from norn.utils.check_daemon import check_daemon

def add_interval(args):
    if check_daemon():
        print("norn-daemon is not running; run: norn start") 
        return None
    run(add_data.add_block_app_interval(args.name, 
                                        normalize_time(args.start),
                                        normalize_time(args.end)))
    notify_daemon("interval")


