import aiosqlite
from norn.config import DATABASE_SQL_PATH

class DataBase:
    def __init__(self):
        self.path = DATABASE_SQL_PATH
        self.db = None
        self.cursor = None

    async def connect(self):
        self.db = await aiosqlite.connect(self.path)
        self.cursor = await self.db.cursor()

    async def close(self):
        await self.db.close()


    async def __aenter__(self):
        self.db = await aiosqlite.connect(self.path)
        self.cursor = await self.db.cursor()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.db:
            await self.db.close()

    
