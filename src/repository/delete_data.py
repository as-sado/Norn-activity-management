from core.sql.dbConnect import DataBase

class DeleteData(DataBase):

    async def delete_block_app(self, app):
        async with self:
            await self.cursor.execute("""
                DELETE FROM block_app
                WHERE app = ? 
                """,
                (app,)
            )

            await self.db.commit()


    async def delete_daily_data(self):
        async with self:
            await self.cursor.execute("""
                DELETE FROM daily_storage
            """)

            await self.db.commit()

    async def delete_storage_data(self):
        async with self:
            await self.cursor.execute("""
                DELETE FROM permanent_storage
            """)

            await self.db.commit()





