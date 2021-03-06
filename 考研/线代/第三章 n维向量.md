# 运算

向量内积

# 线性表示

$存在k_1,k_2,k_3....使得\alpha_i的线性组合可以表示\beta$

>表示法可以不唯一

## 等价

可以互相表出

## 转化为方程

​	方程有解就是可以表出

## 是否可以表出

### 矩阵法

​	两向量组的情况时

​	两个向量组合成一个矩阵，做行最简变换

​	考察B能否由A表出时，分别讨论（A,$b_1$）(A,$b_2$)......

### 秩

​	满秩可以表示当前维度向量空间里所有向量

​	A可以由B表出 r(A)$\le$r(B)

​	A可以由B表出，B不可以由A表出 r(A)<r(B)

>用秩的大小关系只能证明不能表出啊

### 定义

​	$k_1\alpha_1+k_2\alpha_2+k_3\alpha_3=0$

>问 $\alpha_1能否由\alpha_2,\alpha_3线性表出$
>
>证明 $k_1\neq0$

### 有相同的极大无关组

# 线性相关/无关

存在不全为0的数使得......

>向量组里有一个线性表出就是线性相关了

## 条件判断

​	向量组里有零向量，肯定是线性相关。

​	行列式为0

​	向量组线性无关，其延伸组线性无关

	>前面的方程无非零解，后面的方程就不用看了

​	向量组线性相关，其缩短组线性相关

>整个方程有非零解，方程的一部分也都成立

​	多数向量能由少数向量线性表出，多数向量一定线性相关

​	线性无关进行可逆变换，还是线性无关

>若A可逆 r(AB)=r(B)

## 转化为方程

​	齐次方程有非零解就是线性相关，无非零解就是线性无关。

## 单参数矩阵判断线性相关

### 行变换判断

​	r(A)<r(A,b) 无解（零解都没）

​	r(A)=r(A,b) 有解

​		=n 只有零解

​		<n 有非零解

>方程组个数<未知数个数
>行最简时 A的非零行数<A的总列数

### 行列式求可能值，再带入矩阵

## 线性无关的证明

### 定义法

1. 列出定义

2. 根据条件，定义同乘，或者重组（方程式加减）。

   > 题目给出线性无关条件，就重组需要证明的定义，得到一个齐次方程
   >
   > 同乘时，只留下一个k，证明这个k=0，这就简化了方程，把简化的方程继续同乘。

3. 得出只有零解

### 用秩

公式：

​	若A可逆 r(AB)=r(B)
​	r(AB)$\le$min{r(A),r(B)}
​	AB=O,则r(A)+r(B)$\le$n（$A_{m\times n},B_{n\times s}$）

### 反证法

假设线性相关，有非零解。设不为0的k是...然后跟题设矛盾

# 极大无关组

## 求极大无关组

化为行最简，取出线性无关的（可能不唯一）

# 向量组的秩

## 矩阵的秩

# 向量空间

## 施密特正交化

把线性无关的向量组正交化

## 求过度矩阵

### 定义

$A\times 过度矩阵=B$

> 过度矩阵=$A^{-1}B$

所以过度矩阵是列变换

### 解方程组

$x_1\alpha_1+x_2\alpha_2+x_3\alpha_3=u$

## 坐标变换公式

以A的列向量组为基底坐标（x）

向 以B的列向量为基底坐标(y) 变化

设过度矩阵为C, AC=B

则 x=Cy

>存疑

## 向量组正交和线性关系

向量组两两正交，则线性无关

## 两个向量组

### 求在他们向量空间坐标一样的向量

设坐标为$(x_1,x_2,x_3\cdots x_n)$

$x_1(\alpha_1-\beta_1)+x_2(\alpha_2-\beta_2)\cdots=0$

解方程

### 求可以被两个向量组线性表出的向量

先证明两个向量组线性相关

$k_1\alpha_1+k_2\alpha_2+k_3\beta_1+k_4\beta_2=0$

$k_1\alpha_1+k_2\alpha_2=-k_3\beta_1-k_4\beta_2=能被两个向量组线性表出的向量$

解出方程

$k_1\alpha_1+k_2\alpha_2$就是能被两个向量组线性表出的向量

# 问题

## 矩阵等价与向量组等价的区别

矩阵等价的充分必要条件是秩相等

​	矩阵等价向量组未必等价

>一个列在上面的矩阵 和一个列在下面的矩阵
>
>所以向量组秩相同，不一定能相互表出

向量组等价需要能互相表出

AB=C，B是可逆矩阵 则A的列向量与C的列向量等价

## 矩阵化为行最简

注意行除以一个数，要判断这个数是否等于0