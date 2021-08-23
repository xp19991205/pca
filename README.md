# pca/fisher
这里对python的主成分分析做一个程序的总结
这个程序的主要功能有读取excel文件，需要注意的是
df = pd.read_excel('E:\\python_programs\\pca\\1.xlsx',header =0) 这个路劲可以进行修改，Copy->Copy_path 复制绝对路径或者相对路径均可
data_df.columns = ['食品','衣着','居住','家庭设备','交通通讯','文教娱乐','医疗保健','其他']  代表列名，一般指因素1，2，3...
data_df.index = ['特征值','解释方差比','系数矩阵'] 这个无需变动
sklearn——example 对PCA和PLS进行了简单的对比，通过第二主成分加噪数据做预测数据，很好地说明了PLS能够有效地去除数据之间的共线性问题
这里还有Fisher判别法
 
