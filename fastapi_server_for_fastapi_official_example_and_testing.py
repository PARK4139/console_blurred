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

BOOKS_JSON = StateManagementUtil.BOOKS_JSON
BOOKS = FastapiServerUtil.init_and_update_json_file(BOOKS_JSON)


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
    return {"어서와": "fastapi 서버는 처음이지?"}


# fastapi 나름대로 나눈 경우에 따른 실험 테스트, 귀찮지만 꼭 이 실험을 해야 감이 잘 온다.
@app.get("/들어갈게")  # without query
def 들어갈게():
    return {"message": f"나가줄래"}


@app.get("/종아해요/{who}")  # without query
def 종아해요(who):
    return {"message": f"종아해요 {who}을 요"}


@app.get("/파라미터를-넣으면-쿼리스트링-쉡게설정")  # with query #별거없다 reqeust 될 url 에서 {para}(브라켓 처리된 파라미터) 를 지우면 된다.
def love1(q):
    return {"message": f"{q}"}


@app.get("/파라미터-두개를-넣으면-쿼리두개")
def love2(q, w):
    return {"message": f"{q} {w}"}


@app.get("/타입힌팅을-하면-쿼리스트링-벨리데이션-적용설정-너무편하다")  # with query
def love3(q: str):
    return {"message": f"{q}"}


@app.get("/Union을-통한-타입힌팅으로-쿼리스트링-벨리데이션-nullable-하도록-설정-너무편하다")  # with query
def get_item(q: Union[str, None] = None):  # 쿼리스트링 q 를 nullable 하도록 설정
    return {"message": f"{q}"}


@app.get("/fastapi-공식기본예제/items/{item_id}")  # fastapi 기본예제, 몇 번 테스트해보니 이제 어떻게 만들었는지 이해감.
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None, p: Union[int, None] = None):
    return {"item_id": item_id, "q": q, "p": p}


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
