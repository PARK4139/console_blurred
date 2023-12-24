import inspect
import os
import sys
import time
import pyautogui
import pygetwindow
import win32gui
from BlurWindow.blurWindow import blur
from PySide6.QtCore import Qt, QEvent, QCoreApplication
from PySide6.QtWidgets import *

from pkg_park4139 import Park4139
from test_pyside6_debugger import debugger

QEvent_Type_identifiers_reference = {
    "0": "QEvent.None",
    "1": "QEvent.Timer",
    "10": "QEvent.Enter",
    "100": "QEvent.StyleChange",
    "1000": "QEvent.User",
    "101": "QEvent.IconTextChange",
    "102": "QEvent.ModifiedChange",
    "103": "QEvent.WindowBlocked",
    "104": "QEvent.WindowUnblocked",
    "105": "QEvent.WindowStateChange",
    "109": "QEvent.MouseTrackingChange",
    "11": "QEvent.Leave",
    "110": "QEvent.ToolTip",
    "111": "QEvent.WhatsThis",
    "112": "QEvent.StatusTip",
    "113": "QEvent.ActionChanged",
    "114": "QEvent.ActionAdded",
    "115": "QEvent.ActionRemoved",
    "116": "QEvent.FileOpen",
    "117": "QEvent.Shortcut",
    "118": "QEvent.WhatsThisClicked",
    "119": "QEvent.AccessibilityHelp",
    "12": "QEvent.Paint",
    "120": "QEvent.ToolBarChange",
    "121": "QEvent.ApplicationActivate",
    "122": "QEvent.ApplicationDeactivate",
    "123": "QEvent.QueryWhatsThis",
    "124": "QEvent.EnterWhatsThisMode",
    "125": "QEvent.LeaveWhatsThisMode",
    "126": "QEvent.ZOrderChange",
    "127": "QEvent.HoverEnter",
    "128": "QEvent.HoverLeave",
    "129": "QEvent.HoverMove",
    "13": "QEvent.Move",
    "130": "QEvent.AccessibilityDescription",
    "131": "QEvent.ParentAboutToChange",
    "132": "QEvent.WinEventAct",
    "14": "QEvent.Resize",
    "150": "QEvent.EnterEditFocus",
    "151": "QEvent.LeaveEditFocus",
    "153": "QEvent.MenubarUpdated",
    "155": "QEvent.GraphicsSceneMouseMove",
    "156": "QEvent.GraphicsSceneMousePress",
    "157": "QEvent.GraphicsSceneMouseRelease",
    "158": "QEvent.GraphicsSceneMouseDoubleClick",
    "159": "QEvent.GraphicsSceneContextMenu",
    "160": "QEvent.GraphicsSceneHoverEnter",
    "161": "QEvent.GraphicsSceneHoverMove",
    "162": "QEvent.GraphicsSceneHoverLeave",
    "163": "QEvent.GraphicsSceneHelp",
    "164": "QEvent.GraphicsSceneDragEnter",
    "165": "QEvent.GraphicsSceneDragMove",
    "166": "QEvent.GraphicsSceneDragLeave",
    "167": "QEvent.GraphicsSceneDrop",
    "168": "QEvent.GraphicsSceneWheel",
    "169": "QEvent.KeyboardLayoutChange",
    "17": "QEvent.Show",
    "170": "QEvent.DynamicPropertyChange",
    "171": "QEvent.TabletEnterProximity",
    "172": "QEvent.TabletLeaveProximity",
    "173": "QEvent.NonClientAreaMouseMove",
    "174": "QEvent.NonClientAreaMouseButtonPress",
    "175": "QEvent.NonClientAreaMouseButtonRelease",
    "176": "QEvent.NonClientAreaMouseButtonDblClick",
    "177": "QEvent.MacSizeChange",
    "178": "QEvent.ContentsRectChange",
    "18": "QEvent.Hide",
    "181": "QEvent.GraphicsSceneResize",
    "182": "QEvent.GraphicsSceneMove",
    "183": "QEvent.CursorChange",
    "184": "QEvent.ToolTipChange",
    "186": "QEvent.GrabMouse",
    "187": "QEvent.UngrabMouse",
    "188": "QEvent.GrabKeyboard",
    "189": "QEvent.UngrabKeyboard",
    "19": "QEvent.Close",
    "192": "QEvent.StateMachineSignal",
    "193": "QEvent.StateMachineWrapped",
    "194": "QEvent.TouchBegin",
    "195": "QEvent.TouchUpdate",
    "196": "QEvent.TouchEnd",
    "198": "QEvent.Gesture",
    "199": "QEvent.RequestSoftwareInputPanel",
    "2": "QEvent.MouseButtonPress",
    "200": "QEvent.CloseSoftwareInputPanel",
    "202": "QEvent.GestureOverride",
    "203": "QEvent.WinIdChange",
    "21": "QEvent.ParentChange",
    "212": "QEvent.PlatformPanel",
    "24": "QEvent.WindowActivate",
    "25": "QEvent.WindowDeactivate",
    "26": "QEvent.ShowToParent",
    "27": "QEvent.HideToParent",
    "3": "QEvent.MouseButtonRelease",
    "31": "QEvent.Wheel",
    "33": "QEvent.WindowTitleChange",
    "34": "QEvent.WindowIconChange",
    "35": "QEvent.ApplicationWindowIconChange",
    "36": "QEvent.ApplicationFontChange",
    "37": "QEvent.ApplicationLayoutDirectionChange",
    "38": "QEvent.ApplicationPaletteChange",
    "39": "QEvent.PaletteChange",
    "4": "QEvent.MouseButtonDblClick",
    "40": "QEvent.Clipboard",
    "43": "QEvent.MetaCall",
    "5": "QEvent.MouseMove",
    "50": "QEvent.SockAct",
    "51": "QEvent.ShortcutOverride",
    "52": "QEvent.DeferredDelete",
    "6": "QEvent.KeyPress",
    "60": "QEvent.DragEnter",
    "61": "QEvent.DragMove",
    "62": "QEvent.DragLeave",
    "63": "QEvent.Drop",
    "65535": "QEvent.MaxUser",
    "68": "QEvent.ChildAdded",
    "69": "QEvent.ChildPolished",
    "7": "QEvent.KeyRelease",
    "70": "QEvent.ChildInserted",
    "71": "QEvent.ChildRemoved",
    "74": "QEvent.PolishRequest",
    "75": "QEvent.Polish",
    "76": "QEvent.LayoutRequest",
    "77": "QEvent.UpdateRequest",
    "78": "QEvent.UpdateLater",
    "8": "QEvent.FocusIn",
    "82": "QEvent.ContextMenu",
    "83": "QEvent.InputMethod",
    "86": "QEvent.AccessibilityPrepare",
    "87": "QEvent.TabletMove",
    "88": "QEvent.LocaleChange",
    "89": "QEvent.LanguageChange",
    "9": "QEvent.FocusOut",
    "90": "QEvent.LayoutDirectionChange",
    "92": "QEvent.TabletPress",
    "93": "QEvent.TabletRelease",
    "94": "QEvent.OkRequest",
    "96": "QEvent.IconDrag",
    "97": "QEvent.FontChange",
    "98": "QEvent.EnabledChange",
    "99": "QEvent.ActivationChange",
}


