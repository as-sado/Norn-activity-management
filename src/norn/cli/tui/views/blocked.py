from textual.widgets import Label, ListView, ListItem
import norn.cli.tui.data as db
from norn.utils.send_socket import async_notify_daemon
from norn.utils.time_convert import format_time


def update_blocked(app):

    blocked_list = app.query_one( "#blocked", ListView,)
    data_block_app = db.data_block_app

    if data_block_app:
        values = [(application,
                f"{format_time(data_block_app[application]):<8}    {application}",)
                for application in data_block_app
            ]

    else:
        values = [("__empty__", "No blocked applications.",)]

    signature = tuple( (key,text,) for key, text in values)
    if signature == app.blocked_signature:
        return

    app.blocked_signature = signature
    blocked_list.clear()

    for _, text in values:
        blocked_list.append(ListItem(Label(text)))