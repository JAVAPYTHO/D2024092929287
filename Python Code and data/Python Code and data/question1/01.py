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
file_path = 'Appendix 1.xlsx'
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

# 提取总车位数和车位比例
data[['Total Parking', 'Parking Ratio']] = data['parking space'].str.extract(r'(\d+)\(\d+:(\d+\.\d+)\)').astype(float)

# 删除原始列
del data['parking space']

# 处理带 '-' 的物业管理费，将取值区间取中间值
def process_property_fee(value):
    if '-' in str(value):
        low, high = map(float, value.split('-'))
        return (low + high) / 2
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
best_n_neighbors = None
best_mse = float('inf')
for n_neighbors in range(3, 11):
    imputer = KNNImputer(n_neighbors=n_neighbors)
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data_imputed = imputer.fit_transform(data[numeric_columns])
    data[numeric_columns] = data_imputed
    # 简单用训练集测试集划分和MSE评估下填补后的效果（这里只是示例，可以更精细评估）
    X_temp, _, y_temp, _ = train_test_split(data[numeric_columns], data['Total number of households'], test_size=0.3, random_state=42)
    model_temp = LinearRegression().fit(X_temp, y_temp)
    y_pred_temp = model_temp.predict(X_temp)
    mse_temp = mean_squared_error(y_temp, y_pred_temp)
    if mse_temp < best_mse:
        best_mse = mse_temp
        best_n_neighbors = n_neighbors

imputer = KNNImputer(n_neighbors=best_n_neighbors)
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
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

# 筛选与目标变量高度相关的特征（斯皮尔曼相关系数），同时增加统计检验验证相关性是否显著（这里简单用p值判断，可调整）
selected_features = []
for col in numerical_columns:
    corr, p_value = stats.spearmanr(data_processed_scaled['Total number of households'], data_processed_scaled[col])
    if abs(corr) > 0.3 and p_value < 0.05:
        selected_features.append(col)
selected_features.remove('Total number of households')

# 使用递归特征消除（RFE）进一步筛选特征，添加注释说明参数选择依据
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

# 预测测试集
y_pred_linear = linear_model_housing.predict(X_test_housing)

# 计算并输出多元线性回归模型的评价结果
mse_linear, r2_linear = evaluate_model(y_test_housing, y_pred_linear)
print("\n多元线性回归模型:")
print(f"MSE: {mse_linear:.4f}")
print(f"R²: {r2_linear:.4f}")

# 输出多元线性回归方程
coefficients = linear_model_housing.coef_
intercept = linear_model_housing.intercept_
feature_names = X_housing.columns
print("多元线性回归方程 (基于标准化数据): y = {:.4f} + {}".format(intercept, " + ".join([f"{coef:.4f}*{name}" for coef, name in zip(coefficients, feature_names)])))

# 使用随机森林进行住房总量估算，拓展参数网格范围
param_grid_rf = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}
grid_search_rf = GridSearchCV(RandomForestRegressor(random_state=42), param_grid_rf, cv=5, scoring='r2', n_jobs=-1)
grid_search_rf.fit(X_train_housing, y_train_housing)
rf_model_housing = grid_search_rf.best_estimator_

# 预测测试集
y_pred_rf = rf_model_housing.predict(X_test_housing)

# 计算并输出随机森林模型的评价结果
mse_rf, r2_rf = evaluate_model(y_test_housing, y_pred_rf)
print("\n随机森林模型:")
print(f"MSE: {mse_rf:.4f}")
print(f"R²: {r2_rf:.4f}")

# 使用梯度提升回归模型进行住房总量预测，拓展参数网格范围
param_grid_gb = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.05, 0.1, 0.15],
    'max_depth': [3, 5, 8]
}
grid_search_gb = GridSearchCV(GradientBoostingRegressor(random_state=42), param_grid_gb, cv=5, scoring='r2', n_jobs=-1)
grid_search_gb.fit(X_train_housing, y_train_housing)
gb_model_housing = grid_search_gb.best_estimator_

