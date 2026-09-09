## 题型二：相关系数的计算

11. 研究数据表明，某校高中生的数学成绩与物理成绩、物理成绩与化学成绩均有正相关关系。现从该校抽取某班 $^{50}$ 位同学的数学、物理、化学三科成绩作为样本，设数学、物理、化学成绩分别为变量 $^{x,y,z}$ 。若 x,y 的样本相关系数为 $\frac{12}{13}$ ，y,z 的样本相关系数为 $\frac{4}{5}$ ，则 x,z 的样本相关系数的最大值为（）

附：样本相关系数 $r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}$ A. $\frac{48}{65}$ B. $\frac{63}{65}$ C. $\frac{64}{65}$ D. 1

【答案】B

【分析】设 $X=\left(x_{1},x_{2},\cdots,x_{n}\right)$ ， $Y=\left(y_{1},y_{2},\cdots,y_{n}\right)$ ， $Z=\left(z_{1},z_{2},\cdots,z_{n}\right)$ ， $X'=\left(x_{1}-\bar{x},x_{2}-\bar{x},\cdots,x_{n}-\bar{x}\right)$

$Y' = (y_1 - \overline{y}, y_2 - \overline{y}, \cdots, y_n - \overline{y})$ ， $Z' = (z_1 - \overline{z}, z_2 - \overline{z}, \cdots, z_n - \overline{z})$ ， $X'$ 与 $Y'$ 的夹角为 $\alpha$ ， $Y'$ 与 $Z'$ 的夹角为 $\beta$ ，再由相关系数可知 $r = \cos\left\langle X', Y'\right\rangle$ ，则 $X'$ 与 $Z'$ 夹角的余弦值的最大值为 $\cos(\beta - \alpha)$ ，利用余弦差角公式求值即可·

$$
X = \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) \quad Y = \left(y _ {1}, y _ {2}, \dots , y _ {n}\right) \quad Z = \left(z _ {1}, z _ {2}, \dots , z _ {n}\right)
$$

$$
X ^ {\prime} = \left(x _ {1} - \bar {x}, x _ {2} - \bar {x}, \dots , x _ {n} - \bar {x}\right) \quad Y ^ {\prime} = \left(y _ {1} - \bar {y}, y _ {2} - \bar {y}, \dots , y _ {n} - \bar {y}\right) \quad Z ^ {\prime} = \left(z _ {1} - \bar {z}, z _ {2} - \bar {z}, \dots , z _ {n} - \bar {z}\right)
$$

由样本相关系数公式 $r=\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right)}{\sqrt{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}}}$ 可知， $r=\cos\left\langle X',Y'\right\rangle$

设 $X^{\prime}$ 与 $Y^{\prime}$ 的夹角为 $\alpha$ ， $Y^{\prime}$ 与 $Z^{\prime}$ 的夹角为 $\beta$ ，则有 $\cos \alpha = \frac{12}{13}, \cos \beta = \frac{4}{5}$

易知 $\alpha, \beta$ 均为锐角且 $\beta > \alpha$

$X^{\prime}$ 与 $Z^{\prime}$ 夹角的余弦值的最大值为 $\cos (\beta -\alpha)$ ，此时 $x$ 与 $z$ 样本相关系数最大，

$$
\cos (\beta - \alpha) = \cos \beta \cos \alpha + \sin \beta \sin \alpha = \frac {4}{5} \times \frac {1 2}{1 3} + \frac {3}{5} \times \frac {5}{1 3} = \frac {6 3}{6 5}
$$

故 $x, z$ 的样本相关系数的最大值为 $\frac{63}{65}$ .

故选：B.

12．2019年11月份，全国工业生产者出厂价格同比下降 $1.4\%$ ，环比下降 $0.1\%$ ．某企业在了解市场动态之后，决定根据市场动态及时做出相应调整，并结合企业自身的情况制定相应的出厂价格．该企业统计了2019年1-10月份产品的生产数量 $x$ 与销售总额 $y$ 之间的关系，如下表所示．

