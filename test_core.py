import os
import string
from datetime import datetime
from typing import List

import pkg_park4139

Park4139 = pkg_park4139.Park4139()



def TEST():
    pass

TEST()

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
# 파일이 어느폴더에 있든 상관없다. 단지 이름명이 류가 되어있어 찾을 때, 정확히 호출만 되면 되는 일이다. 호출명단을 잘 관리를 하면 되는 일이다,
# 그렇다면 정리할 필요가 없다, 즉 찾는시간이 적은 시스템이 필요한 것이지 정리하는시간이 필요한 게 아니다
# 정리하는시간이 없고 찾는시간이 빠른 시스템 이 나에게 필요한 파일색인시스템.

# (파일명)   #hashtag name #애니 #영화
# 파일명 부여 규칙
# 접두사는 가장 중요한 직관적인 키워드를 넣는다.
# 접미사는 순서에 관계없이 #애니 #영화 이런 걸 붙인다. 이 접미사는 검색 시 중요하므로 잘 보관하고 관리한다.
# 파일명으로 가지고 파일을 검색한다.

# 타겟 삭제 with walking
#  shutil.rmtree(path)
#  하지만 이 명령어 rmdir /s 나 shutil.rmtree() 를 사용하는 것은 위험한 일이다. trash_bin 으로 옮기는 명령어로 대체하자.
#  path에 있는 folder를 지우면서 그 안에 있는 모든 파일을 지워준다. rmdir /s 명령어랑 같은 것 같음?.

# 빈폴더 머지는 확실히 삭제해도 되는 빈폴더를 한 폴더에 두고 빈폴더 삭제 명령어로 처리하자


# def prisonize_storage():
