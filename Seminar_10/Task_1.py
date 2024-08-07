"""
1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_test.csv')

#1. Изобразите отношение households к population с помощью точечного графика

# scatter_plot = sns.scatterplot(data=df, x='households', y='population',)
#
# scatter_plot.set_title('Relationship between Households and Population')
# scatter_plot.set_xlabel('Households')
# scatter_plot.set_ylabel('Population')
# plt.show()

#2. Визуализировать longitude по отношения к median_house_value, используя линейный график

# sns.relplot(x='longitude', y='median_house_value', data=df, kind='line')
# plt.show()

# 3. Представить гистограмму по housing_median_age

# sns.histplot(data=df, x='housing_median_age',)
# plt.show()

# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

# sns.histplot(data=df, x='median_house_value', hue ='housing_median_age')
# plt.show()