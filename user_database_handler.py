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
            "username": each_record[1],
            "hashed_pw": each_record[2]
        }
        response.append(record)
    return json.dumps(response)

class UserDatabaseHandler:
    def get_users_by_username(self, username):
        """
        Get a user from their username.

        Args:
            username: username of a user to get the info

        Returns:
            a json record of user
        """
        cur.execute(
                """SELECT * 
                    FROM public.user
                    WHERE username = %s
                """, (username,)
            )
        return to_json(cur.fetchall())
