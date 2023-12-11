import sys
import re
import os
import traceback
import logging

import keyboard
import pyautogui
# CUSTOM PY PKG SET UP
import pkg_park4139
import clipboard

__author__ = 'Park4139 : Jung Hoon Park'
park4139 = pkg_park4139.Park4139()

if __name__ == '__main__':
    try:
        while (True):
            park4139.run_rpa_program()
    except Exception as e:
        print(str(e))
        park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        park4139.pause()
