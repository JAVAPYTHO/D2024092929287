import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False

folder_path = 'C:/Users/hxh/Desktop/数学建模数据/problem2/data/'

all_files = os.listdir(folder_path)
excel_files = [file for file in all_files if file.endswith('.xlsx')]

all_names = []
all_store_a = []
all_store_b = []

for file in excel_files:
    url = os.path.join(folder_path, file)
    df = pd.read_excel(url, engine='openpyxl')
    condition = df.iloc[:, 1] < df.iloc[:, 2]
    filtered_df = df[condition]

    if not filtered_df.empty:
        for index, row in filtered_df.iterrows():
            all_names.append(row.iloc[0])
            all_store_a.append(row.iloc[1])
            all_store_b.append(row.iloc[2])

plt.figure(figsize=(10, 6))

# 绘制柱状图
x = np.arange(len(all_names))
plt.bar(x - 0.2, all_store_a, width=0.4, label='第二列', align='center')
plt.bar(x + 0.2, all_store_b, width=0.4, label='第三列', align='center')

plt.xticks(x, all_names, rotation=45, ha='right')

plt.title('所有Excel文件的柱状图')
plt.xlabel('商品名称')
plt.ylabel('数量')

plt.legend()
plt.tight_layout()  # 调整布局
plt.show()