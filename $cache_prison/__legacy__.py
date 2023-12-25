# -*- coding: utf-8 -*-
import keyboard
# from random import randint, random
# from SpeechRecognition import speech_recognition as sr
# import pyttsx3
from BlurWindow.blurWindow import blur
from bs4 import BeautifulSoup as bs
from datetime import datetime
from datetime import timedelta
from gtts import gTTS
from moviepy.editor import *
from mutagen.mp3 import MP3
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from pytube import Playlist, YouTube
from screeninfo import get_monitors
from selenium import webdriver
from sys import argv
from urllib.parse import unquote
import clipboard
import googletrans
import json
import os
import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
import pyautogui
import pyperclip
import pyttsx3
import random
import re
import requests
import shutil
import signal
import subprocess
import sys
import time
import traceback
import win32api
from PySide6.QtCore import Qt
from datetime import timedelta
from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QStatusBar,
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

from pkg_park4139 import Park4139




def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(key))


def on_release(key):
    print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# 파일 모든 사용권한 얻기 시도
# os.chmod(target_adspath, 0o777)
# os.chmod(target_adspath, 777)
# os.chmod(target_adspath, 777)


# :: 현재 디렉토리 파일만 사이즈 출력 2
def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return r"%s %s" % (s, size_name[i])


def tasklist():
    for proc in psutil.process_iter():
        try:
            process_im_name = proc.name()
            processID = proc.pid
            print(process_im_name, ' - ', processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
            pass


def startRecordCommand(file_abspath):
    # sys.stdout = open('py cmd recording.txt', 'a', encoding='utf-8')  #
    # sys.stdout = open('py cmd recording.txt', 'w', encoding='utf-8')  #
    # sys.stdout = open('py cmd recording.txt', 'r', encoding='utf-8')  #
    sys.stdout = open(file_abspath, 'w', encoding='utf-8')  # WITH OVERWRITE


def endRecordCommand():
    sys.stdout.close()


def saveFileAs(file_abspath):
    startRecordCommand(file_abspath)
    print("이것은 param 두개가 더 필요해 보입니다.")
    endRecordCommand()


def readFile(file_abspath):
    with open(file_abspath, 'r', encoding='utf-8') as f:
        readed_text = f.read()
    return readed_text


# # 'voiceless mode':
# # 'voice mode':


# '식물조언':
# print('식물에게 물샤워를 줄시간입니다')
# print('물샤워를 시켜주세요')
# print('오늘은 식물에게 햇빛샤워를 시켜주는날입니다')
# print('하늘이가 없을때 샤워를 시켜주세요')
# print('하트축전에게 빠르게 식물등빛을 주세요')
# print('이러다 죽습니다')
# print('서둘러 등빛을 주세요')


def open_url_as_web_browser(target_url: str):
    last_txt = target_url.split('.')[-1]
    if 'http:' in target_url:
        if '%' in target_url:
            target_url = f'explorer "{unquote(target_url).strip()}"'  # url decoding
            os.system(target_url)
        else:
            os.system('start ' + target_url)


def open_target_as_start_command(target_abspath: str):
    if os.path.splitext(target_abspath) == '':  # 디렉토리
        os.system(f'start {target_abspath}')
    elif os.path.splitext(target_abspath) == 'txt':  # 텍스트 파일
        # if os.path.splitext(target_abspath)=='.txt':
        os.system(f'start {target_abspath}')
        # os.startfile(os.getcwd()+'/mp3/'+ text +'.mp3') #비동기처리방식
    # mp3, mp4


def replace_text_B_and_text_C_interchangeably_at_text_A_by_using_(____text_A, ____text_B, ____text_C, _____and):
    foo_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
    text_special = "{{no}}"
    text_B_cnt = ____text_A.count(____text_B)
    foo_list = []
    foo_str = ""
    foo_cmt = 0
    if ____text_C == "":
        ____text_A = ____text_A.replace(____text_B, ____text_C)
    elif text_special in ____text_C:
        print("text_A 에서 " + ____text_B + " 를 총" + str(text_B_cnt) + "개 발견하였습니다")
        foo_list = ____text_A.split(____text_B)
        if ____text_B in ____text_C:
            foo_cmt = 0
            for j in foo_list:
                if j == foo_list[-1]:
                    pass
                else:
                    foo_str = foo_str + j + ____text_C.split(text_special)[0] + str(foo_cmt)
                foo_cmt = foo_cmt + 1
            ____text_A = ""
            ____text_A = foo_str
        else:
            foo_cmt = 0
            for j in foo_list:
                if j == foo_list[-1]:
                    pass
                else:
                    foo_str = foo_str + j + ____text_C.split(text_special)[0] + str(foo_cmt)
                foo_cmt = foo_cmt + 1
            ____text_A = ""
            ____text_A = foo_str
    else:
        ____text_A = ____text_A.replace(____text_C, foo_foo)
        ____text_A = ____text_A.replace(____text_B, ____text_C)
        ____text_A = ____text_A.replace(foo_foo, ____text_B)


def act_via_interchangeable_triangle_model_by_using_(____text_A, ____text_B, ____text_C, _____and):
    foo_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
    if ____text_C == "":
        ____text_A = ____text_A.replace(____text_B, ____text_C)
    else:
        ____text_A = ____text_A.replace(____text_C, foo_foo)
        ____text_A = ____text_A.replace(____text_B, ____text_C)
        ____text_A = ____text_A.replace(foo_foo, ____text_B)


def get_weekday():
    now = time
    localtime = now.localtime()
    weekday = str(localtime.tm_wday)
    return weekday


def get_type(__________):
    if type(__________) == 'None':
        print(None)
    elif type(__________) == 'str':
        print('String')
    else:
        print(__________)


def get_elapsedDaysFromJan01():
    now = time
    localtime = now.localtime()
    elapsedDaysFromJan01 = str(localtime.tm_yday)
    return elapsedDaysFromJan01


print("__________________________________________________________  JSON  ")
data = {
    'ID_REQUEST': 1,
    'CUSTOMER_NAME': '_박_정_훈_',
    'MASSAGE_REQUESTED': '주문서변경요청',
    'DATE_REQUESTED': Park4139.get_time_as_('%Y-%m-%d %H:%M:%S'),
    'USE_YN': "Y",
    'MARVEL CHARACTERS': [
        {'MACHANICAL MEMBER1': ['IRONMAN', 'BLACK PANTHER']},
        {'MITHICAL MEMBER1': ['ROKI', 'THOR PANTHER']},
    ]
}
print(type(data))
print(data)

# json 파일에 data 저장
json_file_path = "./json/__________.json"
with open(json_file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)

data = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'  # data_as_str
data = json.loads(data)  # data_as_tuple

print(json.dumps(data, indent=4, sort_keys=True))
print(data['name'])
print(data['id'])
for depth_level1 in data['history']:
    print(depth_level1['date'], depth_level1['item'])

print("__________________________________________________________  yaml")
import yaml  # pip install PyYAML

with open('__________.yaml') as f:
    conf = yaml.load(f)
__________1 = conf['language']
__________2 = conf['pytest']
print(__________1)
print(__________2)

print("__________________________________________________________ doctest")
import doctest


def ipconfig():
    """
        _____________________________________________________________________
        author      : jung hoon park
        This function works like " c:\> ipconfig"
        we can try like this, if you want to more info.   c:\> python _________.py -v
        _____________________________________________________________________
        >>> ipconfig()
        ???
    """
    return os.system('ipconfig')


doctest.testmod()

print("__________________________________________________________ pytest")
print("__________________________________________________________ data test")
print("데이터의 흐름 변화 그 안에서 마주하게된 정렬에 대한 필요성")

# python 3.6 f-sting
# python f 문자열 포매팅 #f string formatting
number = 3
Park4139.debug_as_cli(f'number = {number}')
# f - sting alignment
Park4139.debug_as_cli(f'{"test":_^22}')  # '_______test_______'
Park4139.debug_as_cli(f'{"test":_<22}')  # 'test______________'
Park4139.debug_as_cli(f'{"test":_>22}')  # '______________test'
Park4139.debug_as_cli(f'{{중괄호 사용법}}')  # {중괄호 사용법}

print("__________________________________________________________ dict sort test")
# 파이썬 3.6 이후는 자동정렬되어 OrderedDict 사용필요 없음
# 파이썬 3.6 이하 버전용 코드
from collections import OrderedDict

od = OrderedDict()
od['a'] = 'app'
od['b'] = 'bow'
od['c'] = 'cow'
print(od)
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
vals = ['app', 'bow', 'cow', 'doc', 'err', 'fly', 'gpu']
od = OrderedDict((key, val) for key, val in zip(keys, vals))
print(od)

# :: get 현재 pc에 연결된 드라이브
connected_drives = []
for drive_letter in string.ascii_uppercase:
    drive_path = drive_letter + ":\\"
    if os.path.exists(drive_path):
        connected_drives.append(drive_path)
current_directory = os.getcwd()
print(f"현재 pc에 연결된 드라이브 : {connected_drives}")
print(f"현재 디렉토리 위치 : {current_directory}")

# :: get 현재 디렉토리 파일의 Modified/Created/Accessed 일자
current_files = subprocess.check_output('dir /b /o /a-d', shell=True).decode('utf-8')  # 파일만
lines = current_files.split("\n")
for line in lines:
    print("Modified : " + time.ctime(os.path.getmtime(line)))
    print("Created : " + time.ctime(os.path.getctime(line)))
    print("Accessed : " + time.ctime(os.path.getatime(line)))

# :: get 현재 디렉토리 파일의 일자
Park4139.commentize(" 생성된지 7일 된 모든 확장자 파일 출력")
# os.system('forfiles /P os.getcwd() /S /M *.* /D -7 /C "cmd /c @echo @path" ')

Park4139.commentize(" 생성된지 1일 된 zip 확장자의 빽업 파일 삭제")
# os.system('forfiles /P os.getcwd() /S /M *.zip /D -1 /C "cmd /c del @file" ')  # 2003 년 이후 설치 된 PC !주의! forfiles의 옵션이 달라서 큰 사이드 이펙트 일으킬 수 있음.

foo = subprocess.check_output('dir /b /s /o /ad', shell=True).decode('utf-8')  # 폴더만 with walking
foo = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만 with walking
foo = subprocess.check_output('dir /b /s /o /a', shell=True).decode('utf-8')  # 전부 with walking
print(foo)

# :: 특정 디렉토리/파일 사이즈 출력 with walking
# current_files = os.popen('dir /b /s /o /a').readlines()    # 전부 with walking
# current_files = os.popen('dir /b /s /o /ad').readlines()   # 폴더만 with walking
current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만 with walking
lines = current_files.split("\n")
for line in lines:
    try:
        foo = round(os.path.getsize(line.strip()) / (1024.0 * 1024.0), 2)
        if (foo < 1):
            print(line.strip() + " : " + str(round(os.path.getsize(line.strip()) / (1024.0), 2)) + ' KB')
        elif (foo < 1024):
            print(line.strip() + " : " + str(round(os.path.getsize(line.strip()) / (1024.0 * 1024.0), 2)) + ' MB')
        else:
            print(line.strip() + " : " + str(round(os.path.getsize(line.strip()) / (1024.0 * 1024.0 * 1024.0), 2)) + ' GB')
    except Exception as e:
        pass

current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
lines = current_files.split("\n")
for line in lines:
    try:
        print(line.strip() + "{{seperator}}" + str(convert_size(os.path.getsize(line.strip()))))
    except Exception as e:
        pass

# :: 현재 디렉토리 파일생성일자 출력 with walking
current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
lines = current_files.split("\n")
for line in lines:
    try:
        # print(os.path.getmtime(line.strip()))
        # print(time.ctime(os.path.getmtime(line.strip())))
        # print(line.strip() + "{{seperator}}" + str(os.path.getctime(line.strip())))
        # print(line.strip() + "{{seperator}}" + str(datetime.datetime.fromtimestamp(os.path.getctime(line.strip())).strftime('%Y-%m-%d %H:%M:%S')))
        print(line.strip() + "{{seperator}}" + str(time.ctime(os.path.getmtime(line.strip()))))
    except Exception as e:
        pass

Park4139.commentize(" 20230414 18:00 이후 생성된 파일 출력")
inputDate = datetime.strptime(str(input('Searching Input Date : ')), '%Y%m%d %H:%M')
opening_directory = r'D:\test'
for (path, dir, files) in os.walk(opening_directory):
    for filename in files:
        fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
        if inputDate < fileMtime:
            print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' % (path, filename, fileMtime))

Park4139.commentize(" 20230414 18:00 이전 생성된 파일 출력")
inputDate = datetime.strptime(str(input('Searching Input Date : ')), '%Y%m%d %H:%M')
opening_directory = r'D:\test'
for (path, dir, files) in os.walk(opening_directory):
    for filename in files:
        fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
        if inputDate > fileMtime:
            print(r'경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' % (path, filename, fileMtime))
            print(r'[%s\%s]' % (path, filename))

Park4139.commentize(" 현재시간기준 생성된지 1일 된 zip 확장자 파일만 출력")
times = Park4139.get_time_as_('%Y-%m-%d %H:%M:%S').split(' ')
time_inputed = times[0] + times[1] + str(int(times[2]) - 1) + " " + times[3] + ":" + times[4]
print(time_inputed)
time_inputed = '20230414 20:53'
print(time_inputed)
inputDate = datetime.strptime(str(time_inputed), '%Y%m%d %H:%M')
opening_directory = opening_directory
for (path, dir, files) in os.walk(opening_directory):
    for filename in files:
        fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
        if inputDate < fileMtime:
            print('[%s\%s    modified : %s]' % (path, filename, fileMtime))
            print('[%s\%s]' % (path, filename))
            print('[%s]' % (filename))




webdriver_chrome = webdriver.Chrome()
webdriver_chrome.implicitly_wait(5)
last_scroll_height = webdriver_chrome.execute_script("return document.body.scrollHeight")  # 기존 scrollHeight를 저장
webdriver_chrome.quit()

# time.sleep(random.uniform(1, 3))  # 자동화크롤링 탐지를 우회 하기 위한 delay









# 네이버 지역 정보 option
#  '네이버 체감온도 정보'
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8'
copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'
url = unquote(url)  # url decoding
page = requests.get(url)
soup = bs(page.text, "html.parser")
copied_html_selector = '_________'
elements = soup.select(copied_html_selector)
AI_print(elements)  # 추출된 elements 출력 시도
for i in range(0, len(page.text.split('\n'))):
    if 'hourlyFcastListJson' in page.text.split('\n')[i]:
        # # hourlyFcastListJson 들어있는 줄들 출력시도 ")
        str_containing_hourlyFcastListJson = page.text.split('\n')[i].strip()
        # print(type(str_containing_hourlyFcastListJson))
        # print(str_containing_hourlyFcastListJson)
        # json_str ")
        json_str = str_containing_hourlyFcastListJson.split('=')[-1].split(';')[0].strip()
        # print(type(json_str))
        # print(json_str)
        # print(json.dumps(json_str, indent=4, sort_keys=True))
        # json_obj ")
        json_obj = json.loads(json_str)
        # print(type(json_str))
        # print(json_obj)
        # print(json.dumps(json_obj, indent=4, sort_keys=True))

# json_obj[i]['windSpd']][json obj 내부의  ")
# for i in range(0,len(json_obj)):
# print(str(i),':', str(json_obj[i]['windSpd']))


# json file 에 저장
file_path = "./json/tmp.json"

json_dict = {}
json_dict['head'] = []
json_dict['head'].append({
    "title": "Android Q, Scoped Storage",
    "url": "https://codechacha.com/ko/android-q-scoped-storage/",
    "draft": "false"
})
json_dict['body'] = []
json_dict['body'].append({
    "that i want to save": str(json_obj[40]['windSpd']),
    "that i want to save2": "foo"
    # "that i want to save": str(json.dump(json_obj[40]['windSpd']))
})
json_dict['tail'] = []
json_dict['tail'].append({
    "title": "Android Q, Scoped Storage",
    "url": "https://codechacha.com/ko/android-q-scoped-storage/",
    "draft": "false"
})
json_dict['tail'].append({
    "that i want to save str": "i",
    "that i want to save str2": "love",
    "that i want to save str2": "love"
})
print(json_dict)
print(type(json_dict))

with open(file_path, 'w') as outfile:
    json.dump(json_dict, outfile, indent=4)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 크롤링 기능 기획

#
#
# https://animeta.net/table/2023Q4/
#     우리들의 비내리는 프로토콜
#     샹그릴라 프론티어
#     돼지의 간은 가열해라
#         hoshikuzu Telepath
#             {제목} 일본제목
#                 盾の勇者の成り上がり
#                 盾の勇者の成り上がり yomikata
#                     tate no yuusha no nariagari
#
#
# https://nyaa.si/?f=0&c=0_0&q=subsplease+1080+&p=1
# https://nyaa.si/?f=0&c=0_0&q=subsplease+1080+&p=2
# https://nyaa.si/?f=0&c=0_0&q=subsplease+1080+&p=14


# content.js
# const CDP = require('chrome-remote-interface');
#
# const userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
#
# CDP(async function(client) {
#   const {Network, Page} = client;
#   await Page.enable();
#   await Network.enable();
#   await Network.setUserAgentOverride({userAgent});
#
#   // user-agent is now set
# });
#
# // overwrite the `languages` property to use a custom getter
# Object.defineProperty(navigator, 'languages', {
#   get: function() {
#     return ['ko-KR', 'ko'];
#   },
# });
#
# // overwrite the `plugins` property to use a custom getter
# Object.defineProperty(navigator, 'plugins', {
#   get: function() {
#     return [1, 2, 3, 4, 5];
#   }
# });
#
# const getParameter = WebGLRenderingContext.getParameter;
# WebGLRenderingContext.prototype.getParameter = function(parameter) {
#   // UNMASKED_VENDOR_WEBGL
#   if (parameter === 37445) {
#     return 'Intel Open Source Technology Center';
#   }
#   // UNMASKED_RENDERER_WEBGL
#   if (parameter === 37446) {
#     return 'Mesa DRI Intel(R) Ivybridge Mobile ';
#   }
#
#   return getParameter(parameter);
# };
#
# ['height', 'width'].forEach(property => {
#   // store the existing descriptor
#   const imageDescriptor = Object.getOwnPropertyDescriptor(HTMLImageElement.prototype, property);
#
#   // redefine the property with a patched descriptor
#   Object.defineProperty(HTMLImageElement.prototype, property, {
#     ...imageDescriptor,
#     get: function() {
#       // return an arbitrary non-zero dimension if the image failed to load
#       if (this.complete && this.naturalHeight == 0) {
#         return 20;
#       }
#       // otherwise, return the actual dimension
#       return imageDescriptor.get.apply(this);
#     },
#   });
# });
#
# // store the existing descriptor
# const elementDescriptor = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');
#
# // redefine the property with a patched descriptor
# Object.defineProperty(HTMLDivElement.prototype, 'offsetHeight', {
#   ...elementDescriptor,
#   get: function() {
#     if (this.id === 'modernizr') {
#         return 1;
#     }
#     return elementDescriptor.get.apply(this);
#   },
# });


# :: 프록시 처리용
# pip install mitmproxy
#
# # inject.py
# from bs4 import BeautifulSoup
# from mitmproxy import ctx
#
# # load in the javascript to inject
# with open('content.js', 'r') as f:
#     content_js = f.read()
#
# def response(flow):
#     # only process 200 responses of html content
#     if flow.response.headers['Content-Type'] != 'text/html':
#         return
#     if not flow.response.status_code == 200:
#         return
#
#     # inject the script tag
#     html = BeautifulSoup(flow.response.text, 'lxml')
#     container = html.head or html.body
#     if container:
#         script = html.new_tag('script', type='text/javascript')
#         script.string = content_js
#         container.insert(0, script)
#         flow.response.text = str(html)
#
#         ctx.log.info('Successfully injected the content.js script.')
#
# :: 크롤링 시에 띄워져 있어야 하는 서버
# mitmdump -p 8080 -s "inject.py"


# import webbrowser
# import urllib.parse
# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# import selenium.webdriver as webdriver
# import sys
# import tkinter.messagebox
# from tkinter import *
# import ssl
# context = ssl._create_unverified_context()
#
#
# soup2 = BeautifulSoup(webpage2.read(),"html.parser")
# for link3 in soup2.find(name="div",attrs={"class":"cont"}):
#     try:
#         title = link3.select('a')[0]['href'] #a태그중 0다음인 1번째 데이터 가져오기
#         req3 = Request('https://series.naver.com'+str(title), headers={'User-Agent': 'Mozilla/5.0'})
#         webpage3 = urlopen(req3, context=context)
#         soup3 = BeautifulSoup(webpage3.read(),"html.parser")
#         num2 = 0 #초기값
#         for link4 in soup3.find_all(name="td",attrs={"class":"serieslist"}):
#             try:
#                 num2 = num2+1
#                 data = link4.select('div')
#                 data = str(data)
#                 data = data.strip("[<div><strong></div>]")
#                 data = data.replace("</strong>","")
#                 data = data.replace("<br/>","")
#                 List2.insert(num2, data)
#             except:
#                     pass
#         global datalist
#         datalist = [] * num2 #리스트 생성
#         for link5 in soup3.find_all(name="td",attrs={"class":"summary"}):
#             try:
#                 dataSt = link5.select('div')[0]
#                 dataSt = dataSt.get_text()
#                 #dataSt2 = link5.select('div')
#                 #print(dataSt2)
#                 datalist.append(str(dataSt)) #리스트에 넣기
#             except:
#                     pass
#         #print(datalist)
#     except:
#             pass


# 'voiceless mode':  특정 사운드가 들리도록 , sound_success.wav, sound_fail.wav

# 'voice mode':


#     # aidi & pasuwado 입력되었는지 확인
#            └> 어떻게하면 PC가 인지할 수 있을 까?
#            └> 크롬 브라우저의 ctrl f 를 통해서 검색 하는 아이디어





# # 2001 ?  2000 ?개의 요소를 지닌 튜플 생성")
# tuple_minus_100_to_100 = tuple(range(-1000, 1000, 1))
# print(tuple_minus_100_to_100)


# 튜플을 개행하여 문자열로 출력")
# s = '\n'.join(map(str, info))
# print(s)


# 튜플을 csv 처럼 문자열로 출력")
# s = ','.join(map(str, info))
# print(s)



# # 아주 유용한 문자열 교체(swap_targets)/넘버링 테스트")
# text_a='''
# {{test}}{{test}}{{pppp}}{{test}}{{test}}{{test}}{{test}}{{test}}{{test}}{{test}}{{pppp}}{{test}}{{test}}
# '''
# text_b="{{test}}"
# text_c="_"
# print(Park4139.replace_text_B_and_text_C_interchangeably_at_text_A_by_using_(text_a, text_b, text_c, magical_words['and_get_it']))


# Park4139.speak("잠시후 RPA를 시작합니다")
# Park4139.speak("키보드와 마우스에서 손을 때주세요")

info = {
    '모니터_크기': pyautogui.size(),
}
# 튜플을 그냥 print로 출력")
print(info)
# 튜플을 구조화 하여 예쁘게 출력")
print("└> 튜플을 구조화 하여 예쁘게 출력")

# 튜플을 데이터타입에 상관없이 문자열로 출력")
s = '\n'.join(map(str, info))
print(s)


# 현재 마우스 위치를 클립보드로 카피!")
target = str(pyautogui.position()).replace("Point(x=", "").replace("y=", "").replace(")", "").replace(" ", "").strip()
print(target)
pyperclip.copy(target)




# # RPA 탐지 회피용 코드")
# time.sleep(round(random.uniform(1, 15), 4))


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
# os.system("pause")


# 마우스 드래그 앤 드롭
# pyautogui.moveTo(1314, 777, duration=0)
# pyautogui.mouseDown(button='right')
# pyautogui.moveTo(1392, 777, duration=0)
# pyautogui.mouseUp(button='right')



# fw = pyautogui.getActiveWindow()
# fw.close()   # 현재 활성화 상태인 창 닫기


# pyautogui.mouseInfo()


# pyautogui.middleClick()
# pyautogui.scroll(500)
# pyautogui.scroll(-500)


# pyautogui.drag(100, 100, duration=0.25)
# pyautogui.dragTo(100, 100, duration=0.25)


# Park4139.commentize('응 형은 다했어. 먼저 퇴근해볼께 프로젝트를 종료합니다')
# Park4139.commentize('RPA를 종료합니다')


# 모든 윈도우 창의 타이틀 가져오기
# def get_window_titles():
#     def callback(hwnd, titles):
#         if win32gui.IsWindowVisible(hwnd):
#             titles.append(win32gui.GetWindowText(hwnd))
#         return True
#
#     titles = []
#     win32gui.EnumWindows(callback, titles)
#     return titles

# 모든 윈도우 창의 제목 출력
# window_titles = get_window_titles()
# window_titles = [x for x in window_titles if x.strip()]  # 리스트 요소 "" 제거
# window_titles = "\n".join(window_titles)  # list to str
# Park4139.debug_as_gui(f"열린 윈도우 창 제목들\n\n{window_titles}")




# 스택 마우스 제작 참고용
# class DraggableLabel(QLabel):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setEnabled(True)
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.drag_start_position = event.pos()
#
#     def mouseMoveEvent(self, event):
#         if not (event.buttons() & Qt.LeftButton):
#             return
#
#         mime_data = QMimeData()
#         drag = QDrag(self)
#         drag.setMimeData(mime_data)
#         drag.setPixmap(self.grab())
#         drag.setHotSpot(event.pos() - self.rect().topLeft())
#
#         drag.exec_(Qt.MoveAction)



# 실험 필요
# 변수명 출력함수
# def Park4139.debug_as_cli(variable):
#     def namestr(obj, namespace):

#         get_name = [name for name in namespace if namespace[name] is obj]
#         return get_name[0]
#     def Change(variable):

#         Park4139.debug_as_cli(namestr(variable, globals()), "=", variable)
#     Park4139.debug_as_cli(f'{Change(variable)} : {variable}')


# 파이선 폴더 동기화 시켜도록 시도해보자


# 재귀 한도 설정
# import sys
# sys.setrecursionlimit(10 ** 5)


# 기능 아이디어
# get replaced clipboard from / to \
#     C:/Users/WIN10PROPC3/Desktop/services/archive_py/.git/index.lock
#     C:\Users\WIN10PROPC3\Desktop\services\archive_py\.git\index.lock


# 이걸로 특정 랜덤태스크를 하루에 몇 번까지 제한하도록 관리 > 만들어둔 toml 데이터베이스 활용해서 하면 되겠음.
# daily_random_tasks = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]



# 일본어 가사검색
# neko iryics romaji






