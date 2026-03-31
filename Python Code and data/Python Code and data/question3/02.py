import pandas as pd
import matplotlib.pyplot as plt
import warnings
import numpy as np

warnings.filterwarnings("ignore")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#比赛结束前最后两天售后群发布无水印可视化结果+无标注代码【可直接提交】为了防止倒卖， 论文写作过程中遗留数个致命问题，无关代码，该问题解决方式仅在官网授权售后群答疑，盗卖方式购买资料不提供答疑，感谢理解 资料助攻购买链接+说明https://docs.qq.com/doc/p/2e45489c100c6a59f013660a1e9c359f434bb706
# 加载数据
city1_data = pd.read_csv('F:\pythonProject\python\question2\Appendix 3/Accommodation service data.csv', encoding='gbk')
city2_data = pd.read_csv('F:\pythonProject\python\question2\Appendix 4/Accommodation service data.csv', encoding='gbk')

def categorize_facility(facility_type):
    if facility_type in ['五星级宾馆', '四星级宾馆', '奢华酒店']:
        return '高级设施'
    elif facility_type in ['三星级宾馆', '经济型连锁酒店', '三星级宾馆|餐饮服务', '三星级宾馆|商务住宅']:
        return '中级设施'
    elif facility_type in ['宾馆酒店', '旅馆招待所', '住宿服务相关', '宾馆酒店|住宿服务', '旅馆招待所|住宿服务',
                            '青年旅舍', '宾馆酒店|生活服务', '旅馆招待所|生活服务']:
        return '基础设施'
    elif facility_type in ['宾馆酒店|餐饮服务', '旅馆招待所|商务住宅', '住宿服务相关|商务住宅', '旅馆招待所|购物服务',
                           '宾馆酒店|购物服务', '经济型连锁酒店|购物服务', '经济型连锁酒店|公司企业']:
        return '特殊设施'#比赛结束前最后两天售后群发布无水印可视化结果+无标注代码【可直接提交】为了防止倒卖， 论文写作过程中遗留数个致命问题，无关代码，该问题解决方式仅在官网授权售后群答疑，盗卖方式购买资料不提供答疑，感谢理解 资料助攻购买链接+说明https://docs.qq.com/doc/p/2e45489c100c6a59f013660a1e9c359f434bb706
    else:
        return '其他设施'

city1_data['设施级别'] = city1_data['type'].apply(categorize_facility)
city2_data['设施级别'] = city2_data['type'].apply(categorize_facility)

def calculate_overall_proportion(city_data):
    total_facilities = len(city_data)
    high_level = len(city_data[city_data['设施级别'] == '高级设施']) / total_facilities
    mid_level = len(city_data[city_data['设施级别'] == '中级设施']) / total_facilities
    basic_level = len(city_data[city_data['设施级别'] == '基础设施']) / total_facilities
    special_level = len(city_data[city_data['设施级别'] == '特殊设施']) / total_facilities
    return pd.Series({
        '高级设施比例': high_level,
        '中级设施比例': mid_level,
        '基础设施比例': basic_level,
        '特殊设施比例': special_level
    })

city1_proportions = calculate_overall_proportion(city1_data)
city2_proportions = calculate_overall_proportion(city2_data)

# 将两个城市的比例放入DataFrame中
mean_df = pd.DataFrame({'城市1': city1_proportions, '城市2': city2_proportions})
#比赛结束前最后两天售后群发布无水印可视化结果+无标注代码【可直接提交】为了防止倒卖， 论文写作过程中遗留数个致命问题，无关代码，该问题解决方式仅在官网授权售后群答疑，盗卖方式购买资料不提供答疑，感谢理解 资料助攻购买链接+说明https://docs.qq.com/doc/p/2e45489c100c6a59f013660a1e9c359f434bb706
# 绘制平均设施比例对比柱状图
ax = mean_df.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'salmon'])
plt.title('城市1和城市2的平均设施比例对比')
plt.ylabel('设施比例')
plt.xlabel('设施类型')
plt.xticks(rotation=0)

# 数据标签
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2, p.get_height()),
                ha='center', va='bottom', fontsize=10)
plt.show()

labels = city1_proportions.index
city1_values = city1_proportions.values
city2_values = city2_proportions.values

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
city1_values = np.concatenate((city1_values, [city1_values[0]]))
city2_values = np.concatenate((city2_values, [city2_values[0]]))
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, city1_values, color='blue', alpha=0.25, label='城市1')
ax.fill(angles, city2_values, color='red', alpha=0.25, label='城市2')
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.title('城市1和城市2的设施比例分布雷达图')
plt.legend()
plt.show()
