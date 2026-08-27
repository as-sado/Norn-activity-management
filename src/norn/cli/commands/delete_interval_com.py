from norn.repository import delete_data
from asyncio import run
from norn.utils.send_socket import notify_daemon


def delete_interval(args):
    run(delete_data.delete_block_app_interval(args.name))
    notify_daemon("interval")



