from subprocess import run


def stop(args):
    run(
        ["systemctl", "--user", "stop", "norn.service"],
        check=True,
    )

    print("Norn daemon stoped")   