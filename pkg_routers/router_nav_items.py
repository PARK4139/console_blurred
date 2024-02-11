import inspect

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from pkg_park4139 import DebuggingUtil, MySqlUtil, BusinessLogicUtil, FastapiUtil, MemberUtil, SecurityUtil, TestUtil, StateManagementUtil

templates = Jinja2Templates(directory=r"pkg_web/templates")

router = APIRouter()
router.mount("/static", StaticFiles(directory="pkg_web/static"), name="static")

prefix_promised = "web"  # /web 는 다른 파일에 작성된 부분이다. 라우터를 다른 파일로 분리했기 때문에 이 부분은 유지보수하며 알아내기가 까다롭다 # 하드코딩
default_redirection_page_without_prefix = '/developer/tests/routing'
# default_redirection_page_without_prefix = '/member/login'
default_redirection_page = f'/{prefix_promised}{default_redirection_page_without_prefix}'




NAV_ITEMS_JSON = StateManagementUtil.NAV_ITEMS_JSON
NAV_ITEMS = FastapiServerUtil.init_and_update_json_file(NAV_ITEMS_JSON)



@app.get("/")
async def return_success():
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    DebuggingUtil.print_ment_via_colorama(f"{inspect.currentframe().f_code.co_name}() 호출되었습니다", colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
    return {"success": f"fastapi 서버로서 {os.path.basename(__file__)}를 구동 중 입니다"}

@app.get("/nav-items")
def get_nav_items():
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    [print(sample) for sample in NAV_ITEMS]
    return NAV_ITEMS

@app.get("/nav-items/{index}")
def get_nav_items_by_index(index: str):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
    try:
        return NAV_ITEMS[int(index)]
    except:
        DebuggingUtil.print_ment_fail(f"({len(NAV_ITEMS)})개의 등록된 nav_items 중, index 가 {index}인 nav_item 이 없습니다.")
        raise HTTPException(status_code=404, detail=f"({len(NAV_ITEMS)})개의 등록된 nav_items 중, index 가 {index}인 nav_item 이 없습니다.")

