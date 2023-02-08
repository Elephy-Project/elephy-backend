"""A Class for connecting to CAMERA RECORDS database"""
import database_connection
import json

connection = database_connection.DatabaseConnection().get_db_cursor()
cur = connection.cursor()

def to_json(params):
    """
    Convert response from db from list to JSON

    Args:
        params: response from db in list form

    Returns:
        Response from db in JSON form
    """
    response = []
    for each_record in params:
        record = {
            "id": each_record[0],
            "datetime": str(each_record[1]),
            "camera_id": each_record[2],
            "location_lat": each_record[3],
            "location_long": each_record[4],
        }
        response.append(record)
    return json.dumps(response)


class CameraDatabaseHandler:

    def get_all_camera(self):
        """
        Get all cameras data

        Returns:
            collection of cameras.
        """
        cur.execute(
                """SELECT * FROM camera"""
            )
        return to_json(cur.fetchall())

    def get_specific_camera(self, camera_id):
        """
        Get the specific data of camera

        Args:
            camera_id: camera id to get the info

        Returns:
            a json record of requested camera id
        """
        cur.execute(
                """SELECT * 
                    FROM camera
                    WHERE camera_id = %s
                """, (camera_id,)
            )
        return to_json(cur.fetchall())
        # return cur.fetchone()

    def post_new_camera(self, camera):
        """
        Post a camera information to camera db

        Args:
            camera: camera information to insert to db

        Returns:
            a json record that has been saved to db
        """
        cur.execute(
            """
            INSERT INTO camera (camera_id, location_lat, location_long)
            VALUES (%s, %s, %s)
            """, (camera.camera_id, camera.location_lat, camera.location_long)
        )
        connection.commit()
        return camera
