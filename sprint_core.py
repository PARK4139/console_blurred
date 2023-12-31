import os
import string
from datetime import datetime
from typing import List

from PySide6.QtCore import Signal, QThread

import pkg_park4139

Park4139 = pkg_park4139.Park4139()

directory_abspath = Park4139.PROJECT_DIRECTORY



while 1:
    # Park4139.monitor_target_edited_and_bkup(target_abspath=Park4139.PROJECT_DIRECTORY)
    # Park4139.is_sync_directory_local(target_abspath=Park4139.PROJECT_DIRECTORY)
    Park4139.monitor_target_edited_and_bkup(target_abspath=Park4139.PARK4139_ARCHIVE_TOML)





