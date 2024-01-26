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

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
settings = FastapiServerUtil.Settings()
# FastapiServerUtil.init_Logging_via_middleware(app)
FastapiServerUtil.init_ip_address_allowed(app)
FastapiServerUtil.init_domain_address_allowed(app)
FastapiServerUtil.init_cors_policy_allowed(app)




# 파비콘 처리
@app.get('/favicon.ico', include_in_schema=False)
async def get_favicon():
    # return PlainTextResponse('')
    # return Response(content=b'', media_type='image/x-icon')
    # raise HTTPException(status_code=404)
    # raise HTTPException(status_code=500)
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

# TodoItem restful api 설계 sample, 저장이 필요없는 경우에는 이와 유사하게 이용
todos = []
@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: DataObjectUtil.TodoItem):
    todo_dict = todo.model_dump()
    todo_dict['id'] = uuid4().hex + BusinessLogicUtil.get_time_as_('%Y%m%d%H%M%S%f') + BusinessLogicUtil.get_random_alphabet()
    print(rf"todo_dict['id'] : {todo_dict['id']}")
    todos.append(todo_dict)
    return {"message": "Todo created successfully"}
@app.put("/todos/{todo_id}")
def update_todo(todo_id: str, todo: DataObjectUtil.TodoItem):
    for todo_ in todos:
        if todo_['id'] == todo_id:
            todo_['title'] = todo.title
            todo_['completed'] = todo.completed
            return {"message": "Todo updated successfully"}
    return {"message": "Todo not found"}
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    for todo_ in todos:
        if todo_['id'] == todo_id:
            # todo_.remove(todo_)
            del todo_
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}


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
