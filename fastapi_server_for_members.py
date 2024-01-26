# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'

import asyncio
import inspect
# from app.routes import index, auth
import json
import logging
import os
import random
from typing import Union
from uuid import uuid4

# from venv import create
import uvicorn
from fastapi import FastAPI, routing
# ! import 에 주석은 import 백업임 지우지말자. 오름차순 정리를 하자. 백업했으면 ctrl alt o를 누르자
from fastapi import Request, HTTPException, UploadFile
from fastapi.encoders import jsonable_encoder
from mangum import Mangum
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from pkg_park4139 import StateManagementUtil, DataObjectUtil, FileSystemUtil, DebuggingUtil, FastapiServerUtil, ColoramaColorUtil, TestUtil, BusinessLogicUtil

# :: SERVER SETTING
app = FastAPI()  # default
handler = Mangum(app)  # ?
app.mount("/$cache_favicon", StaticFiles(directory="$cache_favicon"), name="$cache_favicon")
app.encoding = 'utf-8'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

logger = logging.getLogger(__name__)
settings = FastapiServerUtil.Settings()
FastapiServerUtil.init_ip_address_allowed(app)
FastapiServerUtil.init_domain_address_allowed(app)
FastapiServerUtil.init_cors_policy_allowed(app)

MEMBERS_JSON = StateManagementUtil.MEMBERS_JSON
MEMBERS = FastapiServerUtil.init_and_update_json_file(MEMBERS_JSON)


# 파비콘 처리
@app.get('/favicon.ico', include_in_schema=False)
async def get_favicon():
    pass  # 이렇게 하면 favicon 요청에 대한 콘솔에 출력 안됨


# 매 라우팅 전에 동작하는 함수 # 일종의 aop 같이 처리?
@app.middleware("http")
async def add_process_request_middleware(request, call_next):
    print("")
    print("")
    print("")
    await FastapiServerUtil.do_preprocess_before_request(request)
    response = await call_next(request)
    return response


# 매 라우팅 후에 동작하는 함수
@app.middleware("http")
async def add_process_response_middleware(request, call_next):
    response = await call_next(request)
    await FastapiServerUtil.do_preprocess_after_request(request, response)
    return response

