import pandas as pd
import numpy as np

df1 = pd.read_excel('../The generated images and files/Density index.xlsx')
df2 = pd.read_excel('../The generated images and files/cv_weight.xlsx')
np_array1 = df1.iloc[:, 2].values
np_array2 = df2.iloc[:, 1].values
np_array3 = df2.iloc[:, 2].values


if len(np_array1) == len(np_array2) == len(np_array3):
    sum1 = np.sum(np_array1 * np_array2)
    sum2 = np.sum(np_array1 * np_array3)
else:
    print("数组长度不匹配，无法进行计算。")

print("sum1的值是:", sum1)
print("sum2的值是:", sum2)