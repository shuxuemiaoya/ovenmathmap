## 知识点 06 双曲线中 a, b, c 的几何意义及有关线段的几何特征

双曲线标准方程中， $a$ 、 $b$ 、 $c$ 三个量的大小与坐标系无关，是由双曲线本身的形状大小所确定的，分别表

示双曲线的实半轴长、虚半轴长和半焦距长，均为正数，且三个量的大小关系为： $c > b > 0$ ， $c > a > 0$ ，且

$$
c ^ {2} = b ^ {2} + a ^ {2}
$$

双曲线 $\frac{x^2}{a^2} -\frac{y^2}{b^2} = 1(a > 0,b > 0)$ ，如图：

![](../images/questions/part-001/4e1e36bba39624c0b8721e8ba18bfe63c3bf2b80deb88e1030ba0e84ec65fa25.jpg)

(1) 实轴长 $\left|A_{1}A_{2}\right|=2a$ ，虚轴长 2b，焦距 $\left|F_{1}F_{2}\right|=2c$ ，

(2) 离心率： $e=\frac{|PF_{1}|}{|PM_{1}|}=\frac{|PF_{2}|}{|PM_{2}|}=\frac{|A_{1}F_{1}|}{|A_{1}K_{1}|}=\frac{|A_{2}F_{2}|}{|A_{2}K_{2}|}=\frac{c}{a}=\sqrt{1+\frac{b^{2}}{a^{2}}}\Rightarrow e>1$

(3) 顶点到焦点的距离： $\left|A_{1}F_{1}\right|=\left|A_{2}F_{2}\right|=c-a,\quad\left|A_{1}F_{2}\right|=\left|A_{2}F_{1}\right|=a+c$

(4) $\Delta PF_{1}F_{2}$ 中结合定义 $\left\|PF_1\right| - \left|PF_2\right| = 2a$ 与余弦定理，将有关线段 $\left|PF_1\right|$ 、 $\left|PF_2\right|$ 、 $\left|F_1F_2\right|$ 和角结合起来.

$\Delta PF_{1}F_{2}$ 有关的计算问题时，常考虑到用双曲线的定义及余弦定理（或勾股定理）、三角（5）与焦点三角形

形面积公式 $S_{\Delta PF_1F_2} = \frac{1}{2}\left|PF_1\right|\cdot \left|PF_2\right|\sin \angle F_1PF$ 相结合的方法进行计算与解题，将有关线段 $\left|PF_1\right|$ 、 $\left|PF_2\right|$ 、 $\left|F_1F_2\right|$

有关角 $\angle F_{1}PF_{2}$ 结合起来，建立 $\left|PF_1\right| - \left|PF_2\right|$ 、 $\left|PF_1\right|\cdot \left|PF_2\right|$ 之间的关系.

【即学即练】

1. 若双曲线 $\frac{x^2}{4} - \frac{y^2}{k} = 1$ 的一个焦点为 $(2\sqrt{2}, 0)$ ，则 $k =$ \_\_\_\_.

【答案】4

【详解】由题得， $4 + k = (2\sqrt{2})^2$ P k = 4

故答案为：4.

2. 已知双曲线 $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 (a > 0, b > 0)$ 的左右焦点分别为 $F_1, F_2$ ，过点 $F_1$ 的直线 $l: x - \sqrt{3}y + 2\sqrt{3} = 0$ 与双曲线的左右两支分别交于点 $A, B$ ，且 $\left|AF_2\right| = \left|BF_2\right|$ ，则该双曲线的方程为（）A. $\frac{x^2}{6} - \frac{y^2}{6} = 1$ B. $\frac{x^2}{4} - \frac{y^2}{8} = 1$ C. $x^2 - \frac{y^2}{11} = 1$ D. $\frac{x^2}{3} - \frac{y^2}{9} = 1$

【答案】A

【详解】依题意， $F_{1}(-2\sqrt{3},0),F_{2}(2\sqrt{3},0)$ ，直线l的倾斜角为 $30^{\circ}$ ，即 $\angle AF_{1}F_{2}=30^{\circ}$ ，取AB的中点D，连接 $F_{2}D$ ，由 $\left|AF_{2}\right|=\left|BF_{2}\right|$ ，得 $DF_{2}\perp AB$ ， $|DF_{2}|=2\sqrt{3},|DF_{1}|=6$ ，

![](../images/questions/part-001/5434d4e1db44df7b27908628daeda40a5a26f6c6db7d60f597daad85af190927.jpg)

$$
\left| B F _ {2} \right| = \left| A F _ {2} \right| = 2 a + \left| A F _ {1} \right| \quad \left| B F _ {1} \right| = 2 a + \left| B F _ {2} \right| = 4 a + \left| A F _ {1} \right|
$$

则 $|AD| = \frac{1}{2} |AB| = \frac{1}{2} (|BF_1| - |AF_1|) = 2a$ ， $|AF_2| = |DF_1| = 6$ ，

在 $\mathrm{Rt}\triangle ADF_2$ 中， $2a = \sqrt{|AF_2|^2 - |DF_2|^2} = \sqrt{6^2 - (2\sqrt{3})^2} = 2\sqrt{6}$ ，解得 $a = \sqrt{6}, b = \sqrt{6}$

所以该双曲线的方程为 $\frac{x^{2}}{6}-\frac{y^{2}}{6}=1$

故选：A
