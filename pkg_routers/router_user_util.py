from fastapi import APIRouter

router = APIRouter()

@router.get("/users/")
def get_users():
    return {"message": "Get all users"}

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"Get user with id {user_id}"}

@router.post("/users/")
def create_user():
    return {"message": "Create a new user"}

