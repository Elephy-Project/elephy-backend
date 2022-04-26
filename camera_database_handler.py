"""A Class for connecting to CAMERA RECORDS database"""
import psycopg2
import json
from dotenv import dotenv_values


config = dotenv_values(".env")


def to_json(params):
    response = {}
    for i in params:
        new_dict = {
            str(i[0]): {
                "date": i[1],
                "camera_id": i[2],
                "elephant_name": i[3],
                "location": i[4],
            }
        }
        response.update(new_dict)
    return json.dumps(response)


class CameraDatabaseHandler:

    def __init__(self):
        self.DATABASE_URL = config["CAMERA_DB_DATABASE_URL"]
        self.USER = config["CAMERA_DB_PGUSER"]
        self.PASSWORD = config["CAMERA_DB_PGPASSWORD"]
        self.PORT = config["CAMERA_DB_PGPORT"]
        self.DATABASE = config["CAMERA_DB_PGDATABASE"]
        self.HOST = config["CAMERA_DB_PGHOST"]
        self.db_cursor = None

    def get_db_cursor(self):
        """
        Connect to the database for camera.

        Returns:
            cursor to the database.
        """
        return psycopg2.connect(
            dbname=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT
        )

    def get_elephants_records_from_camera(self):
        """
        Get elephant tracking record captured by camera from the db.

        Returns:
            collection of elephant tracking records sent by camera.
        """
        # with self.get_db_cursor() as cs:
        #     cs.execute(
        cur = self.get_db_cursor().cursor()
        cur.execute(
                """SELECT * FROM elephant_records_camera"""
            )
        return to_json(cur.fetchall())

    def get_specific_record_from_camera(self, camera_number):
        """
        Get the specific record of elephant tracking sent by camera

        Args:
            camera_number: record id to get the info

        Returns:
            a json record of requested elephant_name
        """
        cur = self.get_db_cursor().cursor()
        cur.execute(
                """SELECT * 
                    FROM elephant_records_camera
                    WHERE camera_id=(%s)
                """, camera_number
            )
        return to_json([cur.fetchone()])
        # return cur.fetchone()

    def post_elephant_record_from_camera(self, record):
        """
        Post a record to camera db

        Args:
            record: record to post to db

        Returns:
            a json record that has been saved to db
        """
        cur = self.get_db_cursor().cursor()
        cur.execute(
            """
            INSERT INTO elephant_records_camera (id, datetime, camera_id, elephant_name, location)
            VALUES (%s, %s, %s, %s, %s)
            """, (record.id, record.datetime, record.camera_id, record.elephant_name, record.location)
        )
        return record
