## 三、斜率乘积 $-\frac{b^{2}}{a^{2}}$ 能仿射成直角的面积定值问题

仿射法定理四：若以椭圆 $\frac{x^2}{a^2} +\frac{y^2}{b^2} = 1$ 的对称中心引出两条直线交椭圆于 $A$ 、 $B$ 两点，且 $k_{OA}\cdot k_{OB} = -\frac{b^2}{a^2}$ 则经过仿射变换后 $k_{OA'}\cdot k_{OB'} = -1$ ，所以 $S_{\triangle AOB} = \frac{ab}{2}$ 为定值。我们给一下证明：

## 解法一：联立设直线代入坐标面积公式

设 $l_{1}: y = kx$ ，则 $l_{2}: y = -\frac{b^{2}}{a^{2}k} x$ ，设 $A(x_{1}, y_{1}), B(x_{2}, y_{2})$

由 $\left\{\begin{aligned}y=kx\\ b^{2}x^{2}+a^{2}y^{2}=a^{2}b^{2}\end{aligned}\Rightarrow x_{1}^{2}=\frac{a^{2}b^{2}}{b^{2}+k^{2}a^{2}}\right.$ ，同理可得 $x_{2}^{2}=\frac{a^{2}b^{2}}{b^{2}+a^{2}\left(-\frac{b^{2}}{a^{2}k}\right)^{2}}=\frac{a^{4}k^{2}}{k^{2}a^{2}+b^{2}}$

由坐标面积公式可得 $S = \frac{1}{2}\left|x_{1}y_{2} - x_{2}y_{1}\right| = \frac{1}{2}\left| -\frac{b^{2}x_{1}\cdot x_{2}}{a^{2}k} -x_{2}\cdot kx_{1}\right| = \frac{1}{2}\left|\frac{a^{2}k^{2} + b^{2}}{a^{2}k}\cdot x_{1}x_{2}\right| = \frac{ab}{2}.$

解法二：三角换元

设 $A(a\cos \alpha ,b\sin \alpha)$ ， $C(a\cos \beta ,b\sin \beta)$ ，则 $\frac{b\sin\alpha}{a\cos\alpha}\cdot \frac{b\sin\beta}{a\cos\beta} = -\frac{b^2}{a^2}$ ，即 $\cos (\alpha -\beta) = 0$ ，故 $|\sin (\alpha -\beta)| = 1$ 因此，由坐标面积公式可得 $S = \frac{1}{2}|a\cos \alpha \cdot b\sin \beta -a\cos \beta \cdot b\sin \alpha | = \frac{1}{2} ab|\sin (\alpha -\beta)| = \frac{1}{2} ab.$

此法完美还原了仿射法的数形本质，强烈推荐此法.

解法三：点乘法代入面积公式变形

先证点乘法面积公式变形： $\left(\frac{x_1x_2}{a^2} +\frac{y_1y_2}{b^2}\right)^2 +\frac{(x_1y_2 - x_2y_1)^2}{a^2b^2} = 1.$

证明：由 $\left\{ \begin{array}{l} \frac{x_1^2}{a^2} + \frac{y_1^2}{b^2} = 1 \\ \frac{x_2^2}{a^2} + \frac{y_2^2}{b^2} = 1 \end{array} \right. \Rightarrow \left( \frac{x_1^2}{a^2} + \frac{y_1^2}{b^2} \right) \left( \frac{x_2^2}{a^2} + \frac{y_2^2}{b^2} \right) = 1 \Rightarrow \frac{x_1^2 x_2^2}{a^4} + \frac{y_1^2 y_2^2}{b^4} + \frac{x_1^2 y_2^2 + x_2^2 y_1^2}{a^2 b^2} = 1,$

配方： $\frac{x_{1}^{2}x_{2}^{2}}{a^{4}}+\frac{y_{1}^{2}y_{2}^{2}}{b^{4}}+\frac{2x_{1}x_{2}y_{1}y_{2}}{a^{2}b^{2}}+\frac{x_{1}^{2}y_{2}^{2}+x_{2}^{2}y_{1}^{2}}{a^{2}b^{2}}-\frac{2x_{1}x_{2}y_{1}y_{2}}{a^{2}b^{2}}=1$ ，即 $\left(\frac{x_{1}x_{2}}{a^{2}}+\frac{y_{1}y_{2}}{b^{2}}\right)^{2}+\frac{(x_{1}y_{2}-x_{2}y_{1})^{2}}{a^{2}b^{2}}=1.$

再证本题：由于 $\frac{y_1}{x_1} \frac{y_2}{x_2} = -\frac{b^2}{a^2}$ ，所以 $\frac{x_1 x_2}{a^2} + \frac{y_1 y_2}{b^2} = 0$ ，所以根据 $\left(\frac{x_1 x_2}{a^2} + \frac{y_1 y_2}{b^2}\right)^2 + \frac{(x_1 y_2 - x_2 y_1)^2}{a^2 b^2} = 1$ ，可得： $(x_1 y_2 - x_2 y_1)^2 = (2S)^2 = a^2 b^2$ ，所以 $S = \frac{1}{2} ab$ .

仿射法定理五：若 $|OM|^2 + |ON|^2 = a^2 + b^2$ ，如果直线 $OM$ 、 $ON$ 的斜率都存在，则有 $k_{OM} \cdot k_{ON} = \left|\frac{b^2}{a^2}\right|$ ，解法一：三角换元

设 $M(a\cos \alpha ,a\sin \alpha)$ ， $N(a\cos \beta ,a\sin \beta)$ ， $\alpha$ 、 $\beta \neq \frac{\pi}{2}$ ，故

$|OM|^2 + |ON|^2 = a^2 \cos^2\alpha + b^2 \sin^2\alpha + a^2 \cos^2\beta + b^2 \sin^2\beta = a^2 (1 - \sin^2\alpha) + b^2 \sin^2\alpha + a^2 \cos^2\beta + b^2 (1 - \cos^2\beta) = a^2 + b^2$ ，即 $(a^2 - b^2)\sin^2\alpha = (a^2 - b^2)\cos^2\beta$ ，即 $\sin^2\alpha = \cos^2\beta$ ，进而 $\cos^2\alpha = \sin^2\beta$ 。

因此， $k_{OM}^{2}\cdot k_{ON}^{2} = \frac{b^{2}\sin^{2}\alpha}{a^{2}\cos^{2}\alpha}\cdot \frac{b^{2}\sin^{2}\beta}{a^{2}\cos^{2}\beta} = \frac{b^{4}}{a^{4}}$ ，即 $k_{OM}\cdot k_{ON} = \pm \frac{b^2}{a^2}.$

解法二：利用坐标平方和公式变形

先证明： $\frac{y_1^2y_2^2}{b^4} = 1 + \frac{x_1^2x_2^2}{a^4} -\frac{x_1^2 + x_2^2}{a^2},\frac{x_1^2x_2^2}{a^4} = 1 + \frac{y_1^2y_2^2}{b^4} -\frac{y_1^2 + y_2^2}{b^2};$

证明： $\left\{ \begin{array}{l} \frac{y_1^2}{b^2} = 1 - \frac{x_1^2}{a^2} \\ \frac{y_2^2}{b^2} = 1 - \frac{x_2^2}{a^2} \end{array} \right. \Rightarrow \frac{y_1^2}{b^2} \cdot \frac{y_2^2}{b^2} = \left(1 - \frac{x_1^2}{a^2}\right)\left(1 - \frac{x_2^2}{a^2}\right)$ ，即 $\frac{y_1^2 y_2^2}{b^4} = 1 + \frac{x_1^2 x_2^2}{a^4} - \frac{x_1^2 + x_2^2}{a^2}$ ；同理： $\frac{x_1^2 x_2^2}{a^4} = 1 + \frac{y_1^2 y_2^2}{b^4} - \frac{y_1^2 y_2^2}{b^4}$ . $|OM|^2 + |ON|^2 = x_1^2 + x_2^2 + y_1^2 + y_2^2 = a^2 - \frac{a^2 y_1^2 y_2^2}{b^4} + \frac{x_1^2 x_2^2}{a^2} + b^2 - \frac{b^2 x_1^2 x_2^2}{a^4} + \frac{y_1^2 y_2^2}{b^2} = a^2 + b^2,$ 所以 $\frac{c^2 y_1^2 y_2^2}{b^4} = \frac{c^2 x_1^2 x_2^2}{a^4}$ ，所以 $k_{OM}^2 \cdot k_{ON}^2 = \frac{y_1^2 y_2^2}{x_1^2 x_2^2} = \frac{b^4}{a^4}$ ，即 $k_{OM} \cdot k_{ON} = \pm \frac{b^2}{a^2}$ .

![[高中/总复习/专题/2026版高中《mst老唐说题》圆锥曲线专题（数学）/下册/第13章_新定义下的斜率调整与仿射/第二节_仿射法与面积转化/三_斜率乘积__frac_b__2___a__2___能仿射成直角的面积定值问题/例题/Q00048891.md]]
![[高中/总复习/专题/2026版高中《mst老唐说题》圆锥曲线专题（数学）/下册/第13章_新定义下的斜率调整与仿射/第二节_仿射法与面积转化/三_斜率乘积__frac_b__2___a__2___能仿射成直角的面积定值问题/例题/Q00048970.md]]
![[高中/总复习/专题/2026版高中《mst老唐说题》圆锥曲线专题（数学）/下册/第13章_新定义下的斜率调整与仿射/第二节_仿射法与面积转化/三_斜率乘积__frac_b__2___a__2___能仿射成直角的面积定值问题/例题/Q00048971.md]]
