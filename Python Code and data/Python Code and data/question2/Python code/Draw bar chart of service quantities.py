import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.font_manager import FontProperties

folder_path = '../The generated images and files/Comparison chart of the number of services/'
name = '../The generated images and files/Density index.xlsx'

all_files = os.listdir(folder_path)
excel_files = [file.rsplit('.xlsx', 1)[0] for file in all_files if file.endswith('.xlsx')]
excel_files_np = np.array(excel_files)

for i in range(len(excel_files_np)):
    url = folder_path + excel_files_np[i] + '.xlsx'
    df = pd.read_excel(url, engine='openpyxl')
    df = df.iloc[:-1]

    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(10, 6))

    names = df.iloc[:, 0]
    store_a = df.iloc[:, 1]
    store_b = df.iloc[:, 2]
    x = np.arange(len(names))
    colors = ['#2A6298', '#5A94B9', '#9DC2D5', '#D5E1EF']
    plt.bar(x - 0.2, store_a, color=colors[0], width=0.4, label='City 1', align='center')
    plt.bar(x + 0.2, store_b, color=colors[2], width=0.4, label='City 2', align='center')

    font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=14)

    plt.title(excel_files_np[i], fontproperties=font)
    plt.xlabel('type', fontproperties=font)
    plt.ylabel('number', fontproperties=font)
    plt.xticks(x, names, fontproperties=font, fontsize=8, rotation=45,ha='right')
    plt.legend()

    filename = excel_files_np[i] + '.png'
    plt.savefig(folder_path + filename, dpi=500, bbox_inches='tight')

    plt.tight_layout()
    plt.show()