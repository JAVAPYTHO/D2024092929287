# D2024092929287

基于“数维杯”赛题的数据分析与建模项目，面向两个城市（City 1 / City 2）完成：

- 房价与住房相关指标预测
- 城市服务体系量化评估
- 城市韧性与可持续能力评估
- 综合投资与发展建议

## 项目概览

本项目对应论文 `D2024092929287.pdf` 的 4 个问题，代码与结果文件已按题目拆分：

1. **Question 1：房价预测与住房估算**
   - 数据清洗、缺失值填补、特征工程
   - 多模型回归对比（线性回归 / 随机森林 / 梯度提升 / 决策树）
   - 模型评估与可视化（R²、残差、Q-Q 图等）

2. **Question 2：城市服务系统评估**
   - 15 类服务行业数据统计与对比
   - 综合评分（MCE 思路）
   - 柱状图、雷达图、服务密度等可视化

3. **Question 3：城市韧性评估**
   - 基于交通、医疗、公共设施等指标构建综合评估
   - 识别薄弱环节并形成改进方向

4. **Question 4：综合策略建议**
   - 结合前 3 问结论，给出投资重点与优化建议

---

## 目录结构

```text
D2024092929287/
├─ D2024092929287.pdf
├─ README.md
├─ requirements.txt
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

## 环境要求

- Python 3.9+
- 建议使用虚拟环境（venv/conda）

安装依赖：

```bash
pip install -r requirements.txt
```

---

## 快速开始

### 1) 数据预处理

目录：`Python Code and data/Python Code and data/Data Preprocessing/`

可运行脚本：
- `Appendix1 and Appendix2 Missing Value and Outlier Handling.py`
- `Appendix1 and Appendix2 Boxplot.py`

### 2) Question1 建模

目录：`Python Code and data/Python Code and data/question1/`

核心脚本：
- `Q1_1.py`
- `01.py`

### 3) Question2 服务分析

目录：`Python Code and data/Python Code and data/question2/Python code/`

常用脚本：
- `Calculate the total number of services.py`
- `city scores.py`
- `Service density of two cities.py`
- `Solve for density coefficient.py`
- `Solve for density index.py`
- `Draw bar chart of service quantities.py`
- `Draw radar chart.py`

### 4) Question3 / Question4 相关脚本

目录：`Python Code and data/Python Code and data/question3/`

可运行脚本：
- `q3.py`
- `q3_2.py`
- `q4.py`

---

## 结果文件

主要输出位于：

- `House Price Prediction Results/房价预测结果/`

---

## 注意事项

- 部分脚本包含硬编码路径（如 `F:/...` 或占位路径），运行前请改为本机路径。
- 中英文路径混用较多，建议统一路径命名以提升复现稳定性。
