# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'



import pkg_park4139





if __name__ == '__main__':
    try:
        while (True):
            pkg_park4139.TtsUtil.speak(ment="console Blurred 프로그램을 실행합니다")
            # Park4139Tts.speak(ment="콘솔 블러 프로그램을 실행합니다")
            pkg_park4139.Park4139.run_console_blurred_as_gui()
            break
    except Exception as e:
        pkg_park4139.Park4139.trouble_shoot("%%%FOO%%%")
    pass
