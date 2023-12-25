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
        # Park4139.get_comprehensive_weather_information_from_web()
        # app.exec()

        # __________________________________________________________________________________________________________________________________ TESTED SECTION 1 S
        # import os
        #
        # import matplotlib
        # import pandas as pd  # 데이터 분석용
        # # import metaplotlib # pip install metaplotlib --upgrade
        # import numpy as np  # pip install numpy --upgrade
        # import FinanceDataReader as fdr  # alt+f12 # pip install -U finance-datareader #  FinanceDataReade.chart.plot()는 plotly에 의존성이 있습니다. pip install plotly --upgrade 를 진행하세요
        # from PySide6.QtCore import QCoreApplication
        # from PySide6.QtWidgets import QApplication
        #
        # import pkg_park4139
        #
        # # pyside6의 app이 없으면 pyside6 app을 만들어줌.
        # app: QApplication
        # if QCoreApplication.instance() == None:
        #     app = QApplication()
        #
        # # DataReader() 거래소주식정보(*,시세정보) 를 가져옴
        # # 005930 삼성전자
        # # fdr_dr = fdr.DataReader("005930") # 모든기간
        # # fdr_dr = fdr.DataReader("005930", "2021-01-01", "2022-02-23") # 특정기간
        # fdr_dr = fdr.DataReader("005930", "2023")  # 특정기간(특정년도)
        # #
        # # fdr_dr = fdr.DataReader('000150', '2018-01-01', '2019-10-30', exchange='KRX')  # 두산
        # # fdr_dr = fdr.DataReader('000150', '2018-01-01', '2019-10-30', exchange='SZSE')  # Yihua Healthcare Co Ltd
        # # fdr_dr = fdr.DataReader('036360', exchange='KRX-DELISTING') # KRX에서 상장폐지된
        #
        # # StockListing() 거래소주식정보(*,거래소상장주식목록)  가져옴
        # # df = fdr.StockListing('SSE')  # 상해
        # # df = fdr.StockListing('KONEX') # 코넥스
        # # df = fdr.StockListing('SZSE')
        # # df = fdr.StockListing('KRX')  # 한국
        # # df = fdr.StockListing('KOSDAQ')
        # # df = fdr.StockListing('KOSPI')
        # # df = fdr.StockListing('S&P500')
        # # df = fdr.StockListing('NYSE')  # 뉴욕거래소
        #
        # # test_result = df.plot.
        #
        # # sr = pd.Series(index=["피자", "치킨", "콜라", "맥주"], data=[17000, 18000, 1000, 5000])
        # # test_result = f"""
        # # {sr}
        # #
        # # {'-' * 79}
        # #
        # # index : {sr.index}
        # # values : {sr.values}
        # # """
        # # dialog = pkg_park4139.CustomDialogReplica(title="1차원데이터배열 출력 테스트결과 ( feat. pandas.시리즈 자료구조)", contents=test_result, buttons=["확인"])
        # # dialog.exec_()
        # #
        # #
        # #
        # #
        # #
        # #
        # # columns=['학번', '이름', '점수']
        # # data = [
        # #     ['1000', 'Steve', 90.72],
        # #     ['1001', 'James', 78.09],
        # #     ['1002', 'Doyeon', 98.43],
        # #     ['1003', 'Jane', 64.19],
        # #     ['1004', 'Pilwoong', 81.30],
        # #     ['1005', 'Tony', 99.14],
        # # ]
        # # df = pd.DataFrame(data=data, columns=columns)
        # # test_result= str(df)
        # # dialog = pkg_park4139.CustomDialogReplica(title="2차원데이터배열 출력 테스트결과 ( df 찐활용 feat. list )", contents=test_result, buttons=["확인"])
        # # dialog.exec_()
        #
        # # data = {
        # #     '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
        # #     '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
        # #     '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
        # #     }
        # #
        # # index=None # df 의 index 파라미터의 default , 자동증가숫자가 auto fill 됨
        # # # index=pd.RangeIndex(start=0, stop=5, step=1) # df 의 index 제어
        # # df = pd.DataFrame(data, index=index)
        # # # test_result= df.to_string() # 모든 줄 보기(데이터조회)
        # # # test_result= df.head(3).to_string() # 3 줄만 보기(데이터조회)
        # # # test_result= df['학번'].to_string() # 특정 컬럼만 보기(데이터조회)
        # # # test_result= df['학번'].to_string(index=False) # 특정 컬럼만 보기(데이터조회)
        # # test_result= df['학번'].to_string() # 특정 컬럼만 보기(데이터조회)
        # # dialog = pkg_park4139.CustomDialogReplica(title="2차원데이터배열 출력 테스트결과 ( df 찐활용 feat. dict )", contents=test_result, buttons=["확인"])
        # # dialog.exec_()
        #
        # # FILE_XLS = rf"{pkg_park4139.Park4139.PROJECT_DIRECTORY}\$cache_recycle_bin\test.xlsx"
        # # # df = pd.read_csv(FILE_CSV)
        # # # df = pd.read_sql(FILE_SQL)
        # # # df = pd.read_html(FILE_HTML)
        # # df = pd.read_excel(FILE_XLS)
        # # test_result = df.to_string()
        # # dialog = pkg_park4139.CustomDialogReplica(title="csv파일의 2차원데이터배열 출력 테스트결과", contents=test_result, buttons=["확인"])
        # # dialog.exec_()
        #
        # # pandas 공부 후기
        # # 엑셀에 있는 데이터들 처럼 데이터배열 을 예쁘게 해주는 라이브러리
        # # sr(series) 는 key, value 형태의 1차원배열데이터 에 사용. df 기능으로 대체가 되므로 굳이 잘 안쓸듯.
        # # df(dataframe) 은 2차원배열데이터에 사용. 즉, 엑셀처럼 사용, 엄청유용할 듯
        # # df 를 출력하면 기본적으로 auto increment number 가 auto fill 된다!, 유용함!, 근데 지우는 방법도 찾아보기
        # # csv/txt/xls/sql/html/json 파일 읽어올 수 있다고 하는데, html 도 되는데? 크롤링과 연계할 때 편리한 부분이 있을 수 있겠다
        #
        # data: np.ndarray
        # data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])  # 하드코딩으로 데이터배열
        # # data = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])  # 하드코딩으로 데이터배열
        # # data = np.zeros(shape=(3,3)) # shape=(3,3)인 배열에 모든 값이 0
        # # data = np.ones(shape=(3,3)) # shape=(3,3)인 배열에 모든 값이 1
        # # data = np.eye(3)# shape=(3,3)인 배열에 대각선 값이 1, 나머지 값이 0, 이거 활용도 높을 수 있겠다. 100  010  001 이런 순서 필요할때 있지 않겠나?
        # # data = np.random.random((2,2)) # shape=(3,3)인 배열에 모든 값이 1보다 작은 float(1인 경우가 있나 모르겠음)
        # # data = np.full(shape=(2,3), 7)#  # shape=(3,3)인 배열에 모든 값이 7
        # # data = np.arange(10) #배열개수가 10 인 1차원데이터배열 # 0~9
        # # data = np.arange(0, 10, 1) # 시작0, 종료10, 1씩증가 인1차원데이터배열 # 0~9
        # # data = [i for i in range(0,10,1)] # 0~9
        # # data = np.array(np.arange(30)).reshape((5, 6)) # shape = (5,6) 으로 reshape 한다, shape 안의 숫자들(5, 6) 을 곱(5 x 6)하면 원데이터의 개수(5 x 6 = 30)인와 같게 설정해야 된다. 실험해봐도 이게 맞음, list를 적당한 간격으로 자를때 유용하겠다!
        # # data = data[0, :]# 첫번째 줄 출력
        # # data = data[:,0]# 첫번째 기둥 출력
        # # data = data[1,1]# 특정위치의 원소
        # # data = data[[0, 2], [2, 0]]  # 특정 위치의 원소 두 개를 가져와 새로운 배열 # data[0, 2] 와 data[2, 0] 를 가져와 새로운 배열에 넣었습니다
        # # data = data[0, 2] + data[2, 0] # 원소 두개를 가져와, 합을 구한다
        # # data = data[0, 2] * data[2, 0] # 곱을 구한다, 이는 행렬에 대한 곱이 아니다. 좌표에 대한 곱이다
        # # data = data[0, 2] ** data[2, 0] # 거듭제곱을 구한다
        # # data = data[0, 2] / data[2, 0] # 나눈 결과를 구한다 Q + R/B  B = 나누는 수
        # # data = data[0, 2] // data[2, 0] # 몫을 구한다
        # # data = data[0, 2] % data[2, 0] # 나머지를 구한다
        # # data_ = np.dot(data1, data2)# 행렬곱
        # # test_result = f"""
        # # mat 의 data           :
        # # {str(data)}
        # #
        # # mat 의 축의 개수       :
        # # {data.ndim}
        # #
        # # mat 의 배열의 모양     :
        # # {data.shape}
        # # """
        # # dialog = pkg_park4139.CustomDialogReplica(title="2차원데이터배열 출력 테스트결과 ( feat. numpy )", contents=test_result, buttons=["확인"])
        # # dialog.exec_()
        #
        # # numpy 공부 후기
        # # 배열은 행렬과 같은 관계처럼 느껴졌다.
        # # 다차원 행렬 자료구조 : 그냥 엑셀에서 사용하는 자료구조.
        # # ndarray 는 다차원 행렬 자료구조로 되어 있다.
        # # shape 배열의 생김새 정도 겠다, 표현은 shape=(3,3) 이런 형태
        # # 실험을 해보니 첫번째 shape=(줄번호, 기둥번호) 정도로 생각하면 되겠다
        # # 이제는 shape=(100,101) 이런 코드를 보면 데이터배열을 상상할 때 어떤 모양인지 알겠다.
        #
        # # 행렬 공부 후기
        # # 행렬은 좌표 같다.
        # # 행렬의 연산은 각 좌표끼리 더하거나 곱하는 것과 같다.
        #
        # import matplotlib.pyplot as plt
        #
        # # dir /b /s *.ttf | clip 으로 추출
        # # plt.rcParams['font.family'] ='Malgun Gothic' # 한글폰트 적용
        # font_abspath = rf"{pkg_park4139.Park4139.PROJECT_DIRECTORY}\$cache_fonts\GmarketSans\GmarketSansTTFLight.ttf"
        # # font_abspath = rf"{pkg_park4139.Park4139.PROJECT_DIRECTORY}\$cache_fonts\Rubik_Doodle_Shadow\RubikDoodleShadow-Regular.ttf" # 너무 귀여운 입체감 있는 영어폰트
        # plt.rcParams['font.family'] = pkg_park4139.Park4139.get_font_name_for_mataplot(font_abspath)
        # plt.rcParams['figure.facecolor'] = 'black'  # '바탕색'
        # plt.rcParams['axes.edgecolor'] = 'white'  # '테두리 색'
        # plt.rcParams['axes.facecolor'] = 'black'  # '바탕색'
        #
        # # 제목 설정
        # plt.title('그래프 제목', color='white')
        #
        # # 빨간 꺽은선 그래프
        # x = [1, 2, 3, 4, 5]
        # y = [2, 4, 6, 8, 10]
        # plt.plot(x, y, color="red")
        #
        # # 노란 꺽은선 그래프
        # plt.plot([1.5, 2.5, 3.5, 4.5], [3, 5, 8, 10], color="yellow")  # 라인 새로 추가
        #
        # # 범례 설정
        # legend = plt.legend(['학생 A', '학생 B'], facecolor='k', labelcolor='white')
        # ax = plt.gca()
        # leg = ax.get_legend()
        # leg.legendHandles[0].set_color('red')
        # leg.legendHandles[1].set_color('yellow')
        #
        # # 전체화면 설정
        # # mng = plt.get_current_fig_manager()
        # # mng.full_screen_toggle()
        #
        # # 레이블 설정
        # plt.xlabel('x 축 레이블', color='white')
        # plt.ylabel('y 축 레이블', color='white')
        # plt.tick_params(labelcolor='white')
        #
        # plt.show()
        #
        # # Matplotlib 공부 후기
        # # 읽는 법 : 맷플롯립 이라고 읽는다.
        # # 데이터 시각화 패키지 : 쉽게 데이터로 차트를 그려주는 도구
        # # 설치 : pip install matplotlib --upgrade
        # # import 시 네이밍 관례 : as plt 로 import 한다 : import matplotlib.pyplot as plt
        # # 조아써 이제 그래프 그릴 수 있어
        #
        # # pyside6의 app이 없으면 pyside6 app을 실행
        # try:
        #     app.exec()
        # except:
        #     pass

        # __________________________________________________________________________________________________________________________________ TESTED SECTION 1 E
        # __________________________________________________________________________________________________________________________________ TESTED SECTION 2
        # dialog =  pkg_park4139.CustomDialog(contents="테스트를 시작할까요?", buttons=["시작하기", "시작하지 않기"])
        # dialog.exec()
        # dialog.show()

        # global dialog
        # dialog = pkg_park4139.CustomDialog(contents="다운로드하고 싶은 URL을 제출해주세요?", buttons=["제출", "제출하지 않기"], is_input_text_box=True)
        # dialog.show()
        # text_of_clicked_btn = dialog.text_of_clicked_btn
        # Park4139.commentize("text_of_clicked_btn")
        # Park4139.debug_as_cli(text_of_clicked_btn)
        # if text_of_clicked_btn == "제출":
        #     Park4139.download_from_youtube_to_webm(dialog.box_for_editing_input_text.text())

        # # CustomDialog 를 쓰레드 안에서 띄우기
        # import sys
        # import time
        # from PySide6.QtCore import QThread, Signal
        # from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QDialog
        # app = QApplication(sys.argv)
        # class CustomDialogThread(QThread):
        #     show_dialog_signal = Signal()
        #     def run(self):
        #         self.show_dialog_signal.emit()
        # def show_dialog():
        #     from pkg_park4139 import CustomDialog
        #     dialog = CustomDialog(contents="테스트를 시작할까요?", buttons=["시작하기", "시작하지 않기"])
        #     # dialog.exec()
        #     dialog.show()
        # thread = CustomDialogThread()
        # thread.show_dialog_signal.connect(show_dialog)
        # thread.start()
        # sys.exit(app.exec())
        # __________________________________________________________________________________________________________________________________ TESTED SECTION 2


        # __________________________________________________________________________________________________________________________________  UP (TESTED SUCCESS)
        app = QApplication()
        import test_core       # test_core.py 테스트
        app.exec()
        # __________________________________________________________________________________________________________________________________ BELOW (NOT TESTED YET)
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

        # # 여러개 체크박스 체크 예제
        # for i in pyautogui.locateAllOnScreen("checkbox.png"):
        #     pyautogui.click(i, duration=0.25)

        # 화면에서 특정범위를 제한하여 이동할때
        # img_capture = pyautogui.locateOnScreen("Run_icon.png", region=(1800, 0, 1920, 100))
        # img_capture = pyautogui.locateOnScreen("Run_icon.png", confidence=0.7)  # 인식이 잘안될때   유사도 70%  으로 설정
        # pyautogui.moveTo(img_capture)


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



