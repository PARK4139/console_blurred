# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'


from  pkg_park4139 import TtsUtil

import pkg_park4139

Park4139 = pkg_park4139.Park4139()



if __name__ == '__main__':
    try:
        while (True):
            Park4139.speak_today_time_info()
            if TtsUtil.speak_ment_without_async_and_return_last_word_mp3_length(ment="console Blurred 프로그램을 실행합니다", sleep_after_play=0.95):
                # Park4139Tts.speak(ment="콘솔 블러 프로그램을 실행합니다")
                Park4139.run_console_blurred_as_scheduler()

            break
    except Exception as e:
        Park4139.trouble_shoot("%%%FOO%%%")
    pass
