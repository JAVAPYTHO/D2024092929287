import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = '../The generated images and files/Density index.xlsx'

df = pd.read_excel(file_path)
labels = df.iloc[1:, 0]
print(labels)

array_name_1 = df.iloc[0, 1]
array_name_2 = df.iloc[0, 2]
data_1 = df.iloc[1:, 1].astype(np.float64).values
data_2 = df.iloc[1:, 2].astype(np.float64).values

array1 = np.array(data_1, dtype=np.float64)
array2 = np.array(data_2, dtype=np.float64)

num_vars = len(array1)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

data1 = np.concatenate((array1, [array1[0]]))
data2 = np.concatenate((array2, [array2[0]]))
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

ax.fill(angles, data1, color='red', alpha=0.25)
ax.fill(angles, data2, color='blue', alpha=0.25)

ax.plot(angles, data1, color='red', linewidth=2, linestyle='solid', label='City 1')
ax.plot(angles, data2, color='blue', linewidth=2, linestyle='solid', label='City 2')

plt.text(0.5, -0.1, 'serive number', ha='center', va='top', size=15, color='black', transform=plt.gca().transAxes)

ax.set_xticks(angles[:-1])  # 设置角度，去掉最后一个重复的角度
ax.set_xticklabels(labels)  # 确保标签数量与角度数量匹配

plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()

