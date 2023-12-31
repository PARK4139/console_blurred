# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'

from pkg_park4139 import TtsUtil, Park4139

"""
console_blurred.py 는 build 용 파일
GUI 형태로 할건지 SCHEDULER 형태로 빌드할 형태를 고른 뒤 
Build 배치 수행.

"""

if __name__ == '__main__':
    try:
        while (True):
            Park4139.speak_today_time_info()
            if TtsUtil.speak_ment_without_async_and_return_last_word_mp3_length(ment="console Blurred 프로그램을 실행합니다", sleep_after_play=0.95):
            # if TtsUtil.speak_ment_without_async_and_return_last_word_mp3_length(ment="콘솔 블러 프로그램을 실행합니다", sleep_after_play=0.95):
            #     Park4139.run_console_blurred_as_scheduler()
                Park4139.run_console_blurred_as_gui()
            break
    except Exception as e:
        Park4139.trouble_shoot("%%%FOO%%%")
    pass