# 预测测试集
y_pred_gb = gb_model_housing.predict(X_test_housing)

# 计算并输出梯度提升回归模型的评价结果
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

# 可视化所有模型的真实值与预测值的对比以及残差、QQ图，添加一些美化设置（如坐标轴标签字体大小等）
fig, axs = plt.subplots(3, 3, figsize=(18, 18))

# 多元线性回归
axs[0, 0].scatter(y_test_housing, y_pred_linear, alpha=0.7)
axs[0, 0].plot([y_test_housing.min(), y_test_housing.max()], [y_test_housing.min(), y_test_housing.max()], color='red', linestyle='--')
axs[0, 0].set_title(f'Linear Regression: Actual vs Predicted (R² = {r2_linear:.4f})')
axs[0, 0].set_xlabel('Actual Total Households', fontsize=12)
axs[0, 0].set_ylabel('Predicted Total Households', fontsize=12)

residuals_linear = y_test_housing - y_pred_linear
axs[0, 1].scatter(y_pred_linear, residuals_linear, alpha=0.7)
axs[0, 1].axhline(y=0, color='red', linestyle='--')
axs[0, 1].set_title('Linear Regression: Residual Plot')
axs[0, 1].set_xlabel('Predicted Total Households', fontsize=12)
axs[0, 1].set_ylabel('Residuals', fontsize=12)

stats.probplot(residuals_linear, dist="norm", plot=axs[0, 2])
axs[0, 2].set_title('Linear Regression: Q-Q Plot')

# 随机森林
axs[1, 0].scatter(y_test_housing, y_pred_rf, alpha=0.7)
axs[1, 0].plot([y_test_housing.min(), y_test_housing.max()], [y_test_housing.min(), y_test_housing.max()], color='red', linestyle='--')
axs[1, 0].set_title(f'Random Forest: Actual vs Predicted (R² = {r2_rf:.4f})')
axs[1, 0].set_xlabel('Actual Total Households', fontsize=12)
axs[1, 0].set_ylabel('Predicted Total Households', fontsize=12)

residuals_rf = y_test_housing - y_pred_rf
axs[1, 1].scatter(y_pred_rf, residuals_rf, alpha=0.7)
axs[1, 1].axhline(y=0, color='red', linestyle='--')
axs[1, 1].set_title('Random Forest: Residual Plot')
axs[1, 1].set_xlabel('Predicted Total Households', fontsize=12)
axs[1, 1].set_ylabel('Residuals', fontsize=12)

stats.probplot(residuals_rf, dist="norm", plot=axs[1, 2])
axs[1, 2].set_title('Random Forest: Q-Q Plot')

# 梯度提升回归
axs[2, 0].scatter(y_test_housing, y_pred_gb, alpha=0.7)
axs[2, 0].plot([y_test_housing.min(), y_test_housing.max()], [y_test_housing.min(), y_test_housing.max()], color='red', linestyle='--')
axs[2, 0].set_title(f'Gradient Boosting Regression: Actual vs Predicted (R² = {r2_gb:.4f})')
axs[2, 0].set_xlabel('Actual Total Households', fontsize=12)
axs[2, 0].set_ylabel('Predicted Total Households', fontsize=12)

residuals_gb = y_test_housing - y_pred_gb
axs[2, 1].scatter(y_pred_gb, residuals_gb, alpha=0.7)
axs[2, 1].axhline(y=0, color='red', linestyle='--')
axs[2, 1].set_title('Gradient Boosting Regression: Residual Plot')
axs[2, 1].set_xlabel('Predicted Total Households', fontsize=12)
axs[2, 1].set_ylabel('Residuals', fontsize=12)

stats.probplot(residuals_gb, dist="norm", plot=axs[2, 2])
axs[2, 2].set_title('Gradient Boosting Regression: Q-Q Plot')

plt.tight_layout()
plt.show()