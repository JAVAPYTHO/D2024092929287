from pathlib import Path
import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def categorize_facility(facility_type):
    if facility_type in ["五星级宾馆", "四星级宾馆", "奢华酒店"]:
        return "高级设施"
    if facility_type in ["三星级宾馆", "经济型连锁酒店", "三星级宾馆|餐饮服务", "三星级宾馆|商务住宅"]:
        return "中级设施"
    if facility_type in [
        "宾馆酒店",
        "旅馆招待所",
        "住宿服务相关",
        "宾馆酒店|住宿服务",
        "旅馆招待所|住宿服务",
        "青年旅舍",
        "宾馆酒店|生活服务",
        "旅馆招待所|生活服务",
    ]:
        return "基础设施"
    if facility_type in [
        "宾馆酒店|餐饮服务",
        "旅馆招待所|商务住宅",
        "住宿服务相关|商务住宅",
        "旅馆招待所|购物服务",
        "宾馆酒店|购物服务",
        "经济型连锁酒店|购物服务",
        "经济型连锁酒店|公司企业",
    ]:
        return "特殊设施"
    return "其他设施"


def calculate_overall_proportion(city_data):
    total = len(city_data)
    return pd.Series(
        {
            "高级设施比例": len(city_data[city_data["设施级别"] == "高级设施"]) / total,
            "中级设施比例": len(city_data[city_data["设施级别"] == "中级设施"]) / total,
            "基础设施比例": len(city_data[city_data["设施级别"] == "基础设施"]) / total,
            "特殊设施比例": len(city_data[city_data["设施级别"] == "特殊设施"]) / total,
        }
    )


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    city1_file = Path(
        os.getenv("Q3_CITY1_ACCOM_FILE", str(base_dir / "Appendix 3" / "Accommodation service data.csv"))
    )
    city2_file = Path(
        os.getenv("Q3_CITY2_ACCOM_FILE", str(base_dir / "Appendix 4" / "Accommodation service data.csv"))
    )

    city1_data = pd.read_csv(city1_file, encoding="gbk")
    city2_data = pd.read_csv(city2_file, encoding="gbk")

    city1_data["设施级别"] = city1_data["type"].apply(categorize_facility)
    city2_data["设施级别"] = city2_data["type"].apply(categorize_facility)

    city1_prop = calculate_overall_proportion(city1_data)
    city2_prop = calculate_overall_proportion(city2_data)

    mean_df = pd.DataFrame({"城市1": city1_prop, "城市2": city2_prop})

    ax = mean_df.plot(kind="bar", figsize=(10, 6), color=["skyblue", "salmon"])
    plt.title("城市1和城市2的平均设施比例对比")
    plt.ylabel("设施比例")
    plt.xlabel("设施类型")
    plt.xticks(rotation=0)
    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.2f}",
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center",
            va="bottom",
            fontsize=10,
        )
    plt.show()

    labels = city1_prop.index
    city1_values = city1_prop.values
    city2_values = city2_prop.values
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    city1_values = np.concatenate((city1_values, [city1_values[0]]))
    city2_values = np.concatenate((city2_values, [city2_values[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, city1_values, color="blue", alpha=0.25, label="城市1")
    ax.fill(angles, city2_values, color="red", alpha=0.25, label="城市2")
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.title("城市1和城市2的设施比例分布雷达图")
    plt.legend()
    plt.show()
