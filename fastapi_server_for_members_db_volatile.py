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
# os.system("chcp 65001 >nul")
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
settings = FastapiServerUtil.Settings()
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
# FastapiServerUtil.init_Logging_via_middleware(app)
FastapiServerUtil.init_ip_address_allowed(app)
FastapiServerUtil.init_domain_address_allowed(app)
FastapiServerUtil.init_cors_policy_allowed(app)
MEMBERS_JSON = StateManagementUtil.MEMBERS_JSON
MEMBERS = FastapiServerUtil.init_and_update_json_file(MEMBERS_JSON)
members = []  # 저장이 필요없는 경우의 members restful api 설계


# 파비콘 처리
@app.get('/favicon.ico', include_in_schema=False)
async def get_favicon():
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    pass  # 이렇게 하면 favicon 요청에 대한 콘솔에 출력 안됨


# 매 라우팅 전에 동작하는 함수
@app.middleware("http")
async def add_process_request_middleware(request, call_next):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    print("")
    print("")
    print("")
    await FastapiServerUtil.do_preprocess_before_request(request)
    response = await call_next(request)
    return response


# 매 라우팅 후에 동작하는 함수
@app.middleware("http")
async def add_process_response_middleware(request, call_next):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    response = await call_next(request)
    await FastapiServerUtil.do_preprocess_after_request(request, response)
    return response


@app.on_event("startup")
async def startup_event():
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    print("애플리케이션 시작 시 실행되어야 하는 초기화 작업을 수행합니다.")
    # MEMBERS_JSON 에 더미데이터 생성 후 저장
    # dummy_cnt = random.randint(1, 100)
    dummy_cnt = 100
    with open(MEMBERS_JSON, encoding="utf-8") as file:
        existing_data = json.load(file)
    dummy_data = existing_data
    for _ in range(dummy_cnt):
        member_dummy = {
            'id': uuid4().hex + BusinessLogicUtil.get_time_as_('%Y%m%d%H%M%S%f') + BusinessLogicUtil.get_random_alphabet(),
            'name': random.choice(['김지영', '이민준', '박서연', '최영희', '정민재', '한지수', '서예진', '윤승우', '신하늘', '오준호', '류지현', '임동혁', '송지우', '홍민지', '강성민', '권수진', '신동욱', '최선영', '이지원', '김민재', '정서영', '박준형', '황예린', '강민호', '신지민', '이서연', '한승민', '조윤서', '김동현', '양미경']),
            'date_join': random.choice(['202401270047888999', '202401270047888999']),
            'date_logout_last': random.choice(['202401270047888999', '202401270047888999']),
            'address_house': random.choice(
                ["서울특별시 강남구 역삼동 123-45", "경기도 성남시 분당구 정자동 678-90", "부산광역시 해운대구 우동 12-34", "인천광역시 남구 주안동 56-78", "대구광역시 수성구 만촌동 901-23", "광주광역시 서구 화정동 45-67", "대전광역시 유성구 도룡동 89-01", "울산광역시 남구 삼산동 234-56", "세종특별자치시 도움2로 78", "경기도 고양시 일산동구 백석동 34-56", "강원도 춘천시 소양동 78-90", "충청북도 청주시 상당구 용암동 123-45", "충청남도 천안시 동남구 신방동 67-89", "전라북도 전주시 완산구 효자동 90-12", "전라남도 목포시 상동 34-56", "경상북도 포항시 북구 흥해읍 78-90",
                 "경상남도 창원시 의창구 봉림동 123-45", "제주특별자치도 제주시 이도이동 56-78", "서울특별시 종로구 종로1가 90", "경기도 수원시 팔달구 인계동 12", "부산광역시 동래구 명장동 34", "인천광역시 부평구 부평동 56", "대구광역시 중구 동인동 78", "광주광역시 남구 봉선동 90", "대전광역시 서구 월평동 12", "울산광역시 중구 성남동 34", "세종특별자치시 조치원읍 56", "경기도 안산시 상록구 본오동 78", "강원도 원주시 일산동 90"]),
            'address_e_mail': random.choice(
                ["example1@gmail.com", "example2@yahoo.com", "example3@hotmail.com", "example4@naver.com", "example5@daum.net", "example6@kakao.com", "example7@outlook.com", "example8@icloud.com", "example9@nate.com", "example10@hanmail.net", "example11@google.com", "example12@yahoo.co.kr", "example13@hotmail.co.kr", "example14@naver.com", "example15@daum.net", "example16@kakao.com",
                 "example17@outlook.com", "example18@icloud.com", "example19@nate.com", "example20@hanmail.net", "example21@gmail.com", "example22@yahoo.com", "example23@hotmail.com", "example24@naver.com", "example25@daum.net", "example26@kakao.com", "example27@outlook.com", "example28@icloud.com", "example29@nate.com", "example30@hanmail.net"]),
            'number_phone': random.choice(
                ["010-1234-5678", "02-9876-5432", "031-111-2222", "051-333-4444", "032-555-6666", "053-777-8888", "064-999-0000", "042-111-2222", "062-333-4444", "051-555-6666", "053-777-8888", "064-999-0000", "010-1234-5678", "02-9876-5432", "031-111-2222", "051-333-4444", "032-555-6666", "053-777-8888", "064-999-0000", "042-111-2222", "062-333-4444", "051-555-6666", "053-777-8888",
                 "064-999-0000", "010-1234-5678", "02-9876-5432", "031-111-2222", "051-333-4444", "032-555-6666", "053-777-8888", "064-999-0000"]),
        }
        dummy_data.append(member_dummy)
        members.append(member_dummy)
    [print(sample) for sample in members]
    with open(MEMBERS_JSON, "w", encoding="utf-8") as file:
        json.dump(dummy_data, file, ensure_ascii=False)
    DebuggingUtil.print_as_success(f"더미를 추가로 {dummy_cnt} 개 생성하였습니다 총 {len(dummy_data)}개의 데이터가 {os.path.basename(MEMBERS_JSON)}에 저장되어 있습니다")