class Pyside6CoreObjectMacro(QWidget):
    PROGRAM_WIDTH = 600
    PROGRAM_HEIGHT = 300
    TITLE_NM = "starting_program"
    IMG1 = "minimize.png"
    IMG2 = "close.png"
    BAR_HEIGHT = 36

    push_btn1 = None

    def __init__(self):
        super().__init__()
        self.setupUI()

    def print_info(self):
        Park4139.commentize(f"display infos")
        print(self.screen().size().width())
        print(self.screen().size().height())
        print(self.screen().availableSize().width())
        print(self.screen().availableSize().height())
        print(pyautogui.size())
        Park4139.commentize(f"mouse infos")
        print(pyautogui.position())
        Park4139.commentize(f"keyboard infos")
        print(pyautogui.KEYBOARD_KEYS)
        Park4139.commentize(f"window infos")
        print(pyautogui.getInfo())
        print(pyautogui.size())

        import win32gui
        win32gui.GetWindowText(win32gui.GetForegroundWindow())
        # win32gui.GetWindow()
        # win32gui.GetWindowText(win32gui.GetWindow())

        # print(pyautogui.getWindowsWithTitle("제목 없음")[0])
        # print(pyautogui.getWindowsWithTitle("제목 없음")[0].isActive)
        # print(pyautogui.getWindowsWithTitle("제목 없음")[0].isMaximized)
        # print(pyautogui.getWindowsWithTitle("제목 없음")[0].isMinimized)

    def setupUI(self):
        self.print_info()
        self.setGeometry((self.screen().size().width() - self.PROGRAM_WIDTH) / 2, (self.screen().size().height() - self.PROGRAM_HEIGHT) / 2, self.PROGRAM_WIDTH, self.PROGRAM_HEIGHT)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        blur(self.winId())
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")

        shortcuts = {
            'shortcut1': "` + r : record macro",
            'shortcut2': "` + r : stop macro",
        }
        self.push_btn1 = QPushButton()
        self.push_btn1.setText('''
                                                        << shorcuts >>
                                                        
                                                    ''' + shortcuts['shortcut1'] + '''
                                                    ''' + shortcuts['shortcut2'] + ''' 
                                                    
                                                          << board >>
        ''')
        self.push_btn1.setStyleSheet("color: rgba(255,255,255, 0.9);text-align: left;")
        self.push_btn1.clicked(self.fnc_tmp)

        self.push_btn2 = QPushButton()  # 타이핑하는 내용이 모두 여기에 나오도록.
        self.push_btn2.setText("tmp")
        self.push_btn2.setStyleSheet("color: rgba(255,255,255, 0.9);text-align: left;")
        self.push_btn2.clicked(self.fnc_tmp)

        self.push_btn6 = QPushButton()
        self.push_btn6.setText("quit")
        self.push_btn6.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.push_btn6.size().setWidth(100)
        self.push_btn6.size().setHeight(100)
        self.push_btn6.clicked(QCoreApplication.instance().quit)


        Park4139.commentize("_____________________________________ 레이아웃 설정")
        layout_top = QGridLayout()
        layout_top.addWidget(self.push_btn1, 0, 1)
        layout_top.addWidget(self.push_btn2, 1, 1)

        layout_main = QGridLayout()
        layout_main.addLayout(layout_top, 0, 0)
        self.setLayout(layout_main)

        time.sleep(50 / 1000)
        print(pyautogui.position())

    def changeEvent(self, event):
        Park4139.commentize(f"{inspect.currentframe().f_code.co_name}")
        # changeEvent() 메소드는 개발자가 코드에 직접 호출하지 않아도, 
        # __init__ 처럼 특정 조건에서 호출이 이루어 지는 것 같다.
        # print_event_info_(event, QEvent_Type_identifiers_reference)
        if event.type() == QEvent.WindowStateChange:
            if event.oldState() and Qt.WindowMinimized:
                debugger.print_event_info_(event, QEvent_Type_identifiers_reference)
            elif event.oldState() == Qt.WindowNoState or self.windowState() == Qt.WindowMaximized:
                debugger.print_event_info_(event, QEvent_Type_identifiers_reference)
        elif event.type() == QEvent.ApplicationStateChange:
            debugger.print_event_info_(event, QEvent_Type_identifiers_reference)
        if str(event).strip() == "<PySide6.QtCore.QEvent(QEvent::ActivationChange)>":
            Park4139.commentize(f"foo")

    def on_selection_changed(self):
        print(self.text_entry.textBackgroundColor().name())

    def fnc_tmp(self):
        text = self.push_btn1.text()
        print(+str(text))
        print(str(len(text)))
        print('└>str length ')
        print(str(len(text.split())))
        print('└>words cnt')

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

    def close(self):
        """버튼 명령: 닫기"""
        app.close(self)


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    app = QApplication()
    main_ = Pyside6CoreObjectMacro()
    main_.show()
    app.exec()
    sys.exit()
