# from app.routes import index, auth
import inspect
import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from starlette.middleware.exceptions import ExceptionMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from pkg_park4139 import FastapiUtil, MySqlUtil, DebuggingUtil, FileSystemUtil, StateManagementUtil, UvicornUtil, SecurityUtil, BusinessLogicUtil, MemberUtil
from pkg_routers import router_login, router_main, router_join, router_commutation_management, router_user, router_book

templates = Jinja2Templates(directory=r"pkg_web/templates")

# 개발/운영 모드
StateManagementUtil.is_op_mode = False  # False 이면 dev 모드, 주석하면 op 모드

# 설정데이터를 설정파일에 저장
# FastAPI에서는 환경변수 설정 BaseSettings를 활용, built in pydantic
# config.env, 에 설정 저장 config.env도 파일인데 보안에 안전한가?
# 설정 파일의 내용은 Settings 클래스의 필드에 맞게 작성되어야 합니다.
# class Settings(BaseSettings):
#     database_uri: str
#     sqlalchemy_echo: bool = True
#     sqlalchemy_track_modifications: bool = True
#     secret_key: str  # SESSION? 웹 세션?, DB 세션? 을 위한 시크릿 키?,  random bytes 시크릿 키 비밀번호로 app.secret_key 변수에 저장, 잘 보관해라 이 비밀번호를, 함부로 배포해서는 않되니 방법을 모색할것.
#     config_file: str
#
#     class Config:
#         env_file = ".env"  # 환경 변수 파일명 설정
#
# settings = Settings(
#     _env_file="config.env",  # 환경 변수 파일 경로 설정
#     _env_file_encoding="utf-8"  # 환경 변수 파일 인코딩 설정
# )
# Settings 클래스에 secret_key 필드만 포함되어 있습니다.
# secret_key는 .env 파일이나 환경 변수를 통해 설정할 수 있도록 되어 있습니다.
# config.env 파일을 생성하고, secret_key 값을 해당 파일에 작성해야 합니다.
# 설정데이터를 환경변수에 저장
# ?


# 영한 버전 설정
# en.yaml/ko.yaml


# 데이터베이스
# SQLALCHEMY_TRACK_MODIFICATIONS
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLAlchemy가 데이터베이스의 변경 사항을 추적하는 기능을 활성화 또는 비활성화
# 대규모 애플리케이션에서는 권장되지 않습니다. SQLALCHEMY_TRACK_MODIFICATIONS = False 로 두는 것이 좋다
if not StateManagementUtil.is_op_mode:
    MySqlUtil.Base.metadata.drop_all(bind=MySqlUtil.engine)  # 개발 중에 drop 필요한 경우가 있음
MySqlUtil.Base.metadata.create_all(bind=MySqlUtil.engine)  # 데이터베이스에, Base 클래스에 정의된 모든 테이블을 생성, 옵션코드, class Item(Base): 다음에 호출되어야 동작한다
if not StateManagementUtil.is_op_mode:
    # 테스트 계정 생성
    member_data = {
        'id': "1",
        'pw': "1",
        'name': "아이유",
        'phone_no': "",
        'address': "",
        'e_mail': "",
        'birthday': "",
        'date_joined': BusinessLogicUtil.get_time_as_('%Y_%m_%d_%H_%M_%S'),
        'date_canceled': ''
    }
    MemberUtil.insert_member(member=member_data, db=MySqlUtil.get_session_local())


