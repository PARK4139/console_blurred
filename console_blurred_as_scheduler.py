# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'


from  pkg_park4139 import TtsUtil

import pkg_park4139

Park4139 = pkg_park4139.Park4139()



if __name__ == '__main__':
    try:
        Park4139.run_console_blurred_as_scheduler()
    except Exception as e:
        Park4139.trouble_shoot("%%%FOO%%%")
    pass
