"""A Class for connecting to USER RECORDS database"""
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
            "informant": each_record[2],
            "elephant_name": each_record[3],
            "location": each_record[4]
        }
        response.append(record)
    return json.dumps(response)


class DatabaseHandler:

    def get_elephants_records_db(self):
        """
        Get elephant tracking record from the db.

        Returns:
            collections of elephant tracking records
        """
        cur.execute(
                """SELECT * FROM human_record"""
            )
        return to_json(cur.fetchall())
        # return cur.fetchall()

    def get_specific_record(self, elephant_name):
        """
        Get all records of the elephant name whose name is elephant_name.

        Args:
            elephant_name: elephant name to get the info

        Returns:
            a json record of requested elephant_name
        """
        cur.execute(
                """SELECT * 
                    FROM human_record INNER JOIN camera_record ON 1=1 
                    WHERE human_record.elephant_name = %s or camera_record.elephant_name = %s
                """, (elephant_name, elephant_name)
            )
        return to_json(cur.fetchall())

    def post_elephant_record(self, record):
        """
        Post the specific record to the db

        Args:
            record: record to post to db

        Returns:
            a json record that has been saved to db
        """
        cur.execute(
            """
            INSERT INTO human_record (informant, elephant_name, location)
            VALUES (%s, %s, %s)
            """, (record.informant, record.elephant_name, record.location)
        )
        connection.commit()
        return record
