from datetime import datetime
import argparse

def parse_time(value):
    try:
        datetime.strptime(value, "%H:%M")
        return value
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"invalid time '{value}', expected HH:MM"
        )