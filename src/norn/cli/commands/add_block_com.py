from norn.repository import add_data
from asyncio import run
from norn.utils.send_socket import notify_daemon
from norn.utils.check_daemon import check_daemon
from .start_com import start

def add_block(args):
    if check_daemon():
        print("norn-daemon is not running; run: norn start") 
        return None
    run(add_data.add_block_app(args.name, args.time*60))
    notify_daemon("block")
    