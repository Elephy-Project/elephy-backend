"""A Class for connecting to USER RECORDS database"""
import psycopg2
import psycopg2.extras
import json
from dotenv import dotenv_values

config = dotenv_values(".env")
psycopg2.extras.register_uuid()


def to_json(params):
    response = {}
    for i in params:
        new_dict = {
            str(i[0]): {
                "date": i[1],
                "informant": i[2],
                "elephant_name": i[3],
                "location": i[4],
            }
        }
        response.update(new_dict)
    return json.dumps(response)


class DatabaseHandler:

    def __init__(self):
        self.DATABASE_URL = config["DATABASE_URL"]
        self.USER = config["PGUSER"]
        self.PASSWORD = config["PGPASSWORD"]
        self.PORT = config["PGPORT"]
        self.DATABASE = config["PGDATABASE"]
        self.HOST = config["PGHOST"]
        self.db_cursor = None

    def get_db_cursor(self):
        """
        Connect to the database.

        Returns:

        """
        # try:
        return psycopg2.connect(
            dbname=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT
        )
        #     print("successfully connect to the database")
        # except Exception as e:
        #     SystemError("A problem happens during the db connection", e)
        #     exit(1)

    def get_elephants_records_db(self):
        """
        Get elephant tracking record from the db.

        Returns:
            collections of elephant tracking records
        """
        # with self.get_db_cursor() as cs:
        #     cs.execute(
        cur = self.get_db_cursor().cursor()
        cur.execute(
                """SELECT * FROM elephant_records"""
            )
        return to_json(cur.fetchall())

    def get_specific_record(self, elephant_name):
        """
        Get the specific record of elephant tracking

        Args:
            elephant_name: record id to get the info

        Returns:
            a json record of requested record_number
        """
        # elephant_name = str(elephant_name)
        cur = self.get_db_cursor().cursor()
        cur.execute(
                """SELECT * 
                    FROM elephant_records
                    WHERE elephant_name = %s
                """, elephant_name
            )
        return to_json([cur.fetchone()])

    def post_elephant_record(self, record):
        """
        Post the specific record to the db

        Args:
            record: record to post to db

        Returns:
            a json record that has been saved to db
        """
        cur = self.get_db_cursor().cursor()
        cur.execute(
            """
            INSERT INTO elephant_records (id, datetime, informant, elephant_name, location)
            VALUES (%s, %s, %s, %s, %s)
            """, (record.id, record.datetime, record.informant, record.elephant_name, record.location)
        )
        return record


# if __name__ == '__main__':
#     db = DatabaseHandler()
#     result = await db.get_elephants_records_db()
#     print(result)
# {
#   "id": "80ef9d71-6fde-4adf-b414-5d103bf6f81d",
#   "datetime": "2022-04-26T19:11:27.422Z",
#   "informant": "admin",
#   "elephant_name": "test",
#   "location": "f01"
# }