__author__ = 'PARK4139 : Jung Hoon Park'

# -*- coding: utf-8 -*-  # python 3.x 하위버전 호환을 위한코드
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
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QTextEdit, QTableWidget, QTableWidgetItem, QDialog
import pkg_park4139
import clipboard
import shutil
from BlurWindow.blurWindow import GlobalBlur, blur
import pkg_park4139
from console_blurred import MacroWindow

Park4139 = pkg_park4139.Park4139()


# LOGGER SET UP
# logger = logging.getLogger('park4139_test_logger')
# hdlr = logging.FileHandler('park4139_logger.log')
# hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)


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

# 테스트 루프 카운트 최대치 설정
test_loop_limit = 3


@Park4139.decorate_seconds_performance_measuring_code
@decorate_for_pause  # 테스트 루프 마다 정지 설정
def test():
    try:
        # cmd = rf'python "{test_target_file}"' # SUCCESS # 가상환경이 아닌 로컬환경에서 실행이 됨.
        # cmd = rf'start cmd /k "{test_helping_bat_file}" {test_target_file}'  # SUCCESS # 가상환경에서 실행 # 새 cmd.exe 창에서 열린다
        # cmd = rf'start /b cmd /c "{test_helping_bat_file}" {test_target_file}' # FAIL  # 가상환경에서 실행되나 콘솔에 아무것도 출력되지 않음
        # cmd = rf'call "{test_helping_bat_file}" {test_target_file}'  # FAIL  # 가상환경에서 실행되나 콘솔에 사용자 입력만 출력됨
        # cmd = rf'"{test_helping_bat_file}" {test_target_file}' # FAIL  # 가상환경에서 실행되나  콘솔에 사용자 입력만 출력됨
        # cmd = rf'call cmd /c "{test_helping_bat_file}" {test_target_file}'  # FAIL  # 가상환경에서 실행되나 콘솔에 사용자 입력만 출력됨
        # cmd = rf'start cmd /c "{test_helping_bat_file}" {test_target_file}'  # SUCCESS # 가상환경에서 실행 # 새 cmd.exe 창에서 열린다 #이걸로 선정함
        # park4139.get_cmd_output(cmd)

        # Park4139.debug_as_cli(f"test")
        # Park4139.debug_as_gui(f"test")

        # Park4139.ask_to_google(question)
        # Park4139.ask_to_bard(question)
        # Park4139.ask_to_wrtn(question)

        # Park4139.speak_alt("테스트")

        # app = QApplication()
        # dialog = CustomDialogBox(contents="웹 크롤링 결과를 화면에 시현할까요?", buttons=["시현하기", "시현하지 않기", "좋아요"])
        # dialog.exec_()
        # app.exec()

        # app = QApplication()
        # Park4139.get_comprehensive_weather_information_from_web()
        # app.exec()


        # _________________________________________  UP (TESTED SUCCESS) _________________________________________
        # app = QApplication()
        # import test_core # 호출이 되어 버릴 것을 기대
        # app.exec()

        from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QLabel

        app = QApplication([])

        # 스크롤 영역을 생성합니다.
        scroll_area = QScrollArea()



        # 스크롤 가능한 QGridLayout을 생성합니다.
        grid_layout = QGridLayout()

        # 예시로 QLabel을 몇 개 추가합니다.
        for i in range(100):
            label = QLabel(f"Label {i}")
            grid_layout.addWidget(label, i // 4, i % 4)

        # 스크롤 영역에 스크롤 가능한 위젯을 설정합니다.
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scrollable_widget)

        # 메인 윈도우에 스크롤 영역을 추가합니다.
        main_widget = QWidget()
        main_layout = QGridLayout(main_widget)
        main_layout.addWidget(scroll_area)

        main_widget.show()
        app.exec()

        # _________________________________________ BELOW (NOT TESTED YET) _________________________________________
        # 사용에 유의해야 한다.
        # 값이 공유가 되니 유의해야 한다. 오히려 이점을 활용해서 공유객체를 사용할 수 있지 않을까?

        # 얕은 복사 실험 # 이것도 얕은 복사네요.
        # li = [1, 2]
        # ls_copied = li
        # ls_copied[0] = 2
        # print(ls_copied) # [2, 2]
        # print(ls) # [2, 2]? or [1, 2]?

        # 얕은 복사 실험
        # li = [1, 2]
        # ls_copied = copy.copy(li)
        # ls_copied[0] = 2
        # print(ls_copied) # [2, 2]
        # print(ls) # [2, 2]? or [1, 2]?

        # 깊은 복사 실험
        # li_deepcopied=copy.deepcopy(li) # 오히려 딥카피의 경우가 사용하는데 자유로운 생각이 든다.

        # 셀레니움 새로운 문법
        # https://selenium-python.readthedocs.io/locating-elements.html
        # find_element(By.ID, "id")
        # find_element(By.NAME, "name")
        # find_element(By.XPATH, "xpath")
        # find_element(By.LINK_TEXT, "link text")
        # find_element(By.PARTIAL_LINK_TEXT, "partial link text")
        # find_element(By.TAG_NAME, "tag name")
        # find_element(By.CLASS_NAME, "class name")
        # find_element(By.CSS_SELECTOR, "css selector")

        # park4139_archive_log = Park4139.park4139_archive_LOG
        # key = "park4139_archive_log_line_cnt"
        # park4139.monitor_target_edited_and_bkup(target_abspath=park4139_archive_log, key=key)

        # foo = ",".join(key for key in park4139.keyboards).split(",")# DICTIONARY TO STR AS CSV STYLE
        # print(foo)

        # foo = [keyValue for keyValue in park4139.keyboards]
        # print(foo)

        # for key, value in park4139.keyboards.items():
        #     print(key, value)
        # for key, value in park4139.keyboards.items():
        #     print(key)
        # for key, value in park4139.keyboards.items():
        #     print(value)

        # # 여러개 체크박스 체크 예제
        # for i in pyautogui.locateAllOnScreen("checkbox.png"):
        #     pyautogui.click(i, duration=0.25)

        # 화면에서 특정범위를 제한하여 이동할때
        # img_capture = pyautogui.locateOnScreen("Run_icon.png", region=(1800, 0, 1920, 100))
        # img_capture = pyautogui.locateOnScreen("Run_icon.png", confidence=0.7)  # 인식이 잘안될때   유사도 70%  으로 설정
        # pyautogui.moveTo(img_capture)

        # 파이썬 리스트 특정요소를 특정문자를 기준으로 두 요소로 분리해서 그 특정요소 리스트 자리에 그대로 삽입하는 코드   ['1','온도많음','2'] -> ['1','온도','많음','2']
        # certain_text: str = '온도'
        # results_ = []
        # for item in results:
        #     if certain_text in item:
        #         words = item.split(certain_text)
        #         results_.append(certain_text)
        #         results_.extend(words)
        #     else:
        #         results_.append(item)
        # results: [str] = results_
        # Park4139.debug_as_gui(context=f"{results}")

        # 파이썬 리스트의 요소홀수가 key 요소짝수가 value 로서 dict 에 넣기
        # results_: dict = {}
        # for i in range(0, len(results) - 1, 2):
        #     if i == len(results) - 1:
        #         pass
        #     else:
        #         results_[results[i]] = results[i + 1]
        # results: dict = results_

        # results = soup.select(copied_html_selector)
        # for index, element in enumerate(results, 1):
        #     # print("{} 번째 text: {}".format(index, element.text))
        #     continue
        # element_str = element.text.strip().replace('현재 온도', '')
        # print(element_str)

        # soup.prettify()
        # print(str(soup))
        # print(str(soup.prettify()))

        # for index, element in enumerate(elements, 1):
        #     # print("{} 번째 text: {}".format(index, element.text))
        #     continue

        pass

    except SystemExit:  # sys.exit() 호출을 의도적으로 판단
        pass
    except:
        Park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        Park4139.pause()


