import pandas as pd
import numpy as np

file_path = '../The generated images and files/Density index.xlsx'
df = pd.read_excel(file_path)

array_name_1 = df.iloc[0, 1]
array_name_2 = df.iloc[0, 2]
data_1 = df.iloc[:, 1].astype(np.float64).values
data_2 = df.iloc[:, 2].astype(np.float64).values
array1 = np.array(data_1, dtype=np.float64)
array2 = np.array(data_2, dtype=np.float64)

cv_values = []
for i in range(len(array1)):

    value1 = array1[i]
    value2 = array2[i]
    mean = (value1 + value2) / 2

    std = np.std([value1, value2])
    cv = std / mean if mean != 0 else float('inf')
    cv_values.append(cv)

cv_array = np.array(cv_values)

sum_of_weights = np.sum(cv_array)
weight_array = cv_array / sum_of_weights

data = df.iloc[0:, 0]
array = np.array(data)

df = pd.DataFrame({'serve name': data, 'cv_array': cv_array, 'weight_array': weight_array})
df.to_excel('../The generated images and files/cv_weight.xlsx', index=False, engine='openpyxl')

print("serve name:", array)
print("CV Array:", cv_array)
print("weight Array:", weight_array)