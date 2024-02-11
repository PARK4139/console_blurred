import inspect

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pkg_park4139 import DebuggingUtil, MySqlUtil, BusinessLogicUtil, FastapiUtil, MemberUtil, CommutationManagementUtil

templates = Jinja2Templates(directory=r"pkg_web/templates")

router = APIRouter()
router.mount("/static", StaticFiles(directory="pkg_web/static"), name="static") # 적용되는지 테스트 필요함.

prefix_promised = "web"  # /web 는 다른 파일에 작성된 부분이다. 라우터를 다른 파일로 분리했기 때문에 이 부분은 유지보수하며 알아내기가 까다롭다 # 하드코딩
default_redirection_page_without_prefix = '/developer/tests/routing'
# default_redirection_page_without_prefix = '/member/login'
default_redirection_page = f'/{prefix_promised}{default_redirection_page_without_prefix}'

@router.post('/go-to-office', response_class=HTMLResponse)
def route2023111110321(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # 오늘날짜로 출근한적 있는지 조회
    # 한적있으면 return


    # 변수에 저장
    server_time = BusinessLogicUtil.get_time_as_('%Y %m %d %H %M %S')
    HH = server_time.split(' ')[3]
    mm = server_time.split(' ')[4]
    ss = server_time.split(' ')[5]
    name = request.session['name']

    members = MySqlUtil.get_session_local().query(MemberUtil.Member).filter_by(id=request.session['id'], name=request.session['name']).limit(10).all()
    print(len(members))
    if len(members) == 1:
        for member in members:

            # 객체에 바인딩
            member_data = {
                'id': request.session['id'],
                'name': name,
                'phone_no': member.phone_no,
                'time_to_go_to_office': '-',
                'time_to_leave_office': server_time
            }

            # 데이터베이스에 저장
            CommutationManagementUtil.insert_commutation_management(commutation_management=member_data, db=MySqlUtil.get_session_local())
    return f'''
        <div>{name} 님 {HH}시 {mm}분 {ss}초 출근처리 되었습니다.</div>
        <script>
            setTimeout(function() {{
                window.location.href='/{prefix_promised}/member'  
                // window.close(); 
            }}, 2000);
        </script>
    '''


@router.post('/leave-office', response_class=HTMLResponse)
def route202311110410(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # 오늘날짜로 출근한적 있는지 조회
    # 한적없으면 return



    # 변수에 저장
    server_time = BusinessLogicUtil.get_time_as_('%Y %m %d %H %M %S')
    HH = server_time.split(' ')[3]
    mm = server_time.split(' ')[4]
    ss = server_time.split(' ')[5]
    name = request.session['name']
    members = MySqlUtil.get_session_local().query(MemberUtil.Member).filter_by(id=request.session['id'], name=request.session['name']).limit(10).all()
    print(len(members))
    if (len(members) == 1):
        for member in members:

            # 객체에 바인딩
            member_data = {
                'id': request.session['id'],
                'name': name,
                'phone_no': member.phone_no,
                'time_to_go_to_office': '-',
                'time_to_leave_office': server_time
            }

            # 데이터베이스에 저장
            CommutationManagementUtil.insert_commutation_management(commutation_management=member_data, db=MySqlUtil.get_session_local())

    return f'''
        <div>{name} 님 {HH}시 {mm}분 {ss}초 퇴근처리 되었습니다.</div>
        <script>
            setTimeout(function() {{
                window.location.href='/{prefix_promised}/member'  
                // window.close(); 
            }}, 2000);
        </script>
    '''


# 파일 확장자 유효성 확인 기능
def check_allowed_file_or_not(filename, request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'toml'}  # 파일 업로드 가능 확장자 SETTING


@router.post('/member/faq-board')
def route2023111110316(request: Request, jinja_data: FastapiUtil.jinja_data):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # datas = {
    #     'id': request.session['id'],
    #     'login_time': request.session['login_time'],
    #     'name': request.session['name'],
    # }

    FastapiUtil.jinja_data.prefix_promised = prefix_promised
    context = {
        "request": request, "jinja_data": jinja_data
    }
    return templates.TemplateResponse('/member/faq_board.html', context=context)


@router.get('/member/file-upload')
def route20231111203226(request: Request, jinja_data: FastapiUtil.jinja_data):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")


    # def is_login_allowed():
    # session 기간 내에 로그인 한 경우
    if 'id' in request.session and request.session['id'] != '':
        return '''
            <!doctype html>
            <title>파일 공유</title>
            <h1>파일 공유</h1>
            <!-- __________________________________________________________________________________________________________________________________ 파일 공유 처리 s -->
            <form name='form-file-upload' action="/member/file-upload_" method="post" enctype="multipart/form-data">
                <input  type="file" name="file" value="promised202311110318" id="link20231111185433">
                <button type="submit">파일 업로드</button>
            </form>
            <!-- __________________________________________________________________________________________________________________________________ 파일 공유 처리 e -->
                '''
    else:
        # session 기간 내에 로그인 하지 않은 경우
        FastapiUtil.jinja_data.prefix_promised = prefix_promised
        context = {
            "request": request, "jinja_data": jinja_data
        }
        return templates.TemplateResponse('/member/login.html', context=context)


#
#
# # from werkzeug.utils import secure_filename
# get
# post @ router.route('/member/file-upload_')
# def upload_file( request: Request):
#     DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")
#
#     # check if the post request has the file part
#     if 'file' not in request.files:
#         return f'''
#             <!doctype html>
#             <script>
#             alert("요청하신 파일이 없어 업로드에 실패했습니다");
#             window.location.href = "/member";
#             </script>
#             '''
#     file = request.files['file']
#     if file.filename == '':
#         return f'''
#             <!doctype html>
#             <script>
#             alert("요청하신 파일명이 공백으로 업로드할 수 없습니다");
#             window.location.href = "/member";
#             </script>
#             '''
#     if file and check_allowed_file_or_not(file.filename):
#         print(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
#         # return RedirectResponse('/member')
#         return f'''
#             <!doctype html>
#             <script>
#             alert("파일이 업로드 되었습니다.");
#             window.location.href = "/member";
#             </script>
#             '''
#     return f'''
#     <!doctype html>
#     <script>
#     alert("파일 업로드 중 예외적인 상황이 발생했습니다. 관리자에게 문의해주세요. ");
#     window.location.href = "/member";
#     </script>
#     '''
#


@router.route('/member/file-download')
def route202311161941(request: Request, jinja_data: FastapiUtil.jinja_data):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    if 'id' in request.session and request.session['id'] != '':
        # session 기간 내에 로그인 한 경우
        datas = {
            'id': request.session['id'],
            'login_time': request.session['login_time'],
            'name': request.session['name'],
        }
        FastapiUtil.jinja_data.prefix_promised = prefix_promised
        context = {
            "request": request, "jinja_data": jinja_data
        }
        return templates.TemplateResponse('/member/utility_download.html', context=context)
    else:
        # session 기간 내에 로그인 하지 않은 경우
        FastapiUtil.jinja_data.prefix_promised = prefix_promised
        context = {
            "request": request, "jinja_data": jinja_data
        }
        return templates.TemplateResponse('/member/login.html', context=context)


# 테스트페이지
@router.route('/test-native-query')
def test_native_query_and_render(request: Request):
    DebuggingUtil.commentize(f"{inspect.currentframe().f_code.co_name}()")

    # print(" __________________________________________________________________________________________________________________________________ native_query to dictionary s[명시적이기 때문에 베스트 같다]")
    # db = pymysql.connect(
    #     host        =config_db['host'],
    #     user        =config_db['user'],
    #     password    =config_db['password'],
    #     database    =config_db['database'],
    #     charset='utf8'
    #     cursorclass = pymysql.cursors.DictCursor # 딕셔너리로 받기위한 커서
    # )
    # cursor = db.cursor()
    # sql = """
    #     select * from request_tb rt
    # """
    # cursor.execute(sql)
    # result_dictionary = cursor.fetchall()
    # print(result_dictionary)
    # pause()
    # print(" __________________________________________________________________________________________________________________________________ native_query to dictionary e")

    # print(" __________________________________________________________________________________________________________________________________ NATIVE_QUERY UPDATE SETTING s")
    # # row        = None
    # # connection = None
    # db = pymysql.connect(
    #     host        =config_db['host'],
    #     user        =config_db['user'],
    #     password    =config_db['password'],
    #     database    =config_db['database'],
    #     charset='utf8'
    #     cursorclass = pymysql.cursors.DictCursor
    # )
    # cursor = db.cursor()
    # values_to_bind = [
    #     {'CUSTOMER_NAME': '_박_정_훈_11_', 'MASSAGE': '주문서변경요청','DATE_REQUESTED': str(get_time_as_style("0"))},
    # ]
    # sql ='''
    #     UPDATE REQUEST_TB
    #     SET CUSTOMER_NAME = %(CUSTOMER_NAME)s ,
    #         MASSAGE = %(MASSAGE)s ,
    #         DATE_REQUESTED = %(DATE_REQUESTED)s
    #     WHERE ID_REQUEST = 11
    #     ;
    # '''
    # cursor.executemany(sql, values_to_bind)
    # db.commit()
    # pause()
    # print(" __________________________________________________________________________________________________________________________________ NATIVE_QUERY UPDATE SETTING e")

    # print(" __________________________________________________________________________________________________________________________________ ORM INSERT SETTING s")
    # engine = create_engine(db_url)
    # Base = declarative_base()
    #
    # class REQUEST_TB(Base):
    #     __tablename__ = "REQUEST_TB"
    #     ID_REQUEST = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    #     CUSTOMER_NAME = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
    #     MASSAGE = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
    #     DATE_REQUESTED = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
    #     USE_YN = sqlalchemy.Column(sqlalchemy.VARCHAR(length=2))
    #
    # Session = sqlalchemy.orm.sessionmaker()
    # Session.configure(bind=engine)
    # session = Session()
    # session.add(REQUEST_TB(CUSTOMER_NAME="_박_정_훈_y_", MASSAGE="주문서변경요청", DATE_REQUESTED=BusinessLogicUtil.get_time_as_('%Y_%m_%d_%H_%M_%S'), USE_YN="Y"))
    # session.commit()
    # session.close()
    # print(" __________________________________________________________________________________________________________________________________ ORM INSERT SETTING e")

    return ''

# fastapi app 상단 설정으로 옮겨야함, 쓸 시간에 작업을하면 더 효율이 날 수 있다. 만약 감을 잡은 상태라면. 생각이 먼저고 감이 먼저다. 그다음 효율이다.
# app.config.from_object(config) # config.py 를 사용해서 SETTING
# app.config.from_envvar('APP_CONFIG_FILE')  # 환경변수 APP_CONFIG_FILE 에 저장된 파일주소 가져와서 설정
