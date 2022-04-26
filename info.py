from fastapi import APIRouter
from database_handler import DatabaseHandler

router = APIRouter()


# async def db_connect():
#     return await DatabaseHandler().db_cursor()
#
#
# db = db_connect()
db = DatabaseHandler()


@router.get("/info")
async def get_elephants_records():
    """
    Get the records of elephant from the database
    """
    # return await db.get_elephants_records()
    return "get a record"


@router.get("/info/{record_number}")
async def get_specific_record(record_number):
    """
    Get the specific record of elephant from db

    """
    # return await db.get_specific_record(record_number)
    return "get a record"


@router.get("/summary")
async def summary_elephants_records():
    """get the summary of elephant from the database"""
    return "return summary of elephant records form db"


@router.post("/info")
async def post_elephant_record():
    """
    Send a record of elephant to the database
    """
    return "send record"

# if __name__ == '__main__':
#     # print(db)
#     result = get_elephants_records()
#     print(result)