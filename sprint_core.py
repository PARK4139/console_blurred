import inspect
import os
import string
from datetime import datetime
from typing import List

from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import QApplication

from pkg_park4139 import UiUtil, StateManagementUtil, FileSystemUtil, TestUtil
import requests
from bs4 import BeautifulSoup

# 크롤링할 페이지의 URL
url = 'https://wikidocs.net/book/4706'

# 페이지 요청
response = requests.get(url)

# 요청이 성공했을 경우에만 크롤링 진행
if response.status_code == 200:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.text, 'html.parser')

    # 모든 텍스트 출력
    print(soup.get_text())
else:
    print('페이지 요청이 실패했습니다.')
