from norn.repository import get_data
from asyncio import run
from norn.utils.time_convert import time_convenrot


def list_block(args):
    r = run(get_data.get_all_block_app())
    for i in r: 
        time = time_convenrot(i[2])
        print(f"{time} {i[1]}")

    print(" ")