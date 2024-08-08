import random
import pandas as pd

# Генерируем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one-hot кодировки вручную
one_hot = pd.DataFrame()

# Получаем уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Для каждого уникального значения создаем новый столбец
for value in unique_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)

# Проверяем результат
print(one_hot.head())