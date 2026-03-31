#%%
import pandas as pd

def load_data(file):
    try:
        # 尝试以 UTF-8 读取文件
        df = pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            # 尝试以 ISO-8859-1 读取文件
            df = pd.read_csv(file, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            # 尝试以 GBK 读取文件（常见于中文文件）
            df = pd.read_csv(file, encoding='GBK')

    # 清理列名：去掉回车符和空格
    df.columns = df.columns.str.replace(r'\r', '', regex=True).str.strip()

    # 将“小类”列名替换为“type”
    df.rename(columns={'小类': 'type'}, inplace=True)

    # 去除重复值
    df.drop_duplicates(inplace=True)

    # 检查并处理缺失值
    df = df.ffill()

    return df


import seaborn as sns
import matplotlib.pyplot as plt
#%%
def plot_combined_figure_1(files):
    fig, axs = plt.subplots(2, 2, figsize=(20, 16))

    # Plot Transportation Facilities
    df = load_data(files[0])
    sns.scatterplot(ax=axs[0, 0], data=df, x='lon_gcj02', y='lat_gcj02', hue='type', palette='Set1', s=70, edgecolor='w', alpha=0.85, legend=False)
    axs[0, 0].set_title("Distribution of Transportation Facilities", fontsize=18)
    axs[0, 0].set_xlabel("Longitude (lon_gcj02)", fontsize=14)
    axs[0, 0].set_ylabel("Latitude (lat_gcj02)", fontsize=14)

    # Plot Medical and Health Facilities
    df = load_data(files[1])
    sns.scatterplot(ax=axs[0, 1], data=df, x='lon_gcj02', y='lat_gcj02', hue='type', palette='Set2', s=70, edgecolor='w', alpha=0.85, legend=False)
    axs[0, 1].set_title("Distribution of Medical and Health Facilities", fontsize=18)
    axs[0, 1].set_xlabel("Longitude (lon_gcj02)", fontsize=14)
    axs[0, 1].set_ylabel("Latitude (lat_gcj02)", fontsize=14)

    # Plot Retail Service Facilities
    df = load_data(files[2])
    sns.scatterplot(ax=axs[1, 0], data=df, x='lon_gcj02', y='lat_gcj02', hue='type', palette='Set3', s=70, edgecolor='w', alpha=0.85, legend=False)
    axs[1, 0].set_title("Distribution of Retail Service Facilities", fontsize=18)
    axs[1, 0].set_xlabel("Longitude (lon_gcj02)", fontsize=14)
    axs[1, 0].set_ylabel("Latitude (lat_gcj02)", fontsize=14)

    # Plot Public Facilities
    df = load_data(files[3])
    sns.scatterplot(ax=axs[1, 1], data=df, x='lon_gcj02', y='lat_gcj02', hue='type', palette='Pastel1', s=70, edgecolor='w', alpha=0.85, legend=False)
    axs[1, 1].set_title("Distribution of Public Facilities", fontsize=18)
    axs[1, 1].set_xlabel("Longitude (lon_gcj02)", fontsize=14)
    axs[1, 1].set_ylabel("Latitude (lat_gcj02)", fontsize=14)

    plt.tight_layout()
    plt.show()

# 示例：使用多个数据文件
plot_combined_figure_1([
    'F:\\pythonProject\\python\\question2/Appendix 3/Transportation facilities data.csv',
    'F:\\pythonProject\\python\\question2/Appendix 3/Medical and health data.csv',
    'F:\\pythonProject\\python\\question2/Appendix 3/Retail service data.csv',
    'F:\\pythonProject\\python\\question2/Appendix 3/Public facilities data.csv'
])

#%%
def plot_combined_figure_2(files):
    fig, axs = plt.subplots(2, 2, figsize=(20, 16))

    # Plot Business-Residential Areas
    df = load_data(files[0])
    sns.scatterplot(ax=axs[0, 0], data=df, x='lon_gcj02', y='lat_gcj02', hue='type', palette='Set1', s=70, edgecolor='w', alpha=0.85, legend=False)
    axs[0, 0].set_title("Distribution of Business-Residential Areas", fontsize=18)
    axs[0, 0].set_xlabel("Longitude (lon_gcj02)", fontsize=14)
    axs[0, 0].set_ylabel("Latitude (lat_gcj02)", fontsize=14)

    # Plot Accommodation Services
    df = load_data(files[1])
    sns.scatterplot(ax=axs[0, 1], data=df, x='lon_gcj02', y='lat_gcj02', hue='type', palette='Set2', s=70, edgecolor='w', alpha=0.85, legend=False)
    axs[0, 1].set_title("Distribution of Accommodation Services", fontsize=18)
    axs[0, 1].set_xlabel("Longitude (lon_gcj02)", fontsize=14)
    axs[0, 1].set_ylabel("Latitude (lat_gcj02)", fontsize=14)

    # Plot Government and Social Organizations
    df = load_data(files[2])
    sns.scatterplot(ax=axs[1, 0], data=df, x='lon_gcj02', y='lat_gcj02', hue='type', palette='Set3', s=70, edgecolor='w', alpha=0.85, legend=False)
    axs[1, 0].set_title("Distribution of Government and Social Organizations", fontsize=18)
    axs[1, 0].set_xlabel("Longitude (lon_gcj02)", fontsize=14)
    axs[1, 0].set_ylabel("Latitude (lat_gcj02)", fontsize=14)

    # Plot Food and Beverage Services
    df = load_data(files[3])
    sns.scatterplot(ax=axs[1, 1], data=df, x='lon_gcj02', y='lat_gcj02', hue='type', palette='Pastel2', s=70, edgecolor='w', alpha=0.85, legend=False)
    axs[1, 1].set_title("Distribution of Food and Beverage Services", fontsize=18)
    axs[1, 1].set_xlabel("Longitude (lon_gcj02)", fontsize=14)
    axs[1, 1].set_ylabel("Latitude (lat_gcj02)", fontsize=14)

    plt.tight_layout()
    plt.show()

# 示例：使用多个数据文件
plot_combined_figure_2([
    'F:\\pythonProject\\python\\question2/Appendix 4/Business-residential data.csv',
    'F:\\pythonProject\\python\\question2/Appendix 4/Accommodation service data.csv',
    'F:\\pythonProject\\python\\question2/Appendix 4/Government and social organizations data.csv',
    'F:\\pythonProject\\python\\question2/Appendix 4/Food and beverage service data.csv'
])
