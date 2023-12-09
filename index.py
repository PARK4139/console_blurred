# -*- coding: utf-8 -*-
import sys
import os
import random

import pyautogui

import traceback
import traceback
import pkg_park4139

__author__ = 'Park4139 : Jung Hoon Park'
this_file_dirname = os.path.dirname(os.path.abspath(__file__))
park4139 = pkg_park4139.Park4139()
etc = pkg_park4139.etc()

# STARTING LOGGING SET UP
park4139.log_s()

# 이걸로 특정 랜덤태스크를 하루에 몇 번까지 제한하도록 관리
daily_random_tasks = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]


def decorate_ments_about_lotto(do_schedule_x):
    def wrapper(args):
        park4139.speak(f"{str(args)}번 스케쥴 당첨되었습니다")
        do_schedule_x(args)
        if random.random() >= 0.5:
            park4139.speak(f"다음 랜덤 스케쥴 로또를 기대하세요")

    return wrapper


@decorate_ments_about_lotto
def do_schedule_2(schedule_no: int):
    should_i_empty_trash_can()
    pass


@decorate_ments_about_lotto
def do_schedule_3(schedule_no: int):
    park4139.speak(f'현재 날짜와 시각은')
    park4139.speak(f'{yyyy}년 {int(MM)}월 {int(dd)}일 {int(HH)}시 {int(mm)}분 입니다')
    pass


@decorate_ments_about_lotto
def do_schedule_4(schedule_no: int):
    park4139.speak("콘솔의 색상을 바꿔볼게요")
    park4139.toogle_console_color(color_bg='0', colors_texts=['7', 'f'])
    pass


@decorate_ments_about_lotto
def do_schedule_5(schedule_no: int):
    park4139.speak(f"꽝입니다")
    pass


@decorate_ments_about_lotto
def do_schedule_55(schedule_no: int):
    # park4139.speak(f"용량이 큰 타겟에 대한 빽업을 시도합니다")
    park4139.speak(f"300 메가바이트 이상 타겟에 대한 빽업을 시도합니다")
    try:
        for biggest_target in park4139.biggest_targets:
            park4139.bkup(f'{biggest_target}')
        pass
    except:
        park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        park4139.pause()


@decorate_ments_about_lotto
def do_schedule_56(schedule_no: int):
    # park4139.speak(f"용량이 작은 타겟에 대한 빽업을 시도합니다")
    park4139.speak(f"300 메가바이트 미만 타겟에 대한 빽업을 시도합니다")
    park4139.commentize('300메가 이하 타겟 빽업 시도')
    for target in park4139.smallest_targets:
        park4139.bkup(f'{target}')
    pass


@decorate_ments_about_lotto
def do_schedule_57(schedule_no: int):
    park4139.speak(f"{int(HH)}시")
    park4139.speak(f"{int(mm)}분 입니다")
    pass


@decorate_ments_about_lotto
def do_schedule_58(schedule_no: int):
    park4139.speak('빽업할 파일들의 크기를 분류합니다.')
    targets = [
        fr"{park4139.USERPROFILE}\Desktop\services\helper-from-youtube-url-to-webm",
        fr"{park4139.USERPROFILE}\Desktop\services\helper-from-youtube-url-to-webm",
    ]
    park4139.commentize('biggest_targets(300 메가 초과), smallest_targets(300 메가 이하) 분류 시도')
    for target in targets:
        target_size_megabite = park4139.get_target_megabite(target.strip())
        print(target_size_megabite)
        if target_size_megabite <= 300:
            park4139.smallest_targets.append(target.strip())

        elif 300 < target_size_megabite:
            park4139.biggest_targets.append(target.strip())
        else:
            print(f'{target.strip()}pass')

    park4139.commentize('smallest_target 출력')
    # targets 에서 biggest_targets 과 일치하는 것을 소거 시도
    smallest_targets = [i for i in targets if i not in park4139.biggest_targets]
    for target in park4139.smallest_targets:
        print(target)

    park4139.commentize('biggest_target 출력')
    for target in park4139.biggest_targets:
        print(target)
    pass


