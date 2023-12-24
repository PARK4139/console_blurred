import os

import matplotlib
import pandas as pd  # 데이터 분석용
# import metaplotlib # pip install metaplotlib --upgrade
import numpy as np  # pip install numpy --upgrade
import FinanceDataReader as fdr  # alt+f12 # pip install -U finance-datareader #  FinanceDataReade.chart.plot()는 plotly에 의존성이 있습니다. pip install plotly --upgrade 를 진행하세요
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication

import pkg_park4139

# pyside6의 app이 없으면 pyside6 app을 만들어줌.
app: QApplication
if QCoreApplication.instance() == None:
    app = QApplication()

# __________________________________________________________________________________________________________________________________ TEST CORE CODE START
# DataReader() 거래소주식정보(*,시세정보) 를 가져옴
# 005930 삼성전자
# fdr_dr = fdr.DataReader("005930") # 모든기간
# fdr_dr = fdr.DataReader("005930", "2021-01-01", "2022-02-23") # 특정기간
fdr_dr = fdr.DataReader("005930", "2023")  # 특정기간(특정년도)
#
# fdr_dr = fdr.DataReader('000150', '2018-01-01', '2019-10-30', exchange='KRX')  # 두산
# fdr_dr = fdr.DataReader('000150', '2018-01-01', '2019-10-30', exchange='SZSE')  # Yihua Healthcare Co Ltd
# fdr_dr = fdr.DataReader('036360', exchange='KRX-DELISTING') # KRX에서 상장폐지된


# StockListing() 거래소주식정보(*,거래소상장주식목록)  가져옴
# df = fdr.StockListing('SSE')  # 상해
# df = fdr.StockListing('KONEX') # 코넥스
# df = fdr.StockListing('SZSE')
# df = fdr.StockListing('KRX')  # 한국
# df = fdr.StockListing('KOSDAQ')
# df = fdr.StockListing('KOSPI')
# df = fdr.StockListing('S&P500')
# df = fdr.StockListing('NYSE')  # 뉴욕거래소

# test_result = df.plot.


# sr = pd.Series(index=["피자", "치킨", "콜라", "맥주"], data=[17000, 18000, 1000, 5000])
# test_result = f"""
# {sr}
#
# {'-' * 79}
#
# index : {sr.index}
# values : {sr.values}
# """
# dialog = pkg_park4139.CustomDialogReplica(title="1차원데이터배열 출력 테스트결과 ( feat. pandas.시리즈 자료구조)", contents=test_result, buttons=["확인"])
# dialog.exec_()
#
#
#
#
#
#
# columns=['학번', '이름', '점수']
# data = [
#     ['1000', 'Steve', 90.72],
#     ['1001', 'James', 78.09],
#     ['1002', 'Doyeon', 98.43],
#     ['1003', 'Jane', 64.19],
#     ['1004', 'Pilwoong', 81.30],
#     ['1005', 'Tony', 99.14],
# ]
# df = pd.DataFrame(data=data, columns=columns)
# test_result= str(df)
# dialog = pkg_park4139.CustomDialogReplica(title="2차원데이터배열 출력 테스트결과 ( df 찐활용 feat. list )", contents=test_result, buttons=["확인"])
# dialog.exec_()


# data = {
#     '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
#     '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
#     '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
#     }
#
# index=None # df 의 index 파라미터의 default , 자동증가숫자가 auto fill 됨
# # index=pd.RangeIndex(start=0, stop=5, step=1) # df 의 index 제어
# df = pd.DataFrame(data, index=index)
# # test_result= df.to_string() # 모든 줄 보기(데이터조회)
# # test_result= df.head(3).to_string() # 3 줄만 보기(데이터조회)
# # test_result= df['학번'].to_string() # 특정 컬럼만 보기(데이터조회)
# # test_result= df['학번'].to_string(index=False) # 특정 컬럼만 보기(데이터조회)
# test_result= df['학번'].to_string() # 특정 컬럼만 보기(데이터조회)
# dialog = pkg_park4139.CustomDialogReplica(title="2차원데이터배열 출력 테스트결과 ( df 찐활용 feat. dict )", contents=test_result, buttons=["확인"])
# dialog.exec_()


