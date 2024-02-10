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



'''
출근 처리 페이지
'''

@router.post('/go-to-office')
def route2023111110321( request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # 변수에 저장
    server_time = BusinessLogicUtil.get_time_as_('%Y_%m_%d_%H_%M_%S')
    HH = server_time.split(' ')[3]
    mm = server_time.split(' ')[4]
    ss = server_time.split(' ')[5]
    name = session['name']
    members = db_session.query(member_joined_list).filter_by(id=session['id'], name=session['name']).limit(10).all()
    print(len(members))
    if (len(members) == 1):
        for member in members:
            # print(member.id)
            # print(member.name)
            # print(member.phone_no)
            print(validate_phone_number(member.phone_no))
            # member_commutation_management_tb에 저장
            member_commutation_management.add_db_record(id=session['id'], name=session['name'], phone_no=member.phone_no, time_to_go_to_office=server_time, time_to_leave_office='-')
    return f'''
        <div>{name} 님 {HH}시 {mm}분 {ss}초 출근처리 되었습니다.</div>
        <script>
            setTimeout(function() {{
                window.location.href='/{prefix_promised}/member'  
                // window.close(); 
            }}, 2000);
        </script>
    '''


'''
퇴근 처리 페이지
'''


@router.post('/leave-office')
def route202311110410(, request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # 변수에 저장
    server_time = BusinessLogicUtil.get_time_as_('%Y_%m_%d_%H_%M_%S')
    HH = server_time.split(' ')[3]
    mm = server_time.split(' ')[4]
    ss = server_time.split(' ')[5]
    name = session['name']
    members = db_session.query(member_joined_list).filter_by(id=session['id'], name=session['name']).limit(10).all()
    print(len(members))
    if (len(members) == 1):
        for member in members:
            # print(member.id)
            # print(member.name)
            # print(member.phone_no)
            print(validate_phone_number(member.phone_no))
            # member_commutation_management_tb에 저장
            member_commutation_management_tb.add_db_record(id=session['id'], name=session['name'], phone_no=member.phone_no, time_to_go_to_office='-', time_to_leave_office=server_time)

    return f'''
        <div>{name} 님 {HH}시 {mm}분 {ss}초 퇴근처리 되었습니다.</div>
        <script>
            setTimeout(function() {{
                window.location.href='/{prefix_promised}/member'  
                // window.close(); 
            }}, 2000);
        </script>
    '''
