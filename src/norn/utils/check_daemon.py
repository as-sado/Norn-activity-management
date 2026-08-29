from subprocess import run

result = run(
        ["systemctl", "--user", "is-active", "norn.service"],
        capture_output=True,
        text=True,
    )

def check_daemon():
    
    res = result.stdout.strip()
    if res == "active":
        return False
    return True