from norn.repository import get_data
from asyncio import run

def list_interval(args):
    r = run(get_data.get_all_data_block_interval())
    for i in r: 
        print(f"{i[1]}   {i[2]} {i[3]}")

    print(" ")