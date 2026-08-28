import asyncio
from textual.app import App, ComposeResult
from textual.theme import Theme
from textual.widgets import Label, Input
import norn.cli.tui.data as db
from norn.cli.tui.socket_tui import socket_server_tui
from norn.utils.time_convert import format_time
from time import perf_counter

from norn.cli.tui.navigation import NavigationMixin
from norn.cli.tui.views.apps import update_apps
from norn.cli.tui.views.blocked import update_blocked
from norn.cli.tui.views.intervals import update_intervals
from norn.cli.tui.views.input import handle_input_submitted
from norn.cli.tui.style.wal_colors import get_theme_variables, generate_colors_tcss

from norn.cli.tui.compose import compose_ui

from norn.repository.data_transfer_from_sql import transfer_from_block_app, transfer_from_block_app_interval, transfer_from_daily_storage


data_block_app = db.data_block_app
data_block_app_interval = db.data_block_app_interval


class NornApp(NavigationMixin, App):

    CSS_PATH = ["style/app.tcss", "style/colors.tcss"]

    def __init__(self):
        super().__init__()

        self.current_app = None
        self.socket_task = None
        self.current_view = "apps"

        self.app_items = {}
        self.blocked_items = {}
        self.interval_items = {}
        self.history_items = {}

        self.app_order = []
        self.blocked_order = []
        self.interval_order = []
        self.history_order = []

        self.history_date = None
        self.intervals_signature = None
        self.blocked_signature = None
        self.last_time = perf_counter()

        self.register_theme(
            Theme(
                name="wal",
                primary=get_theme_variables()["accent-color"],
                accent=get_theme_variables()["accent-color"],
                background=get_theme_variables()["background"],
                foreground=get_theme_variables()["text-color"],
                variables=get_theme_variables(),
            )
        )
        self.theme = "wal"



    def compose(self) -> ComposeResult:

        yield from compose_ui()


    async def on_mount(self):

        self.socket_task = asyncio.create_task(socket_server_tui())
        self.show_view("apps")
        self.update_tui()
        self.set_interval(1,self.update_tui)


    def update_tui(self):

        res = db.update_current_app(self.last_time)
        self.last_time = res
        if db.current_app != self.current_app:
            self.current_app = db.current_app
            self.query_one("#current-app",Label).update(self.current_app or "-")

        update_apps(self, self.app_items, self.app_order, format_time)
        update_blocked(self)
        update_intervals(self)


    async def on_input_submitted(self, event: Input.Submitted):

        await handle_input_submitted(self, event)


    async def on_unmount(self):

        if self.socket_task:
            self.socket_task.cancel()
            try:
                await self.socket_task

            except asyncio.CancelledError:
                pass


async def main():
    await transfer_from_block_app()
    await transfer_from_block_app_interval()
    await transfer_from_daily_storage()

    generate_colors_tcss() 

    app = NornApp()

    await app.run_async()

if __name__ == "__main__":
    asyncio.run(main())