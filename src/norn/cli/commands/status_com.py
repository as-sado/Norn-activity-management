from subprocess import run

result = run(
        ["systemctl", "--user", "is-active", "norn.service"],
        capture_output=True,
        text=True,
    )

def status(args):

    print(result.stdout.strip())

def status_util(args):
    return result.stdout.strip()