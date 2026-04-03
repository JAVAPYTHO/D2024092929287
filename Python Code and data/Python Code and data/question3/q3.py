#%%
from pathlib import Path
import os
import random

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point, box


def _read_csv_auto(file_path: Path) -> pd.DataFrame:
    for enc in ("utf-8", "ISO-8859-1", "GBK"):
        try:
            return pd.read_csv(file_path, encoding=enc)
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("csv", b"", 0, 1, f"无法解码文件: {file_path}")


# 读取数据
def load_data(city_folder: Path):
    files = [
        "Transportation facilities data.csv",
        "Medical and health data.csv",
        "Public facilities data.csv",
        "Lifestyle service data.csv",
        "Government and social organizations data.csv",
        "Food and beverage service data.csv",
        "Finance and insurance data.csv",
        "Accommodation service data.csv",
    ]
    data_frames = {}
    for file in files:
        df = _read_csv_auto(city_folder / file)
        df.columns = df.columns.str.replace(r"\r", "", regex=True).str.strip()
        df.drop_duplicates(inplace=True)
        df.fillna(method="ffill", inplace=True)
        data_frames[file] = df
    return data_frames


# 数据清洗：处理缺失值和重复数据
def clean_data(data_frame):
    data_frame = data_frame.dropna(subset=["lon_gcj02", "lat_gcj02"])
    if "id" in data_frame.columns:
        data_frame = data_frame.drop_duplicates(subset=["id"])
    return data_frame


# 转换为地理数据
def to_geodataframe(data_frame):
    geometry = [Point(lon, lat) for lon, lat in zip(data_frame["lon_gcj02"], data_frame["lat_gcj02"])]
    return gpd.GeoDataFrame(data_frame, geometry=geometry)


# 绘制设施分布图（两张图，每张图包含四个子图）
def plot_facility_distributions(data_frames, city_name, city_boundaries):
    fig1, axes1 = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
    axes1 = axes1.flatten()

    for idx, (category, geo_df) in enumerate(list(data_frames.items())[:4]):
        ax = axes1[idx]
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        city_boundaries.plot(ax=ax, facecolor="none", edgecolor="black", linestyle="--", linewidth=2)
        geo_df.plot(ax=ax, marker="^", color=color, markersize=8)
        ax.set_title(f"{city_name} - {category.split(' ')[0]} Distribution", fontsize=15)
        ax.grid(visible=True, linestyle=":", color="gray", alpha=0.7)

    for idx in range(4, len(axes1)):
        fig1.delaxes(axes1[idx])
    plt.tight_layout()
    plt.show()

    fig2, axes2 = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))
    axes2 = axes2.flatten()

    for idx, (category, geo_df) in enumerate(list(data_frames.items())[4:8]):
        ax = axes2[idx]
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        city_boundaries.plot(ax=ax, facecolor="none", edgecolor="black", linestyle="--", linewidth=2)
        geo_df.plot(ax=ax, marker="o", color=color, markersize=8)
        ax.set_title(f"{city_name} - {category.split(' ')[0]} Distribution", fontsize=15)
        ax.grid(visible=True, linestyle=":", color="gray", alpha=0.7)

    for idx in range(len(data_frames) - 4, len(axes2)):
        fig2.delaxes(axes2[idx])
    plt.tight_layout()
    plt.show()


# 计算各类设施密度
def calculate_facility_density(geo_df, city_boundaries):
    min_lon, min_lat, max_lon, max_lat = city_boundaries.bounds.values[0]
    city_area = (float(max_lon) - float(min_lon)) * (float(max_lat) - float(min_lat))
    facilities_in_city = geo_df[geo_df.within(city_boundaries)]
    return len(facilities_in_city) / city_area


# 主程序：评估城市恢复力
def evaluate_resilience(city_folder: Path, city_name, city_boundaries):
    data_frames = load_data(city_folder)
    cleaned_geo_data = {}
    for category, df in data_frames.items():
        cleaned_df = clean_data(df)
        geo_df = to_geodataframe(cleaned_df)
        cleaned_geo_data[category] = geo_df

        density = calculate_facility_density(geo_df, city_boundaries)
        print(f"{category.split(' ')[0]} Density in {city_name}: {density:.4f} facilities per square kilometer")

    plot_facility_distributions(cleaned_geo_data, city_name, city_boundaries)


# 定义城市矩形边界
def define_city_boundary(min_lon, min_lat, max_lon, max_lat):
    city_boundary = box(min_lon, min_lat, max_lon, max_lat)
    return gpd.GeoDataFrame(geometry=[city_boundary])


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    city1_folder = Path(os.getenv("Q3_CITY1_DIR", str(base_dir / "Appendix 3")))
    city2_folder = Path(os.getenv("Q3_CITY2_DIR", str(base_dir / "Appendix 4")))

    city1_boundaries = define_city_boundary(min_lon=124.0, min_lat=43, max_lon=127, max_lat=45.2)
    city2_boundaries = define_city_boundary(min_lon=110.75, min_lat=39.75, max_lon=112.2, max_lat=41.25)

    evaluate_resilience(city1_folder, "Changchun", city1_boundaries)
    evaluate_resilience(city2_folder, "Hohhot", city2_boundaries)

#%%
