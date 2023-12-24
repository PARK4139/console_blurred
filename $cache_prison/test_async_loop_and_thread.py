__author__ = 'PARK4139 : Jung Hoon Park'

import random
# -*- coding: utf-8 -*-  # python 3.x 하위버전 호환을 위한코드
import sys
import time
import traceback
from functools import partial

import pynput
import schedule
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import pkg_park4139

Park4139 = pkg_park4139.Park4139()


# LOGGER SET UP
# logger = logging.getLogger('park4139_test_logger')
# hdlr = logging.FileHandler('park4139_logger.log')
# hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)


@Park4139.decorate_seconds_performance_measuring_code
def generate_mp3_file_for_time_performance():  # time performance : 9028 초 /60 /60  =  2.5 시간
    """
    시간에 대한 mp3 파일 작업 최적화 함수
    """
    for HH in range(24, 0, -1):
        for mm in range(0, 60):
            Park4139.commentize(f'{int(HH)}시')
            Park4139.commentize(f'{int(mm)}분 입니다')


# park4139.commentize() 메소드 테스트 결과, 1개 파일을 만들어 실행하는 데까지 무려 11초 정도로 측정됨, ffmpeg 작업 속도로 문제
# 의도적으로 mp3 파일을 미리 만들어, ffmpeg 로 두 파일 합성작업 시간을 줄일수 있으므로, 성능 최적화 기대,
# 따라서, 코드에서 사용되는 모든 텍스트를 추출하여 park4139.commentize 하도록 하여, 최적화시도해보자
# 번외로 리스트의 파라미터를 몇개까지 가능하지 테스트 해보고 싶긴한데, 망가져도 되는 컴퓨터로 시도해보자




def decorate_for_pause(function):
    """
        # ctrl c ctrl c 이렇게 두번 눌르면 소스 수정 후 재시작 됩니다
        # 안그럼 계속 새롭게 창을 무한정 열게 되어 컴퓨터가 다운될 수 있습니다.
    """

    def wrapper():
        function()
        Park4139.pause()

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
@Park4139.decorate_seconds_performance_measuring_code
@decorate_for_pause  # 테스트 루프 마다 정지 설정
def test():
    try:
        # app = QApplication()  # set this if necessary in test
        while True:
            # dialog = pkg_park4139.CustomDialogReplica(contents="테스트를 시작할까요?", buttons=["시작하기", "시작하지 않기"])
            # dialog.exec_()
            # text_of_clicked_btn = dialog.text_of_clicked_btn
            # if text_of_clicked_btn == "시작하기":

            text_of_clicked_btn =None
            if text_of_clicked_btn == None:
                # _________________________________________  UP (TESTED SUCCESS) _________________________________________
                # 내가 원하는건 그게 아니고 리스너에 우선순위를 부여하고 싶어.
                # 만약 리스너2가 우선순위가 높게 설정한면 on_press  조건이면 둘 다 호출조건이 만족되기 때문에 리스너1과 리스너2가 동시에 호출되겠지?
                # 하지만 그상황에서는 우선순위가 높은 리스너 2만 호출이 되도록 하고 싶어

                import asyncio
                import threading

                # 비동기 이벤트 함수 실행
                async def async_function():
                    print("async_function s")
                    await asyncio.sleep(5)   # 비동기 이벤트 함수 내에서는 time.sleep() 대신 await asyncio.sleep(5)를 사용
                    print("async_function e")

                # 비동기 이벤트 함수 실행
                async def async_function2():
                    print("async_function2 s")
                    await asyncio.sleep(10)
                    print("async_function2 e")

                # 비동기 이벤트 루프 실행
                def run_async_loop1():
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(async_function())

                def run_async_loop2():
                    loop2 = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop2)
                    loop2.run_until_complete(async_function2())

                # 비동기 이벤트 루프 실행할 쓰레드 실행
                if __name__ == "__main__":

                    # java 공부할때는 뭔말인지 하나도 모르겠던 쓰레드도
                    # python에서 테스트를 이것 저것 해보니 이해도 되고
                    # 어떻게 써야할지 감이 오는 것 같다.
                    # 쓰레드를 같이 사용된 타이밍이 요상해진다.
                    # 내가 관찰한 것에서 핵심은 쓰레드는 단지 종료가 제각각이라는 부분이다. 자기 할일을 마치면 쓰레드는 종료된다. 이게 그토록 구현하고자 했던 비동기처리 방법이다.
                    # 빨리일을 맞추기 위한
                    # 추가적으로, 꼭 특정쓰레드 뒤에 동작해야하는 코드가 있다면 그 코드의 앞에 thread.join() 를 작성하면 되겠다.

                    Park4139.sleep(3000)
                    print(10)
                    print(5)

                    thread2 = threading.Thread(target=run_async_loop2)
                    thread2.start()

                    Park4139.sleep(3000)

                    print(2)
                    print(4)

                    thread = threading.Thread(target=run_async_loop1)
                    thread.start()

                    thread.join()
                    print(9)
                    print(9)

                # _________________________________________ BELOW (NOT TESTED YET) _________________________________________
                break
            else:
                break
        # app.exec()  # set this if necessary in test
        pass

    except SystemExit:  # sys.exit() 호출을 의도적으로 판단
        pass
    except:
        Park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        Park4139.pause()


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
                Park4139.trouble_shoot(f'%%%FOO%%%')
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
        # Park4139.pause()
