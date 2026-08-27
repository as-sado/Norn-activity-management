from norn.core.sql.dbConnect import DataBase


class DataBaseTables(DataBase):

    async def create_tables(self):
        async with self:
            await self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS daily_storage(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    app TEXT UNIQUE,
                    time REAL 
                ) 
            """)

            await self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS permanent_storage(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    app TEXT,
                    time REAL  
                )
            """)

            await self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS block_app(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    app TEXT,
                    time REAL 
                )
            """)

            await self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS block_app_interval(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    app TEXT,
                    time_start TEXT,
                    time_end TEXT
                )
            """)

            await self.db.commit()        


