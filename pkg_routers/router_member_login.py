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



@router.get('/member/login')
def login(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # session 에 id 확인
    if 'id' in request.session and request.session['id'] != '':
        return RedirectResponse('/member')
    else:
        return templates.TemplateResponse('/member/login.html', {"request": request})


@router.post('/member/login1', response_class=HTMLResponse)
async def login_(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # html 파일의 form 으로 부터 전송된 데이터 form_data 에 저장
    form_data = await request.form()
    print(rf'form_data["id"] : {form_data["id"]}')
    print(rf'form_data["pw"] : {form_data["pw"]}')

    # sql injection 간단히 확인
    if not SecurityUtil.is_sql_injection_safe_simply(data=form_data["id"]):  # 그럼 아이디에 sql 키워드와 동일한건 못넣는 거네
        return f'''
                    <script>
                        alert("SQL 인젝션")
                        setTimeout(function() {{
                            window.location.href='/{prefix_promised}/member' 
                        }}, 500);
                    </script>
                '''

    if form_data["id"].strip() == "":
        return f'''
                    <script>
                        alert("아이디가 입력되지 않았습니다")
                        setTimeout(function() {{
                            window.location.href='/{prefix_promised}/member' 
                        }}, 500);
                    </script>
                '''
    if form_data["pw"].strip() == "":
        return f'''
                    <script>
                        alert("패스워드가 입력되지 않았습니다")
                        setTimeout(function() {{
                            window.location.href='/{prefix_promised}/member' 
                        }}, 500);
                    </script>
                '''


    if form_data["id"].strip() == "" or form_data["pw"].strip() == "":
        return f'''
                    <script>
                        alert("패스워드 또는 아이디가 입력되지 않았습니다")
                        setTimeout(function() {{
                            window.location.href='/{prefix_promised}/member' 
                        }}, 500);
                    </script>
                '''

    if MemberUtil.is_member_joined(id=form_data['id'], pw=form_data['pw'], request=request):
        # 세션에 세션내 에서 유지할 데이터 저장
        request.session['id'] = form_data['id']
        request.session['login_time'] = BusinessLogicUtil.get_time_as_('%Y_%m_%d_%H_%M_%S')
        for member_joined in result:
            print(f'member_joined.name: {member_joined.name}  member_joined.id: {member_joined.id}   member_joined.pw: {member_joined.pw}')
            request.session['name'] = member_joined.name

        return f'''
                <script>
                    alert("로그인 되었습니다")
                    setTimeout(function() {{
                        window.location.href='/{prefix_promised}/member'
                    }}, 500);
                </script>
                '''
    else:
        return f'''
                <script>
                    alert("패스워드 또는 아이디가 틀렸습니다.") 
                    setTimeout(function() {{
                          window.location.href='/{prefix_promised}/member'
                    }}, 500);
                </script>
                '''
    # context = {"request": request, "jinja_data": jinja_data}
    # return templates.TemplateResponse('login.html', context=context)


@router.post('/member/logout')
def logout(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # 세션에서 id 제거
    request.session.pop('id', None)

    # 세션 내 모든 값 삭제
    # request.session.clear()
    return RedirectResponse(f'/{prefix_promised}/member')

