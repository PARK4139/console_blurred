# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'

import os.path

# PEP8
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


if __name__ == '__main__':
    try:
        while (True):
            Park4139.speak(ment="console Blurred 프로그램을 실행합니다")
            # Park4139.speak(ment="콘솔 블러 프로그램을 실행합니다")
            Park4139.run_console_blurred()

            break
    except Exception as e:
        Park4139.trouble_shoot("%%%FOO%%%")
