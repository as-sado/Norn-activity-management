from typing import Protocol


class StartApp(Protocol):

    async def run_monitor(self):
        pass