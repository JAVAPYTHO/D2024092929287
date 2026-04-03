# D2024092929287

<div align="center">

**Shuwei Cup Modeling Project: Dual-City Housing Forecasting, Urban Service Evaluation, and Resilience Analysis**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](#6-environment--installation)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/GitHub-D2024092929287-black.svg)](https://github.com/JAVAPYTHO/D2024092929287)

[中文版说明](./README.md) | English

</div>

---

## Table of Contents

- [1. Project Abstract](#1-project-abstract)
- [2. Research Questions and Outputs](#2-research-questions-and-outputs)
- [3. Technical Workflow](#3-technical-workflow)
- [4. Project Structure](#4-project-structure)
- [5. Figure Gallery](#5-figure-gallery)
- [6. Environment & Installation](#6-environment--installation)
- [7. How to Run](#7-how-to-run)
- [8. Key Findings](#8-key-findings)
- [9. Reproducibility Notes](#9-reproducibility-notes)
- [10. Repository](#10-repository)

---

## 1. Project Abstract

This project is based on `D2024092929287.pdf` and builds a complete data science workflow for two cities (City 1 / City 2):

1. Housing price forecasting and housing-scale estimation (Question 1)
2. Quantitative evaluation of urban service systems (Question 2)
3. Urban resilience and sustainability evaluation (Question 3)
4. Integrated investment and development strategy recommendations (Question 4)

The pipeline includes data preprocessing, feature engineering, model training, comparative evaluation, visualization, and decision-oriented conclusions.

---

## 2. Research Questions and Outputs

### Q1: Housing Price Forecasting and Housing Estimation
- **Task**: forecast housing price trends and estimate housing-related scale
- **Methods**: Linear Regression, Decision Tree, Random Forest, Gradient Boosting
- **Outputs**: model result files, performance comparison, and plots

### Q2: Urban Service System Evaluation
- **Task**: analyze structure and quantity across 15 service categories
- **Methods**: statistical analysis + density indicators + integrated scoring (MCE idea)
- **Outputs**: service comparison plots, facility density plots, and intermediate scoring files

### Q3: Urban Resilience Evaluation
- **Task**: evaluate emergency response and sustainable development capabilities
- **Methods**: multi-indicator integrated evaluation
- **Outputs**: resilience indicators and comparative analysis between cities

### Q4: Integrated Strategy Recommendation
- **Task**: provide investment recommendations based on Q1–Q3 findings
- **Outputs**: strengths/weaknesses summary and improvement priorities

---

## 3. Technical Workflow

1. Data preprocessing: missing values, outlier/range handling, and field normalization
2. Feature engineering: correlation analysis (Spearman), RFE feature selection
3. Modeling: multi-model training and cross-validation
4. Analysis: error metrics, visual comparison, density, and integrated scoring
5. Decision support: strategy suggestions for urban development and investment

---

## 4. Project Structure

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

## 5. Figure Gallery

All figures below are from:
`Python Code and data/Python Code and data/question2/The generated images and files/`

### 1) Service Capacity Overview

![Service volume](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数据量.png)

Caption: This figure shows the overall service scale across categories for the two cities, used to assess upper-bound service supply capacity.

![Service number](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/service%20number.png)

Caption: This figure highlights the service-type distribution structure and helps identify strong and weak categories.

### 2) Spatial Density at City Level

![City 1 Facility density](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/City%201%20Facility%20density.png)

Caption: City 1 facility density map, showing clustering intensity and spatial coverage of service facilities.

![City 2 Facility density](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/City%202%20Facility%20density.png)

Caption: City 2 facility density map, suitable for core-vs-periphery balance comparison with City 1.

### 3) Category-wise Service Comparison (Examples)

![Medical and health](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数量对比图/Medical%20and%20health.png)

Caption: Medical and health service comparison, reflecting public health resource support capacity.

![Transportation facilities](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数量对比图/Transportation%20facilities.png)

Caption: Transportation facilities comparison, related to accessibility and emergency evacuation support.

![Science, education, and culture](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数量对比图/Science,%20education,%20and%20culture.png)

Caption: Science/education/culture service comparison, indicating long-term talent and education support.

### 4) More Figure Collections

Additional complete category sets are available in:

- `服务数量对比图/`
- `Comparison chart of the number of services/`

These can be further embedded in README or used in appendix sections of reports.

---

## 6. Environment & Installation

- Python 3.9+
- A virtual environment is recommended (`venv` / `conda`)

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3-step Quick Reproduction

```bash
# 1) Install dependencies
pip install -r requirements.txt

# 2) Run one task (example: Q2)
python main.py --task q2

# 3) Check outputs
# House Price Prediction Results/房价预测结果/
# Python Code and data/Python Code and data/question2/The generated images and files/
```

---

## 7. How to Run

### Unified Runner (Recommended)

```bash
# Run only Q1
python main.py --task q1

# Run only Q2
python main.py --task q2

# Run only Q3
python main.py --task q3

# Run all tasks in sequence
python main.py --task all
```

### 1) Data Preprocessing

Directory: `Python Code and data/Python Code and data/Data Preprocessing/`

- `Appendix1 and Appendix2 Missing Value and Outlier Handling.py`
- `Appendix1 and Appendix2 Boxplot.py`

### 2) Q1 Modeling

Directory: `Python Code and data/Python Code and data/question1/`

- `Q1_1.py`
- `01.py`

### 3) Q2 Service Analysis

Directory: `Python Code and data/Python Code and data/question2/Python code/`

- `Calculate the total number of services.py`
- `city scores.py`
- `Service density of two cities.py`
- `Solve for density coefficient.py`
- `Solve for density index.py`
- `Draw bar chart of service quantities.py`
- `Draw radar chart.py`

### 4) Q3/Q4 Resilience and Strategy

Directory: `Python Code and data/Python Code and data/question3/`

- `q3.py`
- `q3_2.py`
- `q4.py`

---

## 8. Key Findings

- Gradient Boosting performs strongly among compared models for housing price prediction.
- The two cities show clear structural differences in service quantity and spatial density.
- Multi-indicator resilience evaluation helps identify weak links and prioritize investment.

---

## 9. Reproducibility Notes

- Some scripts include hardcoded paths (e.g., `F:/...` placeholders). Update to local paths before running.
- Since directories contain spaces and mixed-language names, use quoted paths in command lines.

---

## 10. Output Index (Core)

- Housing model outputs: `House Price Prediction Results/房价预测结果/`
- Q2 figures: `Python Code and data/Python Code and data/question2/The generated images and files/`
- Q3 input folders: `Python Code and data/Python Code and data/question3/Appendix 3/` and `Appendix 4/`

## 11. Repository

- GitHub: https://github.com/JAVAPYTHO/D2024092929287
