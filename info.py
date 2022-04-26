from fastapi import APIRouter, Response
from database_handler import DatabaseHandler
from camera_database_handler import CameraDatabaseHandler
from schema import Record, CameraRecord

router = APIRouter()

db = DatabaseHandler()
cdb = CameraDatabaseHandler()


@router.get("/info")
def get_elephants_records():
    """
    Get the records of elephant from the database
    """
    data = db.get_elephants_records_db()

    return Response(content=data, media_type="application/json")


@router.get("/info-camera")
def get_elephants_records_from_camera():
    """
    Get the records of elephant from the camera database
    """
    data = cdb.get_elephants_records_from_camera()

    return Response(content=data, media_type="application/json")


@router.get("/info/{elephant_name}")
def get_specific_record(elephant_name):
    """
    Get the specific record of elephant from db

    """
    response = db.get_specific_record(elephant_name)
    return Response(content=response, media_type="application/json")


@router.get("/info-camera/{camera_number}")
def get_specific_record_from_camera(camera_number):
    """
    Get the specific record of elephant from camera db
    """
    response = cdb.get_specific_record_from_camera(camera_number)
    return Response(content=response, media_type="application/json")


@router.post("/info")
async def post_elephant_record(record: Record):
    """
    Send a record of elephant to the database
    """
    return db.post_elephant_record(record)


@router.post("/info-camera")
async def post_elephant_record_from_camera(record: CameraRecord):
    """
    Send a record of elephant to the camera database
    """
    return cdb.post_elephant_record_from_camera(record)

if __name__ == '__main__':
    # print(db)
    result = get_elephants_records()
    print(result)