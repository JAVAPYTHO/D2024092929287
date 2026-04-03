# D2024092929287

> 数维杯建模项目：面向双城市的房价预测、服务体系评估与城市韧性分析。

## 项目简介

本项目基于 `D2024092929287.pdf` 的任务要求，围绕两个城市（City 1 / City 2）构建了从数据预处理到建模评估再到策略建议的完整流程，主要包含：

- **问题1：房价预测与住房相关指标估算**（多模型回归）
- **问题2：城市服务体系量化评估**（15类服务指标 + 综合评分）
- **问题3：城市韧性与可持续能力评估**（多指标综合）
- **问题4：综合投资建议与优化方向**

---

## 研究目标

1. 预测两城市未来房价变化趋势并估算住房规模。
2. 对教育、医疗、交通、生活服务等多类型城市服务进行量化比较。
3. 评估城市在极端事件下的应急韧性和可持续发展能力。
4. 给出可落地的城市治理与投资优化建议。

---

## 方法与技术路线

### 1) 数据预处理

- 缺失值填补（中位数、众数、KNN 插补）
- 异常值与区间值处理
- 数值标准化、特征工程

### 2) 模型构建（Question 1）

- 线性回归（Linear Regression）
- 决策树回归（Decision Tree）
- 随机森林回归（Random Forest）
- 梯度提升回归（Gradient Boosting）

并结合交叉验证、残差分析、Q-Q 图等方法进行模型诊断。

### 3) 综合评价（Question 2 & 3）

- 服务数量统计与结构对比
- 密度指数/权重计算
- 多指标综合评价（MCE思路）

---

## 项目结构

```text
D2024092929287/
├─ D2024092929287.pdf
├─ README.md
├─ requirements.txt
├─ LICENSE
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

## 结果图表示例（来自项目现有输出）

### 城市服务总量对比

![服务数据量](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数据量.png)

### 服务数量分布对比

![service number](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/service%20number.png)

### City 1 设施密度

![City 1 Facility density](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/City%201%20Facility%20density.png)

### City 2 设施密度

![City 2 Facility density](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/City%202%20Facility%20density.png)

> 注：以上图均来自仓库现有 `question2/The generated images and files` 目录。

---

## 环境与依赖

- Python 3.9+
- 推荐使用 `venv` 或 `conda` 虚拟环境

安装：

```bash
pip install -r requirements.txt
```

`requirements.txt` 已包含核心依赖：

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- scipy
- geopandas
- shapely
- openpyxl
- chardet

---

## 快速运行指南

### 数据预处理

目录：`Python Code and data/Python Code and data/Data Preprocessing/`

- `Appendix1 and Appendix2 Missing Value and Outlier Handling.py`
- `Appendix1 and Appendix2 Boxplot.py`

### Question1（建模）

目录：`Python Code and data/Python Code and data/question1/`

- `Q1_1.py`
- `01.py`

### Question2（服务体系分析）

目录：`Python Code and data/Python Code and data/question2/Python code/`

- `Calculate the total number of services.py`
- `city scores.py`
- `Service density of two cities.py`
- `Solve for density coefficient.py`
- `Solve for density index.py`
- `Draw bar chart of service quantities.py`
- `Draw radar chart.py`

### Question3/4（韧性与综合建议）

目录：`Python Code and data/Python Code and data/question3/`

- `q3.py`
- `q3_2.py`
- `q4.py`

---

## 主要结论（基于报告摘要）

- 在房价预测任务中，多模型对比后梯度提升回归表现最优（报告中给出较高 R²）。
- 两城市在服务资源结构与密度分布上存在显著差异，综合评分可用于识别优势与短板。
- 通过多指标韧性评估可定位城市应急体系的关键薄弱环节，并指导投资优先级。

---

## 复现提示

- 部分脚本仍含硬编码路径（如 `F:/...` 或占位路径），运行前请改为本机路径。
- 目录中含空格与中英文混合命名，命令行运行时建议使用引号包裹路径。

---

## 仓库地址

- GitHub: https://github.com/JAVAPYTHO/D2024092929287
