"""A Class for connecting to database"""
import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env")


class DatabaseHandler:

    def __init__(self):
        self.DATABASE_URL = config["DATABASE_URL"]
        self.USER = config["PGUSER"]
        self.PASSWORD = config["PGPASSWORD"]
        self.PORT = config["PGPORT"]
        self.DATABASE = config["PGDATABASE"]
        self.HOST = config["PGHOST"]
        self.db_cursor = None

    async def db_cursor(self):
        """
        Connect to the database.

        Returns:

        """
        # try:
        return await psycopg2.connect(
            dbname=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT
        ).cursor()
        #     print("successfully connect to the database")
        # except Exception as e:
        #     SystemError("A problem happens during the db connection", e)
        #     exit(1)

    def get_elephants_records(self):
        """
        Get elephant tracking record from the db.

        Returns:
            collections of elephant tracking records
        """
        with self.db_cursor() as cs:
            cs.execute(
                """SELECT * FROM elephant_records"""
            )
        return cs.fetchall()

    def get_specific_record(self, record_number):
        """
        Get the specific record of elephant tracking

        Args:
            record_number: record id to get the info

        Returns:
            a json record of requested record_number
        """
        return


# if __name__ == '__main__':
#     db = DatabaseHandler()
#     result = await db.get_elephants_records()
#     print(result)