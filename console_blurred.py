# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'

from pkg_park4139 import TextToSpeechUtil, DebuggingUtil, BusinessLogicUtil

if __name__ == '__main__':
    try:
        while (True):
            if TextToSpeechUtil.speak_ment_without_async_and_return_last_word_mp3_length(ment="콘솔 블러 프로그램을 실행합니다", sleep_after_play=0.95):
                # if TtsUtil.speak_ment_without_async_and_return_last_word_mp3_length(ment="콘솔 블러 프로그램을 실행합니다", sleep_after_play=0.95):
                BusinessLogicUtil.run_console_blurred_as_gui()
            break
    except Exception as e:
        DebuggingUtil.trouble_shoot("%%%FOO%%%")
    pass
