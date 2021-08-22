#燕尾花数据集的区分
import matplotlib.pyplot as plt #做绘图使用
from sklearn.decomposition import PCA #用于主成分分析中
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris() #加载燕尾花数据
y = iris.target
x = iris.data
print(pd.DataFrame(x))
pca = PCA(n_components = 2)# 可以调整主成分个数，n_components = 1
pca = pca.fit(x) #单独对自变量进行降维，而这里的y代表着燕尾花的分类
X_dr = pca.transform(x) #变换到主成分区域中
# plt.figure()
# plt.scatter(X_dr)
# print(y == 0) #这里可以看第一种花型在数据中的分布
plt.figure()
color = ["red","black","orange"]
for k in range(3):
    plt.scatter(X_dr[y==k,0],X_dr[y==k,1],color = color[k],label = iris.target_names[k],alpha = 0.7)
plt.legend()
plt.show()

##下面在这里考察新特征的其他信息
landa = pca.explained_variance_ #根据PCA算法计算特征值（由大到小排序）
explined = pca.explained_variance_ratio_ #计算PCA得到主成分的贡献率（由大到小排序）
coeff = pca.components_ #输出各主成分的系数表
var = pca.explained_variance_#各个成分的方差
print(var)
import numpy as np
pca = PCA().fit(x)
plt.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.figure()
plt.plot([1,2,3,4],np.cumsum(pca.explained_variance_ratio_),color= 'blue')
plt.xticks([1,2,3,4])
plt.xlabel("主成分个数")
plt.ylabel("解释比的变化")
plt.show()

#自适应选择主成分个数
pca_mle = PCA(n_components = "mle")
pca_mle.fit(x)
X_mle = pca_mle.transform(x)
print(X_mle)
#最大似然法帮我们选择了两个主成分