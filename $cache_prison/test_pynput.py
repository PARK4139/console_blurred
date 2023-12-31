__author__ = 'PARK4139 : Jung Hoon Park'

# -*- coding: utf-8 -*-  # python 3.x 하위버전 호환을 위한코드
import sys
import traceback
from functools import partial

from PySide6.QtWidgets import QApplication

import pkg_park4139

Park4139 = pkg_park4139.Park4139()


# LOGGER SET UP
# logger = logging.getLogger('park4139_test_logger')
# hdlr = logging.FileHandler('park4139_logger.log')
# hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)


def decorate_test_status_printing_code(function):
    def wrapper():
        Park4139.commentize(rf"test status")
        function()

    return wrapper


@decorate_test_status_printing_code
def print_with_test_status(status: str):
    print(status)


def decorate_for_pause(function):
    """
        # ctrl c ctrl c 이렇게 두번 눌르면 소스 수정 후 재시작 됩니다
        # 안그럼 계속 새롭게 창을 무한정 열게 되어 컴퓨터가 다운될 수 있습니다.
    """

    def wrapper():
        function()
        Park4139Test.pause()

    return wrapper


qss = """
    # QWidget {
    #     color: #FFFFFF;
    #     background: #333333;
    #     height: 32px;
    # }
    # QLabel {
    #     color: #FFFFFF;
    #     background: #333333;
    #     font-size: 16px;
    #     padding: 5px 5px;
    # }
    # QToolButton {
    #     background: #333333;
    #     border: none;
    # }
    # QToolButton:hover{
    #     background: #444444;
    # }
"""

# 테스트 루프 카운트 최대치 설정
test_loop_limit = 3


