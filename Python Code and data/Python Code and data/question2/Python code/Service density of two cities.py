import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import chardet

with open('../Processed appendices/Transportation facilities data_3.csv', 'rb') as file:
    result = chardet.detect(file.read())
    encoding = result['encoding']
def process_csv_files(folder_path):
    # 记录已处理的文件数量，用于生成颜色
    file_count = 0

    for filename in os.listdir(folder_path):
        if filename.endswith("_3.csv"):
            file_path = os.path.join(folder_path, filename)

            df = pd.read_csv(file_path, encoding=encoding)

            if len(df.columns) >= 2:
                x = df.iloc[:, 2]
                y = df.iloc[:, 3]
                color = plt.cm.jet(file_count / float(
                    len([f for f in os.listdir(folder_path) if f.endswith("_3.csv")])))  # 为不同的文件分配不同的颜色
                label = filename.replace("_3.csv", "")

                # 绘制点状图
                sns.scatterplot(x=x, y=y, label=label, color=color)
                file_count += 1
            else:
                print(f"File {filename} does not have enough columns.")

# 设置图形的大小
plt.figure(figsize=(18, 12))

folder_path = '../Processed appendices'
process_csv_files(folder_path)

plt.title('City 1')
plt.xlabel('lon_gcj02')
plt.ylabel('lat_gcj02')
plt.legend()
plt.show()