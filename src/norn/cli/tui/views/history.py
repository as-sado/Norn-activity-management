from textual.widgets import Label, ListItem, ListView

from norn.repository import get_data

from norn.utils.time_convert import format_time


async def load_history(app,date):

    history_list = app.query_one("#history",ListView,)
    app.history_date = date

    try:
        history_list.clear()

        rows = await get_data.get_data_for_date(date)
        if not rows:
            history_list.append(ListItem(Label(f"No data for {date}")))
            app.query_one("#history-title",Label).update(f"HISTORY — {date}")

            return

        sorted_rows = sorted(rows, key=lambda row: row[3], reverse=True,)

        for row in sorted_rows:
            time = row[3]
            time_form = format_time(time)
            history_list.append(ListItem(Label(f"{time_form:<8}    {row[2]}")))

        total_seconds = sum(row[3] for row in rows)
        total_time = format_time(total_seconds)
        app.query_one("#history-title", Label).update(f"HISTORY — {date} — TOTAL: {total_time}")

    except Exception as e:
        history_list.clear()
        history_list.append(ListItem(Label(f"Error: {e}")))
