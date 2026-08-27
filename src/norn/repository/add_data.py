from norn.core.sql.dbConnect import DataBase

class AddData(DataBase):
    async def add_app(self, app ,time):
        async with self:
            await self.cursor.execute("""
                INSERT INTO daily_storage (app, time)  
                VALUES (?,?) 
                """, (app, time)
            )

            await self.db.commit()

    async def add_block_app(self, app ,time):
        async with self:
                await self.cursor.execute("""
                    INSERT INTO block_app (app, time)  
                    VALUES (?,?) 
                    """, (app, time)
                )

                await self.db.commit()

    async def add_block_app_interval(self, app, time_start, time_end):
        async with self:
            await self.cursor.execute("""
                INSERT INTO block_app_interval (app, time_start, time_end)
                VALUES (?, ?, ?)
            """, (app, time_start, time_end))

            await self.db.commit()

    async def transfer_daily_to_permanent(self, date):
        async with self:
            await self.cursor.execute("""
                INSERT INTO permanent_storage (date, app, time)
                SELECT ?, app, time
                FROM daily_storage
            """, (date,))

            await self.db.commit()