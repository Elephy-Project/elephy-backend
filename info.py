from fastapi import APIRouter

router = APIRouter()


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
    """get the records of elephant from the database"""
    return "return list of elephant records form db"


@router.get("/summary")
async def summary_elephants_records():
    """get the summary of elephant from the database"""
    return "return summary of elephant records form db"

