# D2024092929287

<div align="center">

**数维杯建模项目：双城市房价预测、服务体系评估与城市韧性分析**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](#六环境与安装)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-D2024092929287-black.svg)](https://github.com/JAVAPYTHO/D2024092929287)

中文说明 | [English Version](./README_EN.md)

</div>

---

## 目录

- [一、项目摘要](#一项目摘要)
- [二、研究问题与对应产出](#二研究问题与对应产出)
- [三、技术路线](#三技术路线)
- [四、项目结构](#四项目结构)
- [五、图表展示（项目产出）](#五图表展示项目产出)
- [六、环境与安装](#六环境与安装)
- [七、运行说明](#七运行说明)
- [八、关键结论](#八关键结论)
- [九、复现与使用注意](#九复现与使用注意)
- [十、仓库链接](#十仓库链接)

---

## 一、项目摘要

本项目基于 `D2024092929287.pdf`，围绕两个城市（City 1 / City 2）构建了完整的数据建模流程：

1. 房价预测与住房规模估算（Question 1）
2. 城市服务系统量化评估（Question 2）
3. 城市韧性与可持续能力评估（Question 3）
4. 综合投资与发展策略建议（Question 4）

项目覆盖数据清洗、特征工程、模型训练、对比评估、可视化分析与策略输出，具备完整的“数据—模型—决策”闭环。

---

## 二、研究问题与对应产出

### Q1：房价预测与住房估算

- **任务**：预测城市房价趋势并估计住房相关规模
- **方法**：线性回归、决策树、随机森林、梯度提升回归
- **产出**：多模型预测结果文件、模型表现对比、相关可视化图形

### Q2：城市服务体系评估

- **任务**：对 15 类服务行业进行结构与数量分析
- **方法**：统计分析 + 密度指标 + 综合评分（MCE 思路）
- **产出**：服务数量对比图、设施密度图、评分中间文件

### Q3：城市韧性评估

- **任务**：评估城市应急响应与可持续发展能力
- **方法**：多指标融合评价
- **产出**：韧性相关综合指标与城市差异分析

### Q4：综合策略建议

- **任务**：结合前 3 问结果形成投资建议
- **产出**：城市优劣势总结与改进方向

---

## 三、技术路线

1. 数据预处理：缺失值处理、异常值/区间值处理、字段标准化
2. 特征工程：相关性分析（Spearman）、RFE 特征筛选
3. 模型建模：多模型训练与交叉验证
4. 结果分析：误差指标、可视化对比、密度与综合评分
5. 决策输出：形成城市发展与投资建议

---

## 四、项目结构

```text
D2024092929287/
├─ D2024092929287.pdf
├─ README.md
├─ README_EN.md
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

## 五、图表展示（项目产出）

以下图表均来自目录：
`Python Code and data/Python Code and data/question2/The generated images and files/`

### 1）城市服务规模总览

![服务数据量](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数据量.png)

配文：该图展示了两城市在多类服务业中的总体数量规模，是判断城市服务供给能力上限的基础图。

![service number](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/service%20number.png)

配文：该图用于观察服务类型分布结构，帮助识别“优势服务”和“短板服务”类别。

### 2）设施空间密度（城市级）

![City 1 Facility density](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/City%201%20Facility%20density.png)

配文：City 1 设施密度图，反映服务设施在城市空间上的聚集程度与覆盖水平。

![City 2 Facility density](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/City%202%20Facility%20density.png)

配文：City 2 设施密度图，可与 City 1 对照分析核心区—边缘区服务均衡性差异。

### 3）分类服务对比图（示例）

![医疗与健康](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数量对比图/Medical%20and%20health.png)

配文：医疗与健康类服务数量对比，可用于评估城市公共健康资源保障能力。

![交通设施](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数量对比图/Transportation%20facilities.png)

配文：交通设施类服务对比，体现城市通达性与应急疏散基础设施水平。

![科教文化](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数量对比图/Science,%20education,%20and%20culture.png)

配文：科教文化服务对比，反映城市长期发展的人才与教育资源支撑能力。

### 4）更多图表目录

项目中还包含完整分类图集：

- `服务数量对比图/`
- `Comparison chart of the number of services/`

可按类别继续扩展到 README 或用于论文附录展示。

---

## 六、环境与安装

- Python 3.9+
- 推荐使用虚拟环境（`venv` / `conda`）

安装依赖：

```bash
pip install -r requirements.txt
```

### 三步快速复现

```bash
# 1) 安装依赖
pip install -r requirements.txt

# 2) 运行单个任务（示例：Q2）
python main.py --task q2

# 3) 查看输出结果
# House Price Prediction Results/房价预测结果/
# Python Code and data/Python Code and data/question2/The generated images and files/
```

---

## 七、运行说明

### 统一入口（推荐）

```bash
# 只跑 Q1
python main.py --task q1

# 只跑 Q2
python main.py --task q2

# 只跑 Q3
python main.py --task q3

# 全部串行执行
python main.py --task all
```

### 1）数据预处理

目录：`Python Code and data/Python Code and data/Data Preprocessing/`

- `Appendix1 and Appendix2 Missing Value and Outlier Handling.py`
- `Appendix1 and Appendix2 Boxplot.py`

### 2）Q1 建模与预测

目录：`Python Code and data/Python Code and data/question1/`

- `Q1_1.py`
- `01.py`

### 3）Q2 服务体系分析

目录：`Python Code and data/Python Code and data/question2/Python code/`

- `Calculate the total number of services.py`
- `city scores.py`
- `Service density of two cities.py`
- `Solve for density coefficient.py`
- `Solve for density index.py`
- `Draw bar chart of service quantities.py`
- `Draw radar chart.py`

### 4）Q3/Q4 韧性与综合评估

目录：`Python Code and data/Python Code and data/question3/`

- `q3.py`
- `q3_2.py`
- `q4.py`

---

## 八、关键结论

- 房价预测中，梯度提升回归在多模型对比中表现较优。
- 双城市在服务资源数量与空间密度上存在明显结构差异。
- 多指标韧性评估可识别城市应急体系关键短板，并支持投资优先级排序。

---

## 九、复现与使用注意

- 部分脚本存在硬编码路径（如 `F:/...` 或占位路径），运行前需改成本机路径。
- 项目含中英文与空格路径，命令行执行时建议使用引号包裹路径。
- 若仅查看结果，可直接访问：
  - `House Price Prediction Results/房价预测结果/`
  - `question2/The generated images and files/`

---

## 十、结果索引（核心）

- 房价模型输出：`House Price Prediction Results/房价预测结果/`
- Q2 图表输出：`Python Code and data/Python Code and data/question2/The generated images and files/`
- Q3 数据输入：`Python Code and data/Python Code and data/question3/Appendix 3/` 与 `Appendix 4/`

## 十一、仓库链接

- GitHub: https://github.com/JAVAPYTHO/D2024092929287
