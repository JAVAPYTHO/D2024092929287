<<<<<<< HEAD
# D2024092929287 项目说明

本项目是一个基于 Python 的数据分析与建模项目，围绕房地产数据预处理、城市服务设施空间分布分析，以及房价/住房相关指标预测开展。项目包含原始数据、清洗脚本、建模脚本和结果文件。

## 1. 项目做了什么

从代码结构和脚本逻辑来看，项目主要完成了以下工作：

1. **数据预处理（Data Preprocessing）**
   - 读取 `Appendix 1.xlsx` 和 `Appendix 2.xlsx`。
   - 对数值型字段进行提取与标准化（如处理区间值、字符串数值）。
   - 对缺失值进行填补（中位数、众数等策略）。
   - 生成清洗后的数据文件（如 `Processed_Appendix_1.xlsx`、`Processed_Appendix_2.xlsx`）。

2. **问题一（question1）：住房/房价相关建模分析**
   - 进行缺失值分析、经纬度清洗、车位字段解析。
   - 使用 `KNNImputer` 做缺失值插补。
   - 使用 Spearman 相关系数与 RFE 进行特征筛选。
   - 建立并评估多种回归模型：
     - 线性回归（Linear Regression）
     - 随机森林回归（Random Forest Regressor）
     - 梯度提升回归（Gradient Boosting Regressor）
   - 使用交叉验证输出模型泛化效果，并可视化预测对比、残差图、Q-Q 图。

3. **问题二（question2）：城市公共服务设施与韧性分析**
   - 读取多类城市 POI/设施 CSV 数据（交通、医疗、公共设施、生活服务等）。
   - 进行编码兼容读取（UTF-8 / ISO-8859-1 / GBK）、去重、缺失值处理。
   - 进行地理空间转换（`GeoPandas` + `Shapely`），按城市边界计算设施密度。
   - 生成散点分布图、柱状图、雷达图、密度指数相关结果。

4. **问题三（question3）及结果整理**
   - 包含后续问题分析脚本（如 `q3.py`、`q3_2.py`、`q4.py`）。
   - 输出结果汇总在 `House Price Prediction Results/房价预测结果` 中，含多模型结果 Excel 文件。

---

## 2. 目录结构（核心）

```text
D2024092929287/
├─ D2024092929287.pdf
├─ README.md
├─ House Price Prediction Results/
│  └─ 房价预测结果/
│     ├─ city_1.xlsx
│     ├─ city_2.xlsx
│     ├─ Decision Tree_city_1.xlsx
│     ├─ Decision Tree_city_2.xlsx
│     ├─ Gradient Boosting_city_1.xlsx
│     ├─ Gradient Boosting_city_2.xlsx
│     ├─ Random Forest_city_1.xlsx
│     ├─ Random Forest_city_2.xlsx
│     ├─ Processed_Appendix_1.xlsx
│     └─ Processed_Appendix_2.xlsx
└─ Python Code and data/
   └─ Python Code and data/
      ├─ Data Preprocessing/
      ├─ question1/
      ├─ question2/
      └─ question3/
```

---

## 3. 运行环境

建议 Python 版本：`3.9+`

主要依赖（按脚本实际导入汇总）：

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `scipy`
- `geopandas`
- `shapely`
- `openpyxl`

安装示例：

```bash
pip install pandas numpy scikit-learn matplotlib seaborn scipy geopandas shapely openpyxl
```

---

## 4. 运行说明

> 注意：部分脚本中存在硬编码路径（如 `F:/pythonProject/...`、`pathToAppendix1.xlsx`），运行前请先改成本机实际路径。

### 4.1 数据预处理

进入：

- `Python Code and data/Python Code and data/Data Preprocessing/`

运行：

- `Appendix1 and Appendix2 Missing Value and Outlier Handling.py`
- `Appendix1 and Appendix2 Boxplot.py`

### 4.2 question1 建模分析

进入：

- `Python Code and data/Python Code and data/question1/`

运行：

- `Q1_1.py`（核心建模脚本）
- `01.py`（辅助脚本）

### 4.3 question2 城市设施分析

进入：

- `Python Code and data/Python Code and data/question2/Python code/`

按需求运行脚本（例如）：

- `Calculate the total number of services.py`
- `city scores.py`
- `Service density of two cities.py`
- `Solve for density coefficient.py`
- `Solve for density index.py`
- `Draw bar chart of service quantities.py`
- `Draw radar chart.py`

### 4.4 question3 脚本

进入：

- `Python Code and data/Python Code and data/question3/`

运行：

- `q3.py`
- `q3_2.py`
- `q4.py`

---

## 5. 当前代码特点与建议

### 已完成特点

- 覆盖数据预处理、特征工程、模型训练、可视化、空间分析完整流程。
- 采用多模型对比与交叉验证，具备一定实验严谨性。

### 可改进点

1. 建议将硬编码路径改为相对路径或配置文件。
2. 建议补充统一入口脚本（如 `main.py`）与参数化运行方式。
3. 建议增加 `requirements.txt` 便于复现。
4. 建议将中英文命名与路径风格统一，提高可维护性。

---

## 6. 结果文件位置

主要输出位于：

- `House Price Prediction Results/房价预测结果/`

可用于后续报告撰写、图表复现与模型结果对比。
=======
# D2024092929287
>>>>>>> 320752fb5391dd4e33ce79f68d7683b18345edef
