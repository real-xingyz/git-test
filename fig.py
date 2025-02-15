import matplotlib.pyplot as plt
import numpy as np

# 数据
elements = ['Li', 'K', 'Na', 'Mg', 'Al', 'Zn']
mass_capacity = [3500, 200, 1000, 3500, 8000, 500]
volume_capacity = [2000, 100, 500, 2000, 4000, 300]

# 设置柱状图的位置
x = np.arange(len(elements))
width = 0.35

fig, ax = plt.subplots()

# 绘制柱状图
rects1 = ax.bar(x - width/2, mass_capacity, width, label='Mass specific capacity (Ah kg⁻¹)')
rects2 = ax.bar(x + width/2, volume_capacity, width, label='Volume specific capacity (Ah L⁻¹)')

# 添加标签、标题和刻度
ax.set_ylabel('Specific capacity')
ax.set_title('Specific Capacity Comparison')
ax.set_xticks(x)
ax.set_xticklabels(elements)
ax.legend()

# 显示数值在柱子上
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# 显示图形
plt.show()