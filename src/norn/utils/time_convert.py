

def time_convenrot(time):
    str_len = 10
    total_minuts = time // 60
    hours = int(total_minuts // 60)
    minutes = int(total_minuts % 60)

    if minutes == 0:
        minutes =1

    if hours == 0:
        string = f"{minutes}m"
    else:
        string = f"{hours}h {minutes}m"


    length = len(string)

    return string + " " * (str_len - length)


def normalize_time(value: str) -> str:
    hours, minutes = value.split(":")
    return f"{hours.zfill(2)}:{minutes.zfill(2)}"


def format_time(seconds):
    seconds = int(seconds)

    hours, remainder = divmod(
        seconds,
        3600,
    )

    minutes = remainder // 60

    if hours:
        return f"{hours}h {minutes}m"

    return f"{max(minutes, 1)}m"