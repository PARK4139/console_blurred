import random
import sys
import re
import os
import traceback
import logging
from ctypes.wintypes import HWND

import keyboard
import pyautogui
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QScreen, QIcon, QShortcutEvent, QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QTextEdit, QTableWidget, QTableWidgetItem

# CUSTOM PY PKG SET UP
import pkg_park4139
import clipboard

from BlurWindow.blurWindow import GlobalBlur, blur

__author__ = 'Park4139 : Jung Hoon Park'

Park4139 = pkg_park4139.Park4139()

# LOGGER SET UP
logger = logging.getLogger('park4193_test_logger')
hdlr = logging.FileHandler('park4193_logger.log')
hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


@Park4139.decorate_seconds_performance_measuring_code
def generate_mp3_file_for_time_performance():  # time performance : 9028 초 /60 /60  =  2.5 시간
    """
    시간에 대한 mp3 파일 작업 최적화 함수
    """
    for HH in range(24, 0, -1):
        for mm in range(0, 60):
            Park4139.commentize(f'{int(HH)}시')
            Park4139.commentize(f'{int(mm)}분 입니다')


# park4139.commentize() 메소드 테스트 결과, 1개 파일을 만들어 실행하는 데까지 무려 11초 정도로 측정됨, ffmpeg 작업 속도로 문제
# 의도적으로 mp3 파일을 미리 만들어, ffmpeg 로 두 파일 합성작업 시간을 줄일수 있으므로, 성능 최적화 기대,
# 따라서, 코드에서 사용되는 모든 텍스트를 추출하여 park4139.commentize 하도록 하여, 최적화시도해보자
# 번외로 리스트의 파라미터를 몇개까지 가능하지 테스트 해보고 싶긴한데, 망가져도 되는 컴퓨터로 시도해보자


def decorate_test_status_printing_code(function):
    def wrapper():
        Park4139.commentize(rf"test status")
        function()

    return wrapper


@decorate_test_status_printing_code
def print_with_test_status(status: str):
    print(status)


def decorate_for_pause(function):
    """
        # ctrl c ctrl c 이렇게 두번 눌르면 소스 수정 후 재시작 됩니다
        # 안그럼 계속 새롭게 창을 무한정 열게 되어 컴퓨터가 다운될 수 있습니다.
    """

    def wrapper():
        function()
        Park4139.pause()

    return wrapper



qss = """
    # QWidget {
    #     color: #FFFFFF;
    #     background: #333333;
    #     height: 32px;
    # }
    # QLabel {
    #     color: #FFFFFF;
    #     background: #333333;
    #     font-size: 16px;
    #     padding: 5px 5px;
    # }
    # QToolButton {
    #     background: #333333;
    #     border: none;
    # }
    # QToolButton:hover{
    #     background: #444444;
    # }
"""


@Park4139.decorate_seconds_performance_measuring_code
@decorate_for_pause
def test():
    try:
        question = "파이썬 이걸로 개발자로서 20년간 밥벌이가 될까?"

        # Park4139.ask_to_google(question)
        # Park4139.ask_to_bard(question)
        # Park4139.ask_to_wrtn(question)

        # Park4139.search_animation_data_from_web()

        # Park4139.run_rpa_program_legacy()

        Park4139.run_rpa_program()

        # cmd = rf'python "{test_target_file}"' # SUCCESS # 가상환경이 아닌 로컬환경에서 실행이 됨.
        # cmd = rf'start cmd /k "{test_helping_bat_file}" {test_target_file}'  # SUCCESS # 가상환경에서 실행 # 새 cmd.exe 창에서 열린다
        # cmd = rf'start /b cmd /c "{test_helping_bat_file}" {test_target_file}' # FAIL  # 가상환경에서 실행되나 콘솔에 아무것도 출력되지 않음
        # cmd = rf'call "{test_helping_bat_file}" {test_target_file}'  # FAIL  # 가상환경에서 실행되나 콘솔에 사용자 입력만 출력됨
        # cmd = rf'"{test_helping_bat_file}" {test_target_file}' # FAIL  # 가상환경에서 실행되나  콘솔에 사용자 입력만 출력됨
        # cmd = rf'call cmd /c "{test_helping_bat_file}" {test_target_file}'  # FAIL  # 가상환경에서 실행되나 콘솔에 사용자 입력만 출력됨
        # cmd = rf'start cmd /c "{test_helping_bat_file}" {test_target_file}'  # SUCCESS # 가상환경에서 실행 # 새 cmd.exe 창에서 열린다 #이걸로 선정함
        # park4139.get_cmd_output(cmd)

        # target_abspath = fr'{park4139.USERPROFILE}\Desktop\services\archive_py\parks2park_archive.log'
        # key = "parks2park_archive_log_line_cnt"
        # park4139.monitor_target_edited_and_bkup(target_abspath=target_abspath, key=key)

        # 딕셔너리 샘플.
        # tmp = ",".join(key for key in park4139.keyboards).split(",")
        # print(tmp)
        #
        # tmp = [keyValue for keyValue in park4139.keyboards]
        # print(tmp)
        #
        # for key, value in park4139.keyboards.items():
        #     print(key, value)
        # for key, value in park4139.keyboards.items():
        #     print(key)
        # for key, value in park4139.keyboards.items():
        #     print(value)
        #
        # tmp = {keyValue for keyValue in park4139.keyboards}
        # print(tmp)

        # # 여러개 체크박스 체크 예제
        # for i in pyautogui.locateAllOnScreen("checkbox.png"):
        #     pyautogui.click(i, duration=0.25)
        #
        # # 화면에서 특정범위를 제한하여 이동할때
        # img_capture = pyautogui.locateOnScreen("Run_icon.png", region=(1800, 0, 1920, 100))
        # img_capture = pyautogui.locateOnScreen("Run_icon.png", confidence=0.7)  # 인식이 잘안될때   유사도 70%  으로 설정
        # pyautogui.moveTo(img_capture)
        pass

    except:
        Park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        Park4139.pause()


# TDD 유사 환경
# 파일 변화 확인 로직 필요.
# 파일 읽어와서 전체 자리수가 바뀌면 파일 변화 한 것으로 보면 된다. 완벽하진 않아도 대부분 해소


content = r"""


처리할 코드는 여기에 작성


"""

if __name__ == '__main__':
    try:
        test_loop_cnt = 1
        while (True):
            yyyy = Park4139.get_time_as_('%Y')
            MM = Park4139.get_time_as_('%m')
            dd = Park4139.get_time_as_('%d')
            HH = Park4139.get_time_as_('%H')
            mm = Park4139.get_time_as_('%M')
            ss = Park4139.get_time_as_('%S')
            server_time = Park4139.get_time_as_(rf'%Y-%m-%d %H:%M:%S')
            Park4139.commentize("TRYING TO ENTER TEST LOOP...")
            # 5초 마다
            # if int(ss) % 5 == 0:
            if int(ss) % 1 == 0:
                while True:
                    try:
                        Park4139.commentize(f" TEST LOOP {test_loop_cnt} STARTED")
                        test()
                        Park4139.commentize(f" TEST LOOP {test_loop_cnt} ENDED")
                    except:
                        print_with_test_status()
                        continue
                    test_loop_cnt = test_loop_cnt + 1
                    # park4139.sleep(milliseconds=5000)
            # 루프 휴식
            # Park4139.sleep(milliseconds=1000)

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
