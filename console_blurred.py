# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'

import os.path

# PEP8 ?
# PEP8 은 파이썬 코드의 작성에 대한 표준권장규칙 정도로 나는 생각한다.
# recommand to apply naming convention to code
#
# naming convention
# 코드작성용 용어사용 규칙 정도로 나는 생각한다.
#
# PEP8 에 의거해서 내 코드 분석하기
# 지켜지지 않은 부분
# - 권장줄길이 79 : 나는 간단한 건 한줄로...웬만한건 한줄로 작성했고 최대 180 자 정도까지는 작성했다...
# - 주석용법 : 코드자체에 대한 설명이 아닌 코드의 의도를 설명해야한다고 하는데 코드자체의 설명을 작성함.. 상당히 지켜가기 어렵다. 네이밍센스가 좋게 작성된 경우라면 지킬 수 있겠지만 다음에 다시봐도 이해가 안갈 네이밍센스로 작성된 코드라면 코드자체 설명을 주석으로 또 달 것 같다. 노력은 해야겠다.
# - 파이썬 메소드 함수 대소문자 :
# - 상수명 : 어떤건 소문자로 되어있는데...모두 대문자여야 함 : FILE_ABSPATH = "blah\blah\foo\foo"
# - import 순서 : 나중에 내 import 부분 코드를 정리해봐야겠다. import 표준라이브러리모듈, import 서드파티모듈, import 로컬모듈 , 요 순서라고 하는데 몰랐다. 아 하나더 있는 규칙이, 알파벳순서 로 나열할 것. vscode 로 line sort 해야 겠다.
# - import 는 필요한 것만 : 세부적으로 그 모듈에 특정 함수, 객체만 필요한 경우 딱 꼬집어 그것만 import 해야한다.
# - ' 또는 " 로 일관된 사용 권장 : 지켜지기 어려울 것 같다. 그 이유는 나는 f-string 문법으로 포멧팅을 즐겨 사용하는데... string escaping을 위해서 ' 과 " 의 혼용은 필 수이다.
# - 한줄에 여러코드를 작성 시 ; 로 구분권장 : 여러코드를 한줄로 구동하도록 시도한 적이 있는데 그 때 ; 로 구분이 되었었다는 것이 떠올랐다. 모르고 쓴 건데 이번에 알았다,
# - ; 를 사용할 것을 권장하지 않음 : 가독성을 위해서 여러줄로 작성하고 ;를 웬만하면 쓰지 말아야겠다, 나도 공감 ; 를 쓰면 코드를 읽기 어려웠다.

# 지켜진 부분
# - 클래스명 : class RpaProgramWindow(QWindow):
# - 함수, 메소드명 : def love_you():
# - import 중 이름충돌 예상 시 as 사용 : 충돌의 소지가 있을 때 as 를 썻다. PEP8을 알고 지킨건 아니고 jetbrain IDE 의 가이드기능을 잘 따르다 보니, 잘 지켜졌다. : import blahblah as blah


# 국내주식과 미국주식을 크롤링해서 보고 싶어졌다.
# 몇 가지 라이브러리가 있음을 확인했고 기획하는 중이다.
# 데이터수집장소 : 다양한 웹사이트에서 크롤링하여 데이터를 수집하기로 생각하였다, 신뢰도가 높아보이는 데이터를 수집해야 한다
# 데이터신뢰도판단 : 네이버 금융정보 데이터신뢰도가 높다고 판단한 이유는 타블로그에서 정보를 얻었으며, 여러 이유 중 가장 큰 이유는 네이버의 공인력을 내가 믿기때문이다.)
# 데이터수집방식 : 특정데이터는 네이버에서 직접 크롤링할 것. 웹 크롤링도 약간 늘었고, 데이터를 엑셀의 형태로 핸들링 하기 위해서 pandas 배워야 겠다. 잠깐만 기다려라 배워서 다시 오겠다.
# import pykrx # 국내증권데이터 공유 라이브러리,               네이버금융사이트(실시간수정되는 주식데이터),               한국증권사이트 의 데이터 기반, 고신뢰성데이터 인 국내주식정보 를 볼 수 있다.  pykrx의 특징은 국내 주식만 수집이 가능한대신 yfinance보다 국내주식 시세가 정확하고 PER, PBR, 배당수익률과 같은 지표는 신뢰성이 떨어진다 - 출처: https://bigdata-doctrine.tistory.com/7 [경제와 데이터:티스토리]
# import yfinance # 증권데이터 공유 라이브러리,              야후 파이낸스에서 크롤링한 데이터를 제공하는 라이브러리, 미국주식데이터 는 상대적으로 정확 , 국내주식데이터 의 잦은누락,   결론은 다른게 나아보인다.
import FinanceDataReader as fdr  # 증권데이터 공유 라이브러리,      pip install finance-datareader,   한국 주식 가격, 미국 주식 가격, 지수, 환율, 암호 화폐 가격, 종목 리스트 등을 제공하는 API 패키지입니다,

# 나의 가치는 "있어 보이는 척 말고 해본 것" 에서 온다고 믿는다.
# 그만큼 해보려면 시간을 쏟아 부어야 한다는 주변의 어느 개발자의 말씀도 있었다
# comprehensive input 에 대해서 집중하여 작성, 내가 이해한 만큼만 작성을 하자

# 그동안 나는 주관이 나쁜 것이란 착각에 빠져 생각을 하는 방법을 몰랐던 것 같다.
# 내 생각을 갖는 시간이 중요하다라는 것을 깨달았다.

# 까먹으면 기록에서 찾는다. 이 때 그 기록은 기록 시스템으로 되어 있어야 한다.
# 인덱싱하여 빠르게 찾아야 그 기록은 가치가 있다
# 기록을 검색할 때에는 텍스트를 작성하게 된다, 그 텍스트는 기록에 반드시 포함되어야 한다, 이 텍스트는 기록내용에 중복 작성이 가능하다.
# 해시태그를 활용한 기록을 하여 내가 내 기록을 찾는 검색에 있어서 노출이 활률을 높이자.

# 그동안 텍스트를 외운 것을 이해한다고 착각한 것 같다.
# 항상 실험하고 실험결과에서 얻은 통찰을 풀어서 생각하자.
# 논리는 풀어서 이해해야 한다.
# 나는 엄청 메모를 많이 하는 편이지만 이 메모에 너무 의존한 것 같다.
# 그 의존 때문에 그 동안 깊게 생각해보는 시간을 많이 갖지 않았던 것 같다.
# 나에겐 메모하는 시간은 줄이고 이해하기 위해 실험과 그에 의거한 통찰로 생각 해보는 시간을 더 갖도록 해야 겠다.


# import plotly # 대표적인 인터랙티브 시각화 도구
# print(plotly.__version__)
# plotly 오프라인 graph 플로팅 어찌 합니까?
# Candlestick chart를 그려낼것.
# 주피터 노트북으로 하는 방법이 나오는데 나는 주피터 노트북 말고 pyside6 를 활용해서 ui에 띄우거나 웹에 띄우고 싶다.
# import plotly.express as px
# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color='petal_length')
# fig.show()
# df = px.data.stocks()
# df


# interface 에 관하여
# high-level interface : 기계보다 사람에 더 가까운 인터페이스, 이 말은 CLI 보다 GUI 로 가는 이유를 설명하는 근거지 않을까 싶은데.
# 많은 설정을 해야하는 겨우라면 나는 CLI 를 더 선호한다.

# api 에 관하여
# program 간 program 이다. 프로그램들 사이에 위치한 프로그램으로서 통신중계 역할을 주로 한다. api 라 부르는 것은 통신 기능이 들어있기 마련이다


import asyncio
import threading
import inspect
import sys
import threading
import webbrowser
from functools import partial
from typing import Callable, TypeVar

import pynput
import schedule
# numpy
from PIL import Image, ImageFilter  # PIL : Py img lib
import random
import time
import clipboard
import keyboard
import pyautogui
import toml
import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
import pyglet
import re
import shutil
import subprocess
import traceback
import urllib.parse as parser
from datetime import datetime
from datetime import timedelta
import win32api
from mutagen.mp3 import MP3
from pytube import Playlist
# from random import randint, random
from screeninfo import get_monitors
from moviepy.editor import *
from gtts import gTTS  # Google TTS 적용
# 웹 크롤링용
import urllib.parse
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
# GUI 프로그램용
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt, QObject, Signal, QPoint, QEvent, QTimer, QEventLoop, Slot, QThread
from PySide6.QtGui import QScreen, QIcon, QShortcut, QKeySequence, QFont, QCursor, QColor, QFontDatabase
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QLineEdit, QMainWindow, QMessageBox, QDialog, QScrollArea, QSpacerItem, QSizePolicy
from BlurWindow.blurWindow import GlobalBlur

import pkg_park4139

Park4139 = pkg_park4139.Park4139()

#  로깅 설정
# logger = logging.getLogger('park4139_test_logger')
# hdlr = logging.FileHandler('park4139_logger.log')
# hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)

#  타입 힌팅 설정
T = TypeVar('T')


#  ///////////////////////////////////////////////  공유 객체 클래스 정의


class SharedObject(QObject):
    dataChanged = Signal(str)  # 데이터 변경을 알리는 시그널

    def __init__(self):
        super().__init__()
        self._data = ""
        self.answer = ""
        self.question = ""
        self.rpa_program_main_window = None

    #  /////////////////////////////////////////////// SharedObject.data
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.dataChanged.emit(self._data)  # 데이터 변경 시 시그널 발생

    #  /////////////////////////////////////////////// 공유객체 SharedObject.answer
    @property
    def data(self):
        return self.answer

    @data.setter
    def data(self, value):
        self.answer = value
        self.dataChanged.emit(self.answer)

    #  SharedObject.question
    @property
    def data(self):
        return self.question

    @data.setter
    def data(self, value):
        self.question = value
        self.dataChanged.emit(self.question)

    #  SharedObject.rpa_program_main_window ....이래도 되나 모르겠네... 성능 이슈 있을 수도...
    @property
    def data(self):
        return self.rpa_program_main_window

    @data.setter
    def data(self, value):
        self.rpa_program_main_window = value
        self.dataChanged.emit(self.rpa_program_main_window)


