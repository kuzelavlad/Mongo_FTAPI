from fastapi import APIRouter
from models.users import User
from config.database import collection_name
from schema.schemas import list_serial
from bson.objectid import ObjectId

router = APIRouter()


# GET Request Method
@router.get("/")
async def get_users():
    try:
        users = list_serial(collection_name.find())
        return {"users": users}
    except Exception as e:
        return print({"error": str(e)})


# POST Request Method
@router.post("/")
async def create_user(user: User):
    try:
        result = collection_name.insert_one(dict(user))
        return print({"inserted_id": str(result.inserted_id)})
    except Exception as e:
        return print({"error": str(e)})


# PUT Request Method
@router.put("/{id}")
async def update_user(id: str, user: User):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})


# DELETE Request Method
@router.delete("/{id}")
async def delete_user(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
