# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'

from pkg_park4139_for_windows import TextToSpeechUtil, DebuggingUtil, BusinessLogicUtil

"""
console_blurred.py 는 build 용 파일
GUI 형태로 할건지 SCHEDULER 형태로 빌드할 형태를 고른 뒤 
Build 배치 수행
"""

if __name__ == '__main__':
    try:
        while (True):
            TextToSpeechUtil.speak_today_time_info() # debugging factor, 이거 설정하면 gtts 모듈 미작동으로 인해 에러뜨며 패키징해도 실행안된다.
            if TextToSpeechUtil.speak_ment_without_async_experimental_2(ment="콘솔 블러 프로그램을 스케쥴러 모드로 실행합니다", delay=0.95):#success, delay=0.95 가 테스트했을때 적당하다 판단
                BusinessLogicUtil.run_console_blurred_as_scheduler()
            break
    except Exception as e:
        DebuggingUtil.trouble_shoot("%%%FOO%%%")
    pass
