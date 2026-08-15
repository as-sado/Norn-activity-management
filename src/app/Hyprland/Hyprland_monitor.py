import asyncio
from .base import BaseMethod

class HyprlandMonitor(BaseMethod):

    def __init__(self):
        self.event_queue = asyncio.Queue()
        self.loop = None

    async def run_monitor(self):

        self.loop = asyncio.get_running_loop()

        block_task = asyncio.create_task(
            self.block_apps_loop()
        )

        sql_task = asyncio.create_task(
            self.sql_loop()
        )

        event_task = asyncio.create_task(
            self.handle_events()
        )

        try:
            await asyncio.to_thread(
                self.listen_events
            )

        except KeyboardInterrupt:
            print("\nstop monitoring")

        finally:
            block_task.cancel()
            sql_task.cancel()
            event_task.cancel()

            await asyncio.gather(
                block_task,
                sql_task,
                event_task,
                return_exceptions=True
            )

    