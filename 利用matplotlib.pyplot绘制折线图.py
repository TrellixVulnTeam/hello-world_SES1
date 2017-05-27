#--------encoding:utf-8-------------------------------------------------------
# Name: 利用matplotlib.pyplot绘制散点图
# Purpose:
#
# Author:      lenove
#
# Created:     05-12-2015
# Copyright:   (c) lenove 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from random import choice

# myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc')
myfont = fm.FontProperties(fname='/usr/share/fonts/local/simsun.ttc')
#http://matplotlib.org/api/pyplot_api.html?highlight=plot#matplotlib.pyplot.plot

#控制标记
linestyles = {'x': 'x marker', ':': 'dotted line style',
           '<': 'triangle_left marker', '>': 'triangle_right marker',
           '1': 'tri_down marker', 'p': 'pentagon marker',
           '3': 'tri_left marker', '2': 'tri_up marker',
           '4': 'tri_right marker', 'v': 'triangle_down marker',
           'h': 'hexagon1 marker', '+': 'plus marker',
           '*': 'star marker', '-': '实线',
           ',': 'pixel marker', 'o': 'circle marker',
           '.': '点标记', 'd': 'thin_diamond marker',
           '|': 'vline marker', '_': 'hline marker',
           '^': 'triangle_up marker', '-.': '点划线',
           'D': 'diamond marker', 'H': 'hexagon2 marker',
           '--': '虚线', 's': 'square marker'
           }

#http://matplotlib.org/api/markers_api.html#module-matplotlib.markers
markers = {0: 'tickleft', '|': 'vline', 2: 'tickup', 3: 'tickdown',
           4: 'caretleft', 5: 'caretright', ',': 'pixel',
           1: 'tickright', '+': 'plus', 'D': 'diamond',
           'v': 'triangle_down', '1': 'tri_down', None: 'nothing',
           'h': 'hexagon1', '*': 'star', 'None': 'nothing',
           '<': 'triangle_left', '': 'nothing', '2': 'tri_up',
           's': 'square', ' ': 'nothing', 6: 'caretup',
           'H': 'hexagon2', '3': 'tri_left', 'x': 'x',
           7: 'caretdown', '4': 'tri_right','p': 'pentagon',
           '>': 'triangle_right', '8': 'octagon', 'o': 'circle',
           '.': 'point', 'd': 'thin_diamond', '^': 'triangle_up', '_': 'hline',
           '$123$':'使用数学文本渲染字符串',
           #'verts':'点的坐标值(x,y)',
           #'path':'路径实例',
           #'(numsides, style, angle)':'自定义类型（边数，风格，角度）',
           }

#颜色
colors = {'r': (1.0, 0.0, 0.0), 'g': (0.0, 0.5, 0.0), 'c': (0.0, 0.75, 0.75),
          'k': (0.0, 0.0, 0.0), 'w': (1.0, 1.0, 1.0), 'b': (0.0, 0.0, 1.0),
          'm': (0.75, 0, 0.75), 'y': (0.75, 0.75, 0),
          'green':'绿色','#008000':'十六进制字符串，绿色',
          (0,1,0,1):'RGBA 绿色','0.8':'灰度表示',(1,0,0):'RGB颜色'
          }
#线型可以跟颜色在一起组合表示，如‘bo’。