<table><tr><td>x/万件</td><td>2.08</td><td>2.12</td><td>2.19</td><td>2.28</td><td>2.36</td><td>2.48</td><td>2.59</td><td>2.68</td><td>2.80</td><td>2.87</td></tr><tr><td>y/万元</td><td>42.5</td><td>43.7</td><td>44.0</td><td>45.5</td><td>46.4</td><td>47.5</td><td>49.2</td><td>50.3</td><td>51.4</td><td>52.6</td></tr></table>

(1) 计算 $\overline{x}, \overline{y}$ 的值；

(2)计算样本相关系数 $r$ 的值，并通过 $r$ 的值的大小说明 $y$ 与 $x$ 之间的相关程度。

【答案】(1) $\overline{x}=2.445,\overline{y}=47.31$

(2) $r \approx 0.9977$ ，y 与 x 之间具有很强的相关性

【分析】（1）由平均数的计算公式得到 $\bar{x}$ 和 $\bar{y}$ ；

(2) 由相关系数的计算公式计算 r，再由 0.9977 > 0.75 判断相关性.

【详解】（1）依题意， $\overline{x}=\frac{\sum_{i=1}^{10}x_{i}}{10}=2.445,\overline{y}=\frac{\sum_{i=1}^{10}y_{i}}{10}=47.31$

(2) 依题意， $\sum_{i=1}^{10}(x_i - \overline{x})(y_i - \overline{y}) = 8.8325$ ， $\sum_{i=1}^{10}(x_i - \overline{x})^2 = 0.72245$ ， $\sum_{i=1}^{10}(y_i - \overline{y})^2 = 108.489$

所以 $r=\frac{\sum_{i=1}^{10}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right)}{\sqrt{\sum_{i=1}^{10}\left(x_{i}-\bar{x}\right)^{2}}\sqrt{\sum_{i=1}^{10}\left(y_{i}-\bar{y}\right)^{2}}}=\frac{8.8325}{\sqrt{0.72245\times108.489}}\approx0.9977$

因为 $0.9977 > 0.8$ ，所以 $y$ 与 $x$ 之间具有很强的相关性。

![[高中/课堂同步/题库/人教A版高中数学同步讲义(2026)/05_选择性必修第三册/第八章 成对数据的统计分析/专项训练/专题01_成对数据的统计相关性的五大常考题型_高效培优专项训练_数学人/题型二_sec_03/questions/Q00059833.md]]
![[高中/课堂同步/题库/人教A版高中数学同步讲义(2026)/05_选择性必修第三册/第八章 成对数据的统计分析/专项训练/专题01_成对数据的统计相关性的五大常考题型_高效培优专项训练_数学人/题型二_sec_03/questions/Q00059834.md]]
![[高中/课堂同步/题库/人教A版高中数学同步讲义(2026)/05_选择性必修第三册/第八章 成对数据的统计分析/专项训练/专题01_成对数据的统计相关性的五大常考题型_高效培优专项训练_数学人/题型二_sec_03/questions/Q00059835.md]]
![[高中/课堂同步/题库/人教A版高中数学同步讲义(2026)/05_选择性必修第三册/第八章 成对数据的统计分析/专项训练/专题01_成对数据的统计相关性的五大常考题型_高效培优专项训练_数学人/题型二_sec_03/questions/Q00059836.md]]
![[高中/课堂同步/题库/人教A版高中数学同步讲义(2026)/05_选择性必修第三册/第八章 成对数据的统计分析/专项训练/专题01_成对数据的统计相关性的五大常考题型_高效培优专项训练_数学人/题型二_sec_03/questions/Q00059837.md]]
![[高中/课堂同步/题库/人教A版高中数学同步讲义(2026)/05_选择性必修第三册/第八章 成对数据的统计分析/专项训练/专题01_成对数据的统计相关性的五大常考题型_高效培优专项训练_数学人/题型二_sec_03/questions/Q00059838.md]]
![[高中/课堂同步/题库/人教A版高中数学同步讲义(2026)/05_选择性必修第三册/第八章 成对数据的统计分析/专项训练/专题01_成对数据的统计相关性的五大常考题型_高效培优专项训练_数学人/题型二_sec_03/questions/Q00059839.md]]
