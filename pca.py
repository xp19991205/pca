# 读取excel文件进行PCA分析
#这里得到的结果和matlab是一样的
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import numpy as np
import pandas as pd
df = pd.read_excel('D:\\Python_program\\PCA\\1.xlsx',header =0)
data=df.values #获取excel数据
data_matrix = np.mat(data) #转化为numpy格式的数组
data = scale(data_matrix) # 标准化，标准化之后就自动根据协方差矩阵进行主成分分析了（matlab中zscore）
pca = PCA()# 可以调整主成分个数，n_components = 1
pca.fit(data)
# pca.fit(data_matrix)
landa = pca.explained_variance_ #根据PCA算法计算特征值（由大到小排序）
explined = pca.explained_variance_ratio_ #计算PCA得到主成分的贡献率（由大到小排序）
coeff = pca.components_ #输出各主成分的系数表
print(type(coeff))
data_all = [landa,explined] #汇总数据，准备写入excel
data_df = pd.DataFrame(data_all)   #关键1，将ndarray格式转换为DataFrame
data_df.columns = ['主成分1','主成分2','主成分3','主成分4','主成分5','主成分6','主成分7','主成分8']  #这里改成对应的指标名
data_df.index = ['特征值','解释方差比']
coeff_data = list(coeff) #准备在页面二写入系数矩阵信息
data_df2 = pd.DataFrame(coeff_data)
writer = pd.ExcelWriter('result.xlsx')  #关键2，创建名称为hhh的excel表格
data_df.to_excel(writer,'主成分及对应的解释比',float_format='%.5f')  #关键3，float_format 控制精度，将data_df写到表格的第一页中。若多个文件，可以在page_2中写入
data_df2.to_excel(writer,'系数矩阵',float_format='%.5f')
writer.save()  #关键4