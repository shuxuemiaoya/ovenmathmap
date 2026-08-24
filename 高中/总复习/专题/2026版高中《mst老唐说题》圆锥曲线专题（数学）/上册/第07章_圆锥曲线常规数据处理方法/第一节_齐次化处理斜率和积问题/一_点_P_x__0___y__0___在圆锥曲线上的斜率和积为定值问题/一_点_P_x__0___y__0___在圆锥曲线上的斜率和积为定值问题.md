## 一、点 $P(x_{0}, y_{0})$ 在圆锥曲线上的斜率和积为定值问题

咱们以椭圆为例, 已知点 $P(x_{0}, y_{0})$ 是椭圆上一个定点, 椭圆 $C: \frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1 (a > b > 0)$ 上有两动点 $A 、 B$
(1) 若直线 $k_{PA} + k_{PB} = \lambda (\lambda \neq 0)$ , 则直线 $AB$ 过定点 $\left(x_{0} - \frac{2y_{0}}{\lambda}, -y_{0} - \frac{2x_{0}b^{2}}{\lambda a^{2}}\right)$ ; (2017 全国一卷)

(2)若直线 $k_{PA} + k_{PB} = 0$ ，则直线 $AB$ 斜率为定值 $\frac{x_0b^2}{y_0a^2}$

(3)若直线 $k_{PA} \cdot k_{PB} = \lambda \left(\lambda \neq \frac{b^2}{a^2}\right)$ , 则直线 $AB$ 过定点 $\left(\frac{\lambda a^2 + b^2}{\lambda a^2 - b^2} x_0, -\frac{\lambda a^2 + b^2}{\lambda a^2 - b^2} y_0\right)$ ; (2020 山东卷, 全国一卷)

(4)若直线 $k_{PA} \cdot k_{PB} = \frac{b^2}{a^2}$ ，则直线 $AB$ 斜率为定值 $-\frac{y_0}{x_0}$

证明：将椭圆 C 按向量 $\overrightarrow{PO}(-x_{0}, -y_{0})$ 平移得椭圆 $C' : \frac{(x+x_{0})^{2}}{a^{2}} + \frac{(y+y_{0})^{2}}{b^{2}} = 1$ ,

又点 $P(x_0, y_0)$ 在椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 上，所以 $\frac{x_0^2}{a^2} + \frac{y_0^2}{b^2} = 1$ ，代入上式得 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{2x_0}{a^2}x + \frac{2y_0}{b^2}y = 0$ ①。椭圆 $C$ 上的定点 $P(x_0, y_0)$ 和动点 $A$ ， $B$ 分别对应椭圆 $C'$ 上的定点 $O$ 和动点 $A'$ ， $B'$ ，设直线 $A'B'$ 的方程为 $mx + ny = 1$ ，代入 ① 得： $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \left(\frac{2x_0}{a^2}x + \frac{2y_0}{b^2}y\right)(mx + ny) = 0$ ，

当 $x \neq 0$ 时，两边除以 $x^2$ 得： $\frac{1 + 2y_0n}{b^2} \frac{y^2}{x^2} + \left(\frac{2x_0n}{a^2} + \frac{2y_0m}{b^2}\right) \frac{y}{x} + \frac{1 + 2x_0m}{a^2} = 0$

因为点 $A'$ ， $B'$ 的坐标满足这个方程，所以 $k_{OA'}$ ， $k_{OB'}$ 是这个关于 $\frac{y}{x}$ 的方程的两个根.

注意 之所以将 $A'B'$ 的方程设为 $mx + ny = 1$ ，就是利用了乘一法，即乘除一个为一的式子，能改变结构，但不改变结果。在三角函数当中我们经常会将 $m \sin^2\alpha + n \cos^2\alpha$ 转化为 $\frac{m \sin^2\alpha + n \cos^2\alpha}{\sin^2\alpha + \cos^2\alpha} = \frac{m \tan^2\alpha + n}{\tan^2\alpha + 1}$ ，也是利用了齐次化原理化弦为切。

证明：
(1)若 $k_{PA} + k_{PB} = \lambda (\lambda \neq 0)$ ，由平移性质知 $k_{OA'} + k_{OB'} = \lambda$ ，所以 $k_{OA'} + k_{OB'} = \frac{-2b^2 x_0 n - 2a^2 y_0 m}{a^2 (1 + 2y_0 n)} = \lambda$ ，即 $-2b^2 x_0 n - 2a^2 y_0 m = \lambda a^2 + 2a^2 \lambda y_0 n$ ，所以 $-\frac{2y_0}{\lambda} m - \left(\frac{2b^2 x_0}{\lambda a^2} - 2y_0\right)n = 1$ ，

