from fastapi import APIRouter

user_router = APIRouter()
@user_router.get("/users/")
def get_users():
    return {"message": "Get all users"}


@user_router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"Get user with id {user_id}"}


@user_router.post("/users/")
def create_user():
    return {"message": "Create a new user"}



member_router = APIRouter()
@member_router.get("/members/")
def get_members():
    return {"message": "Get all members"}


@member_router.get("/members/{member_id}")
def get_member(member_id: int):
    return {"message": f"Get member with id {member_id}"}


@member_router.post("/members/")
def create_member():
    return {"message": "Create a new member"}
