import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../data/data1.xlsx')

x_tick = []
for i in range(1,53):
    x_tick.append('W' + str(i))

# print(df.head())
# 设置
pd.options.display.notebook_repr_html=True  # 表格显示
plt.rcParams['figure.dpi'] = 300  # 图形分辨率
sns.set_theme(style='darkgrid')  # 图形主题
# 增加散点
p = sns.lineplot(data=df,markers=True)
p.set_xlabel("weekly", fontsize = 20)
p.set_ylabel("Sell-out", fontsize = 20)
p.set_xticks(range(len(x_tick)))
p.set_xticklabels(x_tick)
plt.show()