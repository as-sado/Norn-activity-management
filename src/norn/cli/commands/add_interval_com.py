from norn.repository import add_data
from asyncio import run
from norn.utils.time_convert import normalize_time
from norn.utils.send_socket import notify_daemon

def add_interval(args):
    run(add_data.add_block_app_interval(args.name, 
                                        normalize_time(args.start),
                                        normalize_time(args.end)))
    notify_daemon("interval")


