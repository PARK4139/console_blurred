import inspect
import os
import string
from datetime import datetime
from typing import List

from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import QApplication

from pkg_park4139 import UiUtil, StateManagementUtil, FileSystemUtil, TestUtil

directory_abspath = StateManagementUtil.PROJECT_DIRECTORY






# [print(sample) for sample in FileSystemUtil.get_target_as_pn(target_abspath=r"C:\Users\WIN10PROPC3\Desktop\services\storage\`\pop_sound.mkv") ]
FileSystemUtil. convert_mkv_to_wav(file_mkv=r"C:\Users\WIN10PROPC3\Desktop\services\storage\`\pop_sound.mkv")
TestUtil.pause()







