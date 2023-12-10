import sys
import re
import os
import traceback
import logging

# CUSTOM PY PKG SET UP
import pkg_park4139

__author__ = 'Park4139 : Jung Hoon Park'
park4139 = pkg_park4139.Park4139()

# LOGGER SET UP
logger = logging.getLogger('park4193_test_logger')
hdlr = logging.FileHandler('park4193_logger.log')
hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)




@park4139.decorate_seconds_performance_measuring_code
def generate_mp3_file_for_time_performance():  # time performance : 9028 초 /60 /60  =  2.5 시간
    """
    시간에 대한 mp3 파일 작업 최적화 함수
    """
    for HH in range(24, 0, -1):
        for mm in range(0, 60):
            park4139.speak(f'{int(HH)}시')
            park4139.speak(f'{int(mm)}분 입니다')


# park4139.speak() 메소드 테스트 결과, 1개 파일을 만들어 실행하는 데까지 무려 11초 정도로 측정됨, ffmpeg 작업 속도로 문제
# 의도적으로 mp3 파일을 미리 만들어, ffmpeg 로 두 파일 합성작업 시간을 줄일수 있으므로, 성능 최적화 기대,
# 따라서, 코드에서 사용되는 모든 텍스트를 추출하여 park4139.speak 하도록 하여, 최적화시도해보자
# 번외로 리스트의 파라미터를 몇개까지 가능하지 테스트 해보고 싶긴한데, 망가져도 되는 컴퓨터로 시도해보자


def decorate_test_status_printing_code(function):
    def wrapper():
        park4139.commentize(rf"test status")
        function()
    return wrapper

@decorate_test_status_printing_code
def print_with_test_status(status: str):
    print(status)



content = r"""


처리할 코드는 여기에 작성


"""


@staticmethod
def decorate_for_pause(function):
    """시간성능 측정 코드"""

    def wrapper():
        function()
        park4139.pause()
    return wrapper

@park4139.decorate_seconds_performance_measuring_code
def test_pauseless():
    # ctrl c ctrl c 이렇게 두번 눌르면 소스 수정 후 재시작 된다
    # 안그럼 계속 새롭게 창을 무한정 열게 되어 컴퓨터가 다운될 수 있습니다.
    pass


@park4139.decorate_seconds_performance_measuring_code
@decorate_for_pause
def test():
    # cmd = rf'python "{test_target_file}"' # SUCCESS # 가상환경이 아닌 로컬환경에서 실행이 됨.
    # cmd = rf'start cmd /k "{test_helping_bat_file}" {test_target_file}'  # SUCCESS # 가상환경에서 실행 # 새 cmd.exe 창에서 열린다
    # cmd = rf'start /b cmd /c "{test_helping_bat_file}" {test_target_file}' # FAIL  # 가상환경에서 실행되나 콘솔에 아무것도 출력되지 않음
    # cmd = rf'call "{test_helping_bat_file}" {test_target_file}'  # FAIL  # 가상환경에서 실행되나 콘솔에 사용자 입력만 출력됨
    # cmd = rf'"{test_helping_bat_file}" {test_target_file}' # FAIL  # 가상환경에서 실행되나  콘솔에 사용자 입력만 출력됨
    # cmd = rf'call cmd /c "{test_helping_bat_file}" {test_target_file}'  # FAIL  # 가상환경에서 실행되나 콘솔에 사용자 입력만 출력됨
    # cmd = rf'start cmd /c "{test_helping_bat_file}" {test_target_file}'  # SUCCESS # 가상환경에서 실행 # 새 cmd.exe 창에서 열린다 #이걸로 선정함
    # park4139.get_cmd_output(cmd)

    target_abspath = fr'{park4139.USERPROFILE}\Desktop\services\archive_py\parks2park_archive.log'
    key = "parks2park_archive_log_line_cnt"
    park4139.monitor_target_edited_and_bkup(target_abspath=target_abspath, key=key)





    pass


# TDD 유사 환경
# 파일 변화 확인 로직 필요.
# 파일 읽어와서 전체 자리수가 바뀌면 파일 변화 한 것으로 보면 된다. 완벽하진 않아도 대부분 해소






if __name__ == '__main__':
    try:
        test_loop_cnt = 1
        while (True):
            yyyy = park4139.get_time_as_('%Y')
            MM = park4139.get_time_as_('%m')
            dd = park4139.get_time_as_('%d')
            HH = park4139.get_time_as_('%H')
            mm = park4139.get_time_as_('%M')
            ss = park4139.get_time_as_('%S')
            server_time = park4139.get_time_as_(rf'%Y-%m-%d %H:%M:%S')
            park4139.commentize("TRYING TO ENTER TEST LOOP...")
            # 5초 마다
            if int(ss) % 5 == 0:
                while True:
                    try:
                        park4139.commentize(f"TEST LOOP INITIAL SET UP")
                        test_helping_bat_file = "test foo_py as virtual env.bat"
                        test_target_file = "test_keyboard.py"
                        # test_target_file = "test_pyside6_debugger.py"
                        print(f"test_target_file      :{test_target_file}")


                        park4139.commentize(f"{test_target_file} TEST LOOP {test_loop_cnt} STARTED")
                        # test_pauseless()
                        test()
                        park4139.commentize(f"{test_target_file} TEST LOOP {test_loop_cnt} ENDED")


                        # park4139.sleep(milliseconds=5000)
                        test_loop_cnt = test_loop_cnt + 1

                    except:
                        print_with_test_status()
                        # park4139.sleep(milliseconds=5000)
                        continue

            # 루프 휴식
            park4139.sleep(milliseconds=1000)

        # 의도적 트러블 발생
        # raise shutil.Error("의도적 트러블 발생")

        logger.info(f'logger: dst : {"??????"}')
    except Exception as e:
        # print(str(e))
        logger.error(msg="에러발생?????")
        logger.error(f'logger: str(e) : {"????????"}')

        # park4139.trouble_shoot("%%%FOO%%%")
        # traceback.print_exc(file=sys.stdout)
        # park4139.pause()
