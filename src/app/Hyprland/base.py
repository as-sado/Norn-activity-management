from hyprland_socket import listen
from handlers.Hyprland.block_app import block
from handlers.Hyprland.block_app_interval import block_interval
from handlers.Hyprland.filling_sql import fill_sql
from handlers.Hyprland.app import handler_active_app
from utils.change_data_for_date import data_migration
import asyncio

class BaseMethod:
    def listen_events(self):

        for event in listen():

            if event.name in [
                "activewindow",
                "activewindowv2"
            ]:
                self.loop.call_soon_threadsafe(
                    self.event_queue.put_nowait,
                    event
                )

    async def handle_events(self):

        while True:

            event = await self.event_queue.get()

            await handler_active_app()

    async def block_apps_loop(self):

        while True:

            await asyncio.sleep(10)
            try:
                await block() 
                await block_interval()

            except Exception as e:
                print(
                    f"Error checking block: {e}"
                )

    async def sql_loop(self):

        while True:

            await asyncio.sleep(30)

            try:
                if await fill_sql():
                    await data_migration()


            except Exception as e:
                print(
                    f"Error saving data: {e}"
                )

