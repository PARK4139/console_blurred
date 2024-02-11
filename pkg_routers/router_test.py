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


# @router.get("/")
# def read_root(request: Request):
#     context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
#     # return templates.TemplateResponse("index.html", context=context)
#     print(rf'{default_redirection_page} 로 리디렉션 됨')
#     return RedirectResponse(url=default_redirection_page)


@router.get('/developer/test/dash-board')
def route2023111110308(request: Request, jinja_data: FastapiUtil.jinja_data):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    FastapiUtil.jinja_data.prefix_promised = prefix_promised
    context = {
        "request": request, "jinja_data": jinja_data
    }
    return templates.TemplateResponse("/developer/main.html", context=context)


@router.get('/administrator')
def route2023111110309(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    FastapiUtil.jinja_data.prefix_promised = prefix_promised
    context = {
        "request": request, "jinja_data": FastapiUtil.jinja_data
    }
    return templates.TemplateResponse("/admin/main.html", context=context)

