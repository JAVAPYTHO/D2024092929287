import pandas as pd
import warnings
from sklearn.impute import KNNImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats

# 忽略警告信息
warnings.filterwarnings('ignore')

# 读取文件，添加异常处理
file_path = 'Appendix 2.xlsx'
try:
    data = pd.read_excel(file_path)
except FileNotFoundError:
    print(f"文件 {file_path} 不存在，请检查文件路径是否正确。")
    raise

# 检查数据中各列的缺失值情况
missing_values = data.isnull().sum().reset_index()
missing_values.columns = ['Column', 'Missing Values']
missing_values['Missing Percentage'] = (missing_values['Missing Values'] / len(data)) * 100
print(missing_values)

# 提取需要的列并进行预处理
data.columns = data.columns.str.strip()
selected_columns = ['Price (USD)', 'Total number of households', 'Greening rate', 'Floor area ratio',
                    'Property management fee（/m²/month USD）', 'above-ground parking fee（/month USD）',
                    'underground parking fee（/month USD）', 'lon', 'lat', 'X', 'Y', 'parking space']
data = data[selected_columns]

# 去除度数符号并将经纬度转换为浮点数
data['lon'] = pd.to_numeric(data['lon'].astype(str).str.replace('°', '', regex=False), errors='coerce')
data['lat'] = pd.to_numeric(data['lat'].astype(str).str.replace('°', '', regex=False), errors='coerce')

# 填补缺失的经纬度
data['lon'] = data['lon'].fillna(data['lon'].median())
data['lat'] = data['lat'].fillna(data['lat'].median())

# 提取总车位数和车位比例
data[['Total Parking', 'Parking Ratio']] = data['parking space'].str.extract(r'(\d+)\(\d+:(\d+\.\d+)\)').astype(float)

# 删除原始列
data = data.drop(columns=['parking space'])

# 处理带 '-' 的物业管理费，将取值区间取中间值
def process_property_fee(value):
    if '-' in str(value):
        try:
            low, high = map(float, value.split('-'))
            return (low + high) / 2
        except ValueError:
            return np.nan
    else:
        try:
            return float(value)
        except ValueError:
            return np.nan

data['Property management fee（/m²/month USD）'] = data['Property management fee（/m²/month USD）'].apply(process_property_fee)

# 填充停车费的缺失值
for col in ['above-ground parking fee（/month USD）', 'underground parking fee（/month USD）']:
    data[col] = data[col].fillna(0)
    data[f'No {col.split()[0]} Parking'] = data[col].apply(lambda x: 1 if x == 0 else 0)

# 使用 KNNImputer 进行数值列的缺失值填补，通过循环选择较优的 n_neighbors 参数
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
best_n_neighbors = None
best_mse = float('inf')
for n_neighbors in range(3, 11):
    imputer = KNNImputer(n_neighbors=n_neighbors)
    data_imputed = imputer.fit_transform(data[numeric_columns])
    X_temp, _, y_temp, _ = train_test_split(data_imputed, data_imputed[:, 1], test_size=0.3, random_state=42)
    model_temp = LinearRegression().fit(X_temp, y_temp)
    y_pred_temp = model_temp.predict(X_temp)
    mse_temp = mean_squared_error(y_temp, y_pred_temp)
    if mse_temp < best_mse:
        best_mse = mse_temp
        best_n_neighbors = n_neighbors

# 使用最优的 n_neighbors 重新填补数据
imputer = KNNImputer(n_neighbors=best_n_neighbors)
data[numeric_columns] = imputer.fit_transform(data[numeric_columns])

# 特征选择和数据准备
categorical_columns = ['lon', 'lat']
numerical_columns = ['Total number of households', 'Greening rate', 'Floor area ratio',
                     'Property management fee（/m²/month USD）', 'above-ground parking fee（/month USD）',
                     'underground parking fee（/month USD）', 'Total Parking', 'Parking Ratio']
data_processed = data[numerical_columns + categorical_columns]

# 标准化数据
scaler = StandardScaler()
data_processed_scaled = pd.DataFrame(scaler.fit_transform(data_processed), columns=data_processed.columns)

# 计算斯皮尔曼相关系数
data_spearman_corr = data_processed_scaled.corr(method='spearman')
print("斯皮尔曼相关系数矩阵:\n", data_spearman_corr)

