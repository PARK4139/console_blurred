# 2023 12 07 17 07 apply %%%FOO%%% via dev tool auto increament
# -*- coding: utf-8 -*-
__author__ = 'PARK4139 : Jung Hoon Park'


from pkg_park4139 import TextToSpeechUtil, StateManagementUtil, DebuggingUtil, BusinessLogicUtil

if __name__ == '__main__':
    try:
        BusinessLogicUtil.run_console_blurred_as_scheduler()
    except Exception as e:
        DebuggingUtil.trouble_shoot("%%%FOO%%%")
    pass