# FILE_XLS = rf"{pkg_park4139.Park4139.PROJECT_DIRECTORY}\$cache_recycle_bin\test.xlsx"
# # df = pd.read_csv(FILE_CSV)
# # df = pd.read_sql(FILE_SQL)
# # df = pd.read_html(FILE_HTML)
# df = pd.read_excel(FILE_XLS)
# test_result = df.to_string()
# dialog = pkg_park4139.CustomDialogReplica(title="csv파일의 2차원데이터배열 출력 테스트결과", contents=test_result, buttons=["확인"])
# dialog.exec_()


# pandas 공부 후기
# 엑셀에 있는 데이터들 처럼 데이터배열 을 예쁘게 해주는 라이브러리
# sr(series) 는 key, value 형태의 1차원배열데이터 에 사용. df 기능으로 대체가 되므로 굳이 잘 안쓸듯.
# df(dataframe) 은 2차원배열데이터에 사용. 즉, 엑셀처럼 사용, 엄청유용할 듯
# df 를 출력하면 기본적으로 auto increment number 가 auto fill 된다!, 유용함!, 근데 지우는 방법도 찾아보기
# csv/txt/xls/sql/html/json 파일 읽어올 수 있다고 하는데, html 도 되는데? 크롤링과 연계할 때 편리한 부분이 있을 수 있겠다


data: np.ndarray
data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])  # 하드코딩으로 데이터배열
# data = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])  # 하드코딩으로 데이터배열
# data = np.zeros(shape=(3,3)) # shape=(3,3)인 배열에 모든 값이 0
# data = np.ones(shape=(3,3)) # shape=(3,3)인 배열에 모든 값이 1
# data = np.eye(3)# shape=(3,3)인 배열에 대각선 값이 1, 나머지 값이 0, 이거 활용도 높을 수 있겠다. 100  010  001 이런 순서 필요할때 있지 않겠나?
# data = np.random.random((2,2)) # shape=(3,3)인 배열에 모든 값이 1보다 작은 float(1인 경우가 있나 모르겠음)
# data = np.full(shape=(2,3), 7)#  # shape=(3,3)인 배열에 모든 값이 7
# data = np.arange(10) #배열개수가 10 인 1차원데이터배열 # 0~9
# data = np.arange(0, 10, 1) # 시작0, 종료10, 1씩증가 인1차원데이터배열 # 0~9
# data = [i for i in range(0,10,1)] # 0~9
# data = np.array(np.arange(30)).reshape((5, 6)) # shape = (5,6) 으로 reshape 한다, shape 안의 숫자들(5, 6) 을 곱(5 x 6)하면 원데이터의 개수(5 x 6 = 30)인와 같게 설정해야 된다. 실험해봐도 이게 맞음, list를 적당한 간격으로 자를때 유용하겠다!
# data = data[0, :]# 첫번째 줄 출력
# data = data[:,0]# 첫번째 기둥 출력
# data = data[1,1]# 특정위치의 원소
# data = data[[0, 2], [2, 0]]  # 특정 위치의 원소 두 개를 가져와 새로운 배열 # data[0, 2] 와 data[2, 0] 를 가져와 새로운 배열에 넣었습니다
# data = data[0, 2] + data[2, 0] # 원소 두개를 가져와, 합을 구한다
# data = data[0, 2] * data[2, 0] # 곱을 구한다, 이는 행렬에 대한 곱이 아니다. 좌표에 대한 곱이다
# data = data[0, 2] ** data[2, 0] # 거듭제곱을 구한다
# data = data[0, 2] / data[2, 0] # 나눈 결과를 구한다 Q + R/B  B = 나누는 수
# data = data[0, 2] // data[2, 0] # 몫을 구한다
# data = data[0, 2] % data[2, 0] # 나머지를 구한다
# data_ = np.dot(data1, data2)# 행렬곱
# test_result = f"""
# mat 의 data           :
# {str(data)}
#
# mat 의 축의 개수       :
# {data.ndim}
#
# mat 의 배열의 모양     :
# {data.shape}
# """
# dialog = pkg_park4139.CustomDialogReplica(title="2차원데이터배열 출력 테스트결과 ( feat. numpy )", contents=test_result, buttons=["확인"])
# dialog.exec_()