@asynccontextmanager
async def lifespan(app: FastAPI):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    # 앱 시작 후 1번만 실행(app 객체 생성 뒤) , @app.on_event("startup") deprecated, @app.on_event("startup") 대체품

    # 모드설정
    if StateManagementUtil.is_op_mode:
        mode_type = "op"
        DebuggingUtil.print_ment_light_white(f"{os.path.basename(__file__)}를 {mode_type}모드 로 구동 중입니다")
    else:
        mode_type = "dev"
        DebuggingUtil.print_ment_red(f"{os.path.basename(__file__)}를 {mode_type}모드 로 구동 중입니다")

    # uvicorn url
    DebuggingUtil.print_ment_light_white(rf'UvicornUtil.Settings.url : {UvicornUtil.Settings.url}')

    # mysql url
    DebuggingUtil.print_ment_light_white(rf'MySqlUtil.Settings.uri   : {MySqlUtil.Settings.uri}')
    DebuggingUtil.print_ment_light_white("✧*｡٩(ˊᗜˋ*)و✧*｡")

    # swagger 자동실행
    # FileSystemUtil.explorer(fr"{UvicornUtil.Settings.protocol_type}://{UvicornUtil.Settings.host}:{UvicornUtil.Settings.port}/docs")
    # FileSystemUtil.explorer(fr"{UvicornUtil.Settings.protocol_type}://{UvicornUtil.Settings.host}:{UvicornUtil.Settings.port}/redoc")
    # FileSystemUtil.explorer(fr"{UvicornUtil.Settings.protocol_type}://{UvicornUtil.Settings.host}:{UvicornUtil.Settings.port}")

    # 더미 데이터 객체 생성
    # FileSystemUtil.explorer(fr"{UvicornUtil.Settings.protocol_type}://{UvicornUtil.Settings.host}:{UvicornUtil.Settings.port}/make-dummyies")
    # FastapiUtil.test_client_post_request() # swagger 로 해도 되지만, test 자동화 용도

    # 클라이언트 테스트
    # FastapiUtil.test_client_post_request()  # swagger 로 해도 되지만, test 자동화 용도로 고민 중

    # 콘솔 타이틀 변경 테스트
    # lines = subprocess.check_output(rf'start cmd /k title NETWORK TEST CONSOLE', shell=True).decode('utf-8').split("\n")

    # 클라이언트 테스트
    # lines = subprocess.check_output(rf'start cmd /k title CLIENT TEST CONSOLE ', shell=True).decode('utf-8').split("\n")
    # for i in range(0,10,+1):
    #     os.system(rf'explorer "{url_base}/api/via-db/items/{i}"')

    # 머신러닝 모델 더미 생성
    # def fake_answer_to_everything_ml_model(x: float):
    #     return x * 42
    #
    # # Load the ML model
    # ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model

    # 콘솔 텍스트 컬러 설정
    DebuggingUtil.print_ment_defalut_color(rf'')

    yield  # 이거 꼭 있어야 동작함
    # # Clean up the ML models and release the resources
    # ml_models.clear()


app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"tryItOutEnabled": True})

# handler = Mangum(app)  #  AWS serverless platform 쓸 때 써야한다던 것 같다. function 단위로 쪼개는 역활
app.mount("/pkg_web", StaticFiles(directory="pkg_web"), name="pkg_web")

# app.encoding = 'utf-8'
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)


# 미들웨어
# UvicornUtil.init_ip_address_allowed(app) # nginx 가 앞단이므로 nginx 에서 설정하는 것이 효율적일듯
# UvicornUtil.init_domain_address_allowed(app) # nginx 가 앞단이므로 nginx 에서 설정하는 것이 효율적일듯
if not StateManagementUtil.is_op_mode:
    FastapiUtil.init_cors_policy(app)  # nginx 가 앞단이므로 nginx 에서 설정하는 되어 있으므로 dev 에서 테스트 시에만 필요


