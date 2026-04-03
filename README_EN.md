# D2024092929287

> Shuwei Cup modeling project: housing price forecasting, urban service system evaluation, and urban resilience analysis for two cities.

## 1. Project Abstract

This project is based on `D2024092929287.pdf` and builds a full data science workflow for two cities (City 1 / City 2):

1. Housing price forecasting and housing-scale estimation (Question 1)
2. Quantitative evaluation of urban service systems (Question 2)
3. Urban resilience and sustainability evaluation (Question 3)
4. Integrated investment and development strategy recommendations (Question 4)

The pipeline covers data preprocessing, feature engineering, model training, comparative evaluation, visualization, and decision-oriented conclusions.

## 2. Research Questions and Outputs

### Q1: Housing Price Forecasting and Housing Estimation
- Task: forecast housing price trends and estimate housing-related scale
- Methods: Linear Regression, Decision Tree, Random Forest, Gradient Boosting
- Outputs: model result files, performance comparison, and plots

### Q2: Urban Service System Evaluation
- Task: analyze structure and quantity across 15 service categories
- Methods: statistical analysis + density indicators + integrated scoring (MCE idea)
- Outputs: service comparison plots, facility density plots, and intermediate scoring files

### Q3: Urban Resilience Evaluation
- Task: evaluate emergency response and sustainable development capabilities
- Methods: multi-indicator integrated evaluation
- Outputs: resilience-related indicators and comparative analysis between cities

### Q4: Integrated Strategy Recommendation
- Task: provide investment recommendations based on Q1–Q3 findings
- Outputs: strengths/weaknesses summary and improvement priorities

## 3. Technical Workflow

1. Data preprocessing: missing values, outliers/range handling, field normalization
2. Feature engineering: correlation analysis (Spearman), RFE feature selection
3. Modeling: multi-model training and cross-validation
4. Analysis: error metrics, visual comparison, density and integrated scoring
5. Decision support: strategy suggestions for urban development and investment

## 4. Figure Gallery

![Service volume](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/服务数据量.png)

![Service number](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/service%20number.png)

![City 1 Facility density](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/City%201%20Facility%20density.png)

![City 2 Facility density](./Python%20Code%20and%20data/Python%20Code%20and%20data/question2/The%20generated%20images%20and%20files/City%202%20Facility%20density.png)

## 5. Environment

```bash
pip install -r requirements.txt
```

## 6. Repository

- GitHub: https://github.com/JAVAPYTHO/D2024092929287
