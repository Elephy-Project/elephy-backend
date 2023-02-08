"""A Class for connecting to USER RECORDS database"""
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
            "informant": each_record[2],
            "location_lat": each_record[3],
            "location_long": each_record[4]
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
                """SELECT * FROM record"""
            )
        return to_json(cur.fetchall())
        # return cur.fetchall()

    def get_specific_record_by_informant(self, informant):
        """
        Get all records of the informant name whose name is .

        Args:
            informant: informant name to get the info

        Returns:
            a json record of requested elephant_name
        """
        cur.execute(
                """SELECT * 
                    FROM record
                    WHERE informant = %s
                """, (informant,)
            )
        return to_json(cur.fetchall())

    def post_elephant_record_by_human(self, record):
        """
        Post the specific record to the db, sender is human

        Args:
            record: record to post to db

        Returns:
            a json record that has been saved to db
        """
        cur.execute(
            """
            INSERT INTO record (informant, location_lat, location_long)
            VALUES (%s, %s, %s)
            """, (record.informant, record.location_lat, record.location_long)
        )
        connection.commit()
        return record

    def post_elephant_record_by_camera(self, record):
        """
        Post the specific record to the db, sender is camera

        Args:
            record: record to post to db

        Returns:
            a json record that has been saved to db
        """
        cur.execute(
            """
            INSERT INTO record (informant)
            VALUES (%s)
            """, (record.informant,)
        )
        connection.commit()
        return record
