# from app.routes import index, auth
import json
import logging
from pathlib import Path

from fastapi import FastAPI
from starlette.responses import JSONResponse


# vercel build url history
# 빌드 시에 갱신됨. 빌드할 때 마다 바꿔줘야함.
# https://nextjs-fastapi-dwl7cp8ri-jung-hoon-parks-projects.vercel.app
# https://nextjs-fastapi-dwl7cp8ri-jung-hoon-parks-projects.vercel.app/nav-items
# https://nextjs-fastapi-dwl7cp8ri-jung-hoon-parks-projects.vercel.app/api/python
# https://nextjs-fastapi-dwl7cp8ri-jung-hoon-parks-projects.vercel.app/api/python/nav-items
# https://nextjs-fastapi-dwl7cp8ri-jung-hoon-parks-projects.vercel.app/boards

app = FastAPI()

DB_JSON = rf"{str(Path(__file__).parent.absolute())}\db.json"
print(rf'DB_JSON : {DB_JSON}')
@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/python/{specific_object_name}")
async def get_specific_object_json_db(specific_object_name):
    '''python json 파일에서 특정 객체만 추출'''
    logging.debug(rf'specific_object_name : {specific_object_name}')
    file = open(DB_JSON, encoding="utf-8")
    try:
        object_specific = json.load(file)[specific_object_name]
        object_specific = JSONResponse(object_specific)
    except KeyError:
        logging.debug("json db 에서 해당 객체는 존재하지 않습니다")
        # return {"error": "json db 에서 해당 객체는 존재하지 않습니다"}
        return None
    return object_specific
