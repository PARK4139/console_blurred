import inspect
import os
import sys
import time
from BlurWindow.blurWindow import blur
from PySide6.QtCore import Qt, QEvent, QCoreApplication
from PySide6.QtWidgets import *

from test_pyside6_debugger import debugger

QEvent_Type_identifiers_reference={
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


class Pyside6CoreObjectNotepad(QWidget):
    PROGRAM_WIDTH = 600
    PROGRAM_HEIGHT = 300
    TITLE_NM = "starting_program"
    IMG1 = "minimize.png"
    IMG2 = "close.png"
    BAR_HEIGHT = 36
    def __init__(self):
        super().__init__()
        self.setupUI()

    def print_display_info(self):
        print(self.screen().size().width())
        print(self.screen().size().height())
        print(self.screen().availableSize().width())
        print(self.screen().availableSize().height())

    def setupUI(self):
        self.print_display_info()
        self.setGeometry((self.screen().size().width()-self.PROGRAM_WIDTH)/2, (self.screen().size().height()-self.PROGRAM_HEIGHT)/2, self.PROGRAM_WIDTH, self.PROGRAM_HEIGHT)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        blur(self.winId())
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")

        self.pushButton1= QPushButton()
        self.pushButton1.setText("button1")
        self.pushButton1.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.pushButton1.clicked.connect(self.fnc_tmp)

        self.pushButton2= QPushButton("button2")
        self.pushButton2.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.pushButton2.clicked.connect(self.fnc_tmp)

        self.pushButton3= QPushButton("button3")
        self.pushButton3.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.pushButton3.clicked.connect(self.fnc_tmp)

        self.pushButton4= QPushButton("button4")
        self.pushButton4.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.pushButton4.clicked.connect(self.fnc_tmp)

        self.pushButton5= QPushButton("button4")
        self.pushButton5.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.pushButton5.clicked.connect(self.fnc_tmp)

        self.pushButton6= QPushButton()
        self.pushButton6.setText("quit")
        self.pushButton6.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.pushButton6.size().setWidth(100)
        self.pushButton6.size().setHeight(100)
        # self.pushButton6.resize(self.pushButton3.sizeHint())
        self.pushButton6.clicked.connect(QCoreApplication.instance().quit)

        self.pushButton= QPushButton()
        self.pushButton.setText("button")
        self.pushButton.setStyleSheet("color: rgba(255,255,255, 0.9);")
        self.pushButton.clicked.connect(self.fnc_tmp)

        self.textarea = QTextEdit()
        self.textarea.setMaximumSize( 500 , 500 )# 전체화면의 4분의 1로 설정 나중에 하자
        self.textarea.setAcceptRichText(False)
        self.textarea.setStyleSheet('''
            QTextEdit {
                color: rgba(128,128,128, 0.9);
                /*color: rgba(104,151,187, 0.9);*/
                /*color: rgba(169,183,198, 0.9);*/
                /*color: rgba(204,120,50, 0.9);*/
                font-size: 8px; 
        }''');
        # self.textarea = QTextEdit(self)
        # self.textarea.setMaximumSize( 500 , 500 )# 전체화면의 4분의 1로 설정 나중에 하자
        # self.textarea.setAcceptRichText(False)
        # self.textarea.setHtml('''
        #     <!DOCTYPE HTML>
        #     <html>
        #         <head>
        #             <meta name=\"qrichtext\" content=\"1\" />
        #             <meta charset=\"utf-8\" />
        #             <style type=\"text/css\">\n
        #                 p, li { white-space: pre-wrap; }\n
        #                 hr { height: 1px; border-width: 0; }\n
        #                 li.unchecked::marker { content: \"\\2610\"; }\n
        #                 li.checked::marker { content: \"\\2612\"; }\n
        #             </style>
        #         </head>
        #         <body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n
        #             <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">
        #                 <span style=\" font-family:'MS Sans Serif'; color:#ffffff; background-color:#000000;\">
        #                     I'm black
        #                 </span>
        #             </p>\n
        #         </body>
        #     </html>
        #     ''')
        self.textarea.selectionChanged.connect(self.on_selection_changed)
        self.textarea.textChanged.connect(self.fnc_tmp) #QTextEdit() 의 text change event


        layout_top = QGridLayout()
        layout_top.addWidget(self.pushButton1, 0, 1)
        layout_top.addWidget(self.pushButton2, 0, 2)
        layout_top.addWidget(self.pushButton3, 0, 3)
        layout_top.addWidget(self.pushButton4, 0, 4)
        layout_top.addWidget(self.pushButton5, 0, 5)
        layout_top.addWidget(self.pushButton6, 0, 6)

        layout_bottom = QGridLayout()
        layout_bottom.addWidget(self.textarea, 0, 1)

        layout_main = QGridLayout()
        layout_main.addLayout(layout_top,0,0)
        layout_main.addLayout(layout_bottom,1,0)
        self.setLayout(layout_main)

    def on_selection_changed(self):
        print(self.text_entry.textBackgroundColor().name())
    def fnc_tmp(self):
        text = self.textarea.toPlainText()
        print("_______________________________________________________________ "+inspect.currentframe().f_code.co_name+" s")
        print(+str(text))
        print("└>textarea txt")
        print(str(len(text)))
        print('└>str length ')
        print(str(len(text.split())))
        print('└>words cnt')
        print("_______________________________________________________________ "+inspect.currentframe().f_code.co_name+" e")

    def changeEvent(self, event):#changeEvent() 메소드는 개발자가 코드에 직접 호출하지 않아도, __init__ 처럼 특정 조건에서 호출이 이루어 지는 느낌이 든다
        debugger.print_event_info_(event, QEvent_Type_identifiers_reference)
        if event.type() == QEvent.WindowStateChange:
            if event.oldState() and Qt.WindowMinimized:
                debugger.print_event_info_(event, QEvent_Type_identifiers_reference)
            elif event.oldState() == Qt.WindowNoState or self.windowState() == Qt.WindowMaximized:
                debugger.print_event_info_(event, QEvent_Type_identifiers_reference)
        elif event.type() == QEvent.ApplicationStateChange:
            debugger.print_event_info_(event, QEvent_Type_identifiers_reference)

        if str(event).strip()=="<PySide6.QtCore.QEvent(QEvent::ActivationChange)>":
            debugger.print_function_info(debugger.speak_after_)

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
    main_ = Pyside6CoreObjectNotepad()
    main_.show()
    app.exec()
    sys.exit()

