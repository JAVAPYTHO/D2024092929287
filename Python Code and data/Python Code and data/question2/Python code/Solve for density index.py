import os
import pandas as pd
import numpy as np
def calculate_density_index(df):
    x = df.iloc[:, 2]
    y = df.iloc[:, 3]
    max1, min1 = x.max(), x.min()
    max2, min2 = y.max(), y.min()
    area = (max1 - min1) * (max2 - min2)
    N = len(df) - 1
    Density_index = N / area
    return Density_index

def process_file_names(folder_path):
    unique_names = set()  # 使用集合来自动去重
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            base_name = os.path.splitext(filename)[0]
            cleaned_name = base_name.split("data")[0]
            unique_names.add(cleaned_name)

    return np.array(list(unique_names))
def process_csv_files(folder_path):
    density_indices_3 = []
    density_indices_4 = []
    cleaned_names = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith("_3.csv"):
            print(filename)
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(file_path, encoding='latin1')
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path, encoding='ISO-8859-1')
            base_name = os.path.splitext(filename)[0]
            cleaned_name = base_name.split("data")[0]
            density_index = calculate_density_index(df)
            density_indices_3.append(density_index)
            cleaned_names.append(cleaned_name)

        elif filename.endswith("_4.csv"):
            print(filename)
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(file_path, encoding='latin1')
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path, encoding='ISO-8859-1')
            density_index = calculate_density_index(df)
            density_indices_4.append(density_index)

    return density_indices_3, density_indices_4, cleaned_names

folder_path = '../Processed appendices'
density_indices_3, density_indices_4, cleaned_names = process_csv_files(folder_path)

with pd.ExcelWriter('../The generated images and files/Density index.xlsx') as writer:
    df_results = pd.DataFrame({
        'server': cleaned_names,
        'City 1': density_indices_3,
        'City 2': density_indices_4
    })
    df_results.to_excel(writer, index=False)

print("Excel文件已生成，包含_3.csv和_4.csv的Density_Indices值。")