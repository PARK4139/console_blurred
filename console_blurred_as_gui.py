# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'



import pkg_park4139

Park4139 = pkg_park4139.Park4139()
Park4139Tts = pkg_park4139.Tts()


if __name__ == '__main__':
    try:
        while (True):
            Park4139Tts.speak(ment="console Blurred 프로그램을 실행합니다")
            # Park4139Tts.speak(ment="콘솔 블러 프로그램을 실행합니다")
            Park4139.run_console_blurred_as_gui()
            break
    except Exception as e:
        Park4139.trouble_shoot("%%%FOO%%%")
    pass
