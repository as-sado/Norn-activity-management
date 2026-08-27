from textual.widgets import Label, ListItem, ListView
from norn.utils.send_socket import send_socket
import norn.cli.tui.data as db
from asyncio import run
from norn.utils.send_messege import send_message
import asyncio

def update_intervals(app):
    intervals_list = app.query_one("#intervals",ListView)
    values = []
    data_block_app_interval = (db.data_block_app_interval)

    if data_block_app_interval:
        for application, intervals in (data_block_app_interval.items()):
            if (isinstance(intervals, list) and len(intervals) == 2 and all(
                    isinstance(value, str) for value in intervals
                )
            ):
                start, end = intervals
                values.append((f"{start} - {end}    {application}",))

            else:
                for interval in intervals:
                    if (isinstance(interval, (list, tuple)) and len(interval) == 2):
                        start, end = interval
                        values.append((f"{start} - {end}    {application}"))

    if not values:
        values = [("No intervals.")]

    signature = tuple(value[0]for value in values)
    if signature == app.intervals_signature:
        return

    app.intervals_signature = signature
    intervals_list.clear()
    for value in values:
        intervals_list.append(ListItem(Label(value[0])))
