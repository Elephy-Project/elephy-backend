from fastapi import APIRouter
from database_handler import DatabaseHandler

router = APIRouter()
db = DatabaseHandler()

# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]
#
#
# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}


@router.get("/info")
async def get_elephants_records():
    """
    Get the records of elephant from the database connection

    """
    return db.get_elephants_records()


@router.get("/info/{record_number}")
async def get_elephant_record(record_number):
    """
    Get the specific record of elephant from db

    """
    return db.get_specific_record(record_number)


@router.get("/summary")
async def summary_elephants_records():
    """get the summary of elephant from the database"""
    return "return summary of elephant records form db"