@decorate_ments_about_lotto
def do_schedule_59(schedule_no: int):
    park4139.speak("흩어져있는 storage 들을 한데 모으는 시도를 합니다")
    park4139.commentize(rf'목적지 설정')
    dst = rf"{park4139.USERPROFILE}\Desktop\services\storage"

    park4139.commentize(rf'서비스 디렉토리로 이동')
    services = rf'{park4139.USERPROFILE}\Desktop\services'
    os.chdir(services)
    print(services)

    park4139.commentize(rf'여기저기 흩어져있는 storage  한데 모으기 시도')
    storages = []
    cmd = rf'dir /b /s "{park4139.USERPROFILE}\Downloads"'
    lines = park4139.get_cmd_output(cmd)
    for line in lines:
        if line.strip() != "":
            storages.append(line.strip())
    lines = park4139.get_cmd_output(rf'dir /b /a:d "{services}"')
    for line in lines:
        if line.strip() != "":
            storages.append(rf'{line.strip()}\storage')

    # for storage in storages:
    #     print(rf"{services}\{storage}")
    # park4139.pause()

    park4139.commentize(rf'archive_py 는 storage 목록 에서 제외합니다')
    withouts = ['archive_py']
    for storage in storages:
        for without in withouts:
            if park4139.is_regex_in_contents(contents=storage, regex=without):
                storages.remove(storage)
                print(os.path.abspath(storage))

    park4139.commentize(rf'이동할 storage 목록 중간점검 출력 시도')
    for storage in storages:
        print(os.path.abspath(storage))

    if not storages:
        park4139.commentize(rf'이동할 storage 목록 이 없어 storage 이동을 할 수 없습니다')
    else:
        park4139.commentize(rf'이동할 storage 목록 출력 시도')
        for storage in storages:
            print(os.path.abspath(storage))
        park4139.commentize(rf'목적지 생성 시도')
        if not os.path.exists(dst):
            os.makedirs(dst)
        for storage in storages:
            # print(src)
            try:
                park4139.commentize(rf'storage 이동 시도')
                park4139.move_without_overwrite(storage, dst)
            except FileNotFoundError:
                park4139.trouble_shoot('202312071430')
                traceback.print_exc(file=sys.stdout)
            except Exception as e:
                park4139.trouble_shoot('20231205095308')
                traceback.print_exc(file=sys.stdout)
                os.system('pause')
    pass


@decorate_ments_about_lotto
def do_schedule_60(schedule_no: int):
    park4139.speak(rf'알송종료를 시도합니다')
    park4139.commentize(rf'알송종료를 시도합니다')
    park4139.taskkill('ALSong.exe')
    print(f"{park4139.indent_space_promised}park4139.taskkill('ALSong.exe')")
    print("")
    pass




def do_run_targets_promised():
    try:
        park4139.speak(f"약속된 타겟들을 실행합니다")
        targets = [
            # rf'C:\Python312\Lib\site-packages\pkg_park4139\__init__.py', # 업데이트 시켜두었으므로 이제 실행해볼 필요 없음,파이선 폴더 동기화 시켜도록 시도해보자
            # rf'{park4139.USERPROFILE}\Desktop\services\archive_py\parks2park_archive.log',
            rf"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.3.lnk",
            rf"{park4139.USERPROFILE}\Desktop\services\archive_py",
            rf"{park4139.USERPROFILE}\Desktop\services",
        ]
        for target in targets:
            park4139.get_cmd_output(fr'explorer "{target}"')
    except:
        park4139.trouble_shoot("%%%FOO%%%")
        traceback.print_exc(file=sys.stdout)
        park4139.pause()


