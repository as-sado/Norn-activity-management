from norn.core.sql.dbConnect import DataBase

class UpdateData(DataBase):

    async def set_time_app(self, app ,time):
        async with self:
            await self.cursor.execute(
                "UPDATE daily_storage SET time = ? WHERE app = ?",
                (time, app)
            )

            await self.db.commit()

    