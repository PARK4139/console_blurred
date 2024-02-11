# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'

# -*- coding: utf-8 -*-
# import subprocess
# import pyttsx3
# import requests
# import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
import os
# DB SETTING
import sqlalchemy
import sys
import time
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from urllib.parse import unquote

from utility.data_model import member_joined_list, member_commutation_management_tb, db_session

# ORM SETTING
import sqlalchemy
from pydantic import BaseModel
from sqlalchemy import Integer, Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, backref

engine = sqlalchemy.create_engine(db_url)  # db_url 변경 소지 있음.
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()

# -*- coding: utf-8 -*-
# import subprocess
# import pyttsx3
# import requests
# import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
import pymysql
# DB SETTING
import sqlalchemy
import traceback
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base

# import mysql   # pip install mysql 수행 시 error 발생되어 주석처리.


import asyncio
import inspect
# from app.routes import index, auth
import json
import logging
import os
import random
from typing import Union

# from venv import create
import uvicorn
from fastapi import FastAPI
# ! import 에 주석은 import 백업임 지우지말자. 오름차순 정리를 하자. 백업했으면 ctrl alt o를 누르자
from mangum import Mangum
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from pkg_park4139 import StateManagementUtil, FastapiUtil, FileSystemUtil, DebuggingUtil, FastapiUtil, ColoramaColorUtil, TestUtil

# SERVER SETTING
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})  # 와 찾아보길 잘했다.  # default
handler = Mangum(app)  # ?
app.mount("/$cache_favicon", StaticFiles(directory="$cache_favicon"), name="$cache_favicon")
app.encoding = 'utf-8'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

logger = logging.getLogger(__name__)

# FastapiServerUtil.init_ip_address_allowed(app) # nginx 가 앞단이므로 nginx 에서 설정하는 것이 효율적일듯
# FastapiServerUtil.init_domain_address_allowed(app) # nginx 가 앞단이므로 nginx 에서 설정하는 것이 효율적일듯
FastapiUtil.init_cors_policy(app)  # nginx 가 앞단이므로 nginx 에서 설정하는 되어 있으므로 local dev 에서 테스트 시에만 필요

import sqlalchemy
from pydantic import BaseModel
from sqlalchemy import Integer, Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref
from config import db_url


class Question(BaseModel):
    question_id = Column(Integer, ForeignKey('question.id', ondelete='CASCADE'))
    index = "하나씩 증가하는"
    subject = Column(String(200), nullable=False)
    content = Column(Text(), nullable=False)
    create_date = Column(DateTime(), nullable=False)


class Answer(BaseModel):
    question_id = Column(Integer, ForeignKey('question.id', ondelete='CASCADE'))
    index = "하나씩 증가하는"
    question = relationship('Question', backref=backref('answer_set'))
    content = Column(Text(), nullable=False)
    create_date = Column(DateTime(), nullable=False)


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


