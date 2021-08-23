clear all;;clc;
data=[4,2,2,3,4,9,6,9,8,10;2,4,3,6,4,10,8,5,7,8;1,1,1,1,1,0,0,0,0,0]';
[m,n]=size(data);
%%  ====绘制原始数据点===================
for i=1:m
    if data(i,3)==1 %第1类数据
        plot(data(i,1),data(i,2),'r.','MarkerSize', 15);%Marker是图上画上点的地方表上符号,比如点,十字,星号等等,后面的size就是其大小了
        hold on;
    end
    if data(i,3)==0 %第0类数据
        plot(data(i,1),data(i,2),'b.','MarkerSize', 15);
    end
end
%%  ====绘制原始数据点===================
new_data=zeros(m,n-1);
cen1=zeros(1,2);%第一类的均值向量
cen0=zeros(1,2);%第二类的均值向量
sum1=zeros(1,2);
sum0=zeros(1,2);
num1=0;num0=0;
for i=1:m
    if data(i,3)==1%第一类
        sum1(1,1)=sum1(1,1)+data(i,1); %计算第一个特征的总和
        sum1(1,2)=sum1(1,1)+data(i,2); %计算第二个特征的总和
        num1=num1+1;
    end
    if data(i,3)==0%第二类
        sum0(1,1)=sum0(1,1)+data(i,1);%计算第一个特征的总和
        sum0(1,2)=sum0(1,2)+data(i,2); %计算第二个特征的总和
        num0=num0+1;
    end
end
cen0=sum0/num0;%求出第一类的均值向量
cen1=sum1/num1;%求出第二类的均值向量
%计算类内散度矩阵Sw
Sw=zeros(2,2);
for i=1:m
    if data(i,3)==1
        Sw=Sw+(data(i,[1 2])-cen1(1,:))'*(data(i,[1 2])-cen1(1,:));
    end
    if data(i,3)==0
        Sw=Sw+(data(i,[1 2])-cen0(1,:))'*(data(i,[1 2])-cen0(1,:));
    end
end
%计算类间散度矩阵Sb;
Sb=(cen0-cen1)'*(cen0-cen1);
[L,D]=eigs(Sw\Sb,1);%计算最大特征值和特征向量 为什么这里的L(2)*x1+L(1)*x2才对
%显示投影线
k=L(1)/L(2); %x2方向的系数/x1方向的系数
b=0;
xx=0:10;
yy=k*xx;
plot(xx,yy)
%计算投影点并显示
%% ======计算投影点========
new_data(:,1)=(k*data(:,2)+data(:,1))/(k*k+1); %k/1+k^2这里正好是tan转化为sin的公式 1/(k^2+1)正好是tan转为sin的形式
new_data(:,2)=k*new_data(:,1);
new_data(:,3)=data(:,3); %类型的点保持不变
%投影点坐标为(x0,y0) 原数据点坐标为(x,y) 那么则有(y-y0)/(x-x0)*k = -1(垂直关系) y0 =
%kx0，联立这两个方程正好可以进行求解
%% ======计算投影点========
for i=1:m
    if new_data(i,3)==1
        plot(new_data(i,1),new_data(i,2),'r+','MarkerSize', 7);
    end
    if new_data(i,3)==0
        plot(new_data(i,1),new_data(i,2),'b+','MarkerSize', 7);
    end
end
axis([0 15 0 15])
hold on;
%% =======计算变换后的值(正好是到原点点的距离)
after_projection = zeros(1,length(data));
for k = 1:length(data)
    after_projection(k) = L'*[data(k,2);data(k,1)];
end
%% =======计算变换后到原点的距离
distance = zeros(1,length(new_data));
for k = 1:length(new_data)
    distance(k) = norm([new_data(k,1),new_data(k,2)]);
end