from norn.repository import delete_data
from asyncio import run
from norn.utils.send_socket import notify_daemon

def delete_block(args):
    run(delete_data.delete_block_app(args.name))
    notify_daemon("block")
