# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

import seaborn as sns
# import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

# sns.scatterplot(x='sex', y='body_mass_g', data=penguins)
# sns.scatterplot(data=penguins, x = 'body_mass_g', y = 'flipper_length_mm', hue = 'bill_length_mm',  sizes=(10, 200))
# sns.scatterplot(data=penguins, x = 'body_mass_g', y = 'flipper_length_mm', hue= 'island', style = 'species')
# data_columns = ['spercies', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
# graph = sns.PairGrid(penguins[data_columns],hue='body_mass_g', palette='deep')
# graph = graph.map_diag(mpl.hist)
# graph = graph.map_offdiag(mpl.scatter)
# body_mass = {'light': 3000, 'light_heavy': 4000, 'medium': 5000, 'medium_heavy': 5500, 'heavy': 6000}
# graph = graph.add_legend(legend_data=body_mass, title='Масса тушки')
# mpl.show()
# data = penguins.pivot_table(index='species', columns='island', values='body_mass_g')
# sns.heatmap(data)
# plt.xlabel('Остров', size=14)
# plt.ylabel('Вид пингвина', size=14)
# sns.displot(data=penguins, hue='species', x='body_mass_g', kind='hist', col='sex')
penguins['bill_depth_mm'].hist(bins=10)
plt.show()
