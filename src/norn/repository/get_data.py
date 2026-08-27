from norn.core.sql.dbConnect import DataBase


class getData(DataBase):

    async def get_all_data_day(self):
        async with self:
            await self.cursor.execute("""
                SELECT * FROM daily_storage 
            """)
            
            res = await self.cursor.fetchall()
            await self.close()
            return res

    async def get_all_data(self):
        async with self:
            await self.cursor.execute("""
                SELECT * FROM permanent_storage 
            """)
            
            res = await self.cursor.fetchall()
            await self.close()
            return res

    async def get_all_data_block_interval(self):
        async with self:
            await self.cursor.execute("""
                SELECT * FROM block_app_interval
            """)
            
            res = await self.cursor.fetchall()
            await self.close()
            return res

    async def get_app_by_name(self,app):
        async with self:
            await self.cursor.execute(
                "SELECT app FROM daily_storage WHERE app = ?",
                (app,)
            )

            res = await self.cursor.fetchall()
            await self.close()
            return res

    async def get_all_block_app(self):
        async with self:
            await self.cursor.execute("""
                SELECT * FROM block_app 
            """)
            
            res = await self.cursor.fetchall()
            await self.close()
            return res

    async def get_data_for_date(self, date):
        async with self:
            await self.cursor.execute("""
                SELECT * FROM permanent_storage
                WHERE date = ?""", 
            (date,))

            res = await self.cursor.fetchall()
            await self.close()
            return res