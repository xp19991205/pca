from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import numpy as np
import pandas as pd
df = pd.read_excel('E:\\python_programs\\pca\\1.xlsx',header =0)
data=df.values
data_matrix = np.mat(data)
# print("获取到所有的值:\n{}".format(data))
print(data_matrix)
data = scale(data_matrix) # 标准化，标准化之后就自动根据协方差矩阵进行主成分分析了
print(data)

pca = PCA() # 可以调整主成分个数，n_components = 1
pca.fit(data)
# print("特征根为")
landa = pca.explained_variance_;
# print(type(landa))
explined = pca.explained_variance_ratio_
# print(pca.explained_variance_) # 输出特征根
# print("解释方差比")
# print(pca.explained_variance_ratio_) # 输出解释方差比
# print("主成分")
coeff = pca.components_
# print(pca.components_) # 输出主成分
# print(len(pca.components_))
data_all = [landa,explined,coeff]
print(data_all)
# data_df1 = pd.DataFrame(landa)   #关键1，将ndarray格式转换为DataFrame
data_df = pd.DataFrame(data_all)
data_df.columns = ['食品','衣着','居住','家庭设备','交通通讯','文教娱乐','医疗保健','其他']  #这里改成对应的指标名
data_df.index = ['特征值','解释方差比','系数矩阵']
print(data_df)
writer = pd.ExcelWriter('result.xlsx')  #关键2，创建名称为hhh的excel表格
data_df.to_excel(writer,'page_1',float_format='%.5f')  #关键3，float_format 控制精度，将data_df写到hhh表格的第一页中。若多个文件，可以在page_2中写入
writer.save()  #关键4