@app.on_event("shutdown")
async def shutdown_event():
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    # 애플리케이션 종료 시 실행되어야 하는 정리 작업을 수행하는 코드
    print("애플리케이션 종료 시 실행되어야 하는 정리 작업을 수행합니다.")


@app.get("/")
async def return_success(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    DebuggingUtil.print_via_colorama(f"{inspect.currentframe().f_code.co_name}() 호출되었습니다", colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
    return {"success": f"fastapi 서버로 {os.path.basename(__file__)}를 구동 중 입니다"}


@app.get("/member/{id}")
def get_member(id: str):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    for member_ in members:
        if member_['id'] == id:
            DebuggingUtil.print_as_success(member_)
            return {"message": "member deleted successfully"}
    DebuggingUtil.print_as_fail(f"id가 {id} 인 member 없어요")
    return {"message": "member not found"}


@app.get("/members")
def get_members():
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    [print(sample) for sample in members]
    return members


@app.post("/members")
def create_member(member: DataObjectUtil.Member):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    member_dict = member.model_dump()
    member_dict['id'] = uuid4().hex + BusinessLogicUtil.get_time_as_('%Y%m%d%H%M%S%f') + BusinessLogicUtil.get_random_alphabet()
    # print(rf"member_dict['id'] : {member_dict['id']}")
    DebuggingUtil.print_as_success(member_dict)
    members.append(member_dict)
    return {"message": "member created successfully"}


@app.put("/members/{id}")
def update_member(id: str, member: DataObjectUtil.Member):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    for member_ in members:
        if member_['id'] == id:
            member_['name'] = member.name
            member_['date_join'] = member.date_join
            member_['date_logout_last'] = member.date_logout_last
            member_['address_house'] = member.address_house
            member_['address_e_mail'] = member.address_e_mail
            member_['number_phone'] = member.number_phone
            DebuggingUtil.print_as_magenta(member_)
            return {"message": "member updated successfully"}
    return {"message": "member not found"}


@app.delete("/members/{id}")
def delete_member(id: str):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    for member_ in members:
        if member_['id'] == id:
            DebuggingUtil.print_as_magenta(member_)
            # del member_
            members.remove(member_)
            return {"message": "member deleted successfully"}
    return {"message": "member not found"}


if __name__ == "__main__":
    print()
    print()
    DebuggingUtil.commentize("fastapi 서버가 시작되었습니다")
    uvicorn.run(
        app=f"{FileSystemUtil.get_target_as_n(__file__)}:app",
        host=settings.host[0],
        port=settings.port[0],
    )
