# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# # median_house_value > 70000

import pandas as pd


df = pd.read_csv('california_housing_test.csv')

# # 1. Проверить есть ли в файле пустые значения
# print(df.isnull(). sum())
# 2. Показать median_house_value где median_income < 2
# print(df[df['median_income'] < 2]['median_house_value'])
# # 3. Показать данные в первых 2 столбцах
# # print(df[['longitude', 'latitude']])
# print(df.iloc[:, :2])
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])
