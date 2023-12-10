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


def bkup_biggest_targets():
    park4139.commentize(f"biggest_targets에 대한 빽업을 시도합니다")
    for biggest_target in park4139.biggest_targets:
        park4139.bkup(f'{biggest_target}')


def bkup_smallest_targets():
    park4139.commentize(f"smallest_targets에 대한 빽업을 시도합니다")
    for target in park4139.smallest_targets:
        park4139.bkup(f'{target}')


def speak_HH_mm():
    park4139.speak(f"{int(HH)}시")
    park4139.speak(f"{int(mm)}분 입니다")
    pass


def classify_targets_between_smallest_targes_biggest_targets():
    park4139.commentize('빽업할 파일들의 크기를 분류합니다.')
    targets = [
        fr"{park4139.USERPROFILE}\Desktop\services\helper-from-youtube-url-to-webm",
        fr"{park4139.USERPROFILE}\Desktop\services",
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


def gather_storages():
    starting_directory = os.getcwd()
    park4139.commentize("gather_storages")
    dst = rf"{park4139.USERPROFILE}\Desktop\services\storage"
    services = os.path.dirname(dst)
    os.chdir(services)
    storages = []
    cmd = rf'dir /b /s "{park4139.USERPROFILE}\Downloads"'
    lines = park4139.get_cmd_output(cmd)
    for line in lines:
        if line.strip() != "":
            storages.append(line.strip())

    park4139.commentize(rf'archive_py 는 storage 목록 에서 제외')
    withouts = ['archive_py']
    for storage in storages:
        for without in withouts:
            if park4139.is_regex_in_contents(contents=storage, regex=without):
                storages.remove(storage)
    for storage in storages:
        print(storage)

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

    os.chdir(starting_directory)


def kill_alsong():
    park4139.commentize(rf'알송종료를 시도합니다')
    park4139.taskkill('ALSong.exe')
    pass


def do_run_targets_promised():
    try:
        park4139.commentize(f"약속된 타겟들을 실행합니다")
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


def should_i_empty_trash_can():
    # 숨김 휴지통 을 보여드릴까요
    # 숨김 휴지통 열기
    # explorer c:\$RECYCLE.BIN
    # explorer d:\$RECYCLE.BIN
    # explorer e:\$RECYCLE.BIN
    # explorer f:\$RECYCLE.BIN
    # park4139.run_command('explorer.exe shell:RecycleBinFolder')

    # park4139.commentize(rf'휴지통 용량확인 pyautogui RPA')
    # ment = f'현재 휴지통이 10기가 바이트 이상입니다 쓰레기통을 비울까요'
    ment = f'쓰레기통을 비울까요'
    park4139.speak(ment)
    answser = pyautogui.confirm(ment, title='', buttons=[etc.button_ments['yes'], etc.button_ments['no'], etc.button_ments['again']], timeout=1000 * 30)
    print(f'answser >{park4139.indent_space_promised}{answser}')
    if answser == etc.button_ments['yes']:
        ment = f'네 휴지통을 비울게요'
        print(ment)

        park4139.get_cmd_output('PowerShell.exe -NoProfile -Command Clear-RecycleBin -Confirm:$false')

        # 휴지통 삭제 (외장하드까지)
        # for %%a in (cdefghijk L mnopqrstuvwxyz) do (
        # 존재하는 경우 %%a:\$RECYCLE.BIN for /f "tokens=* usebackq" %%b in (`"dir /a:d/b %%a:\$RECYCLE.BIN\"`) do rd / q/s "%%a:\$RECYCLE.BIN\%%~b"
        # 존재하는 경우 %%a:\RECYCLER for /f "tokens=* usebackq" %%b in (`"dir /a:d/b %%a:\RECYCLER\"`) do rd /q/s "%% a:\RECYCLER\%%~b"
        # )
    elif answser == etc.button_ments['no']:
        print('네 쓰레기통을 비우지않을게요')

    elif answser == etc.button_ments['again']:
        print('네 이따가 다시 물을게요')
    else:
        pass

    # 타겟 삭제 with walking
    #  shutil.rmtree(path)
    #  path에 있는 folder를 지우면서 그 안에 있는 모든 파일을 지워준다.

    # 타겟 휴지통으로 이동
    # pip install send2trash
    # send2trash.send2trash('egg.txt')


def should_i_enter_power_saving_mode():
    ment = f'절전모드로 진입할까요'
    # ment = f'절전모드를 가이드할까요'
    # ment = f'절전모드로 진입을 시도할까요'
    park4139.commentize(ment)
    park4139.commentize(ment)
    answser = pyautogui.confirm(ment, title='', buttons=[etc.button_ments['yes'], etc.button_ments['no'], etc.button_ments['again']], timeout=1000 * 30)
    print(f'answser >{park4139.indent_space_promised}{answser}')
    if answser == etc.button_ments['yes']:
        park4139.commentize('네 절전모드로 진입을 시도합니다')
        cmd = rf'%windir%\System32\rundll32.exe powrprof.dll SetSuspendState'
        park4139.get_cmd_output(cmd)
    elif answser == etc.button_ments['no']:
        park4139.commentize('네 진입을 하지 않겠습니다')
    elif answser == etc.button_ments['again']:
        park4139.commentize('네 나중에 다시 물을게요')
    else:
        pass


def decorate_ment_about_time(do_routine_hh_mm):
    def wrapper():
        park4139.commentize(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다')
        do_routine_hh_mm()

    return wrapper


@decorate_ment_about_time
def do_routine_06_30():
    park4139.commentize(f'아침음악을 준비합니다')
    park4139.commentize(f'아침음악을 재생할게요')
    park4139.sleep(milliseconds=5000)
    park4139.commentize(f'세수와 양치를 하셨나요')


@decorate_ment_about_time
def do_routine_07_30():
    park4139.commentize('지금 나가지 않는 것은')
    park4139.commentize('지각할 수 있습니다')
    park4139.commentize('더이상 나가는 것을 지체하기 어렵습니다')


@decorate_ment_about_time
def do_routine_08_50():
    park4139.commentize('업무시작 10분전입니다')
    park4139.commentize('업무준비를 시작하세요')
    pass


@decorate_ment_about_time
def do_routine_09_00():
    park4139.commentize('근무시간이므로 음악을 종료합니다')
    # taskkill('Music.UI.exe'])
    # taskkill('ALSong.exe'])
    pass


@decorate_ment_about_time
def do_routine_11_30():
    park4139.commentize('점심시간입니다')
    park4139.commentize('음악을 재생합니다')


def speak_yyyy_MM_dd_HH_mm():
    park4139.speak(f'현재 날짜와 시각은')
    park4139.speak(f'{int(yyyy)}년 {int(MM)}월 {int(dd)}일 {int(HH)}시 {int(mm)}분 입니다')


def change_console_color():
    park4139.commentize("콘솔의 색상을 바꿔볼게요")
    park4139.toogle_console_color(color_bg='0', colors_texts=['7', 'f'])


def do_random_schedules():
    park4139.commentize("랜덤 스케쥴을 수행합니다")
    # 정상이 아닌것 같은데 마치 비동기 실행이 됨.
    # random_schedules = [
    #     should_i_empty_trash_can(),
    #     speak_yyyy_MM_dd_HH_mm(),
    #     change_console_color(),
    #     bkup_smallest_targets(),
    #     speak_HH_mm(),
    #     gather_storages(),
    #     kill_alsong(),
    # ]
    # random_no = random.randrange(0, len(random_schedules))  # 0에서 7 사이의 수
    # random_schedules[random_no]

    # 정상이 아닌것 같은데 마치 비동기 실행이 됨.
    random_schedules = [
        speak_yyyy_MM_dd_HH_mm,
        speak_HH_mm, 
    ]
    random_no = random.randrange(0, len(random_schedules))  # 0에서 7 사이의 수
    random_schedules[random_no]



@decorate_ment_about_time
def do_routine_13_00():
    park4139.speak('기분좋아지도록 노동요를 재생합니다')
    park4139.get_cmd_output(r'explorer "C:\Users\WIN10PROPC3\Desktop\services\storage\음악모음.dpl"')

@decorate_ment_about_time
def do_routine_22_10():
    park4139.commentize('씻으실 것을 추천드립니다')
    park4139.commentize('샤워루틴을 수행하실 것을 추천드립니다')
    park4139.commentize('샤워루틴을 보조를 수행할까요')

@decorate_ment_about_time
def do_routine_22_40():
    park4139.commentize('지금 누우실 것을 추천드립니다')
    park4139.commentize('건강을 위해서 씻고 주무실 것을 추천드립니다')

@decorate_ment_about_time
def do_routine_24_00():
    speak_yyyy_MM_dd_HH_mm()
    bkup_biggest_targets()


def do_routine_that_to_make_developer_go_to_sleep():
    park4139.speak('너무 늦은 시간입니다.')
    if random.random() >= 0.5:
        park4139.speak('건강을 위해서 자는 것이 좋습니다')
        park4139.speak('더 나은 삶을 위해 주무셔야 합니다')
    if random.random() >= 0.5:
        park4139.speak('개발을 하고 있는 것이라면 지금 자고 나서')
        park4139.speak('일찍일어나 코드를 작성하는 것이 좋습니다')
        should_i_enter_power_saving_mode()
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
    if random.random() >= 0.5:
        park4139.speak('새벽 입니다')
        park4139.speak('이제 그만 주무세요 정말로')
    if random.random() >= 0.5:
        park4139.speak('아무래도 안되겠군요')
        park4139.speak('이제 하나씩 종료를 할겁니다')
        park4139.speak('팟플레이어를 종료합니다')
        park4139.speak('알송을 종료합니다')
        park4139.speak('개발 도구를 종료합니다')


def decorate_ment_about_routine_per_x_mins(do_routine_per_x_mins):
    def wrapper(args: int):
        park4139.commentize(f'{args}분 간격 루틴을 시작합니다')
        do_routine_per_x_mins(args)

    return wrapper


@decorate_ment_about_routine_per_x_mins
def do_routine_per_30_mins(per_x_mins: int):
    ment = f'깃허브로 파이썬 아카이브 프로젝트 빽업을 시도합니다'
    park4139.commentize(ment)
    park4139.commentize(ment)
    try:
        cmd = fr'start cmd /c call "{park4139.USERPROFILE}\Desktop\services\archive_py\git push by manual.bat"'
        park4139.get_cmd_output(cmd)
    except Exception as e:
        park4139.trouble_shoot('20231203131321')


@decorate_ment_about_routine_per_x_mins
def do_routine_per_60_mins(per_x_min: int):
    should_i_empty_trash_can()


def is_accesable_local_database(db_abspath: str, db_template: str):
    if not os.path.exists(db_abspath):
        park4139.create_db_toml(db_abspath=db_abspath, db_template=db_template)
        return False
    else:
        return True


try:
    if __name__ == "__main__":
        loop_cnt = 0
        target_abspath = fr'{park4139.USERPROFILE}\Desktop\services\archive_py\parks2park_archive.log'
        key = "parks2park_archive_log_line_cnt"
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
                # do_run_targets_promised()

                # park4139.commentize("로컬 데이터베이스 접근 테스트를 시도합니다")
                if not is_accesable_local_database(db_template=park4139.db_template, db_abspath=park4139.db_abspath):
                    park4139.commentize("로컬 데이터베이스에 접근이 가능하도록 설정합니다")

                classify_targets_between_smallest_targes_biggest_targets()

                park4139.monitor_target_edited_and_bkup(target_abspath=target_abspath, key=key)

                # park4139.commentize(title = '전역 pkg_park4139 업데이트')
                # 이 메소드는 프로젝트 내에 지역적으로 위치한 pkg_park4139 하나만 관리해도
                # global site-packages에 위치한 pkg_park4139 동기화를 시켜 pycharm 자동완성 기능 가능.
                # 이제는 더이상 필요없는 함수가 되었는데 타겟의 업데이트가 필요한 경우 상속하거나 변형해 쓰면 되겠다
                # park4139.update_global_pkg_park4139()

            # 루프 카운트 갱신
            loop_cnt = loop_cnt + 1
            # print(f"loop_cnt : {loop_cnt}")
            print(loop_cnt)

            # 0시에서 24시 사이,
            if 0 <= int(HH) <= 24:
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
                        target_abspath = fr'{park4139.USERPROFILE}\Desktop\services\archive_py\parks2park_archive.log'
                        key = "parks2park_archive_log_line_cnt"
                        park4139.monitor_target_edited_and_bkup(target_abspath=target_abspath, key=key)

                # 1분 마다
                if int(mm) % 1 == 0:
                    do_random_schedules()

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
        #   commentize(ment)
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

