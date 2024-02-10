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

from pkg_park4139 import StateManagementUtil, FastapiUtil, FileSystemUtil, DebuggingUtil, FastapiUtil, ColoramaColorUtil, TestUtil, BusinessLogicUtil

# SERVER SETTING
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})  # 와 찾아보길 잘했다.  # default
handler = Mangum(app)  # ?
app.mount("/$cache_favicon", StaticFiles(directory="$cache_favicon"), name="$cache_favicon")
app.encoding = 'utf-8'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

logger = logging.getLogger(__name__)


# FastapiServerUtil.init_ip_address_allowed(app) # nginx 가 앞단이므로 nginx 에서 설정하는 것이 효율적일듯
# FastapiServerUtil.init_domain_address_allowed(app) # nginx 가 앞단이므로 nginx 에서 설정하는 것이 효율적일듯
FastapiUtil.init_cors_policy(app) # nginx 가 앞단이므로 nginx 에서 설정하는 되어 있으므로 local dev 에서 테스트 시에만 필요

BOOKS_JSON = StateManagementUtil.BOOKS_JSON
BOOKS = FastapiUtil.init_and_update_json_file(BOOKS_JSON)






@app.get("/")
async def return_success():
    DebuggingUtil.print_ment_via_colorama(f"{inspect.currentframe().f_code.co_name}() 호출되었습니다", colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
    return {"어서와": "fastapi 서버는 처음이지?"}


# fastapi 나름대로 나눈 경우에 따른 실험 테스트, 귀찮지만 꼭 이 실험을 해야 감이 잘 온다.
@app.get("/들어갈게")
def 들어간대():
    return {"message": f"나가줄래"}


@app.get("/종아해요/{who}")  # without 쿼리스트링
def 종아한대요(who):
    return {"message": f"종아해요 {who}을(를) 요"}


@app.get("/파라미터-로-쿼리스트링-설정")  # with query #별거없다 reqeust 될 url 에서 {para}(브라켓 처리된 파라미터) 를 지우면 된다.
def love1(q):
    return {"message": f"{q}"}


@app.get("/파라미터-타입힌팅-으로-쿼리스트링-벨리데이션-설정")  # with query
def love3(q: str):
    return {"message": f"{q}"}


@app.get("/파라미터-타입힌팅-as-Union-으로-쿼리스트링-벨리데이션-nullable-설정")  # with query
def get_item(q: Union[str, None] = None):  # 쿼리스트링 q 를 nullable 하도록 설정
    return {"message": f"{q}"}


@app.get("/알겠음/items/{item_id}")  # fastapi 기본예제
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/{item_id}")  # 몇 번 테스트해보니 이제 어떻게 만들었는지 이해감.
def read_item(item_id: int, q: Union[str, None] = None, p: Union[int, None] = None):
    return {"item_id": item_id, "q": q, "p": p}



# @app.get("/api/via-db/items/{id}")
# def read_item(id: int, q: Optional[str] = None):
#     return {"id": id, "q": q}

# @app.put("/api/via-db/items/{id}")
# async def update_item(id: int, item: Item):
#     result = {"id": id, **item.dict()}
#
#
# @app.delete("/api/via-db/items/{id}")
# def delete_item(id: int):
#     return {"deleted": id}
#


# @app.post("/files/")
# async def create_file(file: UploadFile):
#     content = await file.read()
#     return JSONResponse({"filename": file.filename})


# boards
# orders
# boards
# lists


if __name__ == "__main__":
    print()
    print()
    DebuggingUtil.commentize("fastapi 서버가 시작되었습니다")

    uvicorn.run(
        app=f"{FileSystemUtil.get_target_as_n(__file__)}:app",
        host=UvicornUtil.Settings.host,
        port=UvicornUtil.Settings.port,
    )
