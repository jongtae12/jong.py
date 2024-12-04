import pandas as pd #pandas 불러오기
df_xlsx = pd.read_excel('C:/Users/dpfla/Desktop/공부/파이썬 코드/관서별/관서별 5대범죄 발생 및 검거.xlsx')
#파일 가져오기
new_data={'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
'서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
'혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
'마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
'광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
'강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구', 
'구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구', 
'방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}


df_xlsx['구별']=df_xlsx['관서명'].map(new_data).fillna('구 없음')
#관서명 매핑 값이 없다면 구 없음 출력
pivot=pd.pivot_table(df_xlsx,index='구별',aggfunc=['sum'])
#pivot_table사용하여  '구별'index 같은 경우 sum
df_xlsx_drop = df_xlsx.drop(df_xlsx[df_xlsx["구별"] == "구없음"].index)
#구없음 행을 삭제

df_xlsx['강간검거율']=(df_xlsx['강간(검거)']/df_xlsx['강간(발생)'])*100
df_xlsx['강도검거율']=(df_xlsx['강도(검거)']/df_xlsx['강도(발생)'])*100
df_xlsx['살인검거율']=(df_xlsx['살인(검거)']/df_xlsx['살인(발생)'])*100
df_xlsx['절도검거율']=(df_xlsx['절도(검거)']/df_xlsx['절도(발생)'])*100
df_xlsx['폭력검거율']=(df_xlsx['폭력(검거)']/df_xlsx['폭력(발생)'])*100
df_xlsx['검거율']=(df_xlsx['소계(검거)']/df_xlsx['소계(발생)'])*100
#(검거/발생)*100을 통해 비율을 구하고 해당 컬럼에 부여

del df_xlsx['강간(검거)']
del df_xlsx['강도(검거)']
del df_xlsx['살인(검거)']
del df_xlsx['절도(검거)']
del df_xlsx['폭력(검거)']
del df_xlsx['소계(발생)']
del df_xlsx['소계(검거)']
#필요없는 컬럼 삭제

df_xlsx.rename(columns={'강간(발생)':'강간',
'강도(발생)':'강도',
'살인(발생)':'살인',
'절도(발생)':'절도',
'폭력(발생)':'폭력'})
print(df_xlsx)
#컬럼명을 바꾸고 프린트

kor_csv=pd.read_csv('C:/Users/dpfla/Desktop/공부/파이썬 코드/관서별/pop_kor.csv')
#데이터 불러오기

df_kor=pd.DataFrame(kor_csv)
#불러온 데이터를 데이터 프레임으로 만들기
merge_df = pd.merge(df_xlsx, df_kor, on='구별', how='inner')
#구별을 기준으로 두 데이터 프레임 merge
df_xlsx.set_index('구별', inplace=True)
df_kor.set_index('구별', inplace=True)
# '구별'index
last_df = df_xlsx.join(df_kor, how='inner')
#index 기준으로 병합
last_df_sorted = last_df.sort_values(by='검거율', ascending=True)
print(last_df_sorted)
#merge된 데이터를 검거율 기준으로 오름차순 정력