class RpaProgramMainWindow(QWidget):
    # def __init__(self, shared_obj): # shared_obj 는 창간 통신용 공유객체 이다
    def __init__(self):  # 공유객체를 적용하기 전 코드
        super().__init__()

        #  창간 통신 설정
        # self.shared_obj = shared_obj  # 창간 통신용 객체
        # self.shared_obj.rpa_program_main_window = self  # 메인 창(self)을 다른 창에서도 공유 할 수 있도록 설정 # 안됨.
        # shared_obj.prompt_window = self.prompt_window

        # deprecated test started at 2023 12 23 01 28
        # self.prompt_window = None
        # self.sub_window = None
        # self.question = None

        #  앱 전역 변수 설정
        self.text = "text"
        self.pw = "`"
        self.id = "`"
        # self.is_window_maximized = False
        self.display_width = Park4139.get_display_info()['width'],
        self.display_height = Park4139.get_display_info()['height'],
        # self.display_width_default = int(int(self.display_width[0]) * 0.106)
        self.display_width_default = int(int(self.display_width[0]) * 0.045)
        self.display_height_default = int(int(self.display_height[0]) * 0.2)

        #  메인창 설정
        self.setWindowTitle('.')
        icon_png = rf"{Park4139.PROJECT_DIRECTORY}\$cache_png\icon.PNG"
        self.setWindowIcon(QIcon(icon_png))  # 메인창 아이콘 설정
        # self.setAttribute(Qt.WA_TranslucentBackground) # 메인창 블러 설정
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # 메인창 최상단 프레임레스 설정
        GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 최대화 최소화 버튼 숨기기
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 모든 창 앞에 위치하도록 설정
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        # self.setStyleSheet(pyqt6css.qss)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # blur(self.winId())
        # self.scale = 1/1
        # self.scale = 1/2
        # self.scale = 1/3
        # self.scale = 1 / 4
        self.scale = 1 / 10
        # self.setGeometry(0, 0, int(self.display_width_default * self.scale), int(self.display_height_default * self.scale))
        # self.setGeometry(0, 0,self.display_width_default, self.display_height_default)
        # self.resize(self.display_width_default, self.display_height_default)

        # self.setGeometry(0, 0, int(self.display_width_default * self.scale), int(self.display_height[0]))
        self.windows_size_mode = 0  # 창크기 모드 설정  #0 ~ 3
        # self.rotate_window_size_mode()

        # inputbox 설정
        # self.inputbox = QLineEdit(self)
        # self.inputbox.setStyleSheet("color: rgba(255,255,255, 0.9);")
        # self.inputbox.setText("0,0")
        # self.inputbox.setFixedWidth(120)
        # # self.inputbox.setStyleSheet("text-shadow: 1px 1px 7px rgba(1, 1, 1, 1);") #텍스트에 그림자 넣고 싶었는데 안된다.
        # self.inputbox.textChanged.connect(self.inputbox_changed)
        # self.inputbox.editingFinished.connect(self.inputbox_edit_finished)
        # self.inputbox.returnPressed.connect(self.inputbox_return_pressed)

        # 이벤트 가 많으면 프로그램이 늦어지는 것 같아보였다
        # 프로그램 외 단축키 이벤트 설정
        self.shortcut_keys_up_promised = {
            "<ctrl>+<cmd>": self.toogle_rpa_window
            # "<ctrl>+h": partial(self.toogle_rpa_window, "<ctrl>+h"),
        }
        self.keyboard_main_listener = pynput.keyboard.GlobalHotKeys(self.shortcut_keys_up_promised)
        self.keyboard_main_listener.start()

        # monitor_mouse_position 이벤트 설정
        # self.listener = pynput.mouse.Listener(on_move=self.monitor_mouse_position) # 아주 빠르게 마우스 움직임 감지
        # self.listener.start()

        # detect_mouse_movement 이벤트 설정 (마우스 멈춤 감지 이벤트/ 5초간 마우스 중지 시 메인화면 자동 숨김 이벤트)
        self.mouse_positions = []
        self.previous_position = None
        self.current_position = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.monitor_mouse_position_per_second)
        self.timer.start(1000)

        # 시작스케쥴러 설정
        self.run_scheduler_without_confirm()

        # 프로그램 내 단축키 설정 mkr
        self.available_shortcut_list = {
            #  Ctrl 단축키 설정(서비스 제어 관련)
            # 'Ctrl+F4' 는 설정하지 마는 것이 좋겠다.
            'ASK AI QUESTION': 'Ctrl+A',
            'BACK UP TARGET': 'Ctrl+S',
            'SHOOT SCREENSHOT FULL': 'Ctrl+F',
            'SHOOT SCREENSHOT CUSTOM': 'Ctrl+C',
            'SHOOT SCREENSHOT FOR RPA': 'Ctrl+4',
            'ANI': 'Ctrl+5',
            'rdp-82106': 'Ctrl+R',
            'DOWNLOAD YOUTUBE(webm)': 'Ctrl+Y',
            'DOWNLOAD YOUTUBE(webm)_': 'Ctrl+Alt+Y',
            'TOOGLE': 'Ctrl+win',  # GHOST MODE?
            # 'DOWNLOAD YOUTUBE(wav)': 'Ctrl+S',
            # 'DOWNLOAD YOUTUBE(webm) ONLY SOUND': 'Ctrl+Alt+S',
            'WEATHER': 'Ctrl+W',
            # 'NO PASTE MEMO': 'Ctrl+M',
            'ENG TO KOR': 'Ctrl+K',
            'KOR TO ENG': 'Ctrl+E',
            'RECORD MACRO': 'Ctrl+M',
            'TEST': 'Ctrl+1',
            'UP AND DOWN GAME': 'F1',
            "CLASSIFY SPECIAL FILES": "F2",
            "GATHER EMPTY DIRECTORY": "F3",
            "GATHER SPECIAL FILES": "F4",
            "GATHER USELESS FILES": "F5",
            "MERGE DIRECTORIES": "F6",

            #  Alt 단축키 설정(시스템 제어 관련)
            'DOWNLOAD VIDEO FROM WEB1': 'Alt+F1',
            'DOWNLOAD VIDEO FROM WEB2': 'Alt+F2',
            # 'KEYMAP': 'Alt+F1',
            'ROTATE WINDOW MODE': 'Alt+W',
            'SYSTEM REBOOT': 'Alt+9',
            'SYSTEM SHUTDOWN': 'Alt+]',
            'SYSTEM POWER SAVING MODE': 'Alt+[',
            # 'LOGIN': 'Alt+F7',
            'PROJECT DIRECTORY': 'Alt+P',
            'EMPTY RECYCLE BIN': 'Alt+E',
            # 'RUN CMD.EXE AS ADMIN': 'Alt+C',
            'NAVER MAP': 'Alt+N',
            'EXIT': 'Alt+Q',
        }
        # self.set_shortcut('RUN CMD.EXE AS ADMIN', self.run_cmd_exe)
        # self.set_shortcut('DOWNLOAD YOUTUBE(wav)', self.download_youtube_as_wav)
        # self.set_shortcut('DOWNLOAD YOUTUBE(webm) ONLY SOUND', self.download_youtube_as_webm_only_sound)
        self.set_shortcut('DOWNLOAD YOUTUBE(webm)_', self.should_i_download_youtube_as_webm_alt)
        # self.set_shortcut('TOOGLE', self.hide_windows_of_this_app)
        # self.set_shortcut('LOGIN', self.login)
        # self.set_shortcut('NO PASTE MEMO', self.run_no_paste_memo)
        self.set_shortcut('PROJECT DIRECTORY', self.open_project_directory)
        self.set_shortcut('rdp-82106', self.connect_to_rdp1)
        self.set_shortcut('TEST', self.test)
        # self.set_shortcut('TEST 2', self.test2)
        self.set_shortcut('ASK AI QUESTION', self.ask_something_to_ai)
        self.set_shortcut('BACK UP TARGET', self.back_up_target)
        self.set_shortcut('SHOOT SCREENSHOT FOR RPA', self.shoot_screenshot_for_rpa)
        self.set_shortcut('DOWNLOAD YOUTUBE(webm)', self.should_i_download_youtube_as_webm)
        self.set_shortcut('EMPTY RECYCLE BIN', self.should_i_empty_trash_can)
        self.set_shortcut('ENG TO KOR', self.should_i_translate_eng_to_kor)
        self.set_shortcut('KOR TO ENG', self.should_i_translate_kor_to_eng)
        self.set_shortcut('TOOGLE', self.toogle_rpa_window)
        self.set_shortcut('EXIT', self.should_i_exit_this_program)
        self.set_shortcut('SYSTEM POWER SAVING MODE', self.should_i_enter_to_power_saving_mode)
        self.set_shortcut('SYSTEM REBOOT', self.should_i_reboot_this_computer)
        self.set_shortcut('SYSTEM SHUTDOWN', self.should_i_shutdown_this_computer)
        self.set_shortcut('ROTATE WINDOW MODE', self.rotate_window_size_mode)
        self.set_shortcut('SHOOT SCREENSHOT CUSTOM', self.shoot_screenshot_custom)
        self.set_shortcut('SHOOT SCREENSHOT FULL', self.shoot_screenshot_full)
        self.set_shortcut('NAVER MAP', self.should_i_find_direction_via_naver_map)
        self.set_shortcut('WEATHER', self.show_weather_from_web)
        self.set_shortcut('ANI', self.should_i_show_animation_information_from_web)
        self.set_shortcut('DOWNLOAD VIDEO FROM WEB1', self.download_video_from_web1)
        self.set_shortcut('DOWNLOAD VIDEO FROM WEB2', self.download_video_from_web2)
        self.set_shortcut('RECORD MACRO', self.record_macro)
        self.set_shortcut('UP AND DOWN GAME', Park4139.run_up_and_down_game)
        self.set_shortcut("CLASSIFY SPECIAL FILES", Park4139.should_i_classify_special_files)
        self.set_shortcut("GATHER EMPTY DIRECTORY", Park4139.should_i_gather_empty_directory)
        self.set_shortcut("GATHER SPECIAL FILES", Park4139.should_i_gather_special_files)
        self.set_shortcut("GATHER USELESS FILES", Park4139.should_i_gather_useless_files)
        self.set_shortcut("MERGE DIRECTORIES", Park4139.should_i_merge_directories)

        # 약속된 버튼명인 버튼 설정
        self.btn_to_show_weather_from_web = self.get_btn(self.get_btn_name_promised('WEATHER'), self.show_weather_from_web)
        #  self.btn_to_run_cmd_exe= self.get_btn(self.get_btn_name_promised('RUN CMD.EXE AS ADMIN'), self.run_cmd_exe)
        #  self.btn_to_download_youtube_as_wav= self.get_btn(self.get_btn_name_promised('DOWNLOAD YOUTUBE(wav)'), self.download_youtube_as_wav)
        #  self.btn_to_download_youtube_as_webm_only_sound= self.get_btn(self.get_btn_name_promised('DOWNLOAD YOUTUBE(webm) ONLY SOUND'), self.download_youtube_as_webm_only_sound)
        self.btn_to_should_i_download_youtube_as_webm_alt = self.get_btn(self.get_btn_name_promised('DOWNLOAD YOUTUBE(webm)_'), self.should_i_download_youtube_as_webm_alt)
        #  self.btn_to_hide_windows_of_this_app= self.get_btn(self.get_btn_name_promised('TOOGLE'), self.hide_windows_of_this_app)
        #  self.btn_to_login= self.get_btn(self.get_btn_name_promised('LOGIN'), self.login)
        #  self.btn_to_run_no_paste_memo= self.get_btn(self.get_btn_name_promised('NO PASTE MEMO'), self.run_no_paste_memo)
        self.btn_to_open_project_directory = self.get_btn(self.get_btn_name_promised('PROJECT DIRECTORY'), self.open_project_directory)
        self.btn_to_connect_to_rdp1 = self.get_btn(self.get_btn_name_promised('rdp-82106'), self.connect_to_rdp1)
        self.btn_to_test = self.get_btn(self.get_btn_name_promised('TEST'), self.test)
        #  self.btn_to_test2= self.get_btn(self.get_btn_name_promised('TEST 2'), self.test2)
        self.btn_to_ask_something_to_ai = self.get_btn(self.get_btn_name_promised('ASK AI QUESTION'), self.ask_something_to_ai)
        self.btn_to_back_up_target = self.get_btn(self.get_btn_name_promised('BACK UP TARGET'), self.back_up_target)
        self.btn_to_shoot_screenshot_for_rpa = self.get_btn(self.get_btn_name_promised('SHOOT SCREENSHOT FOR RPA'), self.shoot_screenshot_for_rpa)
        self.btn_to_should_i_download_youtube_as_webm = self.get_btn(self.get_btn_name_promised('DOWNLOAD YOUTUBE(webm)'), self.should_i_download_youtube_as_webm)
        self.btn_to_should_i_empty_trash_can = self.get_btn(self.get_btn_name_promised('EMPTY RECYCLE BIN'), self.should_i_empty_trash_can)
        self.btn_to_should_i_translate_eng_to_kor = self.get_btn(self.get_btn_name_promised('ENG TO KOR'), self.should_i_translate_eng_to_kor)
        self.btn_to_should_i_translate_kor_to_eng = self.get_btn(self.get_btn_name_promised('KOR TO ENG'), self.should_i_translate_kor_to_eng)
        self.btn_to_toogle_rpa_window = self.get_btn(self.get_btn_name_promised('TOOGLE'), self.toogle_rpa_window)
        self.btn_to_should_i_exit_this_program = self.get_btn(self.get_btn_name_promised('EXIT'), self.should_i_exit_this_program)
        self.btn_to_should_i_enter_to_power_saving_mode = self.get_btn(self.get_btn_name_promised('SYSTEM POWER SAVING MODE'), self.should_i_enter_to_power_saving_mode)
        self.btn_to_should_i_reboot_this_computer = self.get_btn(self.get_btn_name_promised('SYSTEM REBOOT'), self.should_i_reboot_this_computer)
        self.btn_to_should_i_shutdown_this_computer = self.get_btn(self.get_btn_name_promised('SYSTEM SHUTDOWN'), self.should_i_shutdown_this_computer)
        self.btn_to_rotate_window_size_mode = self.get_btn(self.get_btn_name_promised('ROTATE WINDOW MODE'), self.rotate_window_size_mode)
        self.btn_to_shoot_screenshot_custom = self.get_btn(self.get_btn_name_promised('SHOOT SCREENSHOT CUSTOM'), self.shoot_screenshot_custom)
        self.btn_to_shoot_screenshot_full = self.get_btn(self.get_btn_name_promised('SHOOT SCREENSHOT FULL'), self.shoot_screenshot_full)
        self.btn_to_should_i_find_direction_via_naver_map = self.get_btn(self.get_btn_name_promised('NAVER MAP'), self.should_i_find_direction_via_naver_map)
        self.btn_to_should_i_show_animation_information_from_web = self.get_btn(self.get_btn_name_promised('ANI'), self.should_i_show_animation_information_from_web)
        self.btn_to_download_video_from_web1 = self.get_btn(self.get_btn_name_promised('DOWNLOAD VIDEO FROM WEB1'), self.download_video_from_web1)
        self.btn_to_download_video_from_web2 = self.get_btn(self.get_btn_name_promised('DOWNLOAD VIDEO FROM WEB2'), self.download_video_from_web2)
        self.btn_to_record_macro = self.get_btn(self.get_btn_name_promised('RECORD MACRO'), self.record_macro)
        self.btn_to_run_up_and_down_game = self.get_btn(self.get_btn_name_promised('UP AND DOWN GAME'), Park4139.run_up_and_down_game)
        self.btn_to_classify_special_files = self.get_btn(self.get_btn_name_promised("CLASSIFY SPECIAL FILES"), Park4139.should_i_classify_special_files)
        self.btn_to_gather_empty_directory = self.get_btn(self.get_btn_name_promised("GATHER EMPTY DIRECTORY"), Park4139.should_i_gather_empty_directory)
        self.btn_to_gather_special_files = self.get_btn(self.get_btn_name_promised("GATHER SPECIAL FILES"), Park4139.should_i_gather_special_files)
        self.btn_to_gather_useless_files = self.get_btn(self.get_btn_name_promised("GATHER USELESS FILES"), Park4139.should_i_gather_useless_files)
        self.btn_to_merge_directories = self.get_btn(self.get_btn_name_promised("MERGE DIRECTORIES"), Park4139.should_i_merge_directories)

        # 약속된 단축키명 버튼 설정
        self.btn_to_show_weather_from_web_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('WEATHER'), function=self.show_weather_from_web)
        #  self.btn_to_run_cmd_exe_only_shortcut_name= self.get_btn(btn_text_align = "right", btn_name  = self.get_shortcut_name_promised()('RUN CMD.EXE AS ADMIN'), function= self.run_cmd_exe)
        #  self.btn_to_download_youtube_as_wav_only_shortcut_name= self.get_btn(btn_text_align = "right", btn_name  = self.get_shortcut_name_promised()('DOWNLOAD YOUTUBE(wav)'), function= self.download_youtube_as_wav)
        #  self.btn_to_download_youtube_as_webm_only_sound_only_shortcut_name= self.get_btn(btn_text_align = "right", btn_name  = self.get_shortcut_name_promised()('DOWNLOAD YOUTUBE(webm) ONLY SOUND'), function= self.download_youtube_as_webm_only_sound)
        self.btn_to_should_i_download_youtube_as_webm_alt_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('DOWNLOAD YOUTUBE(webm)_'), function=self.should_i_download_youtube_as_webm_alt)
        #  self.btn_to_hide_windows_of_this_app_only_shortcut_name= self.get_btn(btn_text_align = "right", btn_name  = self.get_shortcut_name_promised()('TOOGLE'), function= self.hide_windows_of_this_app)
        #  self.btn_to_login_only_shortcut_name= self.get_btn(btn_text_align = "right", btn_name  = self.get_shortcut_name_promised()('LOGIN'), function= self.login)
        #  self.btn_to_run_no_paste_memo_only_shortcut_name= self.get_btn(btn_text_align = "right", btn_name  = self.get_shortcut_name_promised()('NO PASTE MEMO'), function= self.run_no_paste_memo)
        self.btn_to_open_project_directory_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('PROJECT DIRECTORY'), function=self.open_project_directory)
        self.btn_to_connect_to_rdp1_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('rdp-82106'), function=self.connect_to_rdp1)
        self.btn_to_test_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('TEST'), function=self.test)
        #  self.btn_to_test2_only_shortcut_name= self.get_btn(btn_text_align = "right", btn_name  = self.get_shortcut_name_promised()('TEST 2'), function= self.test2)
        self.btn_to_ask_something_to_ai_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('ASK AI QUESTION'), function=self.ask_something_to_ai)
        self.btn_to_back_up_target_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('BACK UP TARGET'), function=self.back_up_target)
        self.btn_to_shoot_screenshot_for_rpa_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('SHOOT SCREENSHOT FOR RPA'), function=self.shoot_screenshot_for_rpa)
        self.btn_to_should_i_download_youtube_as_webm_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('DOWNLOAD YOUTUBE(webm)'), function=self.should_i_download_youtube_as_webm)
        self.btn_to_should_i_empty_trash_can_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('EMPTY RECYCLE BIN'), function=self.should_i_empty_trash_can)
        self.btn_to_should_i_translate_eng_to_kor_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('ENG TO KOR'), function=self.should_i_translate_eng_to_kor)
        self.btn_to_should_i_translate_kor_to_eng_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('KOR TO ENG'), function=self.should_i_translate_kor_to_eng)
        self.btn_to_toogle_rpa_window_only_shorcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('TOOGLE'), function=self.toogle_rpa_window)
        self.btn_to_should_i_exit_this_program_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('EXIT'), function=self.should_i_exit_this_program)
        self.btn_to_should_i_enter_to_power_saving_mode_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('SYSTEM POWER SAVING MODE'), function=self.should_i_enter_to_power_saving_mode)
        self.btn_to_should_i_reboot_this_computer_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('SYSTEM REBOOT'), function=self.should_i_reboot_this_computer)
        self.btn_to_should_i_shutdown_this_computer_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('SYSTEM SHUTDOWN'), function=self.should_i_shutdown_this_computer)
        self.btn_to_rotate_window_size_mode_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('ROTATE WINDOW MODE'), function=self.rotate_window_size_mode)
        self.btn_to_shoot_screenshot_custom_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('SHOOT SCREENSHOT CUSTOM'), function=self.shoot_screenshot_custom)
        self.btn_to_shoot_screenshot_full_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('SHOOT SCREENSHOT FULL'), function=self.shoot_screenshot_full)
        self.btn_to_should_i_find_direction_via_naver_map_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('NAVER MAP'), function=self.should_i_find_direction_via_naver_map)
        self.btn_to_should_i_show_animation_information_from_web_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('ANI'), function=self.should_i_show_animation_information_from_web)
        self.btn_to_download_video_from_web1_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('DOWNLOAD VIDEO FROM WEB1'), function=self.download_video_from_web1)
        self.btn_to_download_video_from_web2_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('DOWNLOAD VIDEO FROM WEB2'), function=self.download_video_from_web2)
        self.btn_to_record_macro_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('RECORD MACRO'), function=self.record_macro)
        self.btn_to_run_up_and_down_game_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('UP AND DOWN GAME'), function=Park4139.run_up_and_down_game)
        self.btn_to_classify_special_files_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised("CLASSIFY SPECIAL FILES"), function=Park4139.should_i_classify_special_files)
        self.btn_to_gather_empty_directory_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised("GATHER EMPTY DIRECTORY"), function=Park4139.should_i_gather_empty_directory)
        self.btn_to_gather_special_files_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised("GATHER SPECIAL FILES"), function=Park4139.should_i_gather_special_files)
        self.btn_to_gather_useless_files_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised("GATHER USELESS FILES"), function=Park4139.should_i_gather_useless_files)
        self.btn_to_merge_directories_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised("MERGE DIRECTORIES"), function=Park4139.should_i_merge_directories)

        btns = [
            [self.btn_to_toogle_rpa_window, self.btn_to_toogle_rpa_window_only_shorcut_name],
            [self.btn_to_show_weather_from_web, self.btn_to_show_weather_from_web_only_shortcut_name],
            [self.btn_to_should_i_download_youtube_as_webm_alt, self.btn_to_should_i_download_youtube_as_webm_alt_only_shortcut_name],
            [self.btn_to_should_i_download_youtube_as_webm, self.btn_to_should_i_download_youtube_as_webm_only_shortcut_name],
            [self.btn_to_download_video_from_web1, self.btn_to_download_video_from_web1_only_shortcut_name],
            [self.btn_to_download_video_from_web2, self.btn_to_download_video_from_web2_only_shortcut_name],
            [self.btn_to_should_i_translate_kor_to_eng, self.btn_to_should_i_translate_kor_to_eng_only_shortcut_name],
            [self.btn_to_should_i_translate_eng_to_kor, self.btn_to_should_i_translate_eng_to_kor_only_shortcut_name],
            [self.btn_to_ask_something_to_ai, self.btn_to_ask_something_to_ai_only_shortcut_name],
            [self.btn_to_open_project_directory, self.btn_to_open_project_directory_only_shortcut_name],
            [self.btn_to_connect_to_rdp1, self.btn_to_connect_to_rdp1_only_shortcut_name],
            [self.btn_to_back_up_target, self.btn_to_back_up_target_only_shortcut_name],
            [self.btn_to_rotate_window_size_mode, self.btn_to_rotate_window_size_mode_only_shortcut_name],
            # [  self.btn_to_run_cmd_exe,      self.btn_to_run_cmd_exe_only_shortcut_name],
            # [  self.btn_to_download_youtube_as_wav,      self.btn_to_download_youtube_as_wav_only_shortcut_name],
            # [  self.btn_to_download_youtube_as_webm_only_sound,      self.btn_to_download_youtube_as_webm_only_sound_only_shortcut_name],
            # [  self.btn_to_hide_windows_of_this_app,      self.btn_to_hide_windows_of_this_app_only_shortcut_name],
            # [  self.btn_to_login,      self.btn_to_login_only_shortcut_name],
            # [  self.btn_to_run_no_paste_memo,      self.btn_to_run_no_paste_memo_only_shortcut_name],
            [self.btn_to_test, self.btn_to_test_only_shortcut_name],
            [self.btn_to_should_i_empty_trash_can, self.btn_to_should_i_empty_trash_can_only_shortcut_name],
            [self.btn_to_should_i_exit_this_program, self.btn_to_should_i_exit_this_program_only_shortcut_name],
            [self.btn_to_should_i_enter_to_power_saving_mode, self.btn_to_should_i_enter_to_power_saving_mode_only_shortcut_name],
            [self.btn_to_should_i_reboot_this_computer, self.btn_to_should_i_reboot_this_computer_only_shortcut_name],
            [self.btn_to_should_i_shutdown_this_computer, self.btn_to_should_i_shutdown_this_computer_only_shortcut_name],
            [self.btn_to_shoot_screenshot_for_rpa, self.btn_to_shoot_screenshot_for_rpa_only_shortcut_name],
            [self.btn_to_shoot_screenshot_custom, self.btn_to_shoot_screenshot_custom_only_shortcut_name],
            [self.btn_to_shoot_screenshot_full, self.btn_to_shoot_screenshot_full_only_shortcut_name],
            [self.btn_to_should_i_find_direction_via_naver_map, self.btn_to_should_i_find_direction_via_naver_map_only_shortcut_name],
            [self.btn_to_should_i_show_animation_information_from_web, self.btn_to_should_i_show_animation_information_from_web_only_shortcut_name],
            [self.btn_to_record_macro, self.btn_to_record_macro_only_shortcut_name],
            [self.btn_to_run_up_and_down_game, self.btn_to_run_up_and_down_game_only_shortcut_name],
            [self.btn_to_classify_special_files, self.btn_to_classify_special_files_only_shortcut_name],
            [self.btn_to_gather_empty_directory, self.btn_to_gather_empty_directory_only_shortcut_name],
            [self.btn_to_gather_special_files, self.btn_to_gather_special_files_only_shortcut_name],
            [self.btn_to_gather_useless_files, self.btn_to_gather_useless_files_only_shortcut_name],
            [self.btn_to_merge_directories, self.btn_to_merge_directories_only_shortcut_name],
        ]

        # GRID SETTING
        grid = QtWidgets.QGridLayout(self)

        # GRID COORDINATION REFERENCE (ROW, COLUMN)
        #        0,0  0,1  0,2
        #        1,0  1,1  1,2
        #        2,0  2,1  2,2

        # spaver

        # GRID_COLUMN 1 폭 조절용 policy
        # size_policy = QSizePolicy()
        # grid.setHorizontalPolicy(QSizePolicy.Minimum)  # 그리드의 열의 폭을 최소로 설정합니다.
        grid.setVerticalSpacing(9)
        grid.setHorizontalSpacing(5)
        grid.setColumnMinimumWidth(1, 125)
        grid.setColumnMinimumWidth(2, 45)

        btns_grid = btns
        line_no = 0
        for btn in btns_grid:
            grid.addWidget(btn[0], line_no, 0)  # GRID_COLUMN 0 설정
            grid.addWidget(btn[1], line_no, 2)  # GRID_COLUMN 1 설정
            line_no = line_no + 1

        # TEST
        # self.inputbox = QPlainTextEdit(self)
        # self.inputbox = QTextEdit(self)
        # self.ta1 = QTableWidget(self)
        # self.ta1.resize(500, 500)
        # self.ta1.setColumnCount(3)
        # self.ta1.setStyleSheet("color: rgba(255,255,255, 0.9);")
        # self.ta1.setStyleSheet("background-color: rgba(255,255,255, 0.9);")
        # table_column = ["첫번째 열", "두번째 열", "Third 열"]
        # self.ta1.setHorizontalHeaderLabels(table_column)

        # # 행 2개 추가
        # self.ta1.setRowCount(2)

        # # 추가된 행에 데이터 채워넣음
        # self.ta1.setItem(0, 0, QTableWidgetItem("(0,0)"))
        # self.ta1.setItem(0, 1, QTableWidgetItem("(0,1)"))
        # self.ta1.setItem(1, 0, QTableWidgetItem("(1,0)"))
        # self.ta1.setItem(1, 1, QTableWidgetItem("(1,1)"))

        # 마지막에 행 1개추가
        # self.ta1.insertRow(2)
        # self.ta1.setItem(2, 0, QTableWidgetItem("New Data"))

        # 셀의 텍스트 변경
        # self.ta1.item(1, 1).setText("데이터 변경")

        # 셀에 있는 텍스트 출력
        # print(self.ta1.item(0, 1).text())

        # 테이블 데이터 전부 삭제
        # self.ta1.clear()

        # 테이블 행전부 삭제
        # self.ta1.setRowCount(0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.scroll_area.setStyleSheet(f" border: none; width: {self.display_width_default}px; height: {self.display_height_default}px")
        self.scroll_area.setLayout(grid)

        # 레이아웃 설정
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)

        self.toogle_rpa_window()
        self.show()
        # Park4139.press("alt", "w")

        self.event_loop = QEventLoop()
        self.event_loop.exec()

    def monitor_mouse_position_per_second(self):
        """마우스 움직임 감지 함수"""
        x, y = pyautogui.position()  # 현재 마우스 위치 ( 이게 내가 원하던 수치 )
        # print(x, y)
        self.current_position = QCursor.pos()  # 현재 마우스 커서 위치 ( 이건 내가 원하는 수치는 아닌데... 뭘 의미하는 거지? )
        # print(self.current_position)
        if self.previous_position is not None and self.previous_position == self.current_position:
            # print("마우스가 멈췄습니다")
            # print(f"self.mouse_positions : {self.mouse_positions}") # 마우스 위치 리스트
            if 10 <= len(self.mouse_positions):
                # 10번 연속 mouse 중지 감지
                # self.mouse_positions 에 등록된 모든 self.current_position 가 동일하면 10번 연속으로 움직이지 않은 것으로 판단
                if len(self.mouse_positions) == 10:
                    # 동일한 10개 원소를 갖는 리스트 내에서 요소의 중복을 제거하면 중복이 제거된 리스트의 요소의 수는 1개가 나올 것을 기대
                    mouse_positions_removed_duplicatd_elements = list(set(self.mouse_positions))  # orderless way
                    if len(mouse_positions_removed_duplicatd_elements) == 1:
                        # print("10번 연속 중지 감지")
                        self.hide()
                        pass

            if 5 <= len(self.mouse_positions):
                self.mouse_positions = []  # 감지값들이 5개 이상이면 감지값목록 초기화

            elif len(self.mouse_positions) < 5:
                self.mouse_positions.append(self.current_position)
            pass
        else:
            # print("마우스가 움직였습니다")

            # 우측하단 꼭지점 네비게이션
            if x == 3440 and y == 1440:
                Park4139.press("win", "d")
            # 우측 네비게이션
            if 3440 - 50 <= x <= 3440 and 300 <= y <= 1440:
                try:
                    Park4139.explorer(Park4139.PYCHARM64_EXE)
                except:
                    Park4139.trouble_shoot("%%%FOO%%%")
                    pass

            # 좌측 네비게이션
            elif 0 <= x <= 15 and 0 <= y <= 1440:
                self.toogle_rpa_window()
                pass


            else:
                pass
        self.previous_position = self.current_position

    def monitor_mouse_position(self, x, y):
        # 상단 네비게이션
        if 0 <= x <= 3440 and 0 <= y <= 25:
            pass
        else:
            pass

    @staticmethod
    # def rpa_program_method_decorator(function):
    def rpa_program_method_decorator(function: Callable[[T], None]):
        def wrapper(self):
            self.hide()  # 비동기 전까지는 사용자가 다른 명령을 하지 못하도록 이 코드를 사용
            function(self)
            self.bring_this_window()

        return wrapper

    def eventFilter(self, obj, event):
        # if event.type() == QEvent.MouseMove:
        #     x = event.globalX()
        #     y = event.globalY()
        #     print(f"마우스 이동 - X: {x}, Y: {y}")
        # return super().eventFilter(obj, event)
        if event.type() == QEvent.MouseButtonPress and not self.rect().contains(event.pos()):
            print("pyside6 창 외부 클릭 되었습니다")
        return super().eventFilter(obj, event)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:  # 왼쪽 버튼 클릭 시 동작
            print("왼쪽 버튼 클릭")
        #     print(f"마우스 좌표: ({x}, {y})")
        #     print(f"마우스 좌표:\n : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.BackButton:
            print(f"mouse event monitor:\nBackButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton1:
            print(f"mouse event monitor:\nExtraButton1 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton10:
            print(f"mouse event monitor:\nExtraButton10 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton11:
            print(f"mouse event monitor:\nExtraButton11 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton12:
            print(f"mouse event monitor:\nExtraButton12 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton13:
            print(f"mouse event monitor:\nExtraButton13 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton14:
            print(f"mouse event monitor:\nExtraButton14 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton15:
            print(f"mouse event monitor:\nExtraButton15 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton16:
            print(f"mouse event monitor:\nExtraButton16 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton17:
            print(f"mouse event monitor:\nExtraButton17 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton18:
            print(f"mouse event monitor:\nExtraButton18 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton19:
            print(f"mouse event monitor:\nExtraButton19 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton2:
            print(f"mouse event monitor:\nExtraButton2 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton20:
            print(f"mouse event monitor:\nExtraButton20 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton21:
            print(f"mouse event monitor:\nExtraButton21 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton22:
            print(f"mouse event monitor:\nExtraButton22 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton23:
            print(f"mouse event monitor:\nExtraButton23 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton24:
            print(f"mouse event monitor:\nExtraButton24 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton3:
            print(f"mouse event monitor:\nExtraButton3 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton4:
            print(f"mouse event monitor:\nExtraButton4 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton5:
            print(f"mouse event monitor:\nExtraButton5 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton6:
            print(f"mouse event monitor:\nExtraButton6 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton7:
            print(f"mouse event monitor:\nExtraButton7 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton8:
            print(f"mouse event monitor:\nExtraButton8 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ExtraButton9:
            print(f"mouse event monitor:\nExtraButton9 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.ForwardButton:
            print(f"mouse event monitor:\nForwardButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.LeftButton:
            print(f"mouse event monitor:\nLeftButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.MiddleButton:
            print(f"mouse event monitor:\nMiddleButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.NoButton:
            print(f"mouse event monitor:\nNoButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.RightButton:
            print(f"mouse event monitor:\nRightButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.TaskButton:
            print(f"mouse event monitor:\nTaskButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.XButton1:
            print(f"mouse event monitor:\nXButton1 : {str(e.pos().x())} ,{str(e.pos().y())} ")
        elif e.button() == Qt.XButton2:
            print(f"mouse event monitor:\nXButton2 : {str(e.pos().x())} ,{str(e.pos().y())} ")

    # def mouseReleaseEvent(self, e):
    #     self.label10.setText(f"event monitor:\nmouseReleaseEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #
    # def mouseDoubleClickEvent(self, e):
    #     self.label10.setText(f"event monitor:\nmouseDoubleClickEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")

    def keyPressEvent(self, e):
        self.mouse_positions = []  # 키보드가 눌리면 사용자가 사용중인 것으로 간주하고 마우스 위치 값 목록 초기화

    # def keyPressEvent(self, e):
    #     # these keys refered from https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html
    #     # 테스트 결과 한/영, 한자 인식안됨.
    #     if e.key() == Qt.Key_Return:
    #         self.label11.setText(f"keyboard event monitor:\nKey_Return : Key_Return ")
    #         self.showMinimized()
    #         park4139.press("space")
    #         self.showMaximized()
    #     elif e.key() == Qt.Key_0:
    #         self.label11.setText(f"keyboard event monitor:\nKey_0 : Key_0 ")
    #     elif e.key() == Qt.Key_1:
    #         self.label11.setText(f"keyboard event monitor:\nKey_1 : Key_1 ")
    #     elif e.key() == Qt.Key_2:
    #         self.label11.setText(f"keyboard event monitor:\nKey_2 : Key_2 ")
    #     elif e.key() == Qt.Key_3:
    #         self.label11.setText(f"keyboard event monitor:\nKey_3 : Key_3 ")
    #     elif e.key() == Qt.Key_4:
    #         self.label11.setText(f"keyboard event monitor:\nKey_4 : Key_4 ")
    #     elif e.key() == Qt.Key_5:
    #         self.label11.setText(f"keyboard event monitor:\nKey_5 : Key_5 ")
    #     elif e.key() == Qt.Key_6:
    #         self.label11.setText(f"keyboard event monitor:\nKey_6 : Key_6 ")
    #     elif e.key() == Qt.Key_7:
    #         self.label11.setText(f"keyboard event monitor:\nKey_7 : Key_7 ")
    #     elif e.key() == Qt.Key_8:
    #         self.label11.setText(f"keyboard event monitor:\nKey_8 : Key_8 ")
    #     elif e.key() == Qt.Key_9:
    #         self.label11.setText(f"keyboard event monitor:\nKey_9 : Key_9 ")
    #     elif e.key() == Qt.Key_A:
    #         self.label11.setText(f"keyboard event monitor:\nKey_A : Key_A ")
    #         # elif e.key() == Qt.Key_Aacute:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Aacute : Key_Aacute ")
    #         # elif e.key() == Qt.Key_Acircumflex:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Acircumflex : Key_Acircumflex ")
    #         # elif e.key() == Qt.Key_acute:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_acute : Key_acute ")
    #         # elif e.key() == Qt.Key_AddFavorite:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AddFavorite : Key_AddFavorite ")
    #         # elif e.key() == Qt.Key_Adiaeresis:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Adiaeresis : Key_Adiaeresis ")
    #         # elif e.key() == Qt.Key_AE:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AE : Key_AE ")
    #         # elif e.key() == Qt.Key_Agrave:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Agrave : Key_Agrave ")
    #         # elif e.key() == Qt.Key_Alt:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Alt : Key_Alt ")
    #         # elif e.key() == Qt.Key_AltGr:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AltGr : Key_AltGr ")
    #         # elif e.key() == Qt.Key_Ampersand:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Ampersand : Key_Ampersand ")
    #         # elif e.key() == Qt.Key_Any:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Any : Key_Any ")
    #         # elif e.key() == Qt.Key_Apostrophe:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Apostrophe : Key_Apostrophe ")
    #         # elif e.key() == Qt.Key_ApplicationLeft:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_ApplicationLeft : Key_ApplicationLeft ")
    #         # elif e.key() == Qt.Key_ApplicationRight:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_ApplicationRight : Key_ApplicationRight ")
    #         # elif e.key() == Qt.Key_Aring:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Aring : Key_Aring ")
    #         # elif e.key() == Qt.Key_AsciiCircum:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AsciiCircum : Key_AsciiCircum ")
    #         # elif e.key() == Qt.Key_AsciiTilde:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AsciiTilde : Key_AsciiTilde ")
    #         # elif e.key() == Qt.Key_Asterisk:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Asterisk : Key_Asterisk ")
    #         # elif e.key() == Qt.Key_At:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_At : Key_At ")
    #         # elif e.key() == Qt.Key_Atilde:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Atilde : Key_Atilde ")
    #         # elif e.key() == Qt.Key_AudioCycleTrack:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AudioCycleTrack : Key_AudioCycleTrack ")
    #         # elif e.key() == Qt.Key_AudioForward:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AudioForward : Key_AudioForward ")
    #         # elif e.key() == Qt.Key_AudioRandomPlay:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AudioRandomPlay : Key_AudioRandomPlay ")
    #         # elif e.key() == Qt.Key_AudioRepeat:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AudioRepeat : Key_AudioRepeat ")
    #         # elif e.key() == Qt.Key_AudioRewind:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_AudioRewind : Key_AudioRewind ")
    #         # elif e.key() == Qt.Key_Away:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Away : Key_Away ")
    #         # elif e.key() == Qt.Key_B:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_B : Key_B ")
    #         # elif e.key() == Qt.Key_Back:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Back : Key_Back ")
    #         # elif e.key() == Qt.Key_BackForward:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BackForward : Key_BackForward ")
    #         # elif e.key() == Qt.Key_Backslash:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Backslash : Key_Backslash ")
    #         # elif e.key() == Qt.Key_Backspace:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Backspace : Key_Backspace ")
    #         # elif e.key() == Qt.Key_Backtab:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Backtab : Key_Backtab ")
    #         # elif e.key() == Qt.Key_Bar:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Bar : Key_Bar ")
    #         # elif e.key() == Qt.Key_BassBoost:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BassBoost : Key_BassBoost ")
    #         # elif e.key() == Qt.Key_BassDown:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BassDown : Key_BassDown ")
    #         # elif e.key() == Qt.Key_BassUp:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BassUp : Key_BassUp ")
    #         # elif e.key() == Qt.Key_Battery:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Battery : Key_Battery ")
    #         # elif e.key() == Qt.Key_Blue:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Blue : Key_Blue ")
    #         # elif e.key() == Qt.Key_Bluetooth:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Bluetooth : Key_Bluetooth ")
    #         # elif e.key() == Qt.Key_Book:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Book : Key_Book ")
    #         # elif e.key() == Qt.Key_BraceLeft:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BraceLeft : Key_BraceLeft ")
    #         # elif e.key() == Qt.Key_BraceRight:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BraceRight : Key_BraceRight ")
    #         # elif e.key() == Qt.Key_BracketLeft:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BracketLeft : Key_BracketLeft ")
    #         # elif e.key() == Qt.Key_BracketRight:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BracketRight : Key_BracketRight ")
    #         # elif e.key() == Qt.Key_BrightnessAdjust:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_BrightnessAdjust : Key_BrightnessAdjust ")
    #         # elif e.key() == Qt.Key_brokenbar:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_brokenbar : Key_brokenbar ")
    #         # elif e.key() == Qt.Key_C:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_C : Key_C ")
    #         # elif e.key() == Qt.Key_Calculator:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Calculator : Key_Calculator ")
    #         # elif e.key() == Qt.Key_Calendar:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Calendar : Key_Calendar ")
    #         # elif e.key() == Qt.Key_Call:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Call : Key_Call ")
    #         # elif e.key() == Qt.Key_Camera:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Camera : Key_Camera ")
    #         # elif e.key() == Qt.Key_CameraFocus:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_CameraFocus : Key_CameraFocus ")
    #         # elif e.key() == Qt.Key_Cancel:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Cancel : Key_Cancel ")
    #         # elif e.key() == Qt.Key_CapsLock:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_CapsLock : Key_CapsLock ")
    #         # elif e.key() == Qt.Key_Ccedilla:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Ccedilla : Key_Ccedilla ")
    #         # elif e.key() == Qt.Key_CD:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_CD : Key_CD ")
    #         # elif e.key() == Qt.Key_cedilla:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_cedilla : Key_cedilla ")
    #         # elif e.key() == Qt.Key_cent:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_cent : Key_cent ")
    #         # elif e.key() == Qt.Key_ChannelDown:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_ChannelDown : Key_ChannelDown ")
    #         # elif e.key() == Qt.Key_ChannelUp:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_ChannelUp : Key_ChannelUp ")
    #         # elif e.key() == Qt.Key_Clear:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Clear : Key_Clear ")
    #         # elif e.key() == Qt.Key_ClearGrab:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_ClearGrab : Key_ClearGrab ")
    #         # elif e.key() == Qt.Key_Close:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Close : Key_Close ")
    #         # elif e.key() == Qt.Key_Codeinput:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Codeinput : Key_Codeinput ")
    #         # elif e.key() == Qt.Key_Colon:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Colon : Key_Colon ")
    #         # elif e.key() == Qt.Key_Comma:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Comma : Key_Comma ")
    #         # elif e.key() == Qt.Key_Community:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Community : Key_Community ")
    #         # elif e.key() == Qt.Key_Context1:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Context1 : Key_Context1 ")
    #         # elif e.key() == Qt.Key_Context2:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Context2 : Key_Context2 ")
    #         # elif e.key() == Qt.Key_Context3:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Context3 : Key_Context3 ")
    #         # elif e.key() == Qt.Key_Context4:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Context4 : Key_Context4 ")
    #         # elif e.key() == Qt.Key_ContrastAdjust:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_ContrastAdjust : Key_ContrastAdjust ")
    #         # elif e.key() == Qt.Key_Control:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Control : Key_Control ")
    #         # elif e.key() == Qt.Key_Copy:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Copy : Key_Copy ")
    #         # elif e.key() == Qt.Key_copyright:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_copyright : Key_copyright ")
    #         # elif e.key() == Qt.Key_currency:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_currency : Key_currency ")
    #         # elif e.key() == Qt.Key_Cut:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Cut : Key_Cut ")
    #         # elif e.key() == Qt.Key_D:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_D : Key_D ")
    #         # elif e.key() == Qt.Key_Dead_a:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_a : Key_Dead_a ")
    #         # elif e.key() == Qt.Key_Dead_A:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_A : Key_Dead_A ")
    #         # elif e.key() == Qt.Key_Dead_Abovecomma:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Abovecomma : Key_Dead_Abovecomma ")
    #         # elif e.key() == Qt.Key_Dead_Abovedot:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Abovedot : Key_Dead_Abovedot ")
    #         # elif e.key() == Qt.Key_Dead_Abovereversedcomma:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Abovereversedcomma : Key_Dead_Abovereversedcomma ")
    #         # elif e.key() == Qt.Key_Dead_Abovering:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Abovering : Key_Dead_Abovering ")
    #         # elif e.key() == Qt.Key_Dead_Aboveverticalline:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Aboveverticalline : Key_Dead_Aboveverticalline ")
    #         # elif e.key() == Qt.Key_Dead_Acute:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Acute : Key_Dead_Acute ")
    #         # elif e.key() == Qt.Key_Dead_Belowbreve:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowbreve : Key_Dead_Belowbreve ")
    #         # elif e.key() == Qt.Key_Dead_Belowcircumflex:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowcircumflex : Key_Dead_Belowcircumflex ")
    #         # elif e.key() == Qt.Key_Dead_Belowcomma:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowcomma : Key_Dead_Belowcomma ")
    #         # elif e.key() == Qt.Key_Dead_Belowdiaeresis:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowdiaeresis : Key_Dead_Belowdiaeresis ")
    #         # elif e.key() == Qt.Key_Dead_Belowdot:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowdot : Key_Dead_Belowdot ")
    #         # elif e.key() == Qt.Key_Dead_Belowmacron:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowmacron : Key_Dead_Belowmacron ")
    #         # elif e.key() == Qt.Key_Dead_Belowring:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowring : Key_Dead_Belowring ")
    #         # elif e.key() == Qt.Key_Dead_Belowtilde:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowtilde : Key_Dead_Belowtilde ")
    #         # elif e.key() == Qt.Key_Dead_Belowverticalline:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Belowverticalline : Key_Dead_Belowverticalline ")
    #         # elif e.key() == Qt.Key_Dead_Breve:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Breve : Key_Dead_Breve ")
    #         # elif e.key() == Qt.Key_Dead_Capital_Schwa:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Capital_Schwa : Key_Dead_Capital_Schwa ")
    #         # elif e.key() == Qt.Key_Dead_Caron:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Caron : Key_Dead_Caron ")
    #         # elif e.key() == Qt.Key_Dead_Cedilla:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Cedilla : Key_Dead_Cedilla ")
    #         # elif e.key() == Qt.Key_Dead_Circumflex:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Circumflex : Key_Dead_Circumflex ")
    #         # elif e.key() == Qt.Key_Dead_Currency:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Currency : Key_Dead_Currency ")
    #         # elif e.key() == Qt.Key_Dead_Diaeresis:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Diaeresis : Key_Dead_Diaeresis ")
    #         # elif e.key() == Qt.Key_Dead_Doubleacute:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Doubleacute : Key_Dead_Doubleacute ")
    #         # elif e.key() == Qt.Key_Dead_Doublegrave:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Doublegrave : Key_Dead_Doublegrave ")
    #         # elif e.key() == Qt.Key_Dead_e:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_e : Key_Dead_e ")
    #         # elif e.key() == Qt.Key_Dead_E:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_E : Key_Dead_E ")
    #         # elif e.key() == Qt.Key_Dead_Grave:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Grave : Key_Dead_Grave ")
    #         # elif e.key() == Qt.Key_Dead_Greek:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Greek : Key_Dead_Greek ")
    #         # elif e.key() == Qt.Key_Dead_Hook:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Hook : Key_Dead_Hook ")
    #         # elif e.key() == Qt.Key_Dead_Horn:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Horn : Key_Dead_Horn ")
    #         # elif e.key() == Qt.Key_Dead_i:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_i : Key_Dead_i ")
    #         # elif e.key() == Qt.Key_Dead_I:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_I : Key_Dead_I ")
    #         # elif e.key() == Qt.Key_Dead_Invertedbreve:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Invertedbreve : Key_Dead_Invertedbreve ")
    #         # elif e.key() == Qt.Key_Dead_Iota:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Iota : Key_Dead_Iota ")
    #         # elif e.key() == Qt.Key_Dead_Longsolidusoverlay:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Longsolidusoverlay : Key_Dead_Longsolidusoverlay ")
    #         # elif e.key() == Qt.Key_Dead_Lowline:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Lowline : Key_Dead_Lowline ")
    #         # elif e.key() == Qt.Key_Dead_Macron:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Macron : Key_Dead_Macron ")
    #         # elif e.key() == Qt.Key_Dead_o:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_o : Key_Dead_o ")
    #         # elif e.key() == Qt.Key_Dead_O:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_O : Key_Dead_O ")
    #         # elif e.key() == Qt.Key_Dead_Ogonek:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Ogonek : Key_Dead_Ogonek ")
    #         # elif e.key() == Qt.Key_Dead_Semivoiced_Sound:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Semivoiced_Sound : Key_Dead_Semivoiced_Sound ")
    #         # elif e.key() == Qt.Key_Dead_Small_Schwa:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Small_Schwa : Key_Dead_Small_Schwa ")
    #         # elif e.key() == Qt.Key_Dead_Stroke:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Stroke : Key_Dead_Stroke ")
    #         # elif e.key() == Qt.Key_Dead_Tilde:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Tilde : Key_Dead_Tilde ")
    #         # elif e.key() == Qt.Key_Dead_u:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_u : Key_Dead_u ")
    #         # elif e.key() == Qt.Key_Dead_U:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_U : Key_Dead_U ")
    #         # elif e.key() == Qt.Key_Dead_Voiced_Sound:
    #         #     self.label11.setText(f"keyboard event monitor:\nKey_Dead_Voiced_Sound : Key_Dead_Voiced_Sound ")
    #         # elif e.key() == Qt.Key_degree:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_degree : Key_degree ")
    #     # elif e.key() == Qt.Key_Delete:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Delete : Key_Delete ")
    #     # elif e.key() == Qt.Key_diaeresis:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_diaeresis : Key_diaeresis ")
    #     # elif e.key() == Qt.Key_Direction_L:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Direction_L : Key_Direction_L ")
    #     # elif e.key() == Qt.Key_Direction_R:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Direction_R : Key_Direction_R ")
    #     # elif e.key() == Qt.Key_Display:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Display : Key_Display ")
    #     # elif e.key() == Qt.Key_division:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_division : Key_division ")
    #     # elif e.key() == Qt.Key_Documents:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Documents : Key_Documents ")
    #     # elif e.key() == Qt.Key_Dollar:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Dollar : Key_Dollar ")
    #     # elif e.key() == Qt.Key_DOS:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_DOS : Key_DOS ")
    #     # elif e.key() == Qt.Key_Down:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Down : Key_Down ")
    #     # elif e.key() == Qt.Key_E:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_E : Key_E ")
    #     # elif e.key() == Qt.Key_Eacute:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Eacute : Key_Eacute ")
    #     # elif e.key() == Qt.Key_Ecircumflex:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Ecircumflex : Key_Ecircumflex ")
    #     # elif e.key() == Qt.Key_Ediaeresis:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Ediaeresis : Key_Ediaeresis ")
    #     # elif e.key() == Qt.Key_Egrave:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Egrave : Key_Egrave ")
    #     # elif e.key() == Qt.Key_Eisu_Shift:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Eisu_Shift : Key_Eisu_Shift ")
    #     # elif e.key() == Qt.Key_Eisu_toggle:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Eisu_toggle : Key_Eisu_toggle ")
    #     # elif e.key() == Qt.Key_Eject:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Eject : Key_Eject ")
    #     # elif e.key() == Qt.Key_End:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_End : Key_End ")
    #     # elif e.key() == Qt.Key_Enter:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Enter : Key_Enter ")
    #     # elif e.key() == Qt.Key_Equal:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Equal : Key_Equal ")
    #     # elif e.key() == Qt.Key_Escape:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Escape : Key_Escape ")
    #     #     self.label10.setText(f"event monitor:\nkeyPressEvent : Key_Escape")
    #     # elif e.key() == Qt.Key_ETH:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ETH : Key_ETH ")
    #     # elif e.key() == Qt.Key_Excel:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Excel : Key_Excel ")
    #     # elif e.key() == Qt.Key_Exclam:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Exclam : Key_Exclam ")
    #     # elif e.key() == Qt.Key_exclamdown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_exclamdown : Key_exclamdown ")
    #     # elif e.key() == Qt.Key_Execute:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Execute : Key_Execute ")
    #     # elif e.key() == Qt.Key_Exit:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Exit : Key_Exit ")
    #     # elif e.key() == Qt.Key_Explorer:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Explorer : Key_Explorer ")
    #     # elif e.key() == Qt.Key_F:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F : Key_F ")
    #     # elif e.key() == Qt.Key_F1:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F1 : Key_F1 ")
    #     # elif e.key() == Qt.Key_F10:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F10 : Key_F10 ")
    #     # elif e.key() == Qt.Key_F11:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F11 : Key_F11 ")
    #     # elif e.key() == Qt.Key_F12:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F12 : Key_F12 ")
    #     # elif e.key() == Qt.Key_F13:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F13 : Key_F13 ")
    #     # elif e.key() == Qt.Key_F14:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F14 : Key_F14 ")
    #     # elif e.key() == Qt.Key_F15:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F15 : Key_F15 ")
    #     # elif e.key() == Qt.Key_F16:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F16 : Key_F16 ")
    #     # elif e.key() == Qt.Key_F17:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F17 : Key_F17 ")
    #     # elif e.key() == Qt.Key_F18:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F18 : Key_F18 ")
    #     # elif e.key() == Qt.Key_F19:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F19 : Key_F19 ")
    #     # elif e.key() == Qt.Key_F2:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F2 : Key_F2 ")
    #     # elif e.key() == Qt.Key_F20:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F20 : Key_F20 ")
    #     # elif e.key() == Qt.Key_F21:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F21 : Key_F21 ")
    #     # elif e.key() == Qt.Key_F22:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F22 : Key_F22 ")
    #     # elif e.key() == Qt.Key_F23:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F23 : Key_F23 ")
    #     # elif e.key() == Qt.Key_F24:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F24 : Key_F24 ")
    #     # elif e.key() == Qt.Key_F25:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F25 : Key_F25 ")
    #     # elif e.key() == Qt.Key_F26:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F26 : Key_F26 ")
    #     # elif e.key() == Qt.Key_F27:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F27 : Key_F27 ")
    #     # elif e.key() == Qt.Key_F28:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F28 : Key_F28 ")
    #     # elif e.key() == Qt.Key_F29:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F29 : Key_F29 ")
    #     # elif e.key() == Qt.Key_F3:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F3 : Key_F3 ")
    #     # elif e.key() == Qt.Key_F30:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F30 : Key_F30 ")
    #     # elif e.key() == Qt.Key_F31:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F31 : Key_F31 ")
    #     # elif e.key() == Qt.Key_F32:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F32 : Key_F32 ")
    #     # elif e.key() == Qt.Key_F33:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F33 : Key_F33 ")
    #     # elif e.key() == Qt.Key_F34:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F34 : Key_F34 ")
    #     # elif e.key() == Qt.Key_F35:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F35 : Key_F35 ")
    #     # elif e.key() == Qt.Key_F4:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F4 : Key_F4 ")
    #     # elif e.key() == Qt.Key_F5:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F5 : Key_F5 ")
    #     # elif e.key() == Qt.Key_F6:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F6 : Key_F6 ")
    #     # elif e.key() == Qt.Key_F7:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F7 : Key_F7 ")
    #     # elif e.key() == Qt.Key_F8:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F8 : Key_F8 ")
    #     # elif e.key() == Qt.Key_F9:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_F9 : Key_F9 ")
    #     # elif e.key() == Qt.Key_Favorites:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Favorites : Key_Favorites ")
    #     # elif e.key() == Qt.Key_Finance:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Finance : Key_Finance ")
    #     # elif e.key() == Qt.Key_Find:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Find : Key_Find ")
    #     # elif e.key() == Qt.Key_Flip:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Flip : Key_Flip ")
    #     # elif e.key() == Qt.Key_Forward:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Forward : Key_Forward ")
    #     # elif e.key() == Qt.Key_G:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_G : Key_G ")
    #     # elif e.key() == Qt.Key_Game:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Game : Key_Game ")
    #     # elif e.key() == Qt.Key_Go:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Go : Key_Go ")
    #     # elif e.key() == Qt.Key_Greater:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Greater : Key_Greater ")
    #     # elif e.key() == Qt.Key_Green:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Green : Key_Green ")
    #     # elif e.key() == Qt.Key_Guide:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Guide : Key_Guide ")
    #     # elif e.key() == Qt.Key_guillemotleft:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_guillemotleft : Key_guillemotleft ")
    #     # elif e.key() == Qt.Key_guillemotright:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_guillemotright : Key_guillemotright ")
    #     # elif e.key() == Qt.Key_H:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_H : Key_H ")
    #     # elif e.key() == Qt.Key_Hangul:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul : Key_Hangul ")
    #     # elif e.key() == Qt.Key_Hangul_Banja:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_Banja : Key_Hangul_Banja ")
    #     # elif e.key() == Qt.Key_Hangul_End:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_End : Key_Hangul_End ")
    #     # elif e.key() == Qt.Key_Hangul_Hanja:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_Hanja : Key_Hangul_Hanja ")
    #     # elif e.key() == Qt.Key_Hangul_Jamo:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_Jamo : Key_Hangul_Jamo ")
    #     # elif e.key() == Qt.Key_Hangul_Jeonja:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_Jeonja : Key_Hangul_Jeonja ")
    #     # elif e.key() == Qt.Key_Hangul_PostHanja:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_PostHanja : Key_Hangul_PostHanja ")
    #     # elif e.key() == Qt.Key_Hangul_PreHanja:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_PreHanja : Key_Hangul_PreHanja ")
    #     # elif e.key() == Qt.Key_Hangul_Romaja:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_Romaja : Key_Hangul_Romaja ")
    #     # elif e.key() == Qt.Key_Hangul_Special:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_Special : Key_Hangul_Special ")
    #     # elif e.key() == Qt.Key_Hangul_Start:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangul_Start : Key_Hangul_Start ")
    #     # elif e.key() == Qt.Key_Hangup:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hangup : Key_Hangup ")
    #     # elif e.key() == Qt.Key_Hankaku:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hankaku : Key_Hankaku ")
    #     # elif e.key() == Qt.Key_Help:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Help : Key_Help ")
    #     # elif e.key() == Qt.Key_Henkan:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Henkan : Key_Henkan ")
    #     # elif e.key() == Qt.Key_Hibernate:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hibernate : Key_Hibernate ")
    #     # elif e.key() == Qt.Key_Hiragana:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hiragana : Key_Hiragana ")
    #     # elif e.key() == Qt.Key_Hiragana_Katakana:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hiragana_Katakana : Key_Hiragana_Katakana ")
    #     # elif e.key() == Qt.Key_History:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_History : Key_History ")
    #     # elif e.key() == Qt.Key_Home:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Home : Key_Home ")
    #     # elif e.key() == Qt.Key_HomePage:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_HomePage : Key_HomePage ")
    #     # elif e.key() == Qt.Key_HotLinks:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_HotLinks : Key_HotLinks ")
    #     # elif e.key() == Qt.Key_Hyper_L:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hyper_L : Key_Hyper_L ")
    #     # elif e.key() == Qt.Key_Hyper_R:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Hyper_R : Key_Hyper_R ")
    #     # elif e.key() == Qt.Key_hyphen:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_hyphen : Key_hyphen ")
    #     # elif e.key() == Qt.Key_I:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_I : Key_I ")
    #     # elif e.key() == Qt.Key_Iacute:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Iacute : Key_Iacute ")
    #     # elif e.key() == Qt.Key_Icircumflex:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Icircumflex : Key_Icircumflex ")
    #     # elif e.key() == Qt.Key_Idiaeresis:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Idiaeresis : Key_Idiaeresis ")
    #     # elif e.key() == Qt.Key_Igrave:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Igrave : Key_Igrave ")
    #     # elif e.key() == Qt.Key_Info:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Info : Key_Info ")
    #     # elif e.key() == Qt.Key_Insert:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Insert : Key_Insert ")
    #     # elif e.key() == Qt.Key_iTouch:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_iTouch : Key_iTouch ")
    #     # elif e.key() == Qt.Key_J:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_J : Key_J ")
    #     # elif e.key() == Qt.Key_K:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_K : Key_K ")
    #     # elif e.key() == Qt.Key_Kana_Lock:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Kana_Lock : Key_Kana_Lock ")
    #     # elif e.key() == Qt.Key_Kana_Shift:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Kana_Shift : Key_Kana_Shift ")
    #     # elif e.key() == Qt.Key_Kanji:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Kanji : Key_Kanji ")
    #     # elif e.key() == Qt.Key_Katakana:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Katakana : Key_Katakana ")
    #     # elif e.key() == Qt.Key_KeyboardBrightnessDown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_KeyboardBrightnessDown : Key_KeyboardBrightnessDown ")
    #     # elif e.key() == Qt.Key_KeyboardBrightnessUp:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_KeyboardBrightnessUp : Key_KeyboardBrightnessUp ")
    #     # elif e.key() == Qt.Key_KeyboardLightOnOff:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_KeyboardLightOnOff : Key_KeyboardLightOnOff ")
    #     # elif e.key() == Qt.Key_L:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_L : Key_L ")
    #     # elif e.key() == Qt.Key_LastNumberRedial:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LastNumberRedial : Key_LastNumberRedial ")
    #     # elif e.key() == Qt.Key_Launch0:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch0 : Key_Launch0 ")
    #     # elif e.key() == Qt.Key_Launch1:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch1 : Key_Launch1 ")
    #     # elif e.key() == Qt.Key_Launch2:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch2 : Key_Launch2 ")
    #     # elif e.key() == Qt.Key_Launch3:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch3 : Key_Launch3 ")
    #     # elif e.key() == Qt.Key_Launch4:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch4 : Key_Launch4 ")
    #     # elif e.key() == Qt.Key_Launch5:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch5 : Key_Launch5 ")
    #     # elif e.key() == Qt.Key_Launch6:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch6 : Key_Launch6 ")
    #     # elif e.key() == Qt.Key_Launch7:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch7 : Key_Launch7 ")
    #     # elif e.key() == Qt.Key_Launch8:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch8 : Key_Launch8 ")
    #     # elif e.key() == Qt.Key_Launch9:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Launch9 : Key_Launch9 ")
    #     # elif e.key() == Qt.Key_LaunchA:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchA : Key_LaunchA ")
    #     # elif e.key() == Qt.Key_LaunchB:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchB : Key_LaunchB ")
    #     # elif e.key() == Qt.Key_LaunchC:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchC : Key_LaunchC ")
    #     # elif e.key() == Qt.Key_LaunchD:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchD : Key_LaunchD ")
    #     # elif e.key() == Qt.Key_LaunchE:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchE : Key_LaunchE ")
    #     # elif e.key() == Qt.Key_LaunchF:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchF : Key_LaunchF ")
    #     # elif e.key() == Qt.Key_LaunchG:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchG : Key_LaunchG ")
    #     # elif e.key() == Qt.Key_LaunchH:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchH : Key_LaunchH ")
    #     # elif e.key() == Qt.Key_LaunchMail:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchMail : Key_LaunchMail ")
    #     # elif e.key() == Qt.Key_LaunchMedia:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LaunchMedia : Key_LaunchMedia ")
    #     # elif e.key() == Qt.Key_Left:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Left : Key_Left ")
    #     # elif e.key() == Qt.Key_Less:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Less : Key_Less ")
    #     # elif e.key() == Qt.Key_LightBulb:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LightBulb : Key_LightBulb ")
    #     # elif e.key() == Qt.Key_LogOff:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_LogOff : Key_LogOff ")
    #     # elif e.key() == Qt.Key_M:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_M : Key_M ")
    #     # elif e.key() == Qt.Key_macron:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_macron : Key_macron ")
    #     # elif e.key() == Qt.Key_MailForward:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MailForward : Key_MailForward ")
    #     # elif e.key() == Qt.Key_Market:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Market : Key_Market ")
    #     # elif e.key() == Qt.Key_masculine:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_masculine : Key_masculine ")
    #     # elif e.key() == Qt.Key_Massyo:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Massyo : Key_Massyo ")
    #     # elif e.key() == Qt.Key_MediaLast:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MediaLast : Key_MediaLast ")
    #     # elif e.key() == Qt.Key_MediaNext:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MediaNext : Key_MediaNext ")
    #     # elif e.key() == Qt.Key_MediaPause:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MediaPause : Key_MediaPause ")
    #     # elif e.key() == Qt.Key_MediaPlay:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MediaPlay : Key_MediaPlay ")
    #     # elif e.key() == Qt.Key_MediaPrevious:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MediaPrevious : Key_MediaPrevious ")
    #     # elif e.key() == Qt.Key_MediaRecord:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MediaRecord : Key_MediaRecord ")
    #     # elif e.key() == Qt.Key_MediaStop:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MediaStop : Key_MediaStop ")
    #     # elif e.key() == Qt.Key_MediaTogglePlayPause:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MediaTogglePlayPause : Key_MediaTogglePlayPause ")
    #     # elif e.key() == Qt.Key_Meeting:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Meeting : Key_Meeting ")
    #     # elif e.key() == Qt.Key_Memo:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Memo : Key_Memo ")
    #     # elif e.key() == Qt.Key_Menu:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Menu : Key_Menu ")
    #     # elif e.key() == Qt.Key_MenuKB:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MenuKB : Key_MenuKB ")
    #     # elif e.key() == Qt.Key_MenuPB:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MenuPB : Key_MenuPB ")
    #     # elif e.key() == Qt.Key_Messenger:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Messenger : Key_Messenger ")
    #     # elif e.key() == Qt.Key_Meta:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Meta : Key_Meta ")
    #     # elif e.key() == Qt.Key_MicMute:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MicMute : Key_MicMute ")
    #     # elif e.key() == Qt.Key_MicVolumeDown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MicVolumeDown : Key_MicVolumeDown ")
    #     # elif e.key() == Qt.Key_MicVolumeUp:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MicVolumeUp : Key_MicVolumeUp ")
    #     # elif e.key() == Qt.Key_Minus:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Minus : Key_Minus ")
    #     # elif e.key() == Qt.Key_Mode_switch:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Mode_switch : Key_Mode_switch ")
    #     # elif e.key() == Qt.Key_MonBrightnessDown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MonBrightnessDown : Key_MonBrightnessDown ")
    #     # elif e.key() == Qt.Key_MonBrightnessUp:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MonBrightnessUp : Key_MonBrightnessUp ")
    #     # elif e.key() == Qt.Key_mu:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_mu : Key_mu ")
    #     # elif e.key() == Qt.Key_Muhenkan:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Muhenkan : Key_Muhenkan ")
    #     # elif e.key() == Qt.Key_Multi_key:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Multi_key : Key_Multi_key ")
    #     # elif e.key() == Qt.Key_MultipleCandidate:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MultipleCandidate : Key_MultipleCandidate ")
    #     # elif e.key() == Qt.Key_multiply:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_multiply : Key_multiply ")
    #     # elif e.key() == Qt.Key_Music:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Music : Key_Music ")
    #     # elif e.key() == Qt.Key_MySites:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_MySites : Key_MySites ")
    #     # elif e.key() == Qt.Key_N:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_N : Key_N ")
    #     # elif e.key() == Qt.Key_New:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_New : Key_New ")
    #     # elif e.key() == Qt.Key_News:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_News : Key_News ")
    #     # elif e.key() == Qt.Key_No:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_No : Key_No ")
    #     # elif e.key() == Qt.Key_nobreakspace:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_nobreakspace : Key_nobreakspace ")
    #     # elif e.key() == Qt.Key_notsign:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_notsign : Key_notsign ")
    #     # elif e.key() == Qt.Key_Ntilde:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Ntilde : Key_Ntilde ")
    #     # elif e.key() == Qt.Key_NumberSign:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_NumberSign : Key_NumberSign ")
    #     # elif e.key() == Qt.Key_NumLock:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_NumLock : Key_NumLock ")
    #     # elif e.key() == Qt.Key_O:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_O : Key_O ")
    #     # elif e.key() == Qt.Key_Oacute:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Oacute : Key_Oacute ")
    #     # elif e.key() == Qt.Key_Ocircumflex:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Ocircumflex : Key_Ocircumflex ")
    #     # elif e.key() == Qt.Key_Odiaeresis:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Odiaeresis : Key_Odiaeresis ")
    #     # elif e.key() == Qt.Key_OfficeHome:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_OfficeHome : Key_OfficeHome ")
    #     # elif e.key() == Qt.Key_Ograve:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Ograve : Key_Ograve ")
    #     # elif e.key() == Qt.Key_onehalf:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_onehalf : Key_onehalf ")
    #     # elif e.key() == Qt.Key_onequarter:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_onequarter : Key_onequarter ")
    #     # elif e.key() == Qt.Key_onesuperior:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_onesuperior : Key_onesuperior ")
    #     # elif e.key() == Qt.Key_Ooblique:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Ooblique : Key_Ooblique ")
    #     # elif e.key() == Qt.Key_Open:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Open : Key_Open ")
    #     # elif e.key() == Qt.Key_OpenUrl:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_OpenUrl : Key_OpenUrl ")
    #     # elif e.key() == Qt.Key_Option:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Option : Key_Option ")
    #     # elif e.key() == Qt.Key_ordfeminine:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ordfeminine : Key_ordfeminine ")
    #     # elif e.key() == Qt.Key_Otilde:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Otilde : Key_Otilde ")
    #     # elif e.key() == Qt.Key_P:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_P : Key_P ")
    #     # elif e.key() == Qt.Key_PageDown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_PageDown : Key_PageDown ")
    #     # elif e.key() == Qt.Key_PageUp:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_PageUp : Key_PageUp ")
    #     # elif e.key() == Qt.Key_paragraph:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_paragraph : Key_paragraph ")
    #     # elif e.key() == Qt.Key_ParenLeft:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ParenLeft : Key_ParenLeft ")
    #     # elif e.key() == Qt.Key_ParenRight:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ParenRight : Key_ParenRight ")
    #     # elif e.key() == Qt.Key_Paste:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Paste : Key_Paste ")
    #     # elif e.key() == Qt.Key_Pause:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Pause : Key_Pause ")
    #     # elif e.key() == Qt.Key_Percent:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Percent : Key_Percent ")
    #     # elif e.key() == Qt.Key_Period:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Period : Key_Period ")
    #     # elif e.key() == Qt.Key_periodcentered:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_periodcentered : Key_periodcentered ")
    #     # elif e.key() == Qt.Key_Phone:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Phone : Key_Phone ")
    #     # elif e.key() == Qt.Key_Pictures:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Pictures : Key_Pictures ")
    #     # elif e.key() == Qt.Key_Play:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Play : Key_Play ")
    #     # elif e.key() == Qt.Key_Plus:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Plus : Key_Plus ")
    #     # elif e.key() == Qt.Key_plusminus:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_plusminus : Key_plusminus ")
    #     # elif e.key() == Qt.Key_PowerDown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_PowerDown : Key_PowerDown ")
    #     # elif e.key() == Qt.Key_PowerOff:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_PowerOff : Key_PowerOff ")
    #     # elif e.key() == Qt.Key_PreviousCandidate:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_PreviousCandidate : Key_PreviousCandidate ")
    #     # elif e.key() == Qt.Key_Print:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Print : Key_Print ")
    #     # elif e.key() == Qt.Key_Printer:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Printer : Key_Printer ")
    #     # elif e.key() == Qt.Key_Q:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Q : Key_Q ")
    #     # elif e.key() == Qt.Key_Question:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Question : Key_Question ")
    #     # elif e.key() == Qt.Key_questiondown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_questiondown : Key_questiondown ")
    #     # elif e.key() == Qt.Key_QuoteDbl:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_QuoteDbl : Key_QuoteDbl ")
    #     # elif e.key() == Qt.Key_QuoteLeft:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_QuoteLeft : Key_QuoteLeft ")
    #     # elif e.key() == Qt.Key_R:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_R : Key_R ")
    #     # elif e.key() == Qt.Key_Red:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Red : Key_Red ")
    #     # elif e.key() == Qt.Key_Redo:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Redo : Key_Redo ")
    #     # elif e.key() == Qt.Key_Refresh:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Refresh : Key_Refresh ")
    #     # elif e.key() == Qt.Key_registered:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_registered : Key_registered ")
    #     # elif e.key() == Qt.Key_Reload:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Reload : Key_Reload ")
    #     # elif e.key() == Qt.Key_Reply:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Reply : Key_Reply ")
    #     #
    #     # elif e.key() == Qt.Key_Right:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Right : Key_Right ")
    #     # elif e.key() == Qt.Key_Romaji:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Romaji : Key_Romaji ")
    #     # elif e.key() == Qt.Key_RotateWindows:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_RotateWindows : Key_RotateWindows ")
    #     # elif e.key() == Qt.Key_RotationKB:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_RotationKB : Key_RotationKB ")
    #     # elif e.key() == Qt.Key_RotationPB:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_RotationPB : Key_RotationPB ")
    #     # elif e.key() == Qt.Key_S:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_S : Key_S ")
    #     # elif e.key() == Qt.Key_Save:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Save : Key_Save ")
    #     # elif e.key() == Qt.Key_ScreenSaver:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ScreenSaver : Key_ScreenSaver ")
    #     # elif e.key() == Qt.Key_ScrollLock:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ScrollLock : Key_ScrollLock ")
    #     # elif e.key() == Qt.Key_Search:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Search : Key_Search ")
    #     # elif e.key() == Qt.Key_section:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_section : Key_section ")
    #     # elif e.key() == Qt.Key_Select:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Select : Key_Select ")
    #     # elif e.key() == Qt.Key_Semicolon:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Semicolon : Key_Semicolon ")
    #     # elif e.key() == Qt.Key_Send:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Send : Key_Send ")
    #     # elif e.key() == Qt.Key_Settings:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Settings : Key_Settings ")
    #     # elif e.key() == Qt.Key_Shift:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Shift : Key_Shift ")
    #     # elif e.key() == Qt.Key_Shop:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Shop : Key_Shop ")
    #     # elif e.key() == Qt.Key_SingleCandidate:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_SingleCandidate : Key_SingleCandidate ")
    #     # elif e.key() == Qt.Key_Slash:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Slash : Key_Slash ")
    #     # elif e.key() == Qt.Key_Sleep:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Sleep : Key_Sleep ")
    #     # elif e.key() == Qt.Key_Space:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Space : Key_Space ")
    #     # elif e.key() == Qt.Key_Spell:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Spell : Key_Spell ")
    #     # elif e.key() == Qt.Key_SplitScreen:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_SplitScreen : Key_SplitScreen ")
    #     # elif e.key() == Qt.Key_ssharp:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ssharp : Key_ssharp ")
    #     # elif e.key() == Qt.Key_Standby:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Standby : Key_Standby ")
    #     # elif e.key() == Qt.Key_sterling:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_sterling : Key_sterling ")
    #     # elif e.key() == Qt.Key_Stop:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Stop : Key_Stop ")
    #     # elif e.key() == Qt.Key_Subtitle:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Subtitle : Key_Subtitle ")
    #     # elif e.key() == Qt.Key_Super_L:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Super_L : Key_Super_L ")
    #     # elif e.key() == Qt.Key_Super_R:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Super_R : Key_Super_R ")
    #     # elif e.key() == Qt.Key_Support:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Support : Key_Support ")
    #     # elif e.key() == Qt.Key_Suspend:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Suspend : Key_Suspend ")
    #     # elif e.key() == Qt.Key_SysReq:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_SysReq : Key_SysReq ")
    #     # elif e.key() == Qt.Key_T:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_T : Key_T ")
    #     # elif e.key() == Qt.Key_Tab:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Tab : Key_Tab ")
    #     # elif e.key() == Qt.Key_TaskPane:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_TaskPane : Key_TaskPane ")
    #     # elif e.key() == Qt.Key_Terminal:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Terminal : Key_Terminal ")
    #     # elif e.key() == Qt.Key_THORN:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_THORN : Key_THORN ")
    #     # elif e.key() == Qt.Key_threequarters:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_threequarters : Key_threequarters ")
    #     # elif e.key() == Qt.Key_threesuperior:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_threesuperior : Key_threesuperior ")
    #     # elif e.key() == Qt.Key_Time:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Time : Key_Time ")
    #     # elif e.key() == Qt.Key_ToDoList:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ToDoList : Key_ToDoList ")
    #     # elif e.key() == Qt.Key_ToggleCallHangup:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ToggleCallHangup : Key_ToggleCallHangup ")
    #     # elif e.key() == Qt.Key_Tools:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Tools : Key_Tools ")
    #     # elif e.key() == Qt.Key_TopMenu:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_TopMenu : Key_TopMenu ")
    #     # elif e.key() == Qt.Key_TouchpadOff:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_TouchpadOff : Key_TouchpadOff ")
    #     # elif e.key() == Qt.Key_TouchpadOn:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_TouchpadOn : Key_TouchpadOn ")
    #     # elif e.key() == Qt.Key_TouchpadToggle:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_TouchpadToggle : Key_TouchpadToggle ")
    #     # elif e.key() == Qt.Key_Touroku:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Touroku : Key_Touroku ")
    #     # elif e.key() == Qt.Key_Travel:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Travel : Key_Travel ")
    #     # elif e.key() == Qt.Key_TrebleDown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_TrebleDown : Key_TrebleDown ")
    #     # elif e.key() == Qt.Key_TrebleUp:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_TrebleUp : Key_TrebleUp ")
    #     # elif e.key() == Qt.Key_twosuperior:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_twosuperior : Key_twosuperior ")
    #     # elif e.key() == Qt.Key_U:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_U : Key_U ")
    #     # elif e.key() == Qt.Key_Uacute:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Uacute : Key_Uacute ")
    #     # elif e.key() == Qt.Key_Ucircumflex:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Ucircumflex : Key_Ucircumflex ")
    #     # elif e.key() == Qt.Key_Udiaeresis:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Udiaeresis : Key_Udiaeresis ")
    #     # elif e.key() == Qt.Key_Ugrave:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Ugrave : Key_Ugrave ")
    #     # elif e.key() == Qt.Key_Underscore:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Underscore : Key_Underscore ")
    #     # elif e.key() == Qt.Key_Undo:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Undo : Key_Undo ")
    #     # elif e.key() == Qt.Key_unknown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_unknown : Key_unknown ")
    #     # elif e.key() == Qt.Key_Up:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Up : Key_Up ")
    #     # elif e.key() == Qt.Key_UWB:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_UWB : Key_UWB ")
    #     # elif e.key() == Qt.Key_V:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_V : Key_V ")
    #     # elif e.key() == Qt.Key_Video:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Video : Key_Video ")
    #     # elif e.key() == Qt.Key_View:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_View : Key_View ")
    #     # elif e.key() == Qt.Key_VoiceDial:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_VoiceDial : Key_VoiceDial ")
    #     # elif e.key() == Qt.Key_VolumeDown:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_VolumeDown : Key_VolumeDown ")
    #     # elif e.key() == Qt.Key_VolumeMute:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_VolumeMute : Key_VolumeMute ")
    #     # elif e.key() == Qt.Key_VolumeUp:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_VolumeUp : Key_VolumeUp ")
    #     # elif e.key() == Qt.Key_W:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_W : Key_W ")
    #     # elif e.key() == Qt.Key_WakeUp:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_WakeUp : Key_WakeUp ")
    #     # elif e.key() == Qt.Key_WebCam:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_WebCam : Key_WebCam ")
    #     # elif e.key() == Qt.Key_WLAN:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_WLAN : Key_WLAN ")
    #     # elif e.key() == Qt.Key_Word:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Word : Key_Word ")
    #     # elif e.key() == Qt.Key_WWW:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_WWW : Key_WWW ")
    #     # elif e.key() == Qt.Key_X:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_X : Key_X ")
    #     # elif e.key() == Qt.Key_Xfer:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Xfer : Key_Xfer ")
    #     # elif e.key() == Qt.Key_Y:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Y : Key_Y ")
    #     # elif e.key() == Qt.Key_Yacute:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Yacute : Key_Yacute ")
    #     # elif e.key() == Qt.Key_ydiaeresis:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ydiaeresis : Key_ydiaeresis ")
    #     # elif e.key() == Qt.Key_Yellow:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Yellow : Key_Yellow ")
    #     # elif e.key() == Qt.Key_yen:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_yen : Key_yen ")
    #     # elif e.key() == Qt.Key_Yes:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Yes : Key_Yes ")
    #     # elif e.key() == Qt.Key_Z:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Z : Key_Z ")
    #     # elif e.key() == Qt.Key_Zenkaku:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Zenkaku : Key_Zenkaku ")
    #     # elif e.key() == Qt.Key_Zenkaku_Hankaku:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Zenkaku_Hankaku : Key_Zenkaku_Hankaku ")
    #     # elif e.key() == Qt.Key_Zoom:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_Zoom : Key_Zoom ")
    #     # elif e.key() == Qt.Key_ZoomIn:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ZoomIn : Key_ZoomIn ")
    #     # elif e.key() == Qt.Key_ZoomOut:
    #     #     self.label11.setText(f"keyboard event monitor:\nKey_ZoomOut : Key_ZoomOut ")

    def inputbox_changed(self):
        Park4139.commentize("inputbox 텍스트 change event 감지 되었습니다")
        print(self.inputbox.ment())

    def inputbox_edit_finished(self):
        Park4139.commentize("inputbox edit finish event 감지 되었습니다")

    def inputbox_return_pressed(self):
        Park4139.commentize("inputbox return pressed event 감지 되었습니다")

    def get_btn_name_with_shortcut_name(self, button_name_without_shortcut):
        # 버튼명과 shourtcut 명을 을 적당한 간격으로 띄워서 string 으로 반환하는 코드, 폰트 가 고정폭폰트 가 아니면 무용지물인 함수
        numbers = []
        for key, value in self.available_shortcut_list.items():
            numbers.append(len(value) + len(key))
        max_len_value = max(numbers)
        button_name_with_short_cut = ""
        for key, value in self.available_shortcut_list.items():
            if key == button_name_without_shortcut:
                space_between = " " * (max_len_value - len(key) - len(value) + 1)
                # space_between = "\t"
                # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}".strip()
                # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}( {value} )".strip()
                button_name_with_short_cut = button_name_with_short_cut + f"{value}{space_between}( {key} )".strip()
        print(button_name_with_short_cut)
        return button_name_with_short_cut

    def get_btn_name_promised(self, button_name_without_shortcut):
        button_name_with_short_cut = ""
        for key, value in self.available_shortcut_list.items():
            if key == button_name_without_shortcut:
                button_name_with_short_cut = button_name_with_short_cut + f"{key}".strip()
        return button_name_with_short_cut

    def get_shortcut_name_promised(self, button_name_without_shortcut):
        button_name_with_short_cut = ""
        for key, value in self.available_shortcut_list.items():
            if key == button_name_without_shortcut:
                button_name_with_short_cut = button_name_with_short_cut + f"{value}".strip()
        return button_name_with_short_cut

    # def show_available_shortcut_list(self):
    #     # global max
    #     # global 을 설정하면, 이 변수는 함수의 실행이 끝난 다음에도 없어지지 않는다.
    #     # 이 값을 나중에 함수 끝나고도 또 쓸려면 이렇게 쓰면 되겠다. @staticmethod 의 경우에는 변수 간의 값에 간섭이 되지 않도록 굳이 쓰지 않는 것이 좋겠다.
    #     # global 많이 쓰면 이는 변수가 전역화 되니까 메모리의 성능이 저하되는 것이 아닐까?
    #     # 그렇다면 함수 내에서만 전역적으로 변수를 쓰는 경우에, global 을 쓰지 않는 것이 성능을 위해서는 좋은 선택이겠다. 굳이 함수가 끝난 뒤에 밖에서 써야한다면 global 을 써야 겠지만, 나는 무척이나 이게 헷갈릴 것 같다
    #     # 그동안의 경험으로는 코드 맥락 상, global 선언을 하지 않아도 전역변수 처럼 작동 되는 것 같아 보인다.... 아니다 이게 global max 를 선언하지 않았다고 가정하면 max 는 show_available_shortcut_list() 가 종료되면 max 는 사라진다. 그런데 global max를 선언하면 max 는 유지된다!
    #     # 혹시 객체의 인스턴스 같은 것을 global 을 통해서 변수에 저장하고 쓰면 싱글톤 처럼 쓸 수 있는 것일까? 메모리 효율은 많이 나빠질까?
    #
    #     numbers = []
    #     for key_shortcut, value in self.available_shortcut_list.items():
    #         numbers.append(len(value))
    #     max_no: int
    #     max_no = max(numbers)
    #     for key_shortcut, value in self.available_shortcut_list.items():
    #         print(f"{{0: <{max_no}}} : {key_shortcut}".format(value))

    def rotate_window_size_mode(self):
        if self.windows_size_mode == 0:
            self.resize(self.display_width_default, self.display_height_default)
            self.move_window_to_center()  # 불필요 하면 주석하는 게 나쁘지 않겠다
            self.windows_size_mode = self.windows_size_mode + 1
        elif self.windows_size_mode == 1:
            self.setGeometry(0, 0, int(self.display_width_default), int(self.display_height[0]))
            # self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 모든 창 앞에 위치하도록 설정
            self.windows_size_mode = self.windows_size_mode + 1
        elif self.windows_size_mode == 2:
            self.showMaximized()
            self.windows_size_mode = self.windows_size_mode + 1
        elif self.windows_size_mode == 3:
            self.setGeometry(1600 - int(self.display_width_default), 0, int(self.display_width_default), int(self.display_height[0]))
            self.windows_size_mode = 0

    def set_shortcut(self, btn_name_promised, function):
        # self.shortcut = QShortcut(QKeySequence(self.available_shortcut_list[btn_name_promised]), self)  # ctrl+1 2개 키들의 조합 설정
        self.shortcut = QShortcut(self.available_shortcut_list[btn_name_promised], self)  # ctrl+n+d 3개 키들의 조합 설정 시도
        self.shortcut.activated.connect(function)
        pass

    def get_btn(self, btn_name, function, btn_text_align="left"):
        button = QPushButton(btn_name, self)  # alt f4 로 가이드 해도 되겠다. 이건 그냥 설정 되어 있는 부분.
        button.clicked.connect(function)

        # 2023년 12월 14일 (목) 16:28:15
        # 결론, fixed width font로 시도해볼 수 있다 자릿 수를 맞출 수 있다.
        # non-fixed width font 이슈 JAVA 에서도 구현했을 때 마딱드렸던 내용인데,
        # 분명히 문장 전체 길이를 단어 사이의 공백의 수를 결정짓는 함수를 테스트 했음에도 자릿수가 맞지 않았는데
        # 이는 고정 폭이 아님이기 때문이었다 따라서 고정 폭 폰트로 출력되는 콘솔에서는 정상, 비고정 폭 폰트로 출력되는 콘솔에서는 비정상,
        # 이 경우에는 콘솔이 아니라 pyside6 로 만든 UI 에서 나타났다.
        # 새벽에 이 문제를 만나서 잠깐 넋나갔는데 아침에 다시보니 그때 경험이 떠올라서 실험해보니 잘 해결되었다. 덕분에 pyside6에서 위젯에 폰트 적용하는 법도 터득

        # pyside6 버튼 내부폰트 설정
        # pyside6 built in fixed width font
        # font = QFont("Monospace")
        # font = QFont("Ubuntu Mono")
        # font = QFont("Inconsolata")
        # font = QFont("Monaco")
        # font = QFont("Courier")
        # font = QFont("Courier 10 Pitch")
        # font = QFont("Courier Prime")
        # font = QFont("Droid Sans Mono")
        # font = QFont("Fira Mono")
        # font = QFont("Hack")
        # font = QFont("Menlo")
        # font = QFont("Monofur")
        # font = QFont("Noto Mono")
        # font = QFont("PT Mono")
        # font = QFont("Roboto Mono")
        # font = QFont("Source Code Pro")
        # font = QFont("Victor Mono")
        # font = QFont("Courier New")
        # font = QFont("Liberation Mono")
        # font = QFont("DejaVu Sans Mono")
        # font = QFont("Consolas")  # 그나마 가장 마음에 드는 폰트

        # pyside6 버튼 외부폰트 설정
        button.setFont(Park4139.get_font_for_pyside6(font_path=pkg_park4139.FONTS.GMARKETSANSTTFLIGHT_TTF))
        if btn_text_align == "right":
            button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9); height: 20px; font-size: 10px}")
            button.setFixedWidth(65)
            # button.setMinimumWidth(button.sizeHint().width())
        else:
            button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px; font-size: 10px}")
            button.setFixedWidth(225)
            # button.setMinimumWidth(button.sizeHint().width())
        return button

    def move_window_to_center(self):
        center = QScreen.availableGeometry(app.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    @rpa_program_method_decorator
    def show_weather_from_web(self):
        Park4139.get_comprehensive_weather_information_from_web()

    @rpa_program_method_decorator
    def run_no_paste_memo(self):
        Park4139.annouce_service_launch()

    @rpa_program_method_decorator
    def should_i_reboot_this_computer(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents='시스템을 재시작할까요?', buttons=["재시작", "재시작하지 않기"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "재시작":
                Park4139.reboot_this_computer()
            else:
                break

    @QtCore.Slot()
    def login(self):
        Park4139.annouce_service_launch()
        print(self.print_id)

    @rpa_program_method_decorator
    def should_i_show_animation_information_from_web(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="nyaa.si 에서 검색할 내용을 입력하세요", buttons=["입력", "입력하지 않기"], is_input_text_box=True)
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "입력":
                Park4139.search_animation_data_from_web(dialog.box_for_editing_input_text.text())
            else:
                break

    @rpa_program_method_decorator
    def should_i_exit_this_program(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="앱을 종료할까요?", buttons=["종료", "종료하지 않기"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "종료":
                # app.quit()
                Park4139.taskkill("python.exe")
                sys.exit()
            else:
                break

    @rpa_program_method_decorator
    def should_i_find_direction_via_naver_map(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="어디로 길을 찾아드릴까요?", buttons=["입력", "입력하지 않기"], is_input_text_box=True)
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "입력":
                Park4139.find_direction_via_naver_map(dialog.box_for_editing_input_text.text())
            else:
                # self.show()
                break

    @rpa_program_method_decorator
    def download_youtube_as_wav(self):
        Park4139.annouce_service_launch()

    @rpa_program_method_decorator
    def should_i_download_youtube_as_webm(self):
        Park4139.should_i_download_youtube_as_webm()

    @rpa_program_method_decorator
    def should_i_download_youtube_as_webm_alt(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="다운로드하고 싶은 URL을 제출해주세요?", buttons=["제출", "제출하지 않기"], is_input_text_box=True)
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "제출":
                Park4139.download_from_youtube_to_webm_alt(dialog.box_for_editing_input_text.text())
            else:
                break

    @rpa_program_method_decorator
    def download_youtube_as_webm_only_sound(self):
        Park4139.annouce_service_launch()

    def hide_windows_of_this_app(self):
        self.hide()

    @rpa_program_method_decorator
    def should_i_shutdown_this_computer(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="시스템을 종료할까요?", buttons=["종료", "종료하지 않기"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "종료":
                Park4139.shutdown_this_computer()
            else:
                break

    @rpa_program_method_decorator
    def shoot_screenshot_custom(self):
        while True:
            Park4139.shoot_custom_screenshot()
            break

    @rpa_program_method_decorator
    def shoot_screenshot_full(self):
        while True:
            Park4139.shoot_full_screenshot()
            break

    @rpa_program_method_decorator
    def shoot_screenshot_for_rpa(self):
        while True:
            Park4139.shoot_img_for_rpa()
            break

    @rpa_program_method_decorator
    def back_up_target(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="빽업할 타겟경로를 입력하세요?", buttons=["입력", "입력하지 않기"], is_input_text_box=True)
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "입력":
                Park4139.bkup(dialog.box_for_editing_input_text.text())
            else:
                break

    @rpa_program_method_decorator
    @rpa_program_method_decorator
    def test(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="테스트를 시작할까요?", buttons=["시작하기", "시작하지 않기"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            if text_of_clicked_btn == "시작하기":
                # _________________________________________  UP (TESTED SUCCESS) _________________________________________
                import test_core
                # _________________________________________ BELOW (NOT TESTED YET) _________________________________________
                break
            else:
                break

    @staticmethod
    def do_nothing():
        Park4139.commentize("def do_nothing():")

    @rpa_program_method_decorator
    def open_project_directory(self):
        Park4139.get_cmd_output(f'explorer "{os.getcwd()}"')

    @rpa_program_method_decorator
    def should_i_enter_to_power_saving_mode(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="절전모드로 진입할까요?", buttons=["진입", "진입하지 않기"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "진입":
                Park4139.enter_power_saving_mode()
            else:
                break

    @rpa_program_method_decorator
    def should_i_translate_eng_to_kor(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="WRITE SOMETHING YOU WANT TO TRANSLATE \n(FROM ENG TO KOREAN)", buttons=["Translate this", "Don't"], is_input_text_box=True)
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "Translate this":
                Park4139.translate_eng_to_kor(dialog.box_for_editing_input_text.text())
            else:
                break

    @rpa_program_method_decorator
    def should_i_translate_kor_to_eng(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents='번역하고 싶은 내용을 입력하세요\n(한글에서 영어로)', buttons=["번역해줘", "번역하지 않기"], is_input_text_box=True)
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "번역해줘":
                Park4139.translate_kor_to_eng(dialog.box_for_editing_input_text.text())
            else:
                break

    @rpa_program_method_decorator
    def should_i_empty_trash_can(self):
        while True:
            # Park4139.commentize(rf'휴지통 용량확인 pyautogui RPA')
            # ment = f'현재 휴지통이 10기가 바이트 이상입니다 쓰레기통을 비울까요' # 이건 wrapping 할 로직.
            dialog = pkg_park4139.CustomDialog(contents='쓰레기통을 비울까요?', buttons=["비워줘", "비우지 말아줘"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "비워줘":
                Park4139.empty_recycle_bin()
            else:
                break

    @rpa_program_method_decorator
    def run_cmd_exe(self):
        Park4139.run_cmd_exe()

    @rpa_program_method_decorator
    def ask_something_to_ai(self):
        previous_question = None
        if previous_question == None:
            previous_question = clipboard.paste()
        while True:
            dialog = pkg_park4139.CustomDialog(contents='AI 에게 할 질문을 입력하세요', buttons=["질문해줘", "질문하지 않기"], is_input_text_box=True, input_text_default=previous_question)
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "질문해줘":
                Park4139.ask_to_web(dialog.box_for_editing_input_text.text())
            else:
                break
            previous_question = dialog.box_for_editing_input_text.text()

    @rpa_program_method_decorator
    def connect_to_rdp1(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents='rdp1에 원격접속할까요?', buttons=["접속해줘", "접속하지 않기"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            Park4139.commentize("text_of_clicked_btn")
            Park4139.debug_as_cli(text_of_clicked_btn)
            if text_of_clicked_btn == "접속해줘":
                Park4139.connect_remote_rdp1()
            else:
                break

    @QtCore.Slot()
    def print_id(self):
        print(self.id)

    @rpa_program_method_decorator
    def record_macro(self):
        while True:
            dialog = pkg_park4139.CustomDialog(contents="매크로 레코드를 새로 시작할까요?", buttons=["새로 시작하기", "이어서 시작하기", "시작하지 않기"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            if text_of_clicked_btn == "새로 시작하기":
                Park4139.move_target_to_trash_bin(Park4139.MACRO_LOG)
                Park4139.make_leaf_file(Park4139.MACRO_LOG)
                Park4139.explorer(Park4139.MACRO_LOG)
                macro_window = MacroWindow()
                macro_window.show()
                macro_window.activateWindow()
                break
            elif text_of_clicked_btn == "이어서 시작하기":
                if os.path.exists(Park4139.MACRO_LOG):
                    macro_window = MacroWindow()
                    macro_window.show()
                    macro_window.activateWindow()
            else:
                break

    @rpa_program_method_decorator
    def download_video_from_web1(self):
        while True:
            # Park4139.press("ctrl", "0")

            file_png = rf"{os.getcwd()}\$cache_png\download_video_via_chrome_extensions.png"
            Park4139.click_center_of_img_recognized_by_mouse_left(img_abspath=file_png, recognize_loop_limit_cnt=10)

            Park4139.sleep(1000)

            Park4139.press("tab")
            Park4139.sleep(30)

            Park4139.press("enter")
            Park4139.sleep(30)

            Park4139.press("ctrl", "shift", "tab")

            Park4139.press("ctrl", "0")
            Park4139.press("ctrl", "-")
            Park4139.press("ctrl", "-")
            break

    @rpa_program_method_decorator
    def download_video_from_web2(self):
        while True:
            file_png = rf"{os.getcwd()}\$cache_png\download_video_via_chrome_extensions1.png"
            is_image_finded = Park4139.click_center_of_img_recognized_by_mouse_left(img_abspath=file_png, recognize_loop_limit_cnt=100)
            if is_image_finded:
                Park4139.sleep(30)
                Park4139.press("ctrl", "f")
                Park4139.press("end")
                Park4139.press("ctrl", "a")
                Park4139.press("backspace")
                Park4139.write_fast("save")
                Park4139.press("enter")
                Park4139.press("enter")
                Park4139.press("esc")
                Park4139.press("enter")
                file_png = rf"{os.getcwd()}\$cache_png\download_video_via_chrome_extensions2.png"
                is_image_finded = Park4139.click_center_of_img_recognized_by_mouse_left(img_abspath=file_png, recognize_loop_limit_cnt=100)
                if is_image_finded:
                    Park4139.press("shift", "w")
                else:
                    Park4139.speak(ment="이미지를 찾을 수 없어 해당 자동화 기능을 마저 진행할 수 없습니다")
            else:
                Park4139.speak(ment="이미지를 찾을 수 없어 해당 자동화 기능을 마저 진행할 수 없습니다")
            break
        pass

    def toogle_rpa_window(self):
        # Park4139.debug_as_cli(f"def {inspect.currentframe().f_code.co_name}() is called...")
        if self.isHidden() and not self.isVisible():
            # console_blurred 프로그램 창 활성화
            self.bring_this_window()

        else:
            self.hide()

    def run_scheduler_without_confirm(self):
        """  스케쥴러를 실행시키는 함수 """

        # 비동기 이벤트 함수 설정
        async def run_scheduler():
            # schedule.every(30).minutes.do(partial(Park4139.speak_after_x_min, 30))
            # schedule.every().tuesday.at("15:00").do(Park4139.speak_today_time_info)
            # schedule.every().wednesday.at("15:00").do(Park4139.speak_today_time_info)
            # schedule.every().thursday.at("15:00").do(Park4139.speak_today_time_info)
            # schedule.every().friday.at("15:00").do(Park4139.speak_today_time_info)
            # schedule.every().saturday.at("15:00").do(Park4139.speak_today_time_info)
            # schedule.every().sunday.at("15:00").do(Park4139.speak_today_time_info)
            # schedule.every(1).hour.do(Park4139.speak_server_hh_mm)
            # schedule.every(1).day.do(Park4139.speak_server_hh_mm)
            # schedule.every(1).day.at("12:30").do(Park4139.speak_server_hh_mm)
            # while True:
            # schedule.run_pending()
            # Park4139.debug_as_cli(f"async def {inspect.currentframe().f_code.co_name}() is running...")
            # await ....sleep(1000)
            scheduler_loop_cnt = 0
            while True:
                # 루프마다 == 가능한 짧은 시간 마다
                yyyy = Park4139.get_time_as_('%Y')
                MM = Park4139.get_time_as_('%m')
                dd = Park4139.get_time_as_('%d')
                HH = Park4139.get_time_as_('%H')
                mm = Park4139.get_time_as_('%M')
                ss = Park4139.get_time_as_('%S')
                server_time = Park4139.get_time_as_(rf'%Y-%m-%d %H:%M:%S')
                # 한번만 mkr
                if scheduler_loop_cnt == 0:
                    Park4139.speak_today_time_info()

                    Park4139.taskkill_useless_programs()

                    Park4139.run_targets_promised()

                    if not Park4139.is_accesable_local_database(db_template=Park4139.db_template, db_abspath=Park4139.DB_TOML):
                        Park4139.speak("로컬 데이터베이스에 접근할 수 없어 접근이 가능하도록 설정했습니다")

                    Park4139.classify_targets_between_smallest_targets_biggest_targets()

                    Park4139.do_random_schedules()

                    Park4139.speak(ment='혹시 코딩을 할 계획이 계신가요?, 코딩 전 루틴은 수행하셨나요?')
                    #     물한컵
                    #     선풍기로 방환기
                    #     세수
                    #     로션
                    #     식사
                    #     물가글
                    #     양치 without tooth paste
                    #     물가글
                    #     IF 구내염:
                    #         가글양치
                    #     양치 with tooth paste
                    #     음악틀기
                    #     스트레칭 밴드 V 유지 런지 30개
                    #     계단 스쿼트 30 개
                    #     푸쉬업 30 개
                    # 응, 아니 지금할게

                # 루프 카운트 갱신
                scheduler_loop_cnt = scheduler_loop_cnt + 1
                print(f"scheduler_loop_cnt:{scheduler_loop_cnt} scheduler_time:{server_time}")

                # 분단위 스케쥴
                # 0시에서 24시 사이,
                if 0 <= int(HH) <= 24 and int(ss) == 0:
                    Park4139.monitor_target_edited_and_bkup(Park4139.PARK4139_ARCHIVE_TOML, key=Park4139.PARK4139_ARCHIVE_TOML_DATABASE_KEY)
                    if int(HH) == 6 and int(mm) == 30:
                        Park4139.speak(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다')
                        Park4139.speak(f'아침음악을 준비합니다, 아침음악을 재생할게요')
                    if int(HH) == 7 and int(mm) == 30:
                        Park4139.speak(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다')
                        Park4139.speak('지금 나가지 않는다면 지각할 수 있습니다, 더이상 나가는 것을 지체하기 어렵습니다')
                    if int(HH) == 8 and int(mm) == 50:
                        Park4139.speak(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다')
                        Park4139.speak('업무시작 10분전입니다, 업무준비를 시작하세요, 업무 전에 세수와 양치는 하셨나요')
                    if int(HH) == 9:
                        Park4139.speak(f'{int(mm)}시 정각, 루틴을 시작합니다')
                        Park4139.speak('근무시간이므로 음악을 종료합니다')
                        Park4139.taskkill('ALSong.exe')
                    if int(HH) == 11 and int(mm) == 30:
                        Park4139.speak(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다')
                        Park4139.speak('점심시간입니다, 음악을 재생합니다')
                        Park4139.speak('용량이 큰 예약된 타겟들을 빽업을 수행 시도합니다')
                        Park4139.bkup_biggest_targets()
                        Park4139.speak('용량이 작은 예약된 타겟들을 빽업을 수행 시도합니다')
                        Park4139.bkup_smallest_targets()
                        Park4139.speak('흩어져있는 storage 들을 한데 모으는 시도를 합니다')
                        Park4139.gather_storages()
                    if int(HH) == 22 and int(mm) == 10:
                        Park4139.speak(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다')
                        Park4139.speak('씻으실 것을 추천드립니다, 샤워루틴을 수행하실 것을 추천드립니다')  # 샤워루틴 확인창 띄우기.
                    if int(HH) == 22 and int(mm) == 30:
                        Park4139.speak(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다')
                        Park4139.speak('건강을 위해서 지금 씻고 주무실 것을 추천드려요')
                    if int(HH) == 24:
                        Park4139.speak(f'{int(mm)}시 정각, 루틴을 시작합니다')
                        Park4139.speak_server_hh_mm()
                    if int(mm) % 15 == 0:
                        Park4139.speak(f'{int(mm)}분 정각, 루틴을 시작합니다')
                        Park4139.speak(f'랜덤 스케줄을 시작합니다')
                        Park4139.do_random_schedules()
                    if int(mm) % 30 == 0:
                        Park4139.speak(f'{int(mm)}분 정각, 루틴을 시작합니다')
                        Park4139.speak(f'깃허브로 파이썬 아카이브 프로젝트 빽업을 시도합니다')
                        Park4139.git_push_by_auto()
                    if int(mm) % 60 == 0:
                        Park4139.speak(f'{int(mm)}시 정각, 루틴을 시작합니다')
                        Park4139.empty_recycle_bin()
                        Park4139.speak(f'쓰레기통을 비웠습니다')

                # 0시에서 4시 사이, 30초 마다
                if 0 <= int(HH) <= 4 and int(ss) % 30 == 0:
                    Park4139.make_park4139_go_to_sleep()

                # Park4139.sleep(1000)
                await asyncio.sleep(1)  # 비동기 처리된 루프 sleep() 시 , 비동기 이벤트 함수 내에서는 time.sleep() 대신 await asyncio.sleep(5)를 사용해야한다

                # 1년에 한번 수행 아이디어
                # random_schedule.json 에서 leaved_max_count를 읽어온다
                # leaved_max_count=1 이면 년에 1번 수행 하도록
                # leaved_max_count=10 이면 년에 10번 수행 하도록
                # leaved_max_count=0 이면 올해에는 더이상 수행하지 않음
                # leaved_max_count 를 random_schedule_tb.toml 에 저장

                # - 1시간 뒤 시스템 종료 예약 기능
                # - 즉시 시스템 종료 시도 기능
                # - 시간 시현기능 기능(autugui 이용)
                #   ment ='pc 정밀검사를 한번 수행해주세요'
                #   commentize(ment)
                # - 하드코딩된 스케줄 작업 수행 기능
                # - 미세먼지 웹스크래핑 기능
                # - 초미세먼지 웹스크래핑 기능
                # - 종합날씨 웹스크래핑 기능
                # - 습도 웹스크래핑 기능
                # - 체감온도 웹스크래핑 기능
                # - 현재온도 웹스크래핑 기능
                # - 음악재생 기능
                # - 영상재생 기능

        # 비동기 이벤트 루프 설정
        def run_loop_of_run_scheduler():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(run_scheduler())

        # 비동기 이벤트 루프 실행할 쓰레드 설정
        thread_for_run_scheduler = threading.Thread(target=run_loop_of_run_scheduler)
        thread_for_run_scheduler.start()

    def bring_this_window(self):
        # self.activateWindow() 와 self.show() 의 위치는 서로 바뀌면 의도된대로 동작을 하지 않는다
        self.show()
        self.activateWindow()
        import win32gui
        active_window = win32gui.GetForegroundWindow()
        win32gui.SetForegroundWindow(active_window)




class MacroWindow(QWidget):
    def __init__(self):
        super().__init__()
        #  매크로 창 전역 변수 설정

        self.previus_pressed_keys = []
        self.display_width = Park4139.get_display_info()['width'],
        self.display_height = Park4139.get_display_info()['height'],
        # self.display_width_default = int(int(self.display_width[0]) * 0.106)
        self.display_width_default = int(int(self.display_width[0]) * 0.06)
        self.display_height_default = int(int(self.display_height[0]) * 0.2)

        # 마우스 위치, 클릭 정보, 시간 정보를 저장할 리스트
        # self.positions = []

        # 녹화 시작 시간
        self.time_recording_start = time.time()
        # self.time_recording_start_rel = 0.0
        self.elapsed_full_recording_time = 0.0
        self.previous_time = time.time()
        self.time_recording_end = 0.0
        #  메인창 설정
        self.setWindowTitle('.')
        self.setWindowIcon(QIcon(Park4139.ICON_PNG))  # 메인창 아이콘 설정
        # self.setAttribute(Qt.WA_TranslucentBackground) # 메인창 블러 설정
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # 메인창 최상단 프레임레스 설정
        GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 최대화 최소화 버튼 숨기기
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.scale = 1 / 10
        self.windows_size_mode = 0  # 창크기 모드 설정  #0 ~ 3
        self.rotate_window_size_mode()

        # label 설정
        self.label = QLabel(self)
        self.label.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.label.setText(f"녹화 중...\n녹화경과시간: None\n")

        # 단축키 설정
        self.available_shortcut_list = {
            'MACRO EXCUTE': 'Ctrl+E',
            'MACRO EXIT': 'Ctrl+Q',
        }
        # self.set_shortcut('MACRO RECORD',self.record_macro)
        self.set_shortcut('MACRO EXCUTE', self.excute_macro)
        self.set_shortcut('MACRO EXIT', self.exit_macro)

        # 버튼 설정
        btn_to_excute_macro = self.get_btn(self.get_btn_name_with_shortcut_name('MACRO EXCUTE'), self.excute_macro)
        btn_to_exit_macro = self.get_btn(self.get_btn_name_with_shortcut_name('MACRO EXIT'), self.exit_macro)

        # GRID SETTING
        grid = QtWidgets.QGridLayout(self)
        btns = [
            self.label,
            btn_to_excute_macro,
            btn_to_exit_macro
        ]
        cnt = 0
        for i in btns:
            grid.addWidget(i, cnt, 0)
            cnt = cnt + 1

        # 레이아웃 설정
        layout = QGridLayout(self)
        layout.addLayout(grid, 0, 0)

        # 단일 단축키가 같이 눌리는 문제 ( ctrl + v 를 누르면   ctrl + v 에 바인딩된 함수만 호출되길 기대하는데, ctrl 에 바인딩된 함수도 호출되는 문제 )
        # 이벤트를 나누어 만들어 하나의 이벤트가 호출되면 다른 하나의 이벤트는 호출되지 않도록 설정 시도
        self.is_processing_event = False

        # Condition 객체 생성
        # self.condition = threading.Condition()

        # 이벤트 우선순위 설정
        # self.is_event_shortcut_3_processing = False # highest priority
        # self.is_event_shortcut_1_processing = False

        # 마우스 이동 이벤트 핸들러 설정
        listener = pynput.mouse.Listener(on_move=self.on_mouse_move)
        listener.start()

        # 마우스 버튼 클릭 이벤트 핸들러 설정
        listener2 = pynput.mouse.Listener(on_click=self.on_mouse_btn_clicked)
        listener2.start()

        # 키보드 이벤트 핸들러 설정 ( 3개 조합 단축키 , 2개 조합 단축키 , 단일 단축키 모두가능)
        self.keyboard_main_listener = pynput.keyboard.Listener(on_press=self.on_keys_down, on_release=self.on_keys_up)
        self.keyboard_main_listener.start()
        # 충돌이 문제가 아니고 두 이벤트가 중복이 되면 안되고 이벤트에 우선순위를 더 두어서 두 이벤트 호출 시 우선순위가 높은 이벤트만 실행되도록

        # self.is_processing_event = False

        # 이벤트 핸들러 스레드 생성
        # event1_thread = threading.Thread(target=self.listener3)
        # event2_thread = threading.Thread(target=self.listner_2_combination_shorcuts)

        # 이벤트 핸들러 스레드 시작
        # event1_thread.start()
        # event2_thread.start()

        # 키보드 이벤트 핸들러 설정 ( 단일 단축키 )
        # self.listener3 = pynput.keyboard.Listener(on_press=self.on_keboard_press, suppress=True)
        # self.listener3.start()

        # 모니터링 이벤트 설정
        # self.mouse_positions = []
        # self.previous_position = None
        # self.current_position = None
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.on_left_mouse_btn_clicked)
        # self.timer.start(900)

        # 녹화 경과시간 업데이트
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.update_label)
        self.timer2.start(1000)

        Park4139.speak(ment="매크로녹화를 시작합니다")

        # 매크로녹화시작 로깅
        log_title = "매크로녹화시작"
        contents = f"{Park4139.line_length_promised}{Park4139.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title}"
        Park4139.debug_as_cli(contents)
        self.save_macro_log(contents=contents)

        self.bring_this_window()

        # event_loop = QEventLoop()
        # event_loop.exec()

    def on_mouse_move(self, x, y):  # 아주 빠르게 감지
        # 이방식으로 매크로 중지를 할까?
        # print(f"마우스 이동 - X: {x}, Y: {y}")
        # print("마우스가 움직였습니다")
        # 상단 네비게이션
        if 0 <= x <= 3440 and 0 <= y <= 25:
            self.rotate_window_size_mode()
        else:
            pass

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseMove:
            x = event.globalX()
            y = event.globalY()
            print(f"pyside6 창 외부 마우스 이동 감지 시도 - X: {x}, Y: {y}")
        return super().eventFilter(obj, event)

        # if event.type() == QEvent.MouseButtonPress and not self.rect().contains(event.pos()):
        #     print("pyside6 창 외부 클릭 되었습니다")
        # return super().eventFilter(obj, event)

    def get_btn_name_with_shortcut_name(self, button_name_without_shortcut):
        numbers = []
        for key, value in self.available_shortcut_list.items():
            numbers.append(len(value) + len(key))
        max_len_value = max(numbers)
        # print(max_len_value)

        button_name_with_short_cut = ""
        for key, value in self.available_shortcut_list.items():
            # print(key == button_name_without_shortcut)
            # print(key)
            # print(button_name_without_shortcut)

            if key == button_name_without_shortcut:
                space_between = " " * (max_len_value - len(key) - len(value) + 1)
                # space_between = " "
                # space_between = str(max_len_value - len(key) - len(value) + 1)
                # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}\n"
                button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}".strip()
        print(button_name_with_short_cut)
        return button_name_with_short_cut

    def rotate_window_size_mode(self):
        if self.windows_size_mode == 0:
            self.bring_this_window()
            self.setGeometry(0, 0, int(self.display_width_default / 2), int(self.display_height[0] / 5))
            self.move_window_to_center()
            self.windows_size_mode = self.windows_size_mode + 1
        elif self.windows_size_mode == 1:
            self.showMinimized()
            self.windows_size_mode = 0

    def set_shortcut(self, btn_name_promised, function):
        self.shortcut = QShortcut(self.available_shortcut_list[btn_name_promised], self)  # ctrl+n+d 3개 키들의 조합 설정 시도
        self.shortcut.activated.connect(function)
        pass

    def get_btn(self, btn_name, function):
        button = QPushButton(btn_name, self)
        button.clicked.connect(function)

        # 폰트 설정
        button.setFont(Park4139.get_font_for_pyside6(font_path=pkg_park4139.FONTS.RUBIKDOODLESHADOW_REGULAR_TTF))  # 입체감있는 귀여운 영어 폰트
        button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px ; font-size: 10px}")
        # button.setLayoutDirection(QtCore.Qt.)
        return button

    def move_window_to_center(self):
        center = QScreen.availableGeometry(app.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def excute_macro(self):
        pass

    def exit_macro(self):
        # 매크로녹화종료 로깅
        log_title = "매크로녹화종료"
        self.time_recording_end = self.elapsed_full_recording_time
        contents = f"{Park4139.line_length_promised}{Park4139.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title}"
        Park4139.debug_as_cli(contents)
        self.save_macro_log(contents=contents)

        # 매크로 로그 확인
        Park4139.speak(ment="저장된 매크로 로그를 확인합니다")
        Park4139.explorer(Park4139.MACRO_LOG)

    # @Slot() # 최신 버전의 PySide6에서는 @Slot() 데코레이터를 사용하지 않고도 Slot 메서드를 정의할 수 있습니다. 이렇게 되면 자동으로 Slot으로 인식됩니다. 즉 최신버전 pyside6 에서는 쓸 필요 없다.
    def update_label(self):
        try:
            self.elapsed_full_recording_time = int(time.time() - self.time_recording_start)
            self.label.setText(f"녹화 중...\n녹화경과시간: {self.elapsed_full_recording_time} secs \n")
        except:
            traceback.print_exc(file=sys.stdout)

    def on_mouse_btn_clicked(self, x, y, button, pressed):

        # 현재 시간과 녹화 시작 시간의 차이 계산
        current_time = time.time()
        elapsed_time = int((current_time - self.previous_time) * 1000)
        # print(f"current_time : {current_time}")
        # print(f"self.previous_time : {self.previous_time}")

        # x, y = pyautogui.position() # parameter 에서 오는 값과 동일하므로 대안으로 남겨둠.

        if button == pynput.mouse.Button.left and pressed:
            info = f"  Park4139.sleep({elapsed_time})   %%%FOO%%%    Park4139.click_mouse_left_btn(abs_x={x},abs_y={y}) "
            Park4139.debug_as_cli(info)
            self.save_macro_log(contents=f"{Park4139.get_time_as_('%Y-%m-%d_%H:%M:%S')} {info}")
        elif button == pynput.mouse.Button.right and pressed:
            info = f"  Park4139.sleep({elapsed_time})   %%%FOO%%%    Park4139.click_mouse_right_btn(abs_x={x},abs_y={y}) "
            Park4139.debug_as_cli(info)
            self.save_macro_log(contents=f"{Park4139.get_time_as_('%Y-%m-%d_%H:%M:%S')} {info}")

        # 현재시간을 이전시간에 저장
        self.previous_time = current_time

    def save_macro_log(self, contents: str):
        macro_log = Park4139.MACRO_LOG
        Park4139.make_leaf_file(Park4139.MACRO_LOG)
        with open(macro_log, "a", encoding="utf-8") as f:
            f.write(f"{contents}\n")

    def on_keboard_press(self, key):
        # global is_processing_event
        # if self.is_processing_event != False:
        print(f'키보드 입력: {key}')

        # isinstance()
        # all(list) # (iterable) 객체의 모든 요소가 참(True)인지 확인
        # all(dict) # (iterable) 객체의 모든 요소가 참(True)인지 확인
        # all(tuple) # (iterable) 객체의 모든 요소가 참(True)인지 확인

    def on_keys_down(self, key):
        # 현재 시간과 녹화 시작 시간의 차이 계산
        current_time = time.time()
        elapsed_time = int((current_time - self.previous_time) * 1000)

        # for hotkey in self.HOTKEYS:
        #     hotkey.release(self.keyboard_listener1.canonical(key))
        #     print(f"key : {key}")

        # 키이름 여러 형식으로 출력
        # try:
        #     print(key)
        #     print(key.value)
        #     print(key.value.vk)
        # except:
        #     print(key)
        #     pass

        # 키이름 전처리
        key: str = str(key)
        key: str = key.lower()
        key: str = key.replace("\'", "")
        key: str = key.replace("\"", "")
        key: str = key.replace("key.", "")
        key: str = key.replace("<25>", "한자 or ctrl_r")
        key: str = key.replace("<21>", "한영 or alt_r")
        key: str = key.replace("12", "텐키 5")  # 텐키
        key: str = key.replace("cmd", "win")
        key: str = key.replace("page", "pg")
        key: str = key.replace("down", "dn")
        if key != "num_lock":
            key: str = key.replace("_l", "")
        key: str = key.replace("_r", "")

        key: str = key.replace(" ", "")
        key: str = key.replace("<", "")
        key: str = key.replace(">", "")
        # key: str = key.replace("_", "")

        # 전처리 후 출력
        # print(str(key))

        # if key == "ctrl+alt":
        log_title = "키보드인풋"
        info = f"Park4139.sleep({elapsed_time})\nPark4139.keyDown('{key}') "
        Park4139.debug_as_cli(info)
        self.save_macro_log(contents=f"{Park4139.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

        # 현재시간을 이전시간에 저장
        self.previous_time = current_time

        # if self.store = []
        # global is_processing_event
        # if self.is_processing_event == False:
        # self.is_processing_event = True
        # self.is_processing_event = False

        # pynput.keyboard.Listener()는 다시 self.listener3.start() 할 수 없다.
        # 새로 만들어야 한다
        # if self.listener3.is_alive():
        #     self.listener3.stop()
        # else:

        # self.listener3 = pynput.keyboard.Listener(on_press=self.on_keboard_press)
        # self.listener3.start()

        # self.condition.notify()  # event1에게 동작 신호 보내기

    def on_single_key_pressed(self, key):

        # 현재 시간과 녹화 시작 시간의 차이 계산
        current_time = time.time()
        elapsed_time = int((current_time - self.previous_time) * 1000)

        # print(str(key))
        if pynput.keyboard.GlobalHotKeys.name == "<ctrl>":
            log_title = "키보드단일키인풋"
            info = f"  Park4139.sleep({elapsed_time})   %%%FOO%%%    Park4139.press({str(key)}) "
            Park4139.debug_as_cli(info)
            self.save_macro_log(contents=f"{Park4139.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

        # 현재시간을 이전시간에 저장
        self.previous_time = current_time

        # try:
        #     # alphanumeric key
        #     print('{0}'.format(key.char))
        # except AttributeError:
        #     # special key
        #     print('{0}'.format(key.char))

    def on_keys_up(self, key):
        # 현재 시간과 녹화 시작 시간의 차이 계산
        current_time = time.time()
        elapsed_time = int((current_time - self.previous_time) * 1000)

        # for hotkey in self.HOTKEYS:
        #     if hotkey
        #     hotkey.press(self.keyboard_listener1.canonical(key))
        #     print(f"key : {key}")

        # 키이름 전처리
        key: str = str(key)
        key: str = key.lower()
        key: str = key.replace("\'", "")
        key: str = key.replace("\"", "")
        key: str = key.replace("key.", "")
        key: str = key.replace("<25>", "한자 or ctrl_r")
        key: str = key.replace("<21>", "한영 or alt_r")
        key: str = key.replace("12", "텐키 5")  # 텐키
        key: str = key.replace("cmd", "win")
        key: str = key.replace("page", "pg")
        key: str = key.replace("down", "dn")
        if key != "num_lock":
            key: str = key.replace("_l", "")
        key: str = key.replace("_r", "")

        key: str = key.replace(" ", "")
        key: str = key.replace("<", "")
        key: str = key.replace(">", "")
        # key: str = key.replace("_", "")

        # 전처리 후 출력
        # print(str(key))

        log_title = "키보드릴리즈"
        info = f"Park4139.sleep({elapsed_time})\nPark4139.keyUp('{key}') "
        Park4139.debug_as_cli(info)
        self.save_macro_log(contents=f"{Park4139.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

        # 현재시간을 이전시간에 저장
        self.previous_time = current_time
        pass

    def bring_this_window(self):
        self.show()
        self.activateWindow()
        import win32gui
        active_window = win32gui.GetForegroundWindow()
        win32gui.SetForegroundWindow(active_window)


def run_console_blurred():
    # pyautogui 페일세이프 모드 설정
    # pyautogui.FAILSAFE = False
    pyautogui.FAILSAFE = True

    global app
    app = QApplication(sys.argv)
    # global 로 app을 설정 하고 싶진 않았지만 app.primaryScreen() 동작에 필요했다.
    # app.primaryScreen()의 기능에 대한 대체 방법이 있다면 global app 없애고 싶다, 공유객체로 해소가 될 것 같은데 더 쉬운 방법을 못찾았다

    # 프로그램 실행 디렉토리 사용자에게 확인
    # dialog = pkg_park4139.CustomDialogReplica(contents=f"다음의 프로젝트 디렉토리에서 자동화 프로그램이 시작됩니다\n{Park4139.PROJECT_DIRECTORY}", buttons=["실행", "실행하지 않기"], closing_timer=True)
    dialog = pkg_park4139.CustomDialog(contents=f"다음의 프로젝트 디렉토리에서 자동화 프로그램이 시작됩니다\n{Park4139.PROJECT_DIRECTORY}", buttons=["실행", "실행하지 않기"], starting_timer=True)
    dialog.exec_()
    text_of_clicked_btn = dialog.text_of_clicked_btn
    if text_of_clicked_btn == "실행":
        print(Park4139.PROJECT_DIRECTORY)
        os.chdir(Park4139.PROJECT_DIRECTORY)
    if text_of_clicked_btn == "실행하지 않기":
        sys.exit()

    # 창 간 통신 설정
    # shared_obj = SharedObject()
    # rpa_program_main_window = RpaProgramMainWindow(shared_obj=shared_obj)
    rpa_program_main_window = RpaProgramMainWindow()  # 공유객체인 shared_obj 가 사용되는 곳이 없고 불필요할 것으로 판단하여 제거
    rpa_program_main_window.setMouseTracking(True)  # pyside6 창 밖에서도 마우스 추적 가능 설정 # 마우스 움직임 이벤트 감지 허용 설정
    rpa_program_main_window.bring_this_window()

    sys.exit(app.exec_())


if __name__ == '__main__':
    try:
        while (True):
            # Park4139.speak(ment="console Blurred 프로그램을 실행합니다")
            Park4139.speak(ment="콘솔 블러 프로그램을 실행합니다")
            run_console_blurred()

            break
    except Exception as e:
        Park4139.trouble_shoot("%%%FOO%%%")
        # Park4139.pause()
