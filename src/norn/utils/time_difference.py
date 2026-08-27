import time

async def time_difference(last_time):
    new_time = round(time.perf_counter(), 1)
    return round(new_time - last_time, 1), new_time


