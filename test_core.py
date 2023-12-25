import os
import string

from PyInstaller.compat import win32api

import pkg_park4139

Park4139 = pkg_park4139.Park4139()


def prisonize_storage():
    while True:
        dialog = pkg_park4139.CustomDialog(contents="순회하며 분류할 타겟경로를 입력하세요", buttons=["입력", "입력하지 않기"], is_input_text_box=True)
        dialog.exec_()
        text_of_clicked_btn = dialog.text_of_clicked_btn
        if text_of_clicked_btn == "입력":
            target_abspath = dialog.box_for_editing_input_text.text()
            target_abspath = target_abspath.strip()
            target_abspath = target_abspath.replace("\"", "")
            target_abspath = target_abspath.replace("\'", "")
            connected_drives = []
            for drive_letter in string.ascii_uppercase:
                drive_path = drive_letter + ":\\"
                if os.path.exists(drive_path):
                    connected_drives.append(drive_path)
                    if target_abspath == drive_path:
                        Park4139.speak("입력된 타겟경로는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다")
                        break
            if not os.path.exists(target_abspath):
                Park4139.speak("입력된 타겟경로가 존재하지 않습니다")
                break
            if target_abspath == "":
                break
            Park4139.speak("타겟경로를 순회하며 리프 디렉토리만 예약된 폴더로 모읍니다")
            dst = rf"D:\$cache_prisonized\$leaf_directories"
            leaf_directories = []
            if os.path.isdir(target_abspath):
                for dirpath, dirnames, filenames in os.walk(target_abspath, topdown=False):
                    if not dirnames and not filenames:
                        # 하위디렉토리도 없고, 파일도 없는 경우만 leaf directory 로 간주
                        leaf_directories.append(dirpath)
                        print(f"leaf_directory : {dirpath}")
                        Park4139.move_without_overwrite(src=dirpath, dst=dst)
            # for leaf_directory in leaf_directories:
            #     Park4139.move_without_overwrite(src=leaf_directory, dst=dst)


            # Park4139.speak("타겟경로를 순회하며 빈폴더를 예약된 폴더로 모읍니다")
            # dst = rf"D:\$cache_prisonized\$empty_directories"
            # if os.path.isdir(target_abspath):
            #     if not os.listdir(target_abspath):  # os.listdir 은 without walking 으로 동작한다
            #         print(rf"empty_directory : {target_abspath}")
            #         # Park4139.move_without_overwrite(src=target_abspath, dst=dst)
            #         # 디렉토리 머지 without_overwrite(
            #
            # Park4139.speak("타겟경로를 순회하며 예약된 불필요한 파일을 예약된 폴더로 모읍니다")
            # useless_files = [
            #     "最 新 位 址 獲 取.txt",
            #     "聚 合 全 網 H 直 播.html",
            #     "社 區 最 新 情 報.mp4",
            #     "x u u 9 2 .c o m.mp4",
            #     "PotPlayerMini64.dpl",
            #     "PRARBG.txt",
            #     "RARBG_DO_NOT_MIRROR.exe",
            #     "www.btranking.top - 최초배포.url",
            #     "AV大平台.url",
            #     "RARBG.txt",
            #     "PotPlayer64.dpl",
            #     "海獺-穩定高速連接互聯網.url",
            #     "javsubs91.txt",
            #     "楼风最全资源.html",
            #     "www.hhd800.com.txt",
            #     "更多精品獨家資源下載.mht",
            #     "javsubs91.txt",
            # ]
            # dst = rf"D:\$cache_prisonized\$useless_files"
            # if os.path.isfile(target_abspath):
            #     if os.path.dirname(target_abspath) in useless_files:
            #         print(rf"{target_abspath} is uselessfile")
            #         # Park4139.move_without_overwrite(src=target_abspath, dst=dst)
            #         # 디렉토리 머지 without_overwrite(
            #
            # Park4139.speak("타겟경로를 순회하며 모든 파일을 예약된 폴더로 모읍니다")
            # files_ = []
            # if os.path.isdir(target_abspath):
            #     for (root, dirs, files) in os.walk(target_abspath, topdown=False):  # os.walk()는 with walking 으로 동작한다
            #         files_ = files_ + files
            #         print(f"file: {files}")
            #
            # Park4139.speak("타겟경로를 순회하며 특별한 파일을 예약된 폴더로 모읍니다")
            # special_files = []
            # if os.path.isdir(target_abspath):
            #     for (root, dirs, files) in os.walk(target_abspath, topdown=False):  # os.walk()는 with walking 으로 동작한다
            #         special_files = special_files + files
            #         print(f"special_file: {files}")
            #
            # Park4139.speak("타겟경로를 순회하며 파일들을 예약된 키워드로 된 폴더로 분류합니다")
            # keywords_promised = [
            #     "[subplease]",
            # ]
            # keyword_directories = []
            # for keyword in keywords_promised:
            #     keyword_directory = rf"D:\$cache_prisonized\${keyword}"
            #     Park4139.make_leaf_directory(leaf_directory_abspath=keyword_directory)
            #     keyword_directories.append(keyword_directory)
            #     print(f"keyword_directory: {keyword_directory}")
            # if os.path.isdir(target_abspath):
            #     for (root, dirs, files) in os.walk(target_abspath, topdown=False):  # os.walk()는 with walking 으로 동작한다
            #         for keyword in keywords_promised:
            #             if keyword in files:
            #                 print(f"special_file: {files}")

            # 파일분류 기능
            # 이름에 [subplease] 가 있다면 [subplease] 디렉토리를 만들어 그곳으로 move_without_overwrite

            # 파일명 대체 기능 (불필요한 접두/어근/접미, 삭제/추가)
            # 이름에 [subplease] 가 있다면
            # rename_without_overwrite(이름, 이름.replace([subplease],""))
            # 필요한 파일명 부여 삭제
            # 이동시키지 말고 그자리에서 rename

            # 디렉토리 머지 without_overwrite
            # # rename_target_without_overwiting

            # 2024 PROJECT DATA PRISION
            # 내가 아는 것은 30초 이내에 찾을 수 있도록 하기 위한 프로젝트
            # 결국 보고자 하는 것은 디렉토리가 아니라 파일명을 잘 관리해서 인덱싱하면 된다고 생각한다.
            # 디렉토리명은 파일을 찾기 위한 지표정도이다.

            # 파일명 부여 규칙
            # 접두사는 가장 중요한 직관적인 키워드를 넣는다.
            # 접미사는 순서에 관계없이 [애니][영화] 이런 걸 붙인다. 이 접미사는 검색 시 중요하므로 잘 보관하고 관리한다.
            # 파일명으로 가지고 파일을 검색한다.
        else:
            break


prisonize_storage()
