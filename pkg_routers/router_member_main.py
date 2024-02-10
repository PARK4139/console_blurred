import inspect

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from pkg_park4139 import DebuggingUtil, MySqlUtil, BusinessLogicUtil, FastapiUtil, MemberUtil, SecurityUtil, TestUtil

templates = Jinja2Templates(directory=r"pkg_web/templates")

router = APIRouter()
router.mount("/static", StaticFiles(directory="pkg_web/static"), name="static")

prefix_promised = "web"  # /web 는 다른 파일에 작성된 부분이다. 라우터를 다른 파일로 분리했기 때문에 이 부분은 유지보수하며 알아내기가 까다롭다 # 하드코딩
default_redirection_page_without_prefix = '/developer/tests/routing'
# default_redirection_page_without_prefix = '/member/login'
default_redirection_page = f'/{prefix_promised}{default_redirection_page_without_prefix}'


@router.get("/member")
async def route_get_member(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    FastapiUtil.jinja_data.prefix_promised = prefix_promised
    
    if 'id' in request.session and request.session['id'] != '':
        # session 기간 내에 로그인 한 경우
        context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
        return templates.TemplateResponse("/member/main.html", context=context)
    else:
        # session 기간 내에 로그인 하지 않은 경우
        context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
        return templates.TemplateResponse("/member/login.html", context=context)


@router.post("/member")
async def route_post_member(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    FastapiUtil.jinja_data.prefix_promised = prefix_promised

    # foo.html 에서 전송된 form 데이터를 변수에 저장 
    form_data = await request.form()
    for field in form_data:
        print(f"Field: {field}, Value: {form_data[field]}")

    if 'id' in request.session and request.session['id'] == form_data['id']:
        # session 기간 내에 로그인 한 경우
        context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
        return templates.TemplateResponse("/member/main.html", context=context)
    else:
        # session 기간 내에 로그인 하지 않은 경우
        context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
        return templates.TemplateResponse("/member/login.html", context=context)

