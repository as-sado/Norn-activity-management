from core.sql.dbConnect import DataBase

class CheckData(DataBase):

    async def check_date_permament(self, date):
        async with self:       
            await self.cursor.execute("""
                SELECT date
                FROM permanent_storage
                WHERE date = ?
                ORDER BY id DESC
                LIMIT 1
            """, (date,))

            res = await self.cursor.fetchone()
            return res