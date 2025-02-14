import glob
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

import matplotlib.ticker as mticker

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体   
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

def show_fig(ax, name, fun_type, kwargs, x_min, x_max, fontsize=1):
    x = np.arange(x_min, x_max, (x_max-x_min)/100)
    a = kwargs.get('a', 0)
    b = kwargs.get('b', 0)
    k = kwargs.get('k', 0)
    if fun_type == '设置分类权重':
        x = []
        height = []
        labels = []
        for index, (k, v ) in enumerate(kwargs.items(), 1):
            x.append(index)
            height.append(v)
            labels.append(k)
        # print(x, height, labels)
        ax.bar(x, height, align='center', alpha=0.7, width=0.2)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
    elif fun_type == '指数函数':
        y = [(a**(i/b)-1)/(a-1) for i in x]
        plt.plot(x, y, label="y=({}^(x/{})-1)/{}".format(a, b, a-1))
    elif fun_type == 'sigmoid函数':
        y = [1 / (1 + math.exp(-k * (t - a))) for t in x]
        plt.plot(x, y, label="1/(1+exp(-{}*(x-{})))".format(k, a))
    elif fun_type == '对数函数':
        y = [math.log(t -b + 1, a) for t in x]
        plt.plot(x, y, label="y=log {}(x+1)".format(a))
    else:
        raise ValueError("不支持的函数类型：{}".format(fun_type))

    # ax.set_xlabel(name, fontsize=fontsize, color='red')
    ax.set_ylabel("相对价值系数", fontsize=fontsize)
    ax.set_title(name, fontsize=fontsize, color='#fc7100', y=0.8)
    # plt.ylim(0, 1)
    ax.legend()
    return ax

def generator_map_function():
    setup_datas = [['字段数', '对数函数', {'a': 128, 'b': 0}, 1, 130],
                 ['记录数', '对数函数', {'a': 1e9, 'b': 0}, 0, 1e9],
                 ['饱和度', 'sigmoid函数', {'a': 0.5,'k': 10}, 0, 1],
                 ['正确性', 'sigmoid函数', {'a': 0.5,'k': 10}, 0, 1],
                 ['一致度', 'sigmoid函数', {'a': 0.5,'k': 10}, 0, 1],
                 ['距今天数', 'sigmoid函数', {'a': 182,'k': -0.027}, 0, 365],
                 ['更新频率', '设置分类权重', {'实时': 1.0, '日频': 0.95, '周频': 0.8, '月频': 0.7, '季频': 0.6, '年频': 0.4, '不更新': 0.3}, 0, 1],
                 ['关联表数', '指数函数', {'b': 8, 'a': 15}, 1, 9],
                 ['查看频率', '对数函数', {'a': 200, 'b': 0}, 1, 210],
                 ['交易频率', '对数函数', {'a': 100, 'b': 0}, 1, 110],
                 ['调用频率', '对数函数', {'a': 1000, 'b': 0}, 1, 1010],
                 ['查看量', '对数函数', {'a': 800, 'b': 0}, 1, 810],
                 ['交易量', '对数函数', {'a': 400, 'b': 0}, 1, 410],
                 ['调用量', '对数函数', {'a': 4000, 'b': 0}, 1, 4010],
                 ['稀缺度', 'sigmoid函数', {'a': 0.5, 'k': 10}, 0, 1],
                 ['安全分级', '设置分类权重', {'1级': 0.2, '2级': 0.4, '3级': 0.6, '4级': 0.8, '5级': 1.0}, 0, 1],
                 ['业务类别', '设置分类权重', {'分析工具': 0.6, '商家位置': 0.95, '专业排名': 0.75, '城市商圈': 0.85, '城市小区': 0.9, '城市房价': 0.85, '高校排名': 0.7}, 0, 1],
                 ['收入金额', '对数函数', {'a': 100, 'b': 0}, 0, 110]]


    fig = plt.figure()

    for index, (name, fun_type, kwargs, x_min, x_max) in enumerate(setup_datas, 1):
        print(name)
        ax = fig.add_subplot(6, 3, index)

        show_fig(ax, name, fun_type, kwargs, x_min, x_max, fontsize=9)
    # plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=2)
    # plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
    fig.suptitle("指标值的映射曲线", fontsize=12, x=0.5, y=0.92)
    fig.show()
    
def main():
    generator_map_function()



if __name__ == '__main__':
    main()

