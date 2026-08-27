from norn.repository import add_data
from asyncio import run
from norn.utils.send_socket import notify_daemon

def add_block(args):
    run(add_data.add_block_app(args.name, args.time*60))
    notify_daemon("block")
    