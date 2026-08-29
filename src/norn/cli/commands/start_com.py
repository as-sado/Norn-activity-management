from subprocess import run
from .status_com import status_util

def start(args):
    if status_util(None) == "active":
        print("The Norn daemon is already started")
        return 
    run(
        ["systemctl", "--user", "start", "norn.service"],
        check=True,
    )


    print("Norn daemon started")

