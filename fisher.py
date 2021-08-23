import matplotlib.pyplot as plt
import numpy as np
import random
import math

fig = plt.figure()  # 初始化figure对象
ax = fig.add_subplot(111)  # 添加子图
ax.set(xlim=[0, 100], ylim=[0, 100], title='Fisher criterion function')
x1 = np.zeros((2, 100))
x2 = np.zeros((2, 100))  # 新建2*100的矩阵用来保存数据
for i in range(100):  # 随机生成第1类点
    rd = random.uniform(0, 25)  # 随机向量长度
    rd2 = random.uniform(-math.pi, math.pi)  # 随机向量方向
    xlab = 25 + math.sin(rd2) * rd
    ylab = 75 + math.cos(rd2) * rd  # 随机点的坐标
    x1[0][i] = xlab
    x1[1][i] = ylab  # 保存到x1中
    ax.plot(xlab, ylab, color='red', marker='.')  # 图形化显示
for i in range(100):  # 随机生成第2类点
    rd = random.uniform(0, 25)
    rd2 = random.uniform(-math.pi, math.pi)
    xlab = 75 + math.sin(rd2) * rd
    ylab = 25 + math.cos(rd2) * rd
    x2[0][i] = xlab
    x2[1][i] = ylab
    ax.plot(xlab, ylab, color='blue', marker='.')

M1 = np.zeros(2)
M2 = np.zeros(2)
for i in range(100):
    for j in range(2):
        M1[j] = M1[j] + 0.01 * x1[j][i]  # 求第一类点的重心

for i in range(100):
    for j in range(2):
        M2[j] = M2[j] + 0.01 * x2[j][i]  # 求第二类点的重心

ax.plot(M1[0], M1[1], color='black', marker='+', markersize=12)  # 将重心输出
ax.plot(M2[0], M2[1], color='black', marker='+', markersize=12)

Sw = np.zeros((2, 2))  # 求总类内离散度矩阵Sw
for i in range(100):
    Sw = Sw + 0.01 * np.mat(x1[:, i] - M1).T * np.mat(x1[:, i] - M1)
    +0.01 * np.mat(x2[:, i] - M2).T * np.mat(x2[:, i] - M1)

w = np.dot(np.linalg.pinv(Sw), (M1 - M2))  # 求出方向向量
w = np.mat(w.T)
print(w)
midPoint = (M1 + M2) / 2  # 阈值
x = range(0, 100)
y = []
for i in range(100):
    y.append(-float(w[0][0]) / float(w[1][0]) * (i - float(midPoint[0])) + float(midPoint[1]))
# print(y)
ax.plot(x, y, color='green', marker='*')

plt.show()