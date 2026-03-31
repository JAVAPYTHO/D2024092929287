#%%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, box
import random

# 读取数据
def load_data(city_folder):
    files = [
        "Transportation facilities data.csv",
        "Medical and health data.csv",
        "Public facilities data.csv",
        "Lifestyle service data.csv",
        "Government and social organizations data.csv",
        "Food and beverage service data.csv",
        "Finance and insurance data.csv",
        "Accommodation service data.csv"
    ]
    data_frames = {}
    for file in files:
        try:
            # 尝试以 UTF-8 读取文件
            df = pd.read_csv(f'{city_folder}/{file}', encoding='utf-8')
        except UnicodeDecodeError:
            try:
                # 尝试以 ISO-8859-1 读取文件
                df = pd.read_csv(f'{city_folder}/{file}', encoding='ISO-8859-1')
            except UnicodeDecodeError:
                # 尝试以 GBK 读取文件（常见于中文文件）
                df = pd.read_csv(f'{city_folder}/{file}', encoding='GBK')
        
        df.columns = df.columns.str.replace(r'\r', '', regex=True).str.strip()
        # 去除重复值
        df.drop_duplicates(inplace=True)
        # 检查并处理缺失值
        df.fillna(method='ffill', inplace=True)
        data_frames[file] = df
    return data_frames

# 数据清洗：处理缺失值和重复数据
def clean_data(data_frame):
    # 删除包含任何缺失值的行
    data_frame = data_frame.dropna(subset=['lon_gcj02', 'lat_gcj02'])
    # 去除重复数据
    data_frame = data_frame.drop_duplicates(subset=['id'])
    return data_frame

# 转换为地理数据
def to_geodataframe(data_frame):
    # 创建GeoDataFrame，使用经纬度信息
    geometry = [Point(lon, lat) for lon, lat in zip(data_frame['lon_gcj02'], data_frame['lat_gcj02'])]
    geo_df = gpd.GeoDataFrame(data_frame, geometry=geometry)
    return geo_df

# 绘制设施分布图（两张图，每张图包含四个子图）
def plot_facility_distributions(data_frames, city_name, city_boundaries):
    num_categories = len(data_frames)
    midpoint = num_categories // 2
    
    # 绘制第一张图，包含前四个子图
    fig1, axes1 = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
    axes1 = axes1.flatten()
    
    for idx, (category, geo_df) in enumerate(list(data_frames.items())[:4]):
        ax = axes1[idx]
        # 使用随机颜色
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        # 绘制城市边界
        city_boundaries.plot(ax=ax, facecolor='none', edgecolor='black', linestyle='--', linewidth=2)
        # 绘制设施位置
        geo_df.plot(ax=ax, marker='^', color=color, markersize=8)
        ax.set_title(f'{city_name} - {category.split(" ")[0]} Distribution', fontsize=15)
        ax.grid(visible=True, linestyle=':', color='gray', alpha=0.7)
    
    # 删除多余的子图
    for idx in range(4, len(axes1)):
        fig1.delaxes(axes1[idx])
    
    plt.tight_layout()
    plt.show()
    
    # 绘制第二张图，包含剩余的子图
    fig2, axes2 = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
    axes2 = axes2.flatten()
    
    for idx, (category, geo_df) in enumerate(list(data_frames.items())[4:8]):
        ax = axes2[idx]
        # 使用随机颜色
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        # 绘制城市边界
        city_boundaries.plot(ax=ax, facecolor='none', edgecolor='black', linestyle='--', linewidth=2)
        # 绘制设施位置
        geo_df.plot(ax=ax, marker='o', color=color, markersize=8)
        ax.set_title(f'{city_name} - {category.split(" ")[0]} Distribution', fontsize=15)
        ax.grid(visible=True, linestyle=':', color='gray', alpha=0.7)
    
    # 删除多余的子图
    for idx in range(len(data_frames) - 4, len(axes2)):
        fig2.delaxes(axes2[idx])
    
    plt.tight_layout()
    plt.show()

# 计算各类设施密度
def calculate_facility_density(geo_df, city_boundaries):
    # 获取城市矩形边界
    min_lon, min_lat, max_lon, max_lat = city_boundaries.bounds.values[0]
    
    # 将经纬度转换为float类型
    min_lon, min_lat, max_lon, max_lat = float(min_lon), float(min_lat), float(max_lon), float(max_lat)
    city_area = (max_lon - min_lon) * (max_lat - min_lat)  # 矩形区域面积

    # 计算设施在城市边界内的密度
    facilities_in_city = geo_df[geo_df.within(city_boundaries)]
    facility_density = len(facilities_in_city) / city_area  # 单位面积内的设施数
    print(facility_density)
    return facility_density

# 主程序：评估城市的恢复力
def evaluate_resilience(city_folder, city_name, city_boundaries):
    # 加载和清理数据
    data_frames = load_data(city_folder)
    cleaned_geo_data = {}
    for category, df in data_frames.items():
        cleaned_df = clean_data(df)
        geo_df = to_geodataframe(cleaned_df)
        cleaned_geo_data[category] = geo_df
        
        # 计算设施密度
        density = calculate_facility_density(geo_df, city_boundaries)
        print(f'{category.split(" ")[0]} Density in {city_name}: {density:.4f} facilities per square kilometer')
    
    # 可视化每类设施分布
    plot_facility_distributions(cleaned_geo_data, city_name, city_boundaries)

# 定义城市矩形边界（最小经纬度，最大经纬度）
def define_city_boundary(min_lon, min_lat, max_lon, max_lat):
    # 创建矩形边界并转换为GeoDataFrame
    city_boundary = box(min_lon, min_lat, max_lon, max_lat)
    return gpd.GeoDataFrame(geometry=[city_boundary])

# 示例：定义城市边界并评估两个城市
city1_folder = 'F:/pythonProject/python/question2/Appendix 3'
city2_folder = 'F:/pythonProject/python/question2/Appendix 4'

# 长春市经纬度范围
city1_boundaries = define_city_boundary(min_lon=124.0, min_lat=43, max_lon=127, max_lat=45.2)

# 呼和浩特市经纬度范围
city2_boundaries = define_city_boundary(min_lon=110.75, min_lat=39.75, max_lon=112.2, max_lat=41.25)

# 评估长春市
evaluate_resilience(city1_folder, 'Changchun', city1_boundaries)

# 评估呼和浩特市
evaluate_resilience(city2_folder, 'Hohhot', city2_boundaries)

#%%