cache = {'#F0E442': (0.9411764705882353, 0.8941176470588236, 0.25882352941176473),
         '#8A2BE2': (0.5411764705882353, 0.16862745098039217, 0.8862745098039215),
         '#bcbcbc': (0.7372549019607844, 0.7372549019607844, 0.7372549019607844),
         'c': (0.0, 0.75, 0.75),
         'green': (0.0, 0.5019607843137255, 0.0),
         '#8b8b8b': (0.5450980392156862, 0.5450980392156862, 0.5450980392156862),
         '#b3de69': (0.7019607843137254, 0.8705882352941177, 0.4117647058823529),
         '#0072B2': (0.0, 0.4470588235294118, 0.6980392156862745),
         'b': (0.0, 0.0, 1.0),
         '#eeeeee': (0.9333333333333333, 0.9333333333333333, 0.9333333333333333),
         'gray': (0.5019607843137255, 0.5019607843137255, 0.5019607843137255),
         '#6ACC65': (0.41568627450980394, 0.8, 0.396078431372549),
         '#ffed6f': (1.0, 0.9294117647058824, 0.43529411764705883),
         '#FF9F9A': (1.0, 0.6235294117647059, 0.6039215686274509),
         '#6d904f': (0.42745098039215684, 0.5647058823529412, 0.30980392156862746),
         '#FFFEA3': (1.0, 0.996078431372549, 0.6392156862745098),
         '0.70': (0.7, 0.7, 0.7), 'y': (0.75, 0.75, 0),
         'yellow': (1.0, 1.0, 0.0), 'cyan': (0.0, 1.0, 1.0),
         '#FFB5B8': (1.0, 0.7098039215686275, 0.7215686274509804),
         'blue': (0.0, 0.0, 1.0), '0.00': (0.0, 0.0, 0.0),
         '#bc82bd': (0.7372549019607844, 0.5098039215686274, 0.7411764705882353),
         '#ccebc4': (0.8, 0.9215686274509803, 0.7686274509803922),
         '#77BEDB': (0.4666666666666667, 0.7450980392156863, 0.8588235294117647),
         '#009E73': (0.0, 0.6196078431372549, 0.45098039215686275),
         '#97F0AA': (0.592156862745098, 0.9411764705882353, 0.6666666666666666),
         '#D65F5F': (0.8392156862745098, 0.37254901960784315, 0.37254901960784315),
         '.8': (0.8, 0.8, 0.8), '#003FFF': (0.0, 0.24705882352941178, 1.0),
         '#92C6FF': (0.5725490196078431, 0.7764705882352941, 1.0),
         '#fdb462': (0.9921568627450981, 0.7058823529411765, 0.3843137254901961),
         '#FBC15E': (0.984313725490196, 0.7568627450980392, 0.3686274509803922),
         '#8172B2': (0.5058823529411764, 0.4470588235294118, 0.6980392156862745),
         '#B47CC7': (0.7058823529411765, 0.48627450980392156, 0.7803921568627451),
         '#E5E5E5': (0.8980392156862745, 0.8980392156862745, 0.8980392156862745),
         '#CC79A7': (0.8, 0.4745098039215686, 0.6549019607843137),
         '#E24A33': (0.8862745098039215, 0.2901960784313726, 0.2),
         '#006374': (0.0, 0.38823529411764707, 0.4549019607843137),
         '#EEEEEE': (0.9333333333333333, 0.9333333333333333, 0.9333333333333333),
         '#8EBA42': (0.5568627450980392, 0.7294117647058823, 0.25882352941176473),
         'purple': (0.5019607843137255, 0.0, 0.5019607843137255),
         '0.40': (0.4, 0.4, 0.4), 'w': (1.0, 1.0, 1.0),
         'red': (1.0, 0.0, 0.0),
         '#fa8174': (0.9803921568627451, 0.5058823529411764, 0.4549019607843137),
         'magenta': (1.0, 0.0, 1.0), '0.50': (0.5, 0.5, 0.5),
         '#55A868': (0.3333333333333333, 0.6588235294117647, 0.40784313725490196),
         '#B0E0E6': (0.6901960784313725, 0.8784313725490196, 0.9019607843137255),
         '#C44E52': (0.7686274509803922, 0.3058823529411765, 0.3215686274509804),
         '#64B5CD': (0.39215686274509803, 0.7098039215686275, 0.803921568627451),
         '#4C72B0': (0.2980392156862745, 0.4470588235294118, 0.6901960784313725),
         '#D0BBFF': (0.8156862745098039, 0.7333333333333333, 1.0),
         '#f0f0f0': (0.9411764705882353, 0.9411764705882353, 0.9411764705882353),
         '#cbcbcb': (0.796078431372549, 0.796078431372549, 0.796078431372549),
         '#C4AD66': (0.7686274509803922, 0.6784313725490196, 0.4),
         '#03ED3A': (0.011764705882352941, 0.9294117647058824, 0.22745098039215686),
         '#467821': (0.27450980392156865, 0.47058823529411764, 0.12941176470588237),
         '#00FFCC': (0.0, 1.0, 0.8), 'black': (0.0, 0.0, 0.0),
         '#FFC400': (1.0, 0.7686274509803922, 0.0),
         '#30a2da': (0.18823529411764706, 0.6352941176470588, 0.8549019607843137),
         'm': (0.75, 0, 0.75), 'white': (1.0, 1.0, 1.0), 'k': (0.0, 0.0, 0.0),
         '0.75': (0.75, 0.75, 0.75),
         '#988ED5': (0.596078431372549, 0.5568627450980392, 0.8352941176470589),
         '0.5': (0.5, 0.5, 0.5),
         '#e5ae38': (0.8980392156862745, 0.6823529411764706, 0.2196078431372549),
         'darkgoldenrod': (0.7215686274509804, 0.5254901960784314, 0.043137254901960784),
         '#CCB974': (0.8, 0.7254901960784313, 0.4549019607843137),
         '#348ABD': (0.20392156862745098, 0.5411764705882353, 0.7411764705882353),
         '0.8': (0.8, 0.8, 0.8),
         '#feffb3': (0.996078431372549, 1.0, 0.7019607843137254),
         '#bfbbd9': (0.7490196078431373, 0.7333333333333333, 0.8509803921568627),
         '#555555': (0.3333333333333333, 0.3333333333333333, 0.3333333333333333),
         '#8dd3c7': (0.5529411764705883, 0.8274509803921568, 0.7803921568627451),
         '#777777': (0.4666666666666667, 0.4666666666666667, 0.4666666666666667),
         '0.6': (0.6, 0.6, 0.6), '#D55E00': (0.8352941176470589, 0.3686274509803922, 0.0),
         '#fc4f30': (0.9882352941176471, 0.30980392156862746, 0.18823529411764706),
         '#7600A1': (0.4627450980392157, 0.0, 0.6313725490196078),
         '#00D7FF': (0.0, 0.8431372549019608, 1.0),
         '#4878CF': (0.2823529411764706, 0.47058823529411764, 0.8117647058823529),
         '#017517': (0.00392156862745098, 0.4588235294117647, 0.09019607843137255),
         'g': (0.0, 0.5, 0.0), '0.60': (0.6, 0.6, 0.6),
         '#001C7F': (0.0, 0.10980392156862745, 0.4980392156862745),
         'firebrick': (0.6980392156862745, 0.13333333333333333, 0.13333333333333333),
         '#B8860B': (0.7215686274509804, 0.5254901960784314, 0.043137254901960784),
         '#EAEAF2': (0.9176470588235294, 0.9176470588235294, 0.9490196078431372),
         'r': (1.0, 0.0, 0.0), '#E8000B': (0.9098039215686274, 0.0, 0.043137254901960784),
         '#afeeee': (0.6862745098039216, 0.9333333333333333, 0.9333333333333333),
         '#81b1d2': (0.5058823529411764, 0.6941176470588235, 0.8235294117647058),
         '#7A68A6': (0.47843137254901963, 0.40784313725490196, 0.6509803921568628),
         '#8C0900': (0.5490196078431373, 0.03529411764705882, 0.0),
         '.15': (0.15, 0.15, 0.15),
         '#A60628': (0.6509803921568628, 0.023529411764705882, 0.1568627450980392),
         '#56B4E9': (0.33725490196078434, 0.7058823529411765, 0.9137254901960784)
         }

