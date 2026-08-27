from asyncio import run
from .status_com import status_util
from .start_com import start

def start_tui(args):
    from norn.cli.tui.app import main

    if status_util(None) == "inactive":
        start(None)
    
        run(main())
    else:
        run(main())