# fastapi 기본 예외처리 핸들러
# FastAPI는 기본적으로 예외 처리를 자동으로 처리하고 오류 응답을 생성합니다. 하지만 커스텀 핸들러를 추가하여, 예외를 직접 처리할 수 있음
@app.exception_handler(RequestValidationError)
@app.exception_handler(HTTPException)
async def exception_handler(request: Request, exc):  # exc : Exception
    # if isinstance(exc, RequestValidationError):
    #     status_code = 400
    #     msg = "유효성 검사 오류"
    # elif isinstance(exc, HTTPException):
    #     status_code = exc.status_code
    #     msg = "HTTP 오류"
    # else:
    #     status_code = 500
    #     msg = "내부 서버 오류"

    # html 파일로 처리
    # context = {
    #     "request": request,
    #     "msg": msg,
    #     'status_code': status_code,
    #     "exc_errors": exc.errors(),
    #     "exc_body": exc.body,
    #     "window_location_href": default_redirection_page,
    # }
    # return templates.TemplateResponse("/errors/main.html", context=context, status_code=status_code)

    # json 으로 처리
    # context = {
    #     "request": request,
    #     "exc_errors": exc.errors(),
    #     "exc_body": exc.body,
    #     "window_location_href": default_redirection_page,
    # }
    # return JSONResponse(content=context)

    # success, js alert 로 처리
    html_content = f"""
        <script>
        alert('{exc.detail}');
        window.history.go(-1);// 전 페이지로 이동
        //window.history.go(-2);// 전전 페이지로 이동
        //window.history.go(1);// 다음 페이지로 이동
        //window.history.go(2);// 다다음 페이지로 이동
        </script>
        """
    return HTMLResponse(content=html_content)


app.add_middleware(ExceptionMiddleware)
# 커스텀 예외처리 핸들러, Exception 추가 작업 처리를 기대
# async def custom_exception_handler(request: Request, exc: Any) -> JSONResponse:
#     # custom exception handling logic
#     return JSONResponse(
#         status_code=500,
#         content={"message": "Custom exception handler 작동"}
#     )
# exception_handlers: Dict[Type[Exception], Coroutine[Any, Any, JSONResponse]] = {
#     Exception: custom_exception_handler
# }
# app.exception_handlers = exception_handlers


app.add_middleware(
    SessionMiddleware,
    secret_key=SecurityUtil.get_random_bytes(),  # 난수생성기로 세션시크릿 생성 # 세션이 동적으로 생성이 되게 하려고 했는데 그러면, 서버 재시작시 세션데이터가 손실, 동일서버를 다중서버로 운영 시 시크릿 키가 서로 다르면 문제가 됨. 고로 같아야함.
    max_age=3600,  # 세션 수명 3600 초(1시간)
)


@app.middleware("http")
async def preprocess_after_request(request, call_next):
    # 매 라우팅 전에 동작하는 함수 # 일종의 aop 같이 처리? # request 감지하고 트리거로서 가로채기를 하는 느낌이다
    # DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    await FastapiUtil.preprocess_after_request(request)
    response = await call_next(request)
    return response


@app.middleware("http")
async def preprocess_before_response_return(request, call_next):
    # 매 라우팅 후에 동작하는 함수
    # DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    response = await call_next(request)
    await FastapiUtil.preprocess_before_response_return(request, response)
    return response


@app.on_event("shutdown")  # 이것도 deprecated 되었는지 확인필요
async def shutdown_event():
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    # 애플리케이션 종료 시 실행되어야 하는 정리 작업을 수행하는 코드
    print("애플리케이션 종료 시 실행되어야 하는 정리 작업을 수행합니다.")


# 라우팅 동작 설계 (잠정)
# api 엔드포인트
# https://park4139.store/api/
# web 엔드포인트
# https://pjh4139.store/p=


# 라우팅 처리(api)
@app.get("/", tags=["API 동작 테스트"])  # tags 파라미터는 FastAPI 자동문서화에 사용되는 데이터, 엔드포인트를 그룹화하는 데 사용되는 기능, # tags 를 동일하게 입력하면 하나의 api 그룹으로 묶을 수 있다
async def root():
    # DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    DebuggingUtil.print_ment_light_white(f"{inspect.currentframe().f_code.co_name}()")
    # return RedirectResponse(url="/api/via-db/items/")
    # return {"success": "정상동작중입니다"}
    return {"success": f"fastapi 서버로서 {os.path.basename(__file__)}를 구동 중 입니다"}


