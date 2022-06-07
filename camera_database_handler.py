"""A Class for connecting to CAMERA RECORDS database"""
import database_connection
import json

connection = database_connection.DatabaseConnection().get_db_cursor()
cur = connection.cursor()

def to_json(params):
    """
    Convert response from db from list to JSON

    Args:
        params: reponse from db in list form

    Returns:
            Response from db in JSON form
    """
    response = []
    for each_record in params:
        record = {
            "id": each_record[0],
            "datetime": str(each_record[1]),
            "cameraid": each_record[2],
            "elephantname": each_record[3],
            "location": each_record[4],
        }
        response.append(record)
    return json.dumps(response)


class CameraDatabaseHandler:

    def get_elephants_records_from_camera(self):
        """
        Get elephant tracking record captured by camera from the db.

        Returns:
            collection of elephant tracking records sent by camera.
        """
        cur.execute(
                """SELECT * FROM elephantrecordscamera"""
            )
        return to_json(cur.fetchall())

    def get_specific_record_from_camera(self, camera_number):
        """
        Get the specific record of elephant tracking sent by camera_number

        Args:
            camera_number: camera id to get the info

        Returns:
            a json record of requested camera id
        """
        cur.execute(
                """SELECT * 
                    FROM elephantrecordscamera
                    WHERE cameraid = %s
                """, (camera_number,)
            )
        return to_json(cur.fetchall())
        # return cur.fetchone()

    def post_elephant_record_from_camera(self, record):
        """
        Post a record to camera db

        Args:
            record: record to post to db

        Returns:
            a json record that has been saved to db
        """
        cur.execute(
            """
            INSERT INTO elephantrecordscamera (cameraid, elephantname, location)
            VALUES (%s, %s, %s)
            """, (record.cameraid, record.elephantname, record.location)
        )
        connection.commit()
        return record