由此知点 $\left(-\frac{2y_{0}}{\lambda},-\frac{2b^{2}x_{0}}{\lambda a^{2}}-2y_{0}\right)$ 在直线 $A^{\prime}B^{\prime}:mx+ny=1$ 上，从而直线AB过定点 $\left(x_{0}-\frac{2y_{0}}{\lambda},-\frac{2b^{2}x_{0}}{\lambda a^{2}}-y_{0}\right)$ .
(2)依题意知直线 PA, PB 的倾斜角互补且斜率存在，由平移性质知，直线 $OA^{\prime}$ ， $OB^{\prime}$ 的倾斜角也互补且斜率存在，所以 $k_{OA^{\prime}} + k_{OB^{\prime}} = 0$ ，即 $\frac{2x_{0}n}{a^{2}} + \frac{2y_{0}m}{b^{2}} = 0$ ，由此得 $k_{A^{\prime}B^{\prime}} = -\frac{m}{n} = \frac{x_{0}b^{2}}{y_{0}a^{2}}$ 。所以 AB 的斜率为定值 $\frac{x_{0}b^{2}}{y_{0}a^{2}}$
(3) 若 $k_{PA} \cdot k_{PB} = \lambda \left( \lambda \neq \frac{b^{2}}{a^{2}} \right)$ ，由平移性质知 $k_{OA^{\prime}} \cdot k_{OB^{\prime}} = \lambda$ ，所 $k_{OA^{\prime}} \cdot k_{OB^{\prime}} = \frac{b^{2}(1 + 2x_{0}m)}{a^{2}(1 + 2y_{0}n)} = \lambda$ ，
即 $b^{2}+2b^{2}x_{0}m=\lambda a^{2}+2a^{2}\lambda y_{0}n$ ，所以 $\frac{2b^{2}x_{0}}{\lambda a^{2}-b^{2}}m+\frac{-2a^{2}y_{0}\lambda}{\lambda a^{2}-b^{2}}n=1$ ，由此知点 $\left(\frac{2b^{2}x_{0}}{\lambda a^{2}-b^{2}},\frac{-2a^{2}y_{0}\lambda}{\lambda a^{2}-b^{2}}\right)$ 在直线 $A^{\prime}B^{\prime}:mx+ny=1$ 上，从而直线 AB 过定点 $\left(\frac{\lambda a^{2}+b^{2}}{\lambda a^{2}-b^{2}}x_{0},-\frac{\lambda a^{2}+b^{2}}{\lambda a^{2}-b^{2}}y_{0}\right)$ .

前三条考试非常常见，不过有一个局限，就是这个定点 $P$ 必须已知，如果未知，计算量会大到你怀疑人生.

$k_{OA'} \cdot k_{OB'} = \frac{b^2(1 + 2x_0m)}{a^2(1 + 2y_0n)} = \frac{b^2}{a^2}$ ，则 $1 + 2x_0m = 1 + 2y_0n \Rightarrow k = -\frac{m}{n} = -\frac{y_0}{x_0}$ .

![[高中/总复习/专题/2026版高中《mst老唐说题》圆锥曲线专题（数学）/上册/第07章_圆锥曲线常规数据处理方法/第一节_齐次化处理斜率和积问题/一_点_P_x__0___y__0___在圆锥曲线上的斜率和积为定值问题/例题/Q00048628.md]]
![[高中/总复习/专题/2026版高中《mst老唐说题》圆锥曲线专题（数学）/上册/第07章_圆锥曲线常规数据处理方法/第一节_齐次化处理斜率和积问题/一_点_P_x__0___y__0___在圆锥曲线上的斜率和积为定值问题/例题/Q00048629.md]]
![[高中/总复习/专题/2026版高中《mst老唐说题》圆锥曲线专题（数学）/上册/第07章_圆锥曲线常规数据处理方法/第一节_齐次化处理斜率和积问题/一_点_P_x__0___y__0___在圆锥曲线上的斜率和积为定值问题/例题/Q00048630.md]]
![[高中/总复习/专题/2026版高中《mst老唐说题》圆锥曲线专题（数学）/上册/第07章_圆锥曲线常规数据处理方法/第一节_齐次化处理斜率和积问题/一_点_P_x__0___y__0___在圆锥曲线上的斜率和积为定值问题/例题/Q00048631.md]]
