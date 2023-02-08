from fastapi import APIRouter, Response
from database_handler import DatabaseHandler
from camera_database_handler import CameraDatabaseHandler
from schema import Record, Camera

router = APIRouter()

db = DatabaseHandler()
cdb = CameraDatabaseHandler()


@router.get("/elephant-records")
def get_elephants_records():
    """
    Get the records of elephant from the database
    """
    data = db.get_elephants_records_db()
    return Response(content=data, media_type="application/json")


@router.get("/info-camera")
def get_data_camera():
    """
    Get the records of camera information
    """
    data = cdb.get_all_camera()

    return Response(content=data, media_type="application/json")


@router.get("/elephant-records/{informant_name}")
def get_specific_record(informant_name):
    """
    Get the specific record of elephant from db using informant_name

    """
    response = db.get_specific_record_by_informant(informant_name)
    return Response(content=response, media_type="application/json")


@router.get("/info-camera/{camera_id}")
def get_specific_record_from_camera(camera_id):
    """
    Get the specific record of camera data from camera db
    """
    response = cdb.get_specific_camera(camera_id)
    return Response(content=response, media_type="application/json")


@router.post("/record")
async def post_elephant_record(record: Record):
    """
    Send a record of elephant to the database
    """
    return db.post_elephant_record(record)


@router.post("/info-camera")
async def post_new_camera(record: Camera):
    """
    Add new camera to database
    """
    return cdb.post_new_camera(record)