def monitor_target_edited_and_bkup(target_abspath:str, key :str):


    park4139.speak(f'{os.path.basename(target_abspath)} 빽업시도')


    db_abspath = park4139.db_abspath
    if park4139.is_target_edited(target_abspath, key)==True:
        park4139.speak("빽업을 수행합니다")
        park4139.bkup(target_abspath)
        park4139.update_db_toml(key=key, value=park4139.get_line_cnt_of_file(target_abspath), db_abspath=db_abspath)
    if park4139.is_target_edited(target_abspath, key) ==None:
        park4139.speak("데이터베이스 key가 없어 key를 생성합니다")
        park4139.insert_db_toml(key=key, value=park4139.get_line_cnt_of_file(target_abspath), db_abspath=db_abspath)




def should_i_empty_trash_can():
    # 숨김 휴지통 을 보여드릴까요
    # 숨김 휴지통 열기
    # explorer c:\$RECYCLE.BIN
    # explorer d:\$RECYCLE.BIN
    # explorer e:\$RECYCLE.BIN
    # explorer f:\$RECYCLE.BIN
    # park4139.run_command('explorer.exe shell:RecycleBinFolder')

    # park4139.commentize(rf'휴지통 용량확인 pyautogui RPA')

    park4139.commentize(rf'휴지통 비울지 질의')
    ment = f'현재 휴지통이 10기가 바이트 이상입니다 쓰레기통을 비울까요'
    park4139.speak(ment)
    answser = pyautogui.confirm(ment, title='', buttons=[etc.button_ments['yes'], etc.button_ments['no'], etc.button_ments['again']], timeout=1000 * 30)
    print(f'answser >{park4139.indent_space_promised}{answser}')
    if answser == etc.button_ments['yes']:
        ment = f'네 휴지통을 비울게요'
        park4139.speak(ment)
        try:
            park4139.get_cmd_output('PowerShell.exe -NoProfile -Command Clear-RecycleBin -Confirm:$false')
        except Exception as e:
            park4139.trouble_shoot('20231204155143')

        # 휴지통 삭제 (외장하드까지)
        # for %%a in (cdefghijk L mnopqrstuvwxyz) do (
        # 존재하는 경우 %%a:\$RECYCLE.BIN for /f "tokens=* usebackq" %%b in (`"dir /a:d/b %%a:\$RECYCLE.BIN\"`) do rd / q/s "%%a:\$RECYCLE.BIN\%%~b"
        # 존재하는 경우 %%a:\RECYCLER for /f "tokens=* usebackq" %%b in (`"dir /a:d/b %%a:\RECYCLER\"`) do rd /q/s "%% a:\RECYCLER\%%~b"
        # )
    elif answser == etc.button_ments['no']:
        park4139.speak('네 쓰레기통을 비우지않을게요')

    elif answser == etc.button_ments['again']:
        park4139.speak('네 이따가 다시 물을게요')
    else:
        pass

    # 타겟 삭제 with walking
    #  shutil.rmtree(path)
    #  path에 있는 folder를 지우면서 그 안에 있는 모든 파일을 지워준다.

    # 타겟 휴지통으로 이동
    # pip install send2trash
    # send2trash.send2trash('egg.txt')


def should_i_enter_power_saving_mode():
    ment = f'절전모드를 가이드할까요'
    # ment = f'절전모드로 진입을 시도할까요'
    # ment = f'절전모드로 진입할까요'
    park4139.speak(ment)
    park4139.commentize(ment)
    answser = pyautogui.confirm(ment, title='', buttons=[etc.button_ments['yes'], etc.button_ments['no'], etc.button_ments['again']], timeout=1000 * 30)
    print(f'answser >{park4139.indent_space_promised}{answser}')
    if answser == etc.button_ments['yes']:
        park4139.speak('네 절전모드로 진입을 시도합니다')
        cmd = rf'%windir%\System32\rundll32.exe powrprof.dll SetSuspendState'
        park4139.get_cmd_output(cmd)
    elif answser == etc.button_ments['no']:
        park4139.speak('네 진입을 하지 않겠습니다')
    elif answser == etc.button_ments['again']:
        park4139.speak('네 나중에 다시 물을게요')
    else:
        pass