# 可视化斯皮尔曼相关系数矩阵
plt.figure(figsize=(12, 10))
sns.heatmap(data_spearman_corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Spearman Correlation Heatmap')
plt.show()

# 筛选与目标变量高度相关的特征（斯皮尔曼相关系数）
selected_features = []
for col in numerical_columns:
    corr, p_value = stats.spearmanr(data_processed_scaled['Total number of households'], data_processed_scaled[col])
    if abs(corr) > 0.3 and p_value < 0.05:
        selected_features.append(col)
if 'Total number of households' in selected_features:
    selected_features.remove('Total number of households')

# 使用递归特征消除（RFE）进一步筛选特征
linear_model = LinearRegression()
rfe = RFE(estimator=linear_model, n_features_to_select=5)
rfe.fit(data_processed_scaled[selected_features], data_processed_scaled['Total number of households'])
selected_features = [feature for feature, support in zip(selected_features, rfe.support_) if support]

# 设定模型的特征和目标变量（住房总量预测）
X_housing = data_processed_scaled[selected_features]
y_housing = data_processed_scaled['Total number of households']

# 划分训练集和测试集
X_train_housing, X_test_housing, y_train_housing, y_test_housing = train_test_split(X_housing, y_housing, test_size=0.3, random_state=42)

# 封装计算模型评价指标的函数
def evaluate_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, r2

# 多元线性回归模型训练
linear_model_housing = LinearRegression()
linear_model_housing.fit(X_train_housing, y_train_housing)
y_pred_linear = linear_model_housing.predict(X_test_housing)

# 计算并输出多元线性回归模型的评价结果
mse_linear, r2_linear = evaluate_model(y_test_housing, y_pred_linear)
print("\n多元线性回归模型:")
print(f"MSE: {mse_linear:.4f}")
print(f"R²: {r2_linear:.4f}")

# 输出多元线性回归方程
coefficients = linear_model_housing.coef_
intercept = linear_model_housing.intercept_
print("多元线性回归方程 (基于标准化数据): y = {:.4f} + {}".format(intercept, " + ".join([f"{coef:.4f}*{name}" for coef, name in zip(coefficients, X_housing.columns)])))

# 使用随机森林进行住房总量估算
param_grid_rf = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}
grid_search_rf = GridSearchCV(RandomForestRegressor(random_state=42), param_grid_rf, cv=5, scoring='r2', n_jobs=-1)
grid_search_rf.fit(X_train_housing, y_train_housing)
rf_model_housing = grid_search_rf.best_estimator_

y_pred_rf = rf_model_housing.predict(X_test_housing)
mse_rf, r2_rf = evaluate_model(y_test_housing, y_pred_rf)
print("\n随机森林模型:")
print(f"MSE: {mse_rf:.4f}")
print(f"R²: {r2_rf:.4f}")

# 使用梯度提升回归模型进行住房总量预测
param_grid_gb = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.05, 0.1, 0.15],
    'max_depth': [3, 5, 8]
}
grid_search_gb = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid_gb, cv=5, scoring='r2', n_jobs=-1)
grid_search_gb.fit(X_train_housing, y_train_housing)
gb_model_housing = grid_search_gb.best_estimator_

y_pred_gb = gb_model_housing.predict(X_test_housing)
mse_gb, r2_gb = evaluate_model(y_test_housing, y_pred_gb)
print("\n梯度提升回归模型:")
print(f"MSE: {mse_gb:.4f}")
print(f"R²: {r2_gb:.4f}")

# 交叉验证评估三种模型
cv_scores_linear = cross_val_score(linear_model_housing, X_housing, y_housing, cv=5, scoring='r2')
cv_scores_rf = cross_val_score(rf_model_housing, X_housing, y_housing, cv=5, scoring='r2')
cv_scores_gb = cross_val_score(gb_model_housing, X_housing, y_housing, cv=5, scoring='r2')

print("\n多元线性回归交叉验证 R² 平均值: {:.4f}".format(cv_scores_linear.mean()))
print("随机森林交叉验证 R² 平均值: {:.4f}".format(cv_scores_rf.mean()))
print("梯度提升回归交叉验证 R² 平均值: {:.4f}".format(cv_scores_gb.mean()))

# 可视化所有模型的真实值与预测值的对比以及残差、QQ图
fig, axs = plt.subplots(3, 3, figsize=(18, 18))

# 通过循环减少重复代码，绘制每个模型的实际值 vs. 预测值、残差图、QQ图
models = {
    "Linear Regression": (y_test_housing, y_pred_linear, r2_linear),
    "Random Forest": (y_test_housing, y_pred_rf, r2_rf),
    "Gradient Boosting": (y_test_housing, y_pred_gb, r2_gb)
}
for i, (model_name, (y_true, y_pred, r2)) in enumerate(models.items()):
    # 实际值 vs. 预测值
    axs[i, 0].scatter(y_true, y_pred, alpha=0.7)
    axs[i, 0].plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], color='red', linestyle='--')
    axs[i, 0].set_title(f'{model_name}: Actual vs Predicted (R² = {r2:.4f})')
    axs[i, 0].set_xlabel('Actual Total Households', fontsize=12)
    axs[i, 0].set_ylabel('Predicted Total Households', fontsize=12)

    # 残差图
    residuals = y_true - y_pred
    axs[i, 1].scatter(y_pred, residuals, alpha=0.7)
    axs[i, 1].axhline(y=0, color='red', linestyle='--')
    axs[i, 1].set_title(f'{model_name}: Residual Plot')
    axs[i, 1].set_xlabel('Predicted Total Households', fontsize=12)
    axs[i, 1].set_ylabel('Residuals', fontsize=12)

    # QQ图
    stats.probplot(residuals, dist="norm", plot=axs[i, 2])
    axs[i, 2].set_title(f'{model_name}: Q-Q Plot')

plt.tight_layout()
plt.show()