# class REQUEST_TB(Base):
#     __tablename__ = "REQUEST_TB"
#     # __table_args__ = {'mysql_collate': 'utf8_general_ci'}  # encoding 안되면 비슷하게 방법을 알아보자  mysql 용 코드로 보인다.
#     ID_REQUEST = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
#     CUSTOMER_NAME = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
#     MASSAGE = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
#     DATE_REQUESTED = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
#     USE_YN = sqlalchemy.Column(sqlalchemy.VARCHAR(length=2))
#
#     def __init__(self, ID_REQUEST, CUSTOMER_NAME, MASSAGE, DATE_REQUESTED, USE_YN):
#         self.ID_REQUEST = ID_REQUEST
#         self.CUSTOMER_NAME = CUSTOMER_NAME
#         self.MASSAGE = MASSAGE
#         self.DATE_REQUESTED = DATE_REQUESTED
#         self.USE_YN = USE_YN
#
#     def add_new_records(ID_REQUEST, CUSTOMER_NAME, MASSAGE, DATE_REQUESTED, USE_YN):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         new_records = REQUEST_TB(ID_REQUEST=ID_REQUEST, CUSTOMER_NAME=CUSTOMER_NAME, MASSAGE=MASSAGE, DATE_REQUESTED=DATE_REQUESTED, USE_YN=USE_YN)
#         session.add(new_records)
#         session.commit()
#
#     @staticmethod
#     def select_records_all():
#         print("_______________________________________________________________ " + inspect.currentframe().f_code.co_name + " s")
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).all()
#         records_as_str = ''
#         for Record in records:
#             tmp = '{{delimeter}}' + str(Record.ID_REQUEST) + '{{delimeter}}' + Record.CUSTOMER_NAME + '{{delimeter}}' + Record.MASSAGE + '{{delimeter}}' + Record.DATE_REQUESTED + '{{delimeter}}' + Record.USE_YN + ' \n'
#             records_as_str += tmp
#         print(records_as_str)
#         print("_______________________________________________________________ " + inspect.currentframe().f_code.co_name + " e")
#         return records_as_str
#
#     def select_records_by_id_Request(ID_REQUEST):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         return session.query(REQUEST_TB).filter_by(ID_REQUEST=ID_REQUEST).order_by(REQUEST_TB.ID_REQUEST.desc()).all()
#
#     def select_records_by_id_request(ID_REQUEST):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         return session.query(REQUEST_TB).filter_by_(ID_REQUEST=ID_REQUEST).first()
#
#     # def select_records_by_id_Request(ID_REQUEST, CUSTOMER_NAME):
#     #     return session.query(REQUEST_TB).filter(and_(REQUEST_TB.ID_REQUEST == item['ID_REQUEST'],
#     #                                                  REQUEST_TB.sequence_id == item['sequence_id'])).all()
#
#     def select_records_by_RowNumber(RowNumber):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).get(RowNumber)
#         records_as_str = ''
#         for Record in records:
#             tmp = '{{delimeter}}' + str(Record.ID_REQUEST) + '{{delimeter}}' + Record.CUSTOMER_NAME + '{{delimeter}}' + Record.MASSAGE + '{{delimeter}}' + Record.DATE_REQUESTED + '{{delimeter}}' + Record.USE_YN + ' \n'
#             records_as_str += tmp
#             print(records_as_str)
#         return records_as_str
#
#     def select_records_by_CUSTOMER_NAME_via_like(CUSTOMER_NAME='_박_정_훈_'):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).filter(REQUEST_TB.CUSTOMER_NAME.like('%' + CUSTOMER_NAME + '%'))
#         records_as_str = ''
#         for Record in records:
#             tmp = '{{delimeter}}' + str(Record.ID_REQUEST) + '{{delimeter}}' + Record.CUSTOMER_NAME + '{{delimeter}}' + Record.MASSAGE + '{{delimeter}}' + Record.DATE_REQUESTED + '{{delimeter}}' + Record.USE_YN + ' \n'
#             records_as_str += tmp
#             print(records_as_str)
#         return records_as_str
#
#     def select_records_where_CUSTOMER_NAME_is_not_(CUSTOMER_NAME='_박_정_훈_'):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).first(REQUEST_TB.CUSTOMER_NAME != CUSTOMER_NAME)
#         records_as_str = ''
#         for record in records:
#             tmp = '{{delimeter}}' + str(record.ID_REQUEST) + '{{delimeter}}' + record.CUSTOMER_NAME + '{{delimeter}}' + record.MASSAGE + '{{delimeter}}' + record.DATE_REQUESTED + '{{delimeter}}' + record.USE_YN + ' \n'
#             records_as_str += tmp
#             print(records_as_str)
#         return records_as_str
#
#     def select_records_by_Status(isActive):  # ,이건 뭐지?
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).filter_by_(active=isActive)
#         records_as_str = ''
#         for Record in records:
#             tmp = '{{delimeter}}' + str(Record.ID_REQUEST) + '{{delimeter}}' + Record.CUSTOMER_NAME + '{{delimeter}}' + Record.MASSAGE + '{{delimeter}}' + Record.DATE_REQUESTED + '{{delimeter}}' + Record.USE_YN + ' \n'
#             records_as_str += tmp
#             print(records_as_str)
#         return records_as_str
#
#     def update_record_status(ID_REQUEST, isActive):  # isActive 이건 뭐지?  use_yn 개념 같아 보인다.
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).get(ID_REQUEST)
#         records.active = isActive
#         session.commit()
#
#     def update_record_of_MASSAGE_by_ID_REQUEST(ID_REQUEST, MASSAGE):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         session.query(REQUEST_TB).filter(REQUEST_TB.ID_REQUEST == ID_REQUEST).first().MASSAGE = MASSAGE
#         session.commit()
#
#     def delete_records_by_ID_REQUEST(ID_REQUEST):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         session.query(REQUEST_TB).filter(REQUEST_TB.ID_REQUEST == ID_REQUEST).delete()
#         session.commit()
#
#     def delete_records_by_CUSTOMER_NAME(CUSTOMER_NAME='_박_정_훈_'):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         session.query(REQUEST_TB).filter(REQUEST_TB.CUSTOMER_NAME == CUSTOMER_NAME).delete()
#         session.commit()


# success
# result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter(MemberUtil.Member.id == id).first() # success , 그러나 타입힌팅 에러가...
# 테스트
# result = select(ItemsUtil.Item).where(ItemsUtil.Item.id.in_(["id1","id2"]))
# result = session.query(MySqlUtil.members).filter_by(id=id, pw=pw).first()
# result = session.query(MySqlUtil.members).filter_by(id=id).order_by(members.id.desc()).all()
# result = session.query(MySqlUtil.members).filter(members.name.ilike("%_박_정_훈_%").all_())
# result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter_by(id=id, pw=pw).limit(2)

