from textual.widgets import Label, ListView
import norn.cli.tui.data as db
from norn.cli.tui.list_utils import update_list


def update_apps(app, app_items, app_order, format_time,):

    sorted_apps = sorted(db.apps_time.items(), key=lambda item: item[1],reverse=True,)
    values = [(application,
            f"{format_time(seconds):<8}    {application}",)
            for application, seconds in sorted_apps
        ]

    apps_list = app.query_one("#apps", ListView,)
    update_list(apps_list, app_items, app_order, values,)

    total_seconds = sum(db.apps_time.values())
    total_time = format_time(total_seconds)

    app.query_one("#apps-total",Label,).update(f"TOTAL: {total_time}")