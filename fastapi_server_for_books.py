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

BOOKS_JSON = StateManagementUtil.BOOKS_JSON
BOOKS = FastapiServerUtil.init_and_update_json_file(BOOKS_JSON)


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
    return {"success": "fastapi 서버 가 정상 동작 중 입니다"}


@app.get("/dummyies-books-with-overwrite")
def make_dummyies_books_with_overwrite():
    # FileSystemUtil.explorer(fr"{settings.protocol_type[0]}://{settings.host[0]}:{settings.port[0]}/make-dummyies")
    BOOKS_JSON = StateManagementUtil.BOOKS_JSON
    dummy_cnt = 100
    genres = ["러브코메디", "러브픽션", "러브액션"]
    names = ["내 청춘러브 코메디는 잘못되어 있어", "너에게 닿기를"]
    dummy_data = []
    for _ in range(dummy_cnt):
        book_dummy = {
            'book_id': uuid4().hex,
            'name': random.choice(names),
            'genre': random.choice(genres),
            'price': random.randint(1000, 10000),
        }
        dummy_data.append(book_dummy)

    # BOOKS_JSON 에 데이터 저장
    with open(BOOKS_JSON, "w", encoding="utf-8") as file:
        json.dump(dummy_data, file, ensure_ascii=False)

    DebuggingUtil.print_as_success(f"더미를 {dummy_cnt} 개로 리셋하였습니다")
    return {"message": f"더미를 {dummy_cnt} 개로 리셋하였습니다"}


@app.get("/dummyies-books-without-overwrite")
def make_dummyies_books_without_overwrite():
    # FileSystemUtil.explorer(fr"{settings.protocol_type[0]}://{settings.host[0]}:{settings.port[0]}/make-dummyies")
    BOOKS_JSON = StateManagementUtil.BOOKS_JSON

    # 기존의 BOOKS_JSON 데이터 가져오기
    with open(BOOKS_JSON, encoding="utf-8") as file:
        existing_data = json.load(file)

    dummy_data = existing_data
    # dummy_cnt = 100
    dummy_cnt = random.randint(1, 100)
    genres = ["러브코메디", "러브픽션", "러브액션"]
    names = ["내 청춘러브 코메디는 잘못되어 있어", "너에게 닿기를"]

    for _ in range(dummy_cnt):
        book_dummy = {
            'book_id': uuid4().hex,
            'name': random.choice(names),
            'genre': random.choice(genres),
            'price': random.randint(1000, 10000),
        }
        dummy_data.append(book_dummy)

    # BOOKS_JSON 에 데이터 저장
    with open(BOOKS_JSON, "w", encoding="utf-8") as file:
        json.dump(dummy_data, file, ensure_ascii=False)

    DebuggingUtil.print_as_success(f"더미를 추가로 {dummy_cnt} 개 생성하였습니다 총 {len(dummy_data)}개의 데이터가 {os.path.basename(BOOKS_JSON)}에 저장되어 있습니다")
    return {"message": f"더미를 추가로 {dummy_cnt} 개 생성하였습니다 총 {len(dummy_data)}개의 데이터가 {os.path.basename(BOOKS_JSON)}에 저장되어 있습니다"}

@app.get("/list-books")
async def list_books():
    BusinessLogicUtil.print_json_via_jq_pkg(json_file=BOOKS_JSON)
    return {"books": BOOKS}


@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    if index < len(BOOKS):
        BusinessLogicUtil.print_json_via_jq_pkg(json_str=BOOKS[index])
        return BOOKS[index]
    DebuggingUtil.print_as_fail(f"book  인덱스 {index}이 범위({len(BOOKS)}) 밖에 있습니다.")
    # raise HTTPException(status_code=404, detail=f"Book index {index} out of range ({len(BOOKS)}).")
    raise HTTPException(status_code=404, detail=f"book  인덱스 {index}가 범위를 벗어났습니다 ({len(BOOKS)}).")


@app.get("/book-by-book-id")  # 골라야한다면 이게 나는 좋은데
async def book_by_book_id(book_id: str):
    for book in BOOKS:
        # if book.book_id == book_id:
        if book['book_id'] == book_id:
            BusinessLogicUtil.print_json_via_jq_pkg(json_str=book)
            return book
    # raise HTTPException(status_code=404, detail=f"Book ID {book_id} not found in database.")
    DebuggingUtil.print_as_fail(f"({len(BOOKS)})개의 등록된 books 중, book_id 가 {book_id}인 Book 이 없습니다.")
    raise HTTPException(status_code=404, detail=f"({len(BOOKS)})개의 등록된 books 중, book_id 가 {book_id}인 Book 이 없습니다.")


