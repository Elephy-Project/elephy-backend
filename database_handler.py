"""A Class for connecting to database"""


class DatabaseHandler:

    def __init__(self):
        self.connect_to_db()

    async def connect_to_db(self):
        """
        Connect to the database.

        Returns:

        """
        return "successfully connect to the database"

    def get_elephants_records(self):
        """
        Get elephant tracking record from the db.

        Returns:
            collections of elephant tracking records
        """
        return

    def get_specific_record(self, record_number):
        """
        Get the specific record of elephant tracking

        Args:
            record_number: record id to get the info

        Returns:
            a json record of requested record_number
        """
        return