x=np.array([5,0,-9,4,10])

y=pow(x,3) # y=x^3

plt.figure(figsize=(12,6))#设置图的宽度，高度英寸

plt.subplot(331) #3行3列第一个子图,331可以写在一起，也可以分开写：3,3,1，但每个数字最大为9
plt.plot(x, y)        # 折线图，横坐标为x
plt.title('plt.plot(x, y) ',fontproperties=myfont)
#plt.xlabel('x轴',fontproperties=myfont)
#plt.ylabel('y轴',fontproperties=myfont)
#plt.legend(['y={:.2f}*x+{:.2f}'.format(a,b)],prop=myfont)

plt.subplot(332) #第2个子图
plt.plot(x, y, 'bo')  # （x,y）散点图
plt.title('plt.plot(x, y,"bo") ',fontproperties=myfont)

plt.subplot(333) #3第3个子图
plt.plot(y)           # 折线图，横坐标为： 0..N-1
plt.title('plt.plot(y) ',fontproperties=myfont)

plt.subplot(334, axisbg='y') #第4个子图
plt.plot(y, 'r+')     # 散点图
plt.title('plt.plot(y,"r+") ',fontproperties=myfont)

plt.subplot(335) #第5个子图
x1=np.array([3,2,1,4,6])
y1=x1**3
plt.plot(x, y, 'g^', x1, y1, 'g-')#两个子图在一张图上
plt.title("plt.plot(x, y, 'g^', x1, y1, 'g-')",fontproperties=myfont)

plt.subplot(336) #第6个子图
plt.plot([1,2,3,4], [1,5,3,2], 'go-', label='line 1', linewidth=2)#散点及连线同时标出
plt.title("plt.plot([1,2,3], [1,2,3], 'go-', label='线 1', linewidth=2)",fontproperties=myfont)


def abc():
	plt.plot([1,2,3], [1,2,3], 'go-', label='线 1', linewidth=2)
	plt.plot([1,2,3], [1,4,9], 'rs',  label='线 2')
	plt.axis([0, 4, 0, 10])
	#plt.legend(prop=myfont)#图例
	plt.legend(framealpha=0,loc=2,prop=myfont)#framealpha,控制边框的透明度，loc，控制边框的位置
	#plt.show()

plt.subplot(337) #第7个子图
abc()

plt.subplot(3,3,8)#第8个子图
plt.plot(x, y, color='green', linestyle='dashed', marker='o',markerfacecolor='blue', markersize=12)#线型：虚线

plt.subplot(3,3,9,polar=1)#polar:是否投影
plt.plot([1,2,3,4,5],marker='o')

plt.show()


for n in range(9):
    m=choice(list(markers.keys()))#随机选择标记
    c=choice(list(colors.keys()))#随机选择颜色
    l=choice(list(linestyles.keys()))#随机选择线型
    plt.subplot(3,3,n+1)
    print('颜色：{}，标记：{},线型：{}'.format(c,m,l))
    plt.plot(x, y, color=c, linestyle=l,marker=m, markersize=12)
    plt.title('颜色：{}，标记：{},线型：{}'.format(c,m,l),fontproperties=myfont)

plt.show()

def main():
    pass

if __name__ == '__main__':
    main()