@app.get("/test/ui", response_class=HTMLResponse, tags=["테스트 UI"])  # response_class=HTMLResponse 설정하면 return 한 str 이 html response 로 렌더링
async def test_urls_routing(request: Request):
    prefix_promised = '/'
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    content = '''
        <html>
        <head>
        <title>FastAPI - 웹 테스트 UI</title>
        <link rel="icon" href="https://red-steps.netlify.app/favicon.ico" >
        </head>
        <form name="fm_request">
    '''
    for index, route in enumerate(app.routes):
        if hasattr(route, "path"):
            # href = f"{request.base_url}{prefix_promised}{route.path}"
            href = f"{str(request.base_url)[0:-1]}{route.path}"
            a_tag_text = href
            content += f'<span>{index}</span><span><a href="{href}">{a_tag_text}</a></span><br>'
    content += '''
        </form>
        </html>
    '''
    return content


# app.include_router(router_member_test.router, prefix="/test", tags=["테스트"])
app.include_router(router_main.router, prefix="/web", tags=["회원관리 메인페이지"])
app.include_router(router_join.router, prefix="/web", tags=["회원관리 가입페이지"])
app.include_router(router_login.router, prefix="/web", tags=["회원관리 로그인페이지"])
app.include_router(router_commutation_management.router, prefix="/web", tags=["근태관리 웹페이지"])
app.include_router(router_user.router, prefix="/api", tags=["USER API (DB JSON)"])
app.include_router(router_book.router, prefix="/api", tags=["BOOK API (DB JSON)"])
# app.include_router(router_commutation_management.router, prefix="/web", tags=[" 업무파일 백업 공유"])
# app.include_router(router_commutation_management.router, prefix="/web", tags=[" 파일 업로드 처리 페이지"])
# app.include_router(router_commutation_management.router, prefix="/web", tags=[" 업무자동화 파일 공유"])
# app.include_router(router_commutation_management.router, prefix="/web", tags=[" 업무 FAQ"])
# app.include_router(router_commutation_management.router, prefix="/web", tags=[" 업무 FAQ 상세페이지"])

# app.include_router(router_item_util.router, prefix="/api/via-db", tags=["상품관리 API"])
# app.include_router(router_todo_util.router, prefix="/api/via-db", tags=["할일관리 API(mysql.test_db.todos 에 저장), 미완성"])
# app.include_router(router_member_util.router, prefix="/api/via-db", tags=["회원관리 API(maria.test_db.members 에 저장), 미완성"])
# app.include_router(router_user_util.router, prefix="/api/via-db", tags=["회원관리 API(mysql.test_db.users 에 저장), 미완성"])
# pkg_routers 하나의 파일로 관리 __init__.py
# app.include_router(pkg_routers.user_router, prefix="/api/via-db", tags=["pkg_routers 테스트"])
# app.include_router(pkg_routers.member_router, prefix="/api/via-db", tags=["pkg_routers 테스트"])

# 파비콘 라우팅 처리
# @app.get('/favicon.ico', include_in_schema=False)
# async def get_favicon():
#     # DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
#     # return PlainTextResponse('')
#     # return Response(content=b'', media_type='image/x-icon')
#     # raise HTTPException(status_code=404)
#     # raise HTTPException(status_code=500)
#     pass  # 이렇게 하면 favicon 요청에 대한 콘솔에 출력 안됨





# "if name == "main":" 코드는
# 이 파일이 직접 실행되는 경우만 이 코드 블록은 실행됩니다.
# 이 파일을 import하여 사용할 때는 해당 코드 블록이 실행되지 않습니다.
# 이 파일을 uvicorn으로 실행하면 해당 코드 블록이 실행되지 않습니다. 이는 # dev 에서만 동작되는 것으로 사용할 수 있습니다.
if __name__ == "__main__":
    uvicorn.run(app=f"{FileSystemUtil.get_target_as_n(__file__)}:app", host=UvicornUtil.Settings.host, port=UvicornUtil.Settings.port)






