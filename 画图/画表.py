import pytab as pt
import matplotlib.pylab as plt
# 防止中文乱码
plt.mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.mpl.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':
    data = {
        '区域': ['海外'],
        'W12': [20],
        'W13': [23],
        'W14': [25],
        'W15': [27],
        'W15 WOW': ['10%'],
        'YOY': [104]
    }

    # pt.table(
    #     data=data,
    #     rows=rows,
    #     th_c='#aaddff',
    #     td_c='lightgray',
    # )
    pt.table(
        data=data,
        th_face='limegreen', # 文本颜色
        th_text='olive', # 背景颜色
        fontsize= 12,
        figsize=(16,4), # 画布比例
        data_loc='center',
        th_loc='center',
        td_loc='center'
    )
    # pt.save("table.png",dpi=600)
    pt.show()