@app.get("/get-book")  # 이건 내 스타일이 아닌데...이게 보편적인지 확인해보고 싶다..원래 rest 스타일 준수하면 get 쓰면 안되는 것 아닌가? 써도 되나
async def get_book(book_id: str):
    for book in BOOKS:
        # if book.book_id == book_id:
        if book['book_id'] == book_id:
            BusinessLogicUtil.print_json_via_jq_pkg(json_str=book)
            return book
    # raise HTTPException(status_code=404, detail=f"Book ID {book_id} not found in database.")
    DebuggingUtil.print_as_fail(f"({len(BOOKS)})개의 등록된 books 중, book_id 가 {book_id}인 Book 이 없습니다.")
    raise HTTPException(status_code=404, detail=f"({len(BOOKS)})개의 등록된 books 중, book_id 가 {book_id}인 Book 이 없습니다.")


@app.post("/add-book")
async def add_book(book: DataObjectUtil.Book):
    book.book_id = uuid4().hex  # id 를 hex 로 생성하여 할당
    json_book = jsonable_encoder(book)
    BOOKS.append(json_book)
    with open(BOOKS_JSON, "w", encoding="utf-8") as file:
        json.dump(BOOKS, file, ensure_ascii=False)
        BusinessLogicUtil.print_json_via_jq_pkg(json_str=json_book)
    DebuggingUtil.print_as_success(f"book 이 성공적으로 생성되었습니다.")
    return {"book_id": F"{book.book_id} 가 {BOOKS_JSON} 에 저장되었습니다"}


@app.post("/books")  # 일단 1개만 success
async def create_book(book: DataObjectUtil.Book):
    # 여기서 모두 업로드 하면 될 것 같은데
    # BOOKS.append(book) # fail
    BOOKS.append(book.model_dump())  # success
    with open(BOOKS_JSON, "w", encoding="utf-8") as file:
        json.dump(BOOKS, file, indent=4, ensure_ascii=False)
    DebuggingUtil.print_via_colorama(rf'book : {book}', colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
    DebuggingUtil.print_as_success(f"book 이 성공적으로 생성되었습니다.")
    return {"message": "book 이 성공적으로 생성되었습니다."}


@app.put("/update-book")
async def update_book(book_id: str, updated_book: DataObjectUtil.Book):
    for i, book in enumerate(BOOKS):
        if book["book_id"] == book_id:
            BOOKS[i] = updated_book.model_dump()
            # BOOKS[i] = updated_book
            with open(BOOKS_JSON, "w", encoding="utf-8") as file:
                json.dump(BOOKS, file, indent=4, ensure_ascii=False)
            DebuggingUtil.print_via_colorama(rf'book : {book}', colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
            DebuggingUtil.print_as_success(f"아이디 {book_id} 인 book 이 성공적으로 업데이트되었습니다")
            return {"message": f"아이디 {book_id} 인 book 이 성공적으로 업데이트되었습니다"}
    DebuggingUtil.print_as_fail(f"데이터베이스에서 아이디 {book_id} 인 book 이 찾을 수 없습니다.")
    raise HTTPException(status_code=404, detail=f"데이터베이스에서 아이디 {book_id} 인 book 을 찾을 수 없습니다.")


@app.delete("/delete-book/{book_id}")
async def delete_book(book_id: str):
    for i, book in enumerate(BOOKS):
        # if book.book_id== book_id:
        # print(rf'book["book_id"] : {book["book_id"]} book_id : {book_id}')
        if book["book_id"] == book_id:
            del BOOKS[i]
            # BOOKS.remove(book)
            with open(BOOKS_JSON, "w", encoding="utf-8") as file:
                json.dump(BOOKS, file, indent=4, ensure_ascii=False)
            DebuggingUtil.print_via_colorama(rf'book : {book}', colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
            DebuggingUtil.print_as_success(f"아이디 {book_id} 인 book 이 성공적으로 삭제되었습니다.")
            return {"message": f"아이디 {book_id} 인 book 이 성공적으로 삭제되었습니다."}
    DebuggingUtil.print_as_fail(f"데이터베이스에서 아이디 {book_id} 인 book 이 찾을 수 없습니다.")
    raise HTTPException(status_code=404, detail=f"데이터베이스에서 아이디 {book_id} 인 book book 을 찾을 수 없습니다.")


@app.get("/random-book")
async def random_book():
    if len(BOOKS) > 0:
        book_choiced = random.choice(BOOKS)
        BusinessLogicUtil.print_json_via_jq_pkg(json_list=book_choiced)
        return book_choiced
    else:
        DebuggingUtil.print_as_fail(rf"{BOOKS_JSON}에 books가 없습니다")
        raise HTTPException(status_code=404, detail=f"{BOOKS_JSON}에 books가 없습니다")


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
