from fastapi import APIRouter, HTTPException
from models.todos import Todo
from config.database import collection_name 
from schema.schemas import list_serial, individual_serial
from bson import ObjectId 

router = APIRouter() 

@router.get("/")
async def get_todos():
  todos = list_serial(collection_name.find())
  return todos

@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))

@router.put("/{id}")
async def put_todo(id: str, todo: Todo): 
   result = collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
   if not result: 
      raise HTTPException(status_code=404, detail="todo not found")
      

@router.delete("/{id}")
async def delete_todo(id: str):
   todo = collection_name.find_one({"_id": ObjectId(id)})
   if not todo: 
      raise HTTPException(status_code=404, detail="todo not found")
   collection_name.delete_one({"_id": ObjectId(id)})

@router.get("/{id}")
async def get_todo(id: str): 
   todo = collection_name.find_one({"_id": ObjectId(id)})
   if not todo:
      raise HTTPException(status_code=404, detail="todo not found") 
   return individual_serial(todo)
