# Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы


from pandas import read_csv
file_path = 'california_housing_test.csv'
data = read_csv(file_path)

print(type(data))

print(data.shape)

print(data.dtypes)

print(data.info())

print(data.describe())