@app.get("/")
async def return_success(request: Request):
    DebuggingUtil.print_via_colorama(f"{inspect.currentframe().f_code.co_name}() 호출되었습니다", colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
    return {"success": f"fastapi 서버로 {os.path.basename(__file__)}를 구동 중 입니다"}



@app.get("/dummyies-members-with-overwrite")
def make_dummyies_members_with_overwrite():
    # FileSystemUtil.explorer(fr"{settings.protocol_type[0]}://{settings.host[0]}:{settings.port[0]}/make-dummyies")
    MEMBERS_JSON = StateManagementUtil.MEMBERS_JSON
    dummy_cnt = 100
    genres = ["러브코메디", "러브픽션", "러브액션"]
    names = ["내 청춘러브 코메디는 잘못되어 있어", "너에게 닿기를"]
    dummy_data = []
    for _ in range(dummy_cnt):
        member_dummy = {
            'member_id': uuid4().hex,
            'name': random.choice(names),
            'genre': random.choice(genres),
            'price': random.randint(1000, 10000),
        }
        dummy_data.append(member_dummy)

    # MEMBERS_JSON 에 데이터 저장
    with open(MEMBERS_JSON, "w", encoding="utf-8") as file:
        json.dump(dummy_data, file, ensure_ascii=False)

    DebuggingUtil.print_as_success(f"더미를 {dummy_cnt} 개로 리셋하였습니다")
    return {"message": f"더미를 {dummy_cnt} 개로 리셋하였습니다"}


@app.get("/dummyies-members-without-overwrite")
def make_dummyies_members_without_overwrite():
    # FileSystemUtil.explorer(fr"{settings.protocol_type[0]}://{settings.host[0]}:{settings.port[0]}/make-dummyies")
    MEMBERS_JSON = StateManagementUtil.MEMBERS_JSON

    # 기존의 MEMBERS_JSON 데이터 가져오기
    with open(MEMBERS_JSON, encoding="utf-8") as file:
        existing_data = json.load(file)

    dummy_data = existing_data
    # dummy_cnt = 100
    dummy_cnt = random.randint(1, 100)
    genres = ["러브코메디", "러브픽션", "러브액션"]
    names = ["내 청춘러브 코메디는 잘못되어 있어", "너에게 닿기를"]

    for _ in range(dummy_cnt):
        member_dummy = {
            'member_id': uuid4().hex,
            'name': random.choice(names),
            'genre': random.choice(genres),
            'price': random.randint(1000, 10000),
        }
        dummy_data.append(member_dummy)

    # MEMBERS_JSON 에 데이터 저장
    with open(MEMBERS_JSON, "w", encoding="utf-8") as file:
        json.dump(dummy_data, file, ensure_ascii=False)

    DebuggingUtil.print_as_success(f"더미를 추가로 {dummy_cnt} 개 생성하였습니다 총 {len(dummy_data)}개의 데이터가 {os.path.basename(MEMBERS_JSON)}에 저장되어 있습니다")
    return {"message": f"더미를 추가로 {dummy_cnt} 개 생성하였습니다 총 {len(dummy_data)}개의 데이터가 {os.path.basename(MEMBERS_JSON)}에 저장되어 있습니다"}

@app.get("/list-members")
async def list_members():
    BusinessLogicUtil.print_json_via_jq_pkg(json_file=MEMBERS_JSON)
    return {"members": MEMBERS}


@app.get("/member-by-index/{index}")
async def member_by_index(index: int):
    if index < len(MEMBERS):
        BusinessLogicUtil.print_json_via_jq_pkg(json_str=MEMBERS[index])
        return MEMBERS[index]
    DebuggingUtil.print_as_fail(f"member  인덱스 {index}이 범위({len(MEMBERS)}) 밖에 있습니다.")
    # raise HTTPException(status_code=404, detail=f"Book index {index} out of range ({len(MEMBERS)}).")
    raise HTTPException(status_code=404, detail=f"member  인덱스 {index}가 범위를 벗어났습니다 ({len(MEMBERS)}).")


@app.get("/member-by-member-id")  # 골라야한다면 이게 나는 좋은데
async def member_by_member_id(member_id: str):
    for member in MEMBERS:
        # if member.member_id == member_id:
        if member['member_id'] == member_id:
            BusinessLogicUtil.print_json_via_jq_pkg(json_str=member)
            return member
    # raise HTTPException(status_code=404, detail=f"Book ID {member_id} not found in database.")
    DebuggingUtil.print_as_fail(f"({len(MEMBERS)})개의 등록된 members 중, member_id 가 {member_id}인 Book 이 없습니다.")
    raise HTTPException(status_code=404, detail=f"({len(MEMBERS)})개의 등록된 members 중, member_id 가 {member_id}인 Book 이 없습니다.")


@app.get("/get-member")  # 이건 내 스타일이 아닌데...이게 보편적인지 확인해보고 싶다..원래 rest 스타일 준수하면 get 쓰면 안되는 것 아닌가? 써도 되나
async def get_member(member_id: str):
    for member in MEMBERS:
        # if member.member_id == member_id:
        if member['member_id'] == member_id:
            BusinessLogicUtil.print_json_via_jq_pkg(json_str=member)
            return member
    # raise HTTPException(status_code=404, detail=f"Book ID {member_id} not found in database.")
    DebuggingUtil.print_as_fail(f"({len(MEMBERS)})개의 등록된 members 중, member_id 가 {member_id}인 Book 이 없습니다.")
    raise HTTPException(status_code=404, detail=f"({len(MEMBERS)})개의 등록된 members 중, member_id 가 {member_id}인 Book 이 없습니다.")


@app.post("/add-member")
async def add_member(member: DataObjectUtil.Book):
    member.member_id = uuid4().hex  # id 를 hex 로 생성하여 할당
    json_member = jsonable_encoder(member)
    MEMBERS.append(json_member)
    with open(MEMBERS_JSON, "w", encoding="utf-8") as file:
        json.dump(MEMBERS, file, ensure_ascii=False)
        BusinessLogicUtil.print_json_via_jq_pkg(json_str=json_member)
    DebuggingUtil.print_as_success(f"member 이 성공적으로 생성되었습니다.")
    return {"member_id": F"{member.member_id} 가 {MEMBERS_JSON} 에 저장되었습니다"}


@app.post("/members")  # 일단 1개만 success
async def create_member(member: DataObjectUtil.Book):
    # 여기서 모두 업로드 하면 될 것 같은데
    # MEMBERS.append(member) # fail
    MEMBERS.append(member.model_dump())  # success
    with open(MEMBERS_JSON, "w", encoding="utf-8") as file:
        json.dump(MEMBERS, file, indent=4, ensure_ascii=False)
    DebuggingUtil.print_via_colorama(rf'member : {member}', colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
    DebuggingUtil.print_as_success(f"member 이 성공적으로 생성되었습니다.")
    return {"message": "member 이 성공적으로 생성되었습니다."}


@app.put("/update-member")
async def update_member(member_id: str, updated_member: DataObjectUtil.Book):
    for i, member in enumerate(MEMBERS):
        if member["member_id"] == member_id:
            MEMBERS[i] = updated_member.model_dump()
            # MEMBERS[i] = updated_member
            with open(MEMBERS_JSON, "w", encoding="utf-8") as file:
                json.dump(MEMBERS, file, indent=4, ensure_ascii=False)
            DebuggingUtil.print_via_colorama(rf'member : {member}', colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
            DebuggingUtil.print_as_success(f"아이디 {member_id} 인 member 이 성공적으로 업데이트되었습니다")
            return {"message": f"아이디 {member_id} 인 member 이 성공적으로 업데이트되었습니다"}
    DebuggingUtil.print_as_fail(f"데이터베이스에서 아이디 {member_id} 인 member 이 찾을 수 없습니다.")
    raise HTTPException(status_code=404, detail=f"데이터베이스에서 아이디 {member_id} 인 member 을 찾을 수 없습니다.")


@app.delete("/delete-member/{member_id}")
async def delete_member(member_id: str):
    for i, member in enumerate(MEMBERS):
        # if member.member_id== member_id:
        # print(rf'member["member_id"] : {member["member_id"]} member_id : {member_id}')
        if member["member_id"] == member_id:
            del MEMBERS[i]
            # MEMBERS.remove(member)
            with open(MEMBERS_JSON, "w", encoding="utf-8") as file:
                json.dump(MEMBERS, file, indent=4, ensure_ascii=False)
            DebuggingUtil.print_via_colorama(rf'member : {member}', colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
            DebuggingUtil.print_as_success(f"아이디 {member_id} 인 member 이 성공적으로 삭제되었습니다.")
            return {"message": f"아이디 {member_id} 인 member 이 성공적으로 삭제되었습니다."}
    DebuggingUtil.print_as_fail(f"데이터베이스에서 아이디 {member_id} 인 member 이 찾을 수 없습니다.")
    raise HTTPException(status_code=404, detail=f"데이터베이스에서 아이디 {member_id} 인 member member 을 찾을 수 없습니다.")


@app.get("/random-member")
async def random_member():
    if len(MEMBERS) > 0:
        member_choiced = random.choice(MEMBERS)
        BusinessLogicUtil.print_json_via_jq_pkg(json_list=member_choiced)
        return member_choiced
    else:
        DebuggingUtil.print_as_fail(rf"{MEMBERS_JSON}에 members가 없습니다")
        raise HTTPException(status_code=404, detail=f"{MEMBERS_JSON}에 members가 없습니다")


if __name__ == "__main__":
    # :: ASGI SERVER RUN SETTING
    # DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}")
    print()
    print()
    DebuggingUtil.commentize("fastapi 서버가 시작되었습니다")

    # 스웨거 자동실행
    # FileSystemUtil.explorer(fr"{settings.protocol_type[0]}://{settings.host[0]}:{settings.port[0]}/docs")
    # FileSystemUtil.explorer(fr"{settings.protocol_type[0]}://{settings.host[0]}:{settings.port[0]}/redoc")
    # FileSystemUtil.explorer(fr"{settings.protocol_type[0]}://{settings.host[0]}:{settings.port[0]}")

    # 더미 데이터 객체 생성
    # FileSystemUtil.explorer(fr"{settings.protocol_type[0]}://{settings.host[0]}:{settings.port[0]}/make-dummyies")

    uvicorn.run(
        app=f"{FileSystemUtil.get_target_as_n(__file__)}:app",
        host=settings.host[0],  # class 를 사용하면 tuple 로 오며, str(tuple) 이렇게 사용할 수 없고, tuple[0] 으로 가져와야 하네. js 의 destructon 문법처럼 py의 unpacking 을 사용하는 방법이 있으나 변수 새로 생성해야함.
        port=settings.port[0],
        reload=True,  # 이 설정 너무 의존하지는 말자. pkg 변경 되면 rerun 다시 해줘야한다
        # log_level="info",
        # log_level="debug",
    )
