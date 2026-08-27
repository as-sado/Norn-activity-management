import asyncio
from .base import BaseMethod
from norn.core.daemon_socket import socket_server


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
        socket_task = asyncio.create_task(
            socket_server()
        )
        actual_time_task = asyncio.create_task(
            self.actual_time_loop()
        )

        try:
            await self.listen_events()

        except KeyboardInterrupt:
            print("\nstop monitoring")

        finally:
            block_task.cancel()
            sql_task.cancel()
            event_task.cancel()
            socket_task.cancel()
            actual_time_task.cancel()

            await asyncio.gather(
                block_task,
                sql_task,
                event_task,
                actual_time_task,
                return_exceptions=True
            )

    