@Park4139.measure_seconds_performance
@decorate_for_pause  # 테스트 루프 마다 정지 설정
def test():
    try:
        app = QApplication()  # set this if necessary in test
        while True:
            dialog = pkg_park4139.UiUtil.CustomQdialog(ment="테스트를 시작할까요?", buttons=["시작하기", "시작하지 않기"])
            dialog.exec_()
            text_of_clicked_btn = dialog.text_of_clicked_btn
            if text_of_clicked_btn == "시작하기":
                # _________________________________________  UP (TESTED SUCCESS) _________________________________________
                # https: // pynput.readthedocs.io / en / latest / keyboard.html
                # pynput 테스트

                def on_activate_h(temp: str):
                    print(f'{temp} pressed')

                def on_activate_i():
                    print('<ctrl>+<alt>+i pressed')

                def for_canonical(f):
                    return lambda k: f(listner_keyboard.canonical(k))

                # 등록가능한 키들 2023-12-21 23:05
                # "alt"
                # 일반 Alt 키. 이것은 수정자입니다.
                #
                # "alt_gr"
                # AltGr 키. 이것은 수정자입니다.
                #
                # "alt_l"
                # 왼쪽 Alt 키. 이것은 수정자입니다.
                #
                # "alt_r"
                # 오른쪽 Alt 키. 이것은 수정자입니다.
                #
                # "backspace"
                # 백스페이스 키.
                #
                # "caps_lock"
                # CapsLock 키입니다.
                #
                # "cmd"
                # 일반 명령 버튼. PC 플랫폼 에서는 Super 키 또는 Windows 키에 해당하고, Mac 에서는 Command 키에 해당합니다. 이는 수정자일 수 있습니다.
                #
                # "cmd_l"
                # 왼쪽 명령 버튼. PC 플랫폼 에서는 Super 키 또는 Windows 키에 해당하고, Mac 에서는 Command 키에 해당합니다. 이는 수정자일 수 있습니다.
                #
                # "cmd_r"
                # 오른쪽 명령 버튼. PC 플랫폼 에서는 Super 키 또는 Windows 키에 해당하고, Mac 에서는 Command 키에 해당합니다. 이는 수정자일 수 있습니다.
                #
                # "ctrl"
                # 일반 Ctrl 키. 이것은 수정자입니다.
                #
                # "ctrl_l"
                # 왼쪽 Ctrl 키. 이것은 수정자입니다.
                #
                # "ctrl_r"
                # 오른쪽 Ctrl 키. 이것은 수정자입니다.
                #
                # "delete"
                # 삭제 키입니다.
                #
                # "down"
                # 아래쪽 화살표 키.
                #
                # "end"
                # 종료 키.
                #
                # "enter"
                # Enter 또는 Return 키.
                #
                # "esc"
                # Esc 키입니다.
                #
                # "f1"
                # 기능 키. F1~F20이 정의됩니다.
                #
                # "home"
                # 홈 키.
                #
                # "insert"
                # 삽입 키입니다. 일부 플랫폼에서는 정의되지 않을 수 있습니다.
                #
                # "left"
                # 왼쪽 화살표 키.
                #
                # "media_next"
                # 다음 트랙 버튼입니다.
                #
                # "media_play_pause"
                # 재생/일시 정지 토글입니다.
                #
                # "media_previous"
                # 이전 트랙 버튼.
                #
                # "media_volume_down"
                # 볼륨 낮추기 버튼입니다.
                #
                # "media_volume_mute"
                # 볼륨 음소거 버튼입니다.
                #
                # "media_volume_up"
                # 볼륨 높이기 버튼입니다.
                #
                # "menu"
                # 메뉴 키. 일부 플랫폼에서는 정의되지 않을 수 있습니다.
                #
                # "num_lock"
                # NumLock 키입니다. 일부 플랫폼에서는 정의되지 않을 수 있습니다.
                #
                # "page_down"
                # PageDown 키입니다.
                #
                # "page_up"
                # PageUp 키입니다.
                #
                # "pause"
                # 일시정지/중단 키입니다. 일부 플랫폼에서는 정의되지 않을 수 있습니다.
                #
                # "print_screen"
                # PrintScreen 키입니다. 일부 플랫폼에서는 정의되지 않을 수 있습니다.
                #
                # "right"
                # 오른쪽 화살표 키입니다.
                #
                # "scroll_lock"
                # ScrollLock 키입니다. 일부 플랫폼에서는 정의되지 않을 수 있습니다.
                #
                # "shift"
                # 일반 Shift 키입니다. 이것은 수정자입니다.
                #
                # "shift_l"
                # 왼쪽 Shift 키입니다. 이것은 수정자입니다.
                #
                # "shift_r"
                # 오른쪽 Shift 키. 이것은 수정자입니다.
                #
                # "space"
                # 스페이스 키.
                #
                # "tab"
                # 탭 키.
                #
                # "up"
                # 위쪽 화살표 키.

                import pynput
                shortcuts_promised = {
                    "ctrl_plus_alt": "<ctrl>+<alt>",
                    "ctrl_plus_alt_gr": "<ctrl>+<alt_gr>",
                    "ctrl_plus_alt_l": "<ctrl>+<alt_l>",
                    "ctrl_plus_alt_r": "<ctrl>+<alt_r>",
                    "ctrl_plus_backspace": "<ctrl>+<backspace>",
                    "ctrl_plus_caps_lock": "<ctrl>+<caps_lock>",
                    "ctrl_plus_cmd": "<ctrl>+<cmd>",
                    "ctrl_plus_cmd_l": "<ctrl>+<cmd_l>",
                    "ctrl_plus_cmd_r": "<ctrl>+<cmd_r>",
                    # "ctrl_plus_ctrl": "<ctrl>+<ctrl>",
                    "ctrl_plus_ctrl_l": "<ctrl>+<ctrl_l>",
                    "ctrl_plus_ctrl_r": "<ctrl>+<ctrl_r>",
                    "ctrl_plus_delete": "<ctrl>+<delete>",
                    "ctrl_plus_down": "<ctrl>+<down>",
                    "ctrl_plus_end": "<ctrl>+<end>",
                    "ctrl_plus_enter": "<ctrl>+<enter>",
                    "ctrl_plus_esc": "<ctrl>+<esc>",
                    "ctrl_plus_f1": "<ctrl>+<f1>",
                    "ctrl_plus_home": "<ctrl>+<home>",
                    "ctrl_plus_insert": "<ctrl>+<insert>",
                    "ctrl_plus_left": "<ctrl>+<left>",
                    "ctrl_plus_media_next": "<ctrl>+<media_next>",
                    "ctrl_plus_media_play_pause": "<ctrl>+<media_play_pause>",
                    "ctrl_plus_media_previous": "<ctrl>+<media_previous>",
                    "ctrl_plus_media_volume_down": "<ctrl>+<media_volume_down>",
                    "ctrl_plus_media_volume_mute": "<ctrl>+<media_volume_mute>",
                    "ctrl_plus_media_volume_up": "<ctrl>+<media_volume_up>",
                    "ctrl_plus_menu": "<ctrl>+<menu>",
                    "ctrl_plus_num_lock": "<ctrl>+<num_lock>",
                    "ctrl_plus_page_down": "<ctrl>+<page_down>",
                    "ctrl_plus_page_up": "<ctrl>+<page_up>",
                    "ctrl_plus_pause": "<ctrl>+<pause>",
                    "ctrl_plus_print_screen": "<ctrl>+<print_screen>",
                    "ctrl_plus_right": "<ctrl>+<right>",
                    "ctrl_plus_scroll_lock": "<ctrl>+<scroll_lock>",
                    "ctrl_plus_shift": "<ctrl>+<shift>",
                    # "ctrl_plus_shift_l": "<ctrl>+<shift_l>",
                    # "ctrl_plus_shift_r": "<ctrl>+<shift_r>",
                    "ctrl_plus_space": "<ctrl>+<space>",
                    "ctrl_plus_tab": "<ctrl>+<tab>",
                    "ctrl_plus_up": "<ctrl>+<up>",
                    "ctrl_plus_a": "<ctrl>+a",
                    "ctrl_plus_b": "<ctrl>+b",
                    "ctrl_plus_c": "<ctrl>+c",
                    "ctrl_plus_d": "<ctrl>+d",
                    "ctrl_plus_e": "<ctrl>+e",
                    "ctrl_plus_f": "<ctrl>+f",
                    "ctrl_plus_g": "<ctrl>+g",
                    "ctrl_plus_h": "<ctrl>+h",
                    "ctrl_plus_i": "<ctrl>+i",
                    "ctrl_plus_j": "<ctrl>+j",
                    "ctrl_plus_k": "<ctrl>+k",
                    "ctrl_plus_l": "<ctrl>+l",
                    "ctrl_plus_m": "<ctrl>+m",
                    "ctrl_plus_n": "<ctrl>+n",
                    "ctrl_plus_o": "<ctrl>+o",
                    "ctrl_plus_p": "<ctrl>+p",
                    "ctrl_plus_q": "<ctrl>+q",
                    "ctrl_plus_r": "<ctrl>+r",
                    "ctrl_plus_s": "<ctrl>+s",
                    "ctrl_plus_t": "<ctrl>+t",
                    "ctrl_plus_u": "<ctrl>+u",
                    "ctrl_plus_v": "<ctrl>+v",
                    "ctrl_plus_w": "<ctrl>+w",
                    "ctrl_plus_x": "<ctrl>+x",
                    "ctrl_plus_y": "<ctrl>+y",
                    "ctrl_plus_z": "<ctrl>+z",
                }
                # with pynput.keyboard.GlobalHotKeys({
                #     # '<ctrl>+v': on_activate_i ,
                #     # '<ctrl>+v': partial(on_activate_h, "love"),
                #     shortcuts_promised["ctrl_plus_c"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_c"]),
                # }) as foo:
                #     foo.join()

                # with pynput.keyboard.GlobalHotKeys({
                #     shortcuts_promised["ctrl_plus_alt"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_alt"]),
                #     shortcuts_promised["ctrl_plus_v"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_v"]),
                # }) as foo:
                #     foo.join()


                shortcuts_promised_ = {
                    shortcuts_promised["ctrl_plus_alt"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_alt"]),
                    # shortcuts_promised["ctrl_plus_alt_gr"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_alt_gr"]),
                    # shortcuts_promised["ctrl_plus_alt_l"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_alt_l"]),
                    # shortcuts_promised["ctrl_plus_alt_r"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_alt_r"]),
                    # shortcuts_promised["ctrl_plus_backspace"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_backspace"]),
                    # shortcuts_promised["ctrl_plus_caps_lock"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_caps_lock"]),
                    shortcuts_promised["ctrl_plus_cmd"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_cmd"]),
                    # shortcuts_promised["ctrl_plus_cmd_l"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_cmd_l"]),
                    # shortcuts_promised["ctrl_plus_cmd_r"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_cmd_r"]),
                    # shortcuts_promised["ctrl_plus_ctrl"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_ctrl"]),
                    # shortcuts_promised["ctrl_plus_ctrl_l"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_ctrl_l"]),
                    # shortcuts_promised["ctrl_plus_ctrl_r"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_ctrl_r"]),
                    # shortcuts_promised["ctrl_plus_delete"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_delete"]),
                    # shortcuts_promised["ctrl_plus_down"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_down"]),
                    # shortcuts_promised["ctrl_plus_end"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_end"]),
                    # shortcuts_promised["ctrl_plus_enter"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_enter"]),
                    # shortcuts_promised["ctrl_plus_esc"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_esc"]),
                    # shortcuts_promised["ctrl_plus_f1"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_f1"]),
                    # shortcuts_promised["ctrl_plus_home"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_home"]),
                    # shortcuts_promised["ctrl_plus_insert"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_insert"]),
                    # shortcuts_promised["ctrl_plus_left"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_left"]),
                    # shortcuts_promised["ctrl_plus_media_next"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_media_next"]),
                    # shortcuts_promised["ctrl_plus_media_play_pause"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_media_play_pause"]),
                    # shortcuts_promised["ctrl_plus_media_previous"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_media_previous"]),
                    # shortcuts_promised["ctrl_plus_media_volume_down"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_media_volume_down"]),
                    # shortcuts_promised["ctrl_plus_media_volume_mute"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_media_volume_mute"]),
                    # shortcuts_promised["ctrl_plus_media_volume_up"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_media_volume_up"]),
                    # shortcuts_promised["ctrl_plus_menu"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_menu"]),
                    # shortcuts_promised["ctrl_plus_num_lock"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_num_lock"]),
                    # shortcuts_promised["ctrl_plus_page_down"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_page_down"]),
                    # shortcuts_promised["ctrl_plus_page_up"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_page_up"]),
                    # shortcuts_promised["ctrl_plus_pause"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_pause"]),
                    # shortcuts_promised["ctrl_plus_print_screen"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_print_screen"]),
                    # shortcuts_promised["ctrl_plus_right"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_right"]),
                    # shortcuts_promised["ctrl_plus_scroll_lock"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_scroll_lock"]),
                    shortcuts_promised["ctrl_plus_shift"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_shift"]),
                    # shortcuts_promised["ctrl_plus_shift_l"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_shift_l"]),
                    # shortcuts_promised["ctrl_plus_shift_r"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_shift_r"]),
                    # shortcuts_promised["ctrl_plus_space"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_space"]),
                    # shortcuts_promised["ctrl_plus_tab"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_tab"]),
                    # shortcuts_promised["ctrl_plus_up"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_up"]),
                    shortcuts_promised["ctrl_plus_a"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_a"]),
                    shortcuts_promised["ctrl_plus_b"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_b"]),
                    shortcuts_promised["ctrl_plus_c"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_c"]),
                    shortcuts_promised["ctrl_plus_d"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_d"]),
                    shortcuts_promised["ctrl_plus_e"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_e"]),
                    shortcuts_promised["ctrl_plus_f"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_f"]),
                    shortcuts_promised["ctrl_plus_g"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_g"]),
                    shortcuts_promised["ctrl_plus_h"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_h"]),
                    shortcuts_promised["ctrl_plus_i"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_i"]),
                    shortcuts_promised["ctrl_plus_j"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_j"]),
                    shortcuts_promised["ctrl_plus_k"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_k"]),
                    shortcuts_promised["ctrl_plus_l"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_l"]),
                    shortcuts_promised["ctrl_plus_m"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_m"]),
                    shortcuts_promised["ctrl_plus_n"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_n"]),
                    shortcuts_promised["ctrl_plus_o"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_o"]),
                    shortcuts_promised["ctrl_plus_p"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_p"]),
                    shortcuts_promised["ctrl_plus_q"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_q"]),
                    shortcuts_promised["ctrl_plus_r"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_r"]),
                    shortcuts_promised["ctrl_plus_s"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_s"]),
                    shortcuts_promised["ctrl_plus_t"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_t"]),
                    shortcuts_promised["ctrl_plus_u"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_u"]),
                    shortcuts_promised["ctrl_plus_v"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_v"]),
                    shortcuts_promised["ctrl_plus_w"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_w"]),
                    shortcuts_promised["ctrl_plus_x"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_x"]),
                    shortcuts_promised["ctrl_plus_y"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_y"]),
                    shortcuts_promised["ctrl_plus_z"]: partial(on_activate_h, shortcuts_promised["ctrl_plus_z"]),
                }
                with pynput.keyboard.GlobalHotKeys(shortcuts_promised_) as foo:
                    foo.join()


                # with pynput.keyboard.Listener(on_press=for_canonical(pynput.keyboard.HotKey.press),on_release=for_canonical(pynput.keyboard.HotKey.release)) as listner_keyboard:
                #     pass
                # listner_keyboard.join()

                listner_keyboard = pynput.keyboard.Listener(on_press=for_canonical(pynput.keyboard.HotKey.press), on_release=for_canonical(pynput.keyboard.HotKey.release))
                listner_keyboard.start()
                # _________________________________________ BELOW (NOT TESTED YET) _________________________________________
                break
            else:
                break
        app.exec()  # set this if necessary in test
        pass

    except SystemExit:  # sys.exit() 호출을 의도적으로 판단
        pass
    except:
        Park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        Park4139Test.pause()


content = r"""


처리할 코드는 여기에 작성


"""

# 나중에 TDD 공부를 해볼 것.
# 파일 변화 확인 로직 필요.
# 파일 읽어와서 전체 자리수가 바뀌면 파일 변화 한 것으로 보면 된다. 완벽하진 않아도 대부분 해소
# git으로 관리되는 프로젝트이면 git으로도 확인 가능
error_cnt = 0
if __name__ == '__main__':
    try:
        test_loop_cnt = 1
        Park4139.commentize("TRYING TO ENTER TEST LOOP...")
        while True:  # test loop
            try:
                if test_loop_cnt == test_loop_limit + 1:
                    break
                Park4139.commentize(f" TEST LOOP {test_loop_cnt} STARTED")
                test()
                Park4139.commentize(f" TEST LOOP {test_loop_cnt} ENDED")

            except:
                print_with_test_status()
                continue
            test_loop_cnt = test_loop_cnt + 1
            # Park4139.sleep(milliseconds=1000)# 루프 텀 설정

        # 의도적 트러블 발생 테스트
        # raise shutil.Error("의도적 트러블 발생")
    except Exception as e:
        # print(str(e))
        # logger.info(f'logger: dst : {"??????"}')
        # logger.error(msg="에러발생?????")
        # logger.error(f'logger: str(e) : {"????????"}')
        # park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        error_cnt = error_cnt + 1
        error_str = traceback.format_exc()
        Park4139.debug_as_gui(f"TEST LOOP ERROR CNT REPORT:\nerror_cnt : {error_cnt}\nerror_str : {error_str}")
        # Park4139Test.pause()
