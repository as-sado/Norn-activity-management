from norn.repository import delete_data
from asyncio import run
from norn.utils.send_socket import notify_daemon
from norn.utils.check_daemon import check_daemon

def delete_block(args):
    if check_daemon():
        print("norn-daemon is not running; run: norn start") 
        return None
    run(delete_data.delete_block_app(args.name))
    notify_daemon("block")