content = r"""


처리할 코드는 여기에 작성


"""

# 나중에 TDD 공부를 해볼 것.
# 파일 변화 확인 로직 필요.
# 파일 읽어와서 전체 자리수가 바뀌면 파일 변화 한 것으로 보면 된다. 완벽하진 않아도 대부분 해소
# git으로 관리되는 프로젝트이면 git으로도 확인 가능
error_cnt = 0
if __name__ == '__main__':
    try:
        test_loop_cnt = 1
        Park4139.commentize("TRYING TO ENTER TEST LOOP...")
        while True:  # test loop
            try:
                if test_loop_cnt == test_loop_limit + 1:
                    break
                Park4139.commentize(f" TEST LOOP {test_loop_cnt} STARTED")
                test()
                Park4139.commentize(f" TEST LOOP {test_loop_cnt} ENDED")

            except:
                print_with_test_status()
                continue
            test_loop_cnt = test_loop_cnt + 1
            # Park4139.sleep(milliseconds=1000)# 루프 텀 설정

        # 의도적 트러블 발생 테스트
        # raise shutil.Error("의도적 트러블 발생")
    except Exception as e:
        # print(str(e))
        # logger.info(f'logger: dst : {"??????"}')
        # logger.error(msg="에러발생?????")
        # logger.error(f'logger: str(e) : {"????????"}')
        # park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        error_cnt = error_cnt + 1
        error_str = traceback.format_exc()
        Park4139.debug_as_gui(f"TEST LOOP ERROR CNT REPORT:\nerror_cnt : {error_cnt}\nerror_str : {error_str}")
        # Park4139.pause()
