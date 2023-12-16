# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'

import inspect
from typing import Callable, TypeVar
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
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtGui import QScreen, QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QLineEdit
from BlurWindow.blurWindow import GlobalBlur

import pkg_park4139

park4139 = pkg_park4139.Park4139()

# /////////////////////////////////////////////// 로깅 설정
# logger = logging.getLogger('park4139_test_logger')
# hdlr = logging.FileHandler('park4139_logger.log')
# hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)

# /////////////////////////////////////////////// 타입 힌팅 설정
T = TypeVar('T')


#  ///////////////////////////////////////////////  공유 객체 클래스 정의
class SharedObject(QObject):
    dataChanged = Signal(str)  # 데이터 변경을 알리는 시그널

    def __init__(self):
        super().__init__()
        self._data = ""
        self.answer = ""
        self.question = ""

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

    # /////////////////////////////////////////////// SharedObject.question
    @property
    def data(self):
        return self.question

    @data.setter
    def data(self, value):
        self.question = value
        self.dataChanged.emit(self.question)


class PromptWindow(QWidget):

    # def __init__(self):
    def __init__(self, ment, buttons, default, countdown, shared_obj, function: Callable[[T or None], T or None]):
        super().__init__()

        park4139.commentize(ment)
        park4139.speak_fast(ment)  # 말하도록 설정

        self.function = function
        self.ment = str(ment.strip())
        self.buttons = buttons
        self.default = default
        self.countdown = countdown

        # /////////////////////////////////////////////// 창간 통신 설정
        self.question = None
        # 창간 통신 재시도
        self.shared_obj = shared_obj
        #

        global btn_no
        pyautogui.FAILSAFE = False

        # /////////////////////////////////////////////// 팝업창 전역 변수 설정
        self.display_width = park4139.get_display_info()['width'],
        self.display_height = park4139.get_display_info()['height'],
        self.pop_up_window_width_default = int(int(self.display_width[0]) * 0.18)
        self.pop_up_window_height_default = int(int(self.display_height[0]) * 0.09)
        # contents 의 내용이 얼마나 많은 지 보고 많으면 최대화하는 건 어떤가?

        # /////////////////////////////////////////////// 팝업창 설정
        self.setWindowTitle('.')  # 팝업창 타이틀 설정
        # self.setWindowTitle('5 초 후 이 팝업은 닫칩니다')  # schedule 여기서 걸어두면 되지 않을까?

        icon_png = rf"C:\Users\WIN10PROPC3\Desktop\services\archive_py\$cache_png\icon.PNG"
        self.setWindowIcon(QIcon(icon_png))  # 팝업창 아이콘 설정
        # self.setAttribute(Qt.WA_TranslucentBackground) # 팝업창 블러 설정
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # 팝업창 최상단 프레임레스 설정
        GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 팝업창 최대화 최소화 버튼숨기기
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)  # 팝업창 닫기 버튼 disable
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 모든 창들 중 가장 앞에 팝업창 위치하도록 설정
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")  # 팝업창 스타일시트 적용 설정
        self.resize(self.pop_up_window_width_default, self.pop_up_window_height_default)
        # self.setGeometry(0, 0, self.pop_up_window_width_default, self.pop_up_window_height_default)
        self.move_window_to_center()  # 팝업창 화면의 중심으로 이동

        # /////////////////////////////////////////////// inputbox 설정
        self.inputbox = QLineEdit(self)
        self.inputbox.setStyleSheet("color: rgba(255,255,255, 0.9);")

        self.inputbox.setText(self.default)
        self.inputbox.setFixedWidth(self.pop_up_window_width_default)
        # # self.inputbox.setStyleSheet("text-shadow: 1px 1px 7px rgba(1, 1, 1, 1);") #텍스트에 그림자 넣고 싶었는데 안된다.
        # self.inputbox.textChanged.connect(self.inputbox_changed)
        # self.inputbox.editingFinished.connect(self.inputbox_edit_finished)
        # self.inputbox.returnPressed.connect(self.inputbox_return_pressed)

        # /////////////////////////////////////////////// 단축키 설정
        self.set_shortcut1(function=self.do_positive)
        self.set_shortcut2(function=self.do_nagative)
        self.set_shortcut3(function=self.do_proper)

        # /////////////////////////////////////////////// 레이블 설정
        self.pop_up_label = QLabel(self.ment)
        if len(self.ment.split("\n")) < 10:
            self.pop_up_label.setAlignment(Qt.AlignCenter)  # 레이블 가운데 정렬
        self.pop_up_label.setStyleSheet("QLabel { color: rgba(255,255,255, 0.9); height: 70px ; width: 500px ; font-size: 10px}")

        # /////////////////////////////////////////////// 버튼 설정
        try:
            # self.btn1 = self.get_btn(btn_name=f"{buttons[0]}", function=self.do_action1)
            # self.btn2 = self.get_btn(btn_name=f"{buttons[1]}", function=self.do_action2)
            self.btn1 = self.get_btn(btn_name=f"{self.buttons[0]} (Alt+Y)", function=self.do_positive)
            self.btn2 = self.get_btn(btn_name=f"{self.buttons[1]} (Alt+N)", function=self.do_nagative)
            self.btn3 = self.get_btn(btn_name=f"{self.buttons[2]} (Alt+R)", function=self.do_proper)
        except:
            pass

        # /////////////////////////////////////////////// TEST
        # self.inputbox = QPlainTextEdit(self)
        # self.inputbox = QTextEdit(self)
        # self.ta1 = QTableWidget(self)
        # self.ta1.resize(500, 500)
        # self.ta1.setColumnCount(3)
        # self.ta1.setStyleSheet("color: rgba(255,255,255, 0.9);")
        # self.ta1.setStyleSheet("background-color: rgba(255,255,255, 0.9);")
        # table_column = ["첫번째 열", "두번째 열", "Third 열"]
        # self.ta1.setHorizontalHeaderLabels(table_column)
        #
        # # 행 2개 추가
        # self.ta1.setRowCount(2)
        #
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

        # /////////////////////////////////////////////// 레이아웃 일부 설정
        self.pop_up_answer_layout = QtWidgets.QGridLayout()
        try:
            self.pop_up_answer_layout.addWidget(self.btn1, 0, 1)
            self.pop_up_answer_layout.addWidget(self.btn2, 0, 2)
            self.pop_up_answer_layout.addWidget(self.btn3, 0, 3)
        except:
            pass

        # 레이아웃 설정
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pop_up_label)
        # layout.addWidget(self.textEdit)
        # layout.addWidget(self.btn_yes)
        layout.addWidget(self.inputbox)
        layout.addLayout(self.pop_up_answer_layout)
        self.setLayout(layout)

    def __del__(self):
        park4139.commentize("소멸자 실행")
        # return self.answer

    def move_window_to_center(self):
        center = QScreen.availableGeometry(app.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def keyPressEvent(self, e):
        # 이걸로 나온 숫자로 확인하면된다.
        # print(type(e.key()))
        # print(e.key())
        if e.key() == 16777220:  # enter
            park4139.press("space")

    def set_shortcut1(self, function):
        self.shortcut = QShortcut(QKeySequence("alt+y"), self)
        self.shortcut.activated.connect(function)

    def set_shortcut2(self, function):
        self.shortcut = QShortcut(QKeySequence("alt+n"), self)
        self.shortcut.activated.connect(function)

    def set_shortcut3(self, function):
        self.shortcut = QShortcut(QKeySequence("alt+r"), self)
        self.shortcut.activated.connect(function)

    def do_positive(self):
        try:
            park4139.commentize(f"_________________________________________________ {inspect.currentframe().f_code.co_name}")
            RpaProgramMainWindow.hide(self)
            self.hide()

            try:
                if park4139.is_void_function(self.function):
                    self.function()
                elif park4139.is_void_function(self.function)==False:
                    answer = self.inputbox.text()
                    print(fr"{type(answer)} : 사용자로부터 {answer} 입력되었습니다 ")
                    if answer != None:
                        if answer != "":
                            self.function(answer)
            except AttributeError:# app.quit() 호출 에 대한 예외처리
                # function 이 함수가 아닌경우,
                # function 이 객체의 경우 여기에 속한다
                self.function()

            # # park4139.commentize("공유 객체에 저장 예시")
            # self.shared_obj.answer = self.inputbox.text()
            # print(self.shared_obj.data)

            RpaProgramMainWindow.show(self)
            self.close()
        except:
            traceback.print_exc(file=sys.stdout)

    def do_nagative(self):
        park4139.commentize(f"_________________________________________________ {inspect.currentframe().f_code.co_name}")
        RpaProgramMainWindow.hide(self)
        self.hide()
        self.answer = self.buttons[1]
        answer = self.answer
        print(fr"{type(answer)} : 사용자로부터 {answer} 입력되었습니다 ")
        park4139.speak_fast(fr"{answer} 입력되었습니다")
        RpaProgramMainWindow.show(self)
        self.close()

    def do_proper(self):
        park4139.commentize(f"_________________________________________________ {inspect.currentframe().f_code.co_name}")
        RpaProgramMainWindow.hide(self)
        self.hide()
        self.answer = self.buttons[2]
        answer = self.answer
        print(fr"{type(answer)} : 사용자로부터 {answer} 입력되었습니다 ")
        park4139.speak(fr"{answer} 입력되었습니다")
        # park4139.speak_fast("나중에 다시 물어볼게요")
        park4139.speak_fast('나중에 다시 물을게요')
        RpaProgramMainWindow.show(self)
        self.close()

    @staticmethod
    def app_method_decorator(app_method):
        def wrapper(self):
            self.hide()  # 비동기 전까지는 사용자가 다른 명령을 하지 못하도록 이 코드를 사용
            app_method(self)
            # window_main.activateWindow()
            self.show()
            pass

        return wrapper

    def inputbox_changed(self):
        park4139.commentize("inputbox 텍스트 change event 감지 되었습니다")
        print(self.inputbox.text())

    def inputbox_edit_finished(self):
        park4139.commentize("inputbox edit finish event 감지 되었습니다")

    def inputbox_return_pressed(self):
        park4139.commentize("inputbox return pressed event 감지 되었습니다")

    def get_btn(self, btn_name, function):
        button = QPushButton(btn_name, self)
        button.clicked.connect(function)  # 버튼 함수 설정
        font = QtGui.QFont("Consolas")
        button.setFont(font)  # 버튼 폰트 설정
        font.setFixedPitch(True)  # 고정폭 폰트 설정
        # button.setStyleSheet("QLabel { text-align: left; color: rgba(255,255,255, 0.9); height: 20px ; font-size: 10px}")
        button.setStyleSheet("QPushButton { text-align: center; color: rgba(255,255,255, 0.9); height: 20px ; font-size: 10px}")
        return button


class RpaProgramMainWindow(QWidget):
    # def __init__(self ): # 공유객체를 적용하기 전 코드
    # shared_obj 는 창간 통신용 공유객체 이다
    def __init__(self, shared_obj):
        super().__init__()

        ment = "자동화 프로그램을 실행 시도합니다"
        park4139.speak_fast(ment)
        pyautogui.FAILSAFE = False

        # /////////////////////////////////////////////// 창간 통신 설정
        self.prompt_window = None
        self.question = None
        # 창간 통신 재시도
        self.shared_obj = shared_obj
        #

        # /////////////////////////////////////////////// 앱 전역 변수 설정
        self.text = "text"
        self.pw = "`"
        self.id = "`"
        # self.is_window_maximized = False
        self.display_width = park4139.get_display_info()['width'],
        self.display_height = park4139.get_display_info()['height'],
        # self.display_width_default = int(int(self.display_width[0]) * 0.106)
        self.display_width_default = int(int(self.display_width[0]) * 0.06)
        self.display_height_default = int(int(self.display_height[0]) * 0.2)

        # /////////////////////////////////////////////// 메인창 설정
        self.setWindowTitle('.')
        icon_png = rf"C:\Users\WIN10PROPC3\Desktop\services\archive_py\$cache_png\icon.PNG"
        self.setWindowIcon(QIcon(icon_png))  # 메인창 아이콘 설정
        # self.setAttribute(Qt.WA_TranslucentBackground) # 메인창 블러 설정
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # 메인창 최상단 프레임레스 설정
        GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 최대화 최소화 버튼 숨기기
        # self.setWindowFlags(Qt.WindowStaysOnTopHint) # 모든 창 앞에 위치하도록 설정
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
        # self.move_window_to_center() # 화면의 중심으로 창 이동
        # self.setGeometry(0, 0, int(self.display_width_default * self.scale), int(self.display_height[0]))
        self.windows_size_mode = 0  # 창크기 모드 설정  #0 ~ 3
        self.rotate_window_size_mode()

        # mkr /////////////////////////////////////////////// inputbox 설정
        # self.inputbox = QLineEdit(self)
        # self.inputbox.setStyleSheet("color: rgba(255,255,255, 0.9);")
        # self.inputbox.setText("0,0")
        # self.inputbox.setFixedWidth(120)
        # # self.inputbox.setStyleSheet("text-shadow: 1px 1px 7px rgba(1, 1, 1, 1);") #텍스트에 그림자 넣고 싶었는데 안된다.
        # self.inputbox.textChanged.connect(self.inputbox_changed)
        # self.inputbox.editingFinished.connect(self.inputbox_edit_finished)
        # self.inputbox.returnPressed.connect(self.inputbox_return_pressed)

        # mkr /////////////////////////////////////////////// LABEL 설정
        # self.label10 = QLabel("event monitor:\n")
        # self.label10.setStyleSheet("color: rgba(255,255,255, 0.9);")
        #
        # self.label11 = QLabel("mouse event monitor:\n")
        # self.label11.setStyleSheet("color: rgba(255,255,255, 0.9);")

        # mkr /////////////////////////////////////////////// 단축키 설정
        self.available_shortcut_list = {
            # /////////////////////////////////////////////// Ctrl 단축키 설정(서비스 제어 관련)
            'ASK AI QUESTION': 'Ctrl+A',
            'BACK UP TARGET': 'Ctrl+S',
            'SCREENSHOT FULL': 'Ctrl+F',
            'SCREENSHOT CUSTOM': 'Ctrl+C',
            'COLLECT IMG FOR RPA': 'Ctrl+4',
            # '': 'Ctrl+F4', # 스스로 종료되도록 이대로 남겨 두는 것도 좋겠다. 일반적인 단축키이니까
            'ANI': 'Ctrl+5',
            # 'rdp-82106': 'Ctrl+R',
            'DOWNLOAD YOUTUBE(webm)': 'Ctrl+Y',
            # 'DOWNLOAD YOUTUBE(webm)_': 'Ctrl+Alt+Y',
            # 'DOWNLOAD YOUTUBE(wav)': 'Ctrl+S',
            # 'DOWNLOAD YOUTUBE(webm) ONLY SOUND': 'Ctrl+Alt+S',
            'WEATHER': 'Ctrl+W',
            # 'NO PASTE MEMO': 'Ctrl+M',
            'ENG TO KOR': 'Ctrl+K',
            'KOR TO ENG': 'Ctrl+E',
            # 'TEST 1': 'Ctrl+1',
            # 'TEST 2': 'Ctrl+2',

            # /////////////////////////////////////////////// Alt 단축키 설정(시스템 제어 관련)
            # 'KEYMAP': 'Alt+F1',
            'TOOGLE WINDOW SIZE': 'Alt+W',
            'SYSTEM REBOOT': 'Alt+9',
            'SYSTEM SHUTDOWN': 'Alt+]',
            'SYSTEM POWER SAVING MODE': 'Alt+[',
            # 'LOGIN': 'Alt+F7',
            'EXIT': 'Alt+Q',
            # 'HIDE': 'Alt+H',
            # 'PROJECT DIRECTORY': 'Alt+P',
            'EMPTY RECYCLE BIN': 'Alt+E',
            # 'RUN CMD.EXE AS ADMIN': 'Alt+C',
            'RECORD MACRO': 'Alt+M',
        }
        # self.set_shortcut('RUN CMD.EXE AS ADMIN', self.run_cmd_exe)
        # self.set_shortcut('DOWNLOAD YOUTUBE(wav)', self.download_youtube_as_wav)
        # self.set_shortcut('DOWNLOAD YOUTUBE(webm) ONLY SOUND', self.download_youtube_as_webm_only_sound)
        # self.set_shortcut('DOWNLOAD YOUTUBE(webm)_', self.download_youtube_as_webm_alt)
        # self.set_shortcut('HIDE', self.hide_windows_of_this_app)
        # self.set_shortcut('LOGIN', self.login)
        # self.set_shortcut('NO PASTE MEMO', self.run_no_paste_memo)
        # self.set_shortcut('PROJECT DIRECTORY', self.open_project_directory)
        # self.set_shortcut('rdp-82106', self.connect_to_another_computer_as_rdp1)
        # self.set_shortcut('TEST 1', self.test1)
        # self.set_shortcut('TEST 2', self.test2)
        self.set_shortcut('ASK AI QUESTION', self.ask_something_to_ai_via_web)
        self.set_shortcut('BACK UP TARGET', self.back_up_target)
        self.set_shortcut('COLLECT IMG FOR RPA', self.collect_imgs_for_rpa_setting)
        self.set_shortcut('DOWNLOAD YOUTUBE(webm)', self.should_i_download_youtube_as_webm)
        self.set_shortcut('EMPTY RECYCLE BIN', self.should_i_empty_trash_can)
        self.set_shortcut('ENG TO KOR', self.should_i_translate_eng_to_kor)
        self.set_shortcut('KOR TO ENG', self.translate_kor_to_eng)
        self.set_shortcut('EXIT', self.should_i_exit_this_program)
        self.set_shortcut('SYSTEM POWER SAVING MODE', self.should_i_enter_to_power_saving_mode)

        self.set_shortcut('SYSTEM REBOOT', self.reboot_this_computer)
        self.set_shortcut('SCREENSHOT CUSTOM', self.make_screenshot_custom)
        self.set_shortcut('SCREENSHOT FULL', self.make_screenshot_full)
        self.set_shortcut('SYSTEM SHUTDOWN', self.shutdown_this_computer)
        self.set_shortcut('TOOGLE WINDOW SIZE', self.rotate_window_size_mode)
        self.set_shortcut('WEATHER', self.show_weather_from_web)
        self.set_shortcut('ANI', self.show_animation_data_from_web)
        # self.set_shortcut('RECORD MACRO', self.record_macro)

        # mkr /////////////////////////////////////////////// 버튼 설정
        # btn_to_show_weather_from_web = self.get_btn(self.get_button_name_with_shortcut('WEATHER'), self.show_weather_from_web)
        # btn_to_run_no_paste_memo = self.get_btn(self.get_button_name_with_shortcut('NO PASTE MEMO'), self.run_no_paste_memo)
        # btn_to_login = self.get_btn(self.get_button_name_with_shortcut('LOGIN'), self.login)
        # btn_to_show_animation_data_from_web = self.get_btn(self.get_button_name_with_shortcut('ANI'), self.show_animation_data_from_web)
        # btn_to_quit_rpa_program = self.get_btn(self.get_button_name_with_shortcut('EXIT'), self.quit_rpa_program)
        # btn_to_download_youtube_as_wav = self.get_btn(self.get_button_name_with_shortcut('DOWNLOAD YOUTUBE(wav)'), self.download_youtube_as_wav)
        # btn_to_download_youtube_as_webm = self.get_btn(self.get_button_name_with_shortcut('DOWNLOAD YOUTUBE(webm)'), self.download_youtube_as_webm)
        # btn_to_download_youtube_as_webm_alt = self.get_btn(self.get_button_name_with_shortcut('DOWNLOAD YOUTUBE(webm)_'), self.download_youtube_as_webm_alt)
        # btn_to_download_youtube_as_webm_only_sound = self.get_btn(self.get_button_name_with_shortcut('DOWNLOAD YOUTUBE(webm) ONLY SOUND'), self.download_youtube_as_webm_only_sound)
        # btn_to_collect_imgs_for_rpa_setting = self.get_btn(self.get_button_name_with_shortcut('COLLECT IMG FOR RPA'), self.collect_imgs_for_rpa_setting)
        # btn_to_hide_windows_of_this_app = self.get_btn(self.get_button_name_with_shortcut('HIDE'), self.hide_windows_of_this_app)
        # btn_to_toogle_window_size_max_or_min = self.get_btn(self.get_button_name_with_shortcut('TOOGLE WINDOW SIZE'), self.rotate_window_size_mode)
        # btn_to_make_screenshot_custom = self.get_btn(self.get_button_name_with_shortcut('SCREENSHOT CUSTOM'), self.make_screenshot_custom)
        # btn_to_back_up_target = self.get_btn(self.get_button_name_with_shortcut('BACK UP TARGET'), self.back_up_target)
        # btn_to_test1 = self.get_btn(self.get_button_name_with_shortcut('TEST 1'), self.test1)
        # btn_to_test2 = self.get_btn(self.get_button_name_with_shortcut('TEST 2'), self.test2)
        # btn_to_make_screenshot_full = self.get_btn(self.get_button_name_with_shortcut('SCREENSHOT FULL'), self.make_screenshot_full)
        # btn_to_empty_recycle_bin = self.get_btn(self.get_button_name_with_shortcut('EMPTY RECYCLE BIN'), self.empty_recycle_bin)
        # btn_to_ask_something_to_ai_via_web = self.get_btn(self.get_button_name_with_shortcut('ASK AI QUESTION'), self.ask_something_to_ai_via_web)
        # btn_to_connect_to_another_computer_as_rdp1 = self.get_btn(self.get_button_name_with_shortcut('rdp-82106'), self.connect_to_another_computer_as_rdp1)
        # btn_to_reboot_this_computer = self.get_btn(self.get_button_name_with_shortcut('SYSTEM REBOOT'), self.reboot_this_computer)
        # btn_to_shutdown_this_computer = self.get_btn(self.get_button_name_with_shortcut('SYSTEM SHUTDOWN'), self.shutdown_this_computer)
        # btn_to_open_project_directory = self.get_btn(self.get_button_name_with_shortcut('PROJECT DIRECTORY'), self.open_project_directory)
        # btn_to_enter_to_power_saving_mode = self.get_btn(self.get_button_name_with_shortcut('SYSTEM POWER SAVING MODE'), self.enter_to_power_saving_mode)

        # 버튼기능이 무의미해보여 레이블로 실험적으로 대체
        numbers = []
        for key, value in self.available_shortcut_list.items():
            numbers.append(len(value) + len(key))
        max_len_value = max(numbers)
        keymap_colum1 = ""
        keymap_colum2 = ""
        cnt = 0
        column_lines = len(self.available_shortcut_list) / 2
        for key, value in self.available_shortcut_list.items():
            if cnt <= column_lines:
                space_between = " " * (max_len_value - len(key) - len(value) + 1)
                # keymap_colum1 = keymap_colum1 + f"{key}{space_between}{value}\n"
                keymap_colum1 = keymap_colum1 + f"{key}{space_between}{value}\n\n"
            elif column_lines < cnt:
                space_between = " " * (max_len_value - len(key) - len(value) + 1)
                # keymap_colum2 = keymap_colum2 + f"{key}{space_between}{value}\n"
                keymap_colum2 = keymap_colum2 + f"{key}{space_between}{value}\n\n"
        print(keymap_colum1)
        print(keymap_colum2)
        btn_to_do_nothing1 = self.get_btn(keymap_colum1, self.do_nothing)
        btn_to_do_nothing2 = self.get_btn(keymap_colum2, self.do_nothing)

        # GRID SETTING
        grid = QtWidgets.QGridLayout(self)

        # GRID COORDINATION REFERENCE (ROW, COLUMN)
        #        0,0  0,1  0,2
        #        1,0  1,1  1,2
        #        2,0  2,1  2,2

        # COLUMN1
        # btns = [
        #     btn_to_ask_something_to_ai_via_web,
        #     btn_to_make_screenshot_custom,
        #     btn_to_make_screenshot_full,
        #     btn_to_collect_imgs_for_rpa_setting,
        #     btn_to_hide_windows_of_this_app,
        #     btn_to_login,
        #     btn_to_quit_rpa_program,
        #
        #     btn_to_show_animation_data_from_web,
        #     btn_to_show_weather_from_web,
        #     btn_to_run_no_paste_memo,
        # ]
        btns = [
            btn_to_do_nothing1
        ]
        cnt = 0
        for i in btns:
            grid.addWidget(i, cnt, 0)
            cnt = cnt + 1

        # COLUMN2
        # btns = [
        #     btn_to_download_youtube_as_wav,
        #     btn_to_download_youtube_as_webm_alt,
        #     btn_to_download_youtube_as_webm_only_sound,
        #     btn_to_download_youtube_as_webm,
        #     btn_to_connect_to_another_computer_as_rdp1,
        #     btn_to_empty_recycle_bin,
        #     btn_to_open_project_directory,
        #     btn_to_back_up_target,
        #     btn_to_reboot_this_computer,
        #     btn_to_shutdown_this_computer,
        #     btn_to_toogle_window_size_max_or_min,
        #     btn_to_enter_to_power_saving_mode,
        #     btn_to_test1,
        #     btn_to_test2,
        # ]
        btns = [
            btn_to_do_nothing2
        ]
        cnt = 0
        for i in btns:
            grid.addWidget(i, cnt, 1)
            cnt = cnt + 1

        # mkr /////////////////////////////////////////////// TEST
        # self.inputbox = QPlainTextEdit(self)
        # self.inputbox = QTextEdit(self)
        # self.ta1 = QTableWidget(self)
        # self.ta1.resize(500, 500)
        # self.ta1.setColumnCount(3)
        # self.ta1.setStyleSheet("color: rgba(255,255,255, 0.9);")
        # self.ta1.setStyleSheet("background-color: rgba(255,255,255, 0.9);")
        # table_column = ["첫번째 열", "두번째 열", "Third 열"]
        # self.ta1.setHorizontalHeaderLabels(table_column)
        #
        # # 행 2개 추가
        # self.ta1.setRowCount(2)
        #
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

        # 레이아웃 설정
        layout = QGridLayout(self)
        layout.addLayout(grid, 0, 0)
        # layout.addLayout(self.ta1, 1, 0)

    @staticmethod
    # def rpa_program_method_decorator(method):
    def rpa_program_method_decorator(method: Callable[[T], None]):
        def wrapper(self):
            self.hide()  # 비동기 전까지는 사용자가 다른 명령을 하지 못하도록 이 코드를 사용
            method(self)
            # RpaProgramMainWindow.activateWindow()
            # self.show()
            pass

        return wrapper

    # def mouseMoveEvent(self, e):
    #     self.label10.setText(f"event monitor:\nmouseMoveEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #
    # def mousePressEvent(self, e):
    #     self.label10.setText(f"event monitor:\nmousePressEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     if e.pos() == Qt.AllButtons:
    #         self.label11.setText(f"mouse event monitor:\nAllButtons : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.BackButton:
    #         self.label11.setText(f"mouse event monitor:\nBackButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton1:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton1 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton10:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton10 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton11:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton11 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton12:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton12 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton13:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton13 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton14:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton14 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton15:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton15 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton16:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton16 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton17:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton17 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton18:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton18 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton19:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton19 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton2:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton2 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton20:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton20 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton21:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton21 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton22:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton22 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton23:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton23 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton24:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton24 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton3:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton3 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton4:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton4 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton5:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton5 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton6:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton6 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton7:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton7 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton8:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton8 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ExtraButton9:
    #         self.label11.setText(f"mouse event monitor:\nExtraButton9 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.ForwardButton:
    #         self.label11.setText(f"mouse event monitor:\nForwardButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.LeftButton:
    #         self.label11.setText(f"mouse event monitor:\nLeftButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.MiddleButton:
    #         self.label11.setText(f"mouse event monitor:\nMiddleButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.NoButton:
    #         self.label11.setText(f"mouse event monitor:\nNoButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.RightButton:
    #         self.label11.setText(f"mouse event monitor:\nRightButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.TaskButton:
    #         self.label11.setText(f"mouse event monitor:\nTaskButton : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.XButton1:
    #         self.label11.setText(f"mouse event monitor:\nXButton1 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #     elif e.pos() == Qt.XButton2:
    #         self.label11.setText(f"mouse event monitor:\nXButton2 : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #
    # def mouseReleaseEvent(self, e):
    #     self.label10.setText(f"event monitor:\nmouseReleaseEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")
    #
    # def mouseDoubleClickEvent(self, e):
    #     self.label10.setText(f"event monitor:\nmouseDoubleClickEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")

    # def keyPressEvent(self, e):
    #     # these keys refered from https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html
    #     # 테스트 결과 한/영, 한자 인식안됨.
    #     if e.key() == Qt.Key_Return:
    #         self.label11.setText(f"keyboard event monitor:\nKey_Return : Key_Return ")
    #         self.showMinimized()
    #         # self.hide()
    #         park4139.press("space")
    #         # self.show()
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
        park4139.commentize("inputbox 텍스트 change event 감지 되었습니다")
        print(self.inputbox.ment())

    def inputbox_edit_finished(self):
        park4139.commentize("inputbox edit finish event 감지 되었습니다")

    def inputbox_return_pressed(self):
        park4139.commentize("inputbox return pressed event 감지 되었습니다")

    def get_button_name_with_shortcut(self, button_name_without_shortcut):
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

    # def show_available_shortcut_list(self):
    #     # global max
    #     # global 을 설정하면, 이 변수는 함수의 실행이 끝난 다음에도 없어지지 않는다.
    #     # 이 값을 나중에 함수 끝나고도 또 쓸려면 이렇게 쓰면 되겠다. @staticmethod 의 경우에는 변수 간의 값에 간섭이 되지 않도록 굳이 쓰지 않는 것이 좋겠다.
    #     # global 많이 쓰면 이는 변수가 전역화 되니까 메모리의 성능이 저하되는 것이 아닐까?
    #     # 그렇다면 함수 내에서만 전역적으로 변수를 쓰는 경우에, global 을 쓰지 않는 것이 성능을 위해서는 좋은 선택이겠다. 굳이 함수가 끝난 뒤에 밖에서 써야한다면 global 을 써야 겠지만, 나는 무척이나 이게 헷갈릴 것 같다
    #     # 그동안의 경험으로는 코드 맥락 상, global 선언을 하지 않아도 전역변수 처럼 작동 되는 것 같아 보인다.
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
            self.showMaximized()
            self.windows_size_mode = self.windows_size_mode + 1
        elif self.windows_size_mode == 2:
            self.setGeometry(1000, 0, int(self.display_width_default), int(self.display_height[0]))
            self.windows_size_mode = self.windows_size_mode + 1
        elif self.windows_size_mode == 3:
            self.setGeometry(1500, 0, int(self.display_width_default), int(self.display_height[0]))
            self.windows_size_mode = self.windows_size_mode + 1
        elif self.windows_size_mode == 4:
            self.setGeometry(0, 0, int(self.display_width_default * self.scale), int(self.display_height[0]))
            self.windows_size_mode = 0
        # elif self.windows_size_mode == 5:
        #     self.hide()
        #     self.windows_size_mode = self.windows_size_mode + 1
        #     self.show()
        # park4139.speak_fast("창이 최소화 되었습니다")
        # park4139.press("win", "1")

        elif self.windows_size_mode == 6:  # unreachable code
            park4139.press("win", "1")
            self.windows_size_mode = 0

    def set_shortcut(self, btn_name_promised, function):
        self.shortcut = QShortcut(QKeySequence(self.available_shortcut_list[btn_name_promised]), self)
        self.shortcut.activated.connect(function)
        pass

    def get_btn(self, btn_name, function):
        # button = QPushButton(btn_name, self)  # alt f4 로 가이드 해도 되겠다. 이건 그냥 설정 되어 있는 부분.
        button = QLabel(btn_name, self)  # 원래는 버튼이나 임시로 Label 로 변경.
        # button.clicked.connect(function)
        # button.setStyleSheet("color: rgba(255,255,255, 0.9);")
        # button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px ; font-size: 10px}")

        # 2023년 12월 14일 (목) 16:28:15
        # 결론, fixed width font로 시도해볼 수 있다 자릿 수를 맞출 수 있다.
        # non-fixed width font 이슈 JAVA 에서도 구현했을 때 마딱드렸던 내용인데,
        # 분명히 문장 전체 길이를 단어 사이의 공백의 수를 결정짓는 함수를 테스트 했음에도 자릿수가 맞지 않았는데
        # 이는 고정 폭이 아님이기 때문이었다 따라서 고정 폭 폰트로 출력되는 콘솔에서는 정상, 비고정 폭 폰트로 출력되는 콘솔에서는 비정상,
        # 이 경우에는 콘솔이 아니라 pyside6 로 만든 UI 에서 나타났다.
        # 새벽에 이 문제를 만나서 잠깐 넋나갔는데 아침에 다시보니 그때 경험이 떠올라서 실험해보니 잘 해결되었다. 덕분에 pyside6에서 위젯에 폰트 적용하는 법도 터득

        # fixed width font
        # font = QtGui.QFont("Monospace")
        # font = QtGui.QFont("Ubuntu Mono")
        # font = QtGui.QFont("Inconsolata")
        # font = QtGui.QFont("Monaco")
        # font = QtGui.QFont("Courier")
        # font = QtGui.QFont("Courier 10 Pitch")
        # font = QtGui.QFont("Courier Prime")
        # font = QtGui.QFont("Droid Sans Mono")
        # font = QtGui.QFont("Fira Mono")
        # font = QtGui.QFont("Hack")
        # font = QtGui.QFont("Menlo")
        # font = QtGui.QFont("Monofur")
        # font = QtGui.QFont("Noto Mono")
        # font = QtGui.QFont("PT Mono")
        # font = QtGui.QFont("Roboto Mono")
        # font = QtGui.QFont("Source Code Pro")
        # font = QtGui.QFont("Victor Mono")
        # font = QtGui.QFont("Courier New")
        # font = QtGui.QFont("Liberation Mono")
        # font = QtGui.QFont("DejaVu Sans Mono")
        font = QtGui.QFont("Consolas")  # 그나마 가장 마음에 드는 폰트
        font.setFixedPitch(True)
        button.setFont(font)
        button.setStyleSheet("QLabel { text-align: left; color: rgba(255,255,255, 0.9); height: 20px ; font-size: 10px}")
        # button.setLayoutDirection(QtCore.Qt.)
        return button

    def move_window_to_center(self):
        center = QScreen.availableGeometry(app.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def show_weather_from_web(self):
        park4139.annouce_service_launch()

    def run_no_paste_memo(self):
        park4139.annouce_service_launch()

    # def show_shortcuts(self):
    #     self.show_available_shortcut_list()

    def reboot_this_computer(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='시스템을 재시작할까요?', buttons=["재시작", "재시작하지 않기"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.reboot_this_computer)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    @QtCore.Slot()
    def login(self):
        park4139.annouce_service_launch()
        print(self.print_id)

    def show_animation_data_from_web(self):
        park4139.search_animation_data_from_web()

    def should_i_exit_this_program(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='앱을 종료할까요?', buttons=["종료", "종료하지 않기"], default="", countdown=0, shared_obj=self.shared_obj, function=app.quit) #function 타입힌팅을 function 만 받으려고 해서 해두었는데 app.quit 도 메소드이지 않을까 했는데 아닌가 보다, app.quit 호출 시 AttributeError 에러가 발생한다. 일단 AttributeError 예외 발생 시 동작되도록 처리를 해두었다
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None


    @rpa_program_method_decorator
    def download_youtube_as_wav(self):
        park4139.annouce_service_launch()

    def should_i_download_youtube_as_webm(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='다운로드하고 싶은 URL을 제출해주세요', buttons=["제출", "제출하지 않기"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.download_from_youtube_to_webm)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    def should_i_download_youtube_as_webm_alt(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='다운로드하고 싶은 URL을 제출해주세요.', buttons=["제출", "제출하지 않기"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.download_from_youtube_to_webm_alt)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    @rpa_program_method_decorator
    def download_youtube_as_webm_only_sound(self):
        park4139.annouce_service_launch()

    @rpa_program_method_decorator
    def collect_imgs_for_rpa_setting(self):
        park4139.get_img_for_rpa()

    @rpa_program_method_decorator
    def hide_windows_of_this_app(self):
        self.hide()

    @rpa_program_method_decorator
    def shutdown_this_computer(self):
        park4139.shutdown_this_computer()

    @rpa_program_method_decorator
    def make_screenshot_custom(self):
        park4139.get_custom_screenshot()

    @rpa_program_method_decorator
    def make_screenshot_full(self):
        park4139.get_full_screenshot()

    def back_up_target(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='백업할 타겟경로를 입력하세요', buttons=["제출하기"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.bkup)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    @rpa_program_method_decorator
    def test1(self):
        park4139.speak("test")

    @staticmethod
    def do_nothing():
        park4139.commentize("def do_nothing():")

    @rpa_program_method_decorator
    def test2(self):
        park4139.speak("test")


    def open_project_directory(self):
        park4139.get_cmd_output(f'explorer "{os.getcwd()}"')

    def should_i_enter_to_power_saving_mode(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='절전모드로 진입할까요', buttons=["진입하기", "진입하지 않기", "다시물어봐줄래"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.enter_power_saving_mode)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    def should_i_translate_eng_to_kor(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='WRITE SOMETHING YOU WANT TO TRANSLATE \n(FROM ENG TO KOREAN)', buttons=["Translate this", "Don't", "Could you ask me again"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.translate_eng_to_kor)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    def translate_kor_to_eng(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment=f'번역하고 싶은 내용을 입력하세요\n(한글에서 영어로)', buttons=["번역해줘", "번역하지 않기", "다시물어봐줄래"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.translate_kor_to_eng)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    def should_i_empty_trash_can(self):
        while True:
            if self.prompt_window is None:
                # Park4139.commentize(rf'휴지통 용량확인 pyautogui RPA')
                # ment = f'현재 휴지통이 10기가 바이트 이상입니다 쓰레기통을 비울까요' # 이건 wrapping 할 로직.
                self.prompt_window = PromptWindow(ment='쓰레기통을 비울까요', buttons=["비우기", "비우지 않기", "다시물어봐줄래"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.empty_recycle_bin)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    @rpa_program_method_decorator
    def run_cmd_exe(self):
        park4139.run_cmd_exe()

    def ask_something_to_ai_via_web(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='AI 에게 할 질문을 입력하세요', buttons=["제출하기"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.ask_to_web)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    def connect_to_another_computer_as_rdp1(self):
        while True:
            if self.prompt_window is None:
                self.prompt_window = PromptWindow(ment='rdp1에 원격접속할까요?', buttons=["그래", "아니"], default="", countdown=0, shared_obj=self.shared_obj, function=park4139.connect_remote_rdp1)
                self.prompt_window.show()
                self.showMinimized()
                break
            else:
                self.prompt_window = None

    @QtCore.Slot()
    def print_id(self):
        print(self.id)


def run_console_blurred():
    global app
    # global 로 app을 설정 하고 싶진 않았지만 app.primaryScreen(), app.quit() 동작에 필요했다.
    # 두 메소드에 대한 대체 방법이 있다면 global 없애고 싶다
    # if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 창 간 통신 설정
    shared_obj = SharedObject()

    rpa_program_main_window = RpaProgramMainWindow(shared_obj=shared_obj)
    rpa_program_main_window.show()

    rpa_program_main_window.activateWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    try:
        while (True):
            # pyautogui 는 라이브러리 레벨 같고, pyside6 는 framework 레벨 같았다.
            run_console_blurred()
    except Exception as e:
        print(str(e))
        park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        park4139.pause()
