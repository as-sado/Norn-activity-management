from norn.repository import get_data
from norn.utils.time_convert import time_convenrot
from asyncio import run
from norn.utils.date_correct import is_valid_date

def list_date(args):
    if is_valid_date(args.date):

        res = run(get_data.get_data_for_date(args.date))
        res.sort(key= lambda item: item[3], reverse=True)
        for i in res:
            time = time_convenrot(i[3])
            print(f"{time} {i[2]}")
        if res:
            total_seconds = sum(
                    row[3]
                    for row in res
                )
            total_time = time_convenrot(total_seconds)
        
            print(f"TOTAL TIME: {total_time}")

            print("  ")
        else:
            print("No entry found")

    else:
        print("Invalid date (YYYY-MM-DD)")