def decorate_ment_about_time(do_routine_hh_mm):
    def wrapper():
        park4139.speak(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다')
        do_routine_hh_mm()

    return wrapper


@decorate_ment_about_time
def do_routine_06_30():
    park4139.speak(f'아침음악을 준비합니다')
    park4139.speak(f'아침음악을 재생할게요')
    park4139.sleep(milliseconds=5000)
    park4139.speak(f'세수와 양치를 하셨나요')


@decorate_ment_about_time
def do_routine_07_30():
    park4139.speak('지금 나가지 않는 것은')
    park4139.speak('지각할 수 있습니다')
    park4139.speak('더이상 나가는 것을 지체하기 어렵습니다')


@decorate_ment_about_time
def do_routine_08_50():
    park4139.speak('업무시작 10분전입니다')
    park4139.speak('업무준비를 시작하세요')
    pass


@decorate_ment_about_time
def do_routine_09_00():
    park4139.speak('근무시간이므로 음악을 종료합니다')
    # taskkill('Music.UI.exe'])
    # taskkill('ALSong.exe'])
    pass


@decorate_ment_about_time
def do_routine_11_30():
    park4139.speak('점심시간입니다')
    park4139.speak('음악을 재생합니다')


def do_random_schedules():
    if random.random() >= 0.5:
        park4139.speak(f"랜덤 스케쥴 로또를 돌릴 시간이 찾아왔습니다")
    park4139.speak(f"랜덤 스케쥴 로또를 돌립니다")
    if random.random() >= 0.5:
        park4139.speak(f"두구두구두")
    if random.random() >= 0.5:
        park4139.speak(f"어떤숫자가 나올까요")
    while True:

        random_no = random.randrange(1, 101)  # 1에서 100 사이의 수
        if random_no == 1:
            park4139.speak(f"1번 당첨입니다")
            park4139.speak(f"이번엔 특별히 쉬세요")
            break
        elif random_no == 2:
            do_schedule_2(2)
            break
        elif random_no == 3:
            do_schedule_3(3)
            break
        elif random_no == 4:
            do_schedule_4(4)
            break
        elif random_no == 5:
            do_schedule_5(5)
            break
        elif random_no == 55:
            do_schedule_55(55)
            break
        elif random_no == 56:
            do_schedule_56(56)
            break
        elif random_no == 57:
            do_schedule_57(57)
            break
        elif random_no == 58:
            do_schedule_58(58)
            break
        elif random_no == 59:
            do_schedule_59(59)
            break
        elif random_no == 60:
            do_schedule_60(60)
            break
        else:
            park4139.speak(f"꽝입니다")
            if random.random() >= 0.5:
                park4139.speak(f"다시 랜덤 스케쥴 로또를 돌립니다")
            else:
                park4139.speak(f"나올때까지 계속 돌릴겁니다")




@decorate_ment_about_time
def do_routine_24_00():
    park4139.speak(f'{int(yyyy)}년 {int(MM)}월 {int(dd)}일 {int(HH)}시 {int(mm)}분 입니다')


@decorate_ment_about_time
def do_routine_13_00():
    park4139.speak('기분좋아지도록 음악을 재생합니다')


@decorate_ment_about_time
def do_routine_22_10():
    park4139.speak('씻으실 것을 추천드립니다')
    park4139.speak('샤워루틴을 수행하실 것을 추천드립니다')
    park4139.speak('샤워루틴을 보조를 수행할까요')


@decorate_ment_about_time
def do_routine_22_40():
    park4139.speak('지금 누우실 것을 추천드립니다')
    park4139.speak('건강을 위해서 씻고 주무실 것을 추천드립니다')


def do_routine_that_to_make_developer_go_to_sleep():
    if int(HH) != 2 and int(mm) != 00:
        park4139.speak('너무 늦은 시간입니다.')
        if random.random() >= 0.5:
            park4139.speak('건강을 위해서 자는 것이 좋습니다')
            park4139.speak('더 나은 삶을 위해 주무셔야 합니다')
        if random.random() >= 0.5:
            park4139.speak('개발을 하고 있는 것이라면 지금 자고 나서')
            park4139.speak('일찍일어나 코드를 작성하는 것이 좋습니다')
            if random.random() >= 0.5:
                if loop_cnt % 2 == 0:
                    park4139.speak('늦게까지 개발하고 일찍일어 나지 못할 것이라면요')
                else:
                    # park4139.speak('늦게까지하고 일찍일어 나는 것도 아니니까요')
                    park4139.speak('늦게까지 개발하고 못 일어날 거잖아요')
            else:
                park4139.speak('늦게까지 개발하고 내일 너무 피곤하지 않을까요')
                if random.random() >= 0.5:
                    park4139.speak('내일 하루를 망쳐버릴 수도 있어요')
    else:
        park4139.speak('새벽 입니다')
        park4139.speak('이제 그만 주무세요 정말로')

    should_i_enter_power_saving_mode()
    if random.random() >= 0.5:
        park4139.speak('아무래도 안되겠군요')
        park4139.speak('이제 하나씩 종료를 할겁니다')
        park4139.speak('개발도구를 종료합니다')
        park4139.speak('팟플레이어를 종료합니다')
        # park4139.speak('알송을 종료합니다')


def decorate_ment_about_routine_per_x_mins(do_routine_per_x_mins):
    def wrapper(args : int):
        park4139.speak(f'{args}분 간격 루틴을 시작합니다')
        do_routine_per_x_mins(args)
    return wrapper


@decorate_ment_about_routine_per_x_mins
def do_routine_per_30_mins(per_x_mins: int):
    ment = f'깃허브로 아카이브 파이 빽업을 시도합니다'
    park4139.commentize(ment)
    park4139.speak(ment)
    try:
        cmd = fr'start cmd /c call "{park4139.USERPROFILE}\Desktop\services\archive_py\git push by manual.bat"'
        park4139.get_cmd_output(cmd)
    except Exception as e:
        park4139.trouble_shoot('20231203131321')


@decorate_ment_about_routine_per_x_mins
def do_routine_per_60_mins(per_x_min: int):
    should_i_empty_trash_can()


def check_local_database():
    park4139.speak("로컬 데이터베이스 접근 테스트를 시도합니다")
    if not os.path.exists(park4139.db_abspath):
        park4139.speak("로컬 데이터베이스 접근이 불가능합니다")
        park4139.speak("접근이 가능하도록 설정합니다")
        park4139.create_db_toml(target_abspath=park4139.db_abspath, db_template=park4139.db_template)
    else:
        park4139.speak("로컬 데이터베이스에 접근이 가능한 상태입니다")

try:
    if __name__ == "__main__":
        loop_cnt = 0
        try:
            os.chdir(park4139.working_directory)
            # park4139.speak(f"자동화 프로그램이 시작되었습니다")
            # park4139.commentize(f"자동화 프로그램이 시작되었습니다")
        except Exception as e:
            park4139.trouble_shoot("202312071431")
            traceback.print_exc(file=sys.stdout)
            park4139.pause()

        while True:
            # 가능한 짧은 시간 마다(루프마다)
            yyyy = park4139.get_time_as_('%Y')
            MM = park4139.get_time_as_('%m')
            dd = park4139.get_time_as_('%d')
            HH = park4139.get_time_as_('%H')
            mm = park4139.get_time_as_('%M')
            ss = park4139.get_time_as_('%S')
            server_time = park4139.get_time_as_(rf'%Y-%m-%d %H:%M:%S')

            # 한번만
            if loop_cnt == 0:
                # 테스트는 여기에서

                check_local_database()

                do_run_targets_promised()

                # park4139.commentize(title = '전역 pkg_park4139 업데이트')
                # 이 메소드는 프로젝트 내에 지역적으로 위치한 pkg_park4139 하나만 관리해도
                # global site-packages에 위치한 pkg_park4139 동기화를 시켜 pycharm 자동완성 기능 가능.
                # 이제는 더이상 필요없는 함수가 되었는데 타겟의 업데이트가 필요한 경우 상속하거나 변형해 쓰면 되겠다
                # park4139.update_global_pkg_park4139()

            # 루프 카운트 갱신
            loop_cnt = loop_cnt + 1

            # 0시에서 24시 사이,
            if 0 <= int(HH) and int(HH) <= 24:
                # 6시 30분
                if int(HH) == 6 and int(mm) == 30:
                    do_routine_06_30()
                # 7시 30분
                if int(HH) == 7 and int(mm) == 30:
                    do_routine_07_30()
                # 8시 50분
                if int(HH) == 8 and int(mm) == 50:
                    do_routine_08_50()
                if int(HH) == 9 and int(mm) == 0:
                    do_routine_09_00()
                # 11시 30분
                if int(HH) == 11 and int(mm) == 30:
                    do_routine_11_30()
                if int(HH) == 13 and int(mm) == 00:  # 0이 아닌 00 으로도 동작하는 지 실험
                    do_routine_13_00()
                # 22시 10분
                if int(HH) == 22 and int(mm) == 10:
                    do_routine_22_10()
                # 22시 30분
                if int(HH) == 22 and int(mm) == 30:
                    do_routine_22_40()
                # 24시이면
                if int(HH) == 24 and int(mm) == 0 and int(ss) == 0:
                    do_routine_24_00()
                    # 5초 마다
                if int(ss) % 5 == 0:
                    if loop_cnt == 1:
                        park4139.speak(f"5초마다 자동빽업 루틴을 수행합니다")
                    monitor_target_edited_and_bkup()
                    # 5분 마다
                if int(mm) % 5 == 0:
                    if loop_cnt == 1:
                        park4139.speak(f"5분 마다 랜덤 스케쥴 루틴을 수행합니다")
                    try:
                        do_random_schedules()
                    except Exception as e:
                        park4139.trouble_shoot("%%%FOO%%%")
                        traceback.print_exc(file=sys.stdout)
                        park4139.pause()
                    pass
                    # 30분 마다
                if int(mm) % 30 == 0:
                    do_routine_per_30_mins(30)
                    # 60분 마다
                if int(mm) % 60 == 0:
                    do_routine_per_60_mins(60)
                    pass

                # 0시에서 4시 사이, 30분 마다
                # if 0 <= int(HH) <= 4 and int(mm) % 30 == 0:
                #     pass

                # 0시에서 4시 사이, 30초 마다
                if 0 <= int(HH) <= 4:
                    if int(ss) % 30 == 0:
                        do_routine_that_to_make_developer_go_to_sleep()

            # 루프 휴식
            park4139.sleep(milliseconds=1000)
        # 1년에 한번 수행 아이디어
        # random_schedule.json 에서 leaved_max_count를 읽어온다
        # leaved_max_count=1 이면 년에 1번 수행 하도록
        # leaved_max_count=10 이면 년에 10번 수행 하도록
        # leaved_max_count=0 이면 올해에는 더이상 수행하지 않음
        # leaved_max_count 를 random_schedule_tb.toml 에 저장

        # - 1시간 뒤 시스템 종료 예약 기능
        # - 즉시 시스템 종료 시도 기능
        # - 시간 시현기능 기능(autugui 이용)
        #   ment ='pc 정밀검사를 한번 수행해주세요'
        #   speak(ment)
        # - 하드코딩된 스케줄 작업 수행 기능
        # - 미세먼지 웹스크래핑 기능
        # - 초미세먼지 웹스크래핑 기능
        # - 종합날씨 웹스크래핑 기능
        # - 습도 웹스크래핑 기능
        # - 체감온도 웹스크래핑 기능
        # - 현재온도 웹스크래핑 기능
        # - 음악재생 기능
        # - 영상재생 기능

except Exception as e:
    park4139.trouble_shoot("%%%FOO%%%")
    traceback.print_exc(file=sys.stdout)
    park4139.pause()

# ENDING LOGGING SET UP
park4139.log_e()
park4139.pause()