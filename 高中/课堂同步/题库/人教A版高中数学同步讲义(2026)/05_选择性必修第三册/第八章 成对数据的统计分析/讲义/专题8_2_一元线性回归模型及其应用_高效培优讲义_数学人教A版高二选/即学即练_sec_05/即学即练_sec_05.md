## 【即学即练】

1. 红铃虫（Pectinophora gossypiella）是棉花的主要害虫之一，其产卵数与温度有关。现收集到一只红铃虫

的产卵数 $y$ （个）和温度 $x$ （ $^{\circ}\mathrm{C}$ ）的8组观测数据，制成图1所示的散点图·现用两种模型① $y = \mathrm{e}^{bx + a}$ ，②

$$
y = c x ^ {2} + d
$$

分别进行拟合，由此得到相应的回归方程并进行残差分析，进一步得到图2所示的残差图。

![](../images/questions/part-001/f3b3b587626a55aeba849c0d049e57c80baa4fd7cf75ce9f4928f364d81add52.jpg)
图1 产卵数散点图

![](../images/questions/part-001/e0acb1d4fb10552decef637ed0aa69d4eae37144f61d9178ac953d023be2803c.jpg)
图2 两种模型的残差图

根据收集到的数据，计算得到如下值：

<table><tr><td> $\overline{x}$ </td><td> $\overline{z}$ </td><td> $\overline{t}$ </td><td> $\sum_{i=1}^{8}\left(x_i - \overline{x}\right)^2$ </td><td> $\sum_{i=1}^{8}\left(t_i - \overline{t}\right)^2$ </td><td> $\sum_{i=1}^{8}\left(z_i - z\right)\left(x_i - x\right)$ </td><td> $\sum_{i=1}^{8}\left(y_i - \overline{y}\right)\left(t_i - \overline{t}\right)$ </td></tr><tr><td>25</td><td>2.9</td><td>646</td><td>168</td><td>422688</td><td>50.4</td><td>70308</td></tr></table>

表中 $z_{i}=\ln y_{i}$ ; $\overline{z}=\frac{1}{8}\sum_{i=1}^{8}z_{i}$ ; $t_{i}=x_{i}^{2}$ ; $\overline{t}=\frac{1}{8}\sum_{i=1}^{8}t_{i}$

(1)根据残差图，比较模型①、②的拟合效果，哪种模型比较合适？

(2)根据（1）中所选择的模型，求出 $y$ 关于 $x$ 的回归方程.

附：对于一组数据 $\left(\omega_1,v_1\right)\left(\omega_2,v_2\right),\ldots \left(\omega_n,v_n\right)$ ，其回归直线 $\hat{v} = \hat{\alpha} +\hat{\beta}\omega$ 的斜率和截距的最小二乘估计分别为，

$$
\hat {\beta} = \frac {\sum_ {i = 1} ^ {n} (\omega_ {i} - \overline {{\omega}}) (v _ {i} - \overline {{v}})}{\sum_ {i = 1} ^ {n} (\omega_ {i} - \overline {{\omega}}) ^ {2}}, \quad \hat {\alpha} = \overline {{v}} - \hat {\beta} \overline {{\omega}}
$$

【答案】(1)①；

(2) $\hat{y} = \mathrm{e}^{0.3x - 4.6}$

【分析】（ $^{1}$ ）根据残差点的分布情况分析即可；

(2) 取对数，将非线性回归转化为线性回归，然后根据所给数据代入公式即可得回归方程.

【详解】（1）模型①更合适.

模型①残差点比较均匀地落在水平的带状区域中，且带状区域的宽度比模型②带状宽度窄，

所以模型①的拟合精度更高，回归方程的预报精度相应就会越高，故选模型①比较合适。

(2) 令 $z = \ln y, z$ 与温度 $x$ 可以用线性回归方程来拟合，则 $\hat{z} = \hat{a} + \hat{b} x$

$$
\hat {b} = \frac {\sum_ {i = 1} ^ {8} \left(x _ {i} - \bar {x}\right) \left(z _ {i} - \bar {z}\right)}{\sum_ {i = 1} ^ {8} \left(x _ {i} - \bar {x}\right) ^ {2}} = \frac {5 0 . 4}{1 6 8} = 0. 3
$$

$$
\hat {a} = \overline {{{z}}} - \hat {b} \overline {{{x}}} = 2. 9 - 0. 3 \times 2 5 = - 4. 6
$$

则 z 关于 x 的线性回归方程为 $\hat{z}=0.3x-4.6$ ，即 $\ln y=0.3x-4.6$ ，

$\therefore$ 产卵数 $y$ 关于温度 $x$ 的回归方程为 $\hat{y} = \mathrm{e}^{0.3x - 4.6}$

![[高中/课堂同步/题库/人教A版高中数学同步讲义(2026)/05_选择性必修第三册/第八章 成对数据的统计分析/讲义/专题8_2_一元线性回归模型及其应用_高效培优讲义_数学人教A版高二选/即学即练_sec_05/questions/Q00059926.md]]
