# Pandas
import numpy as np
import pandas as pd

# 딕셔너리 데이터 타입
# 형식 {'key' : 'value'}
sample = {'name' : '조재영', '직업' : '강사', '나이' : 34, '나이' : 24}
print(sample)
print(sample['나이'])
sample['직업'] = '학생'
print(sample)
print(sample.values())

sample = {'name' : ['소나타', '그랜져', '제네시스', '페라리'], 'year' : [2022, 2023, 2024, 2001], 'price' : [1000,2000,4000,8000]}

dataframe = pd.DataFrame(sample, index = sample['price'])
print(dataframe)

# csv를 통해서 대용량의 데이터 처리 가능
# csv 파일 열 때, 경로 확인 해줘야 됨
csv_df = pd.read_csv('data.csv')
print(csv_df)
print(csv_df[['country', 'population']])
print(csv_df.iloc[100:130])

