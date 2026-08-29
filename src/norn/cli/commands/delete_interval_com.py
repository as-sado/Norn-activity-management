from norn.repository import delete_data
from asyncio import run
from norn.utils.send_socket import notify_daemon
from norn.utils.check_daemon import check_daemon
from .start_com import start

def delete_interval(args):
    if check_daemon():
        print("norn-daemon is not running; run: norn start")        
        return None     
    run(delete_data.delete_block_app_interval(args.name))
    notify_daemon("interval")