# numpy 공부 후기
# 배열은 행렬과 같은 관계처럼 느껴졌다.
# 다차원 행렬 자료구조 : 그냥 엑셀에서 사용하는 자료구조.
# ndarray 는 다차원 행렬 자료구조로 되어 있다.
# shape 배열의 생김새 정도 겠다, 표현은 shape=(3,3) 이런 형태
# 실험을 해보니 첫번째 shape=(줄번호, 기둥번호) 정도로 생각하면 되겠다
# 이제는 shape=(100,101) 이런 코드를 보면 데이터배열을 상상할 때 어떤 모양인지 알겠다.

# 행렬 공부 후기
# 행렬은 좌표 같다.
# 행렬의 연산은 각 좌표끼리 더하거나 곱하는 것과 같다.


import matplotlib.pyplot as plt


# dir /b /s *.ttf | clip 으로 추출
# plt.rcParams['font.family'] ='Malgun Gothic' # 한글폰트 적용
font_abspath = rf"{pkg_park4139.Park4139.PROJECT_DIRECTORY}\$cache_fonts\GmarketSans\GmarketSansTTFLight.ttf"
# font_abspath = rf"{pkg_park4139.Park4139.PROJECT_DIRECTORY}\$cache_fonts\Rubik_Doodle_Shadow\RubikDoodleShadow-Regular.ttf" # 너무 귀여운 입체감 있는 영어폰트
plt.rcParams['font.family'] = pkg_park4139.Park4139.get_font_name_for_mataplot(font_abspath)
plt.rcParams['figure.facecolor'] = 'black'  # '바탕색'
plt.rcParams['axes.edgecolor'] = 'white'  # '테두리 색'
plt.rcParams['axes.facecolor'] = 'black'  # '바탕색'


# 제목 설정
plt.title('그래프 제목', color='white')

# 빨간 꺽은선 그래프
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, color = "red")

# 노란 꺽은선 그래프
plt.plot([1.5, 2.5, 3.5, 4.5], [3, 5, 8, 10], color = "yellow")  # 라인 새로 추가

# 범례 설정
legend =plt.legend(['학생 A', '학생 B'],facecolor='k', labelcolor='white' )
ax = plt.gca()
leg = ax.get_legend()
leg.legendHandles[0].set_color('red')
leg.legendHandles[1].set_color('yellow')

# 전체화면 설정
# mng = plt.get_current_fig_manager()
# mng.full_screen_toggle()

# 레이블 설정
plt.xlabel('x 축 레이블', color='white')
plt.ylabel('y 축 레이블', color='white')
plt.tick_params(labelcolor='white')


plt.show()


# Matplotlib 공부 후기
# 읽는 법 : 맷플롯립 이라고 읽는다.
# 데이터 시각화 패키지 : 쉽게 데이터로 차트를 그려주는 도구
# 설치 : pip install matplotlib --upgrade
# import 시 네이밍 관례 : as plt 로 import 한다 : import matplotlib.pyplot as plt
# 조아써 이제 그래프 그릴 수 있어

# __________________________________________________________________________________________________________________________________ TEST CORE CODE END


# pyside6의 app이 없으면 pyside6 app을 실행
try:
    app.exec()
except:
    pass
