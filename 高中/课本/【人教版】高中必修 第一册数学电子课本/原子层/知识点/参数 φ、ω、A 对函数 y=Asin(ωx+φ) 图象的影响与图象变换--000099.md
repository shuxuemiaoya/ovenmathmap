---
title: "参数 φ、ω、A 对函数 y=Asin(ωx+φ) 图象的影响与图象变换"
atom_type: "knowledge"
atom_key: "atom-1ee2871c9140af69"
owner_key: "semantic-09513"
source: "【人教版】高中必修 第一册数学电子课本.pdf"
source_pdf: "【人教版】高中必修 第一册数学电子课本.pdf"
source_sha256: "7f72df7a79284ad2b10d8bfaf58065e74b24f237bf6b7ad750a46bf557eb9051"
source_range: [9514, 9610]
used_by:
  - "普通高中教科书 数学 必修 第一册"
  - "第五章 三角函数"
  - "5.6 函数 y = A sin(ωx + φ)"
  - "5.6.2 函数 $y=A\\sin(\\omega x+\\varphi)$ 的图象"
organizers:
  - "普通高中教科书 数学 必修 第一册"
  - "第五章 三角函数"
  - "5.6 函数 y = A sin(ωx + φ)"
  - "5.6.2 函数 $y=A\\sin(\\omega x+\\varphi)$ 的图象"
updated_at: "2026-11-09"
review_status: "passed"
estimated_learning_minutes: 45
difficulty: "advanced"
importance: "core"
learning_objectives:
  - "系统探究并掌握相位参数φ（左右平移）、频率参数ω（横坐标伸缩）与振幅参数A（纵坐标伸缩）对函数 y=Asin(ωx+φ) 图象的影响及由 y=sin(x) 变换作图的完整步骤。"
knowledge_number: 99
knowledge_granularity: "complete-teaching-unit"
is_definition_card: false
prerequisites:
  - "匀速圆周运动的数学模型"
defined_concepts:
  - "参数 φ、ω、A 对函数 y=Asin(ωx+φ) 图象的影响与图象变换"
keywords:
  - "参数 φ、ω、A 对函数 y=Asin(ωx+φ) 图象的影响与图象变换"
---

上面我们利用三角函数的知识建立了一个形如 $y = A \sin(\omega x + \varphi)$ （其中 A > 0, $\omega > 0$ ）的函数．显然，这个函数由参数 A, $\omega$ , $\varphi$ 所确定．因此，只要了解这些参数的意义，知道它们的变化对函数图象的影响，就能把握这个函数的性质．

思考

从解析式看，函数 $y=\sin x$ 就是函数 $y=A\sin(\omega x+\varphi)$ 在 A=1, $\omega=1$ , $\varphi=0$ 时的特殊情形.

（1）能否借助我们熟悉的函数 $y=\sin x$ 的图象与性质研究参数 A, $\omega$ , $\varphi$ 对函数 $y=A\sin(\omega x+\varphi)$ 的影响？

(2) 函数 $y = A \sin(\omega x + \varphi)$ 含有三个参数，你认为应按怎样的思路进行研究？


为了更加直观地观察参数 $\varphi$ 对函数图象的影响，下面借助信息技术做一个数学实验。如图 5.6-4，取 A=1， $\omega=1$ ，动点 M 在单位圆 $O_{1}$ 上以单位角速度按逆时针方向运动。如果动点 M 以 $Q_{0}$ 为起点（此时 $\varphi=0$ ），经过 x s 后运动到点 P，那么点 P 的纵坐标y 就等于 $\sin x$ 。以 $(x, y)$ 为坐标描点，可得正弦函数 $y = \sin x$ 的图象。

![](../../%E8%B5%84%E6%BA%90/images/part002_95e804d14c276badfdf2d28278fe7e3327cb28e0ebab70875b8045f9408f5f80.jpg)  
图5.6-4

探究

在单位圆上拖动起点 $Q_{0}$ ，使点 $Q_{0}$ 绕点 $O_{1}$ 旋转 $\frac{\pi}{6}$ 到 $Q_{1}$ ，你发现图象有什么变化？如果使点 $Q_{0}$ 绕点 $O_{1}$ 旋转 $-\frac{\pi}{6}, \frac{\pi}{3}, -\frac{\pi}{3}$ ，或者旋转一个任意角 $\varphi$ 呢？

当起点位于 $Q_{1}$ 时， $\varphi = \frac{\pi}{6}$ ，可得函数 $y = \sin \left(x + \frac{\pi}{6}\right)$ 的图象.


进一步，在单位圆上，设两个动点分别以 $Q_{0}$ ， $Q_{1}$ 为起点同时开始运动。如果以 $Q_{0}$ 为起点的动点到达圆周上点 $P$ 的时间为 $x \mathrm{~s}$ ，那么以 $Q_{1}$ 为起点的动点相继到达点 $P$ 的时间是 $\left(x - \frac{\pi}{6}\right)\mathrm{s}$ 。这个规律反映在图象上就是：如果 $F(x, y)$ 是函数 $y = \sin x$ 图象上的一点，那么 $G\left(x - \frac{\pi}{6}, y\right)$ 就是函数 $y = \sin \left(x + \frac{\pi}{6}\right)$ 图象上的点，如图5.6-4所示。这说明，把正弦曲线 $y = \sin x$ 上的所有点向左平移 $\frac{\pi}{6}$ 个单位长度，就得到 $y = \sin \left(x + \frac{\pi}{6}\right)$ 的图象。

分别说一说旋转 $-\frac{\pi}{6}$ ， $\frac{\pi}{3}, -\frac{\pi}{3}$ 时的情况.

一般地，当动点 M 的起点位置 Q 所对应的角为 $\varphi$ 时，对应的函数是 $y=\sin(x+\varphi)$ $(\varphi\neq0)$ ，把正弦曲线上的所有点向左（当 $\varphi>0$ 时）或向右（当 $\varphi<0$ 时）平移 $|\varphi|$ 个单位长度，就得到函数 $y=\sin(x+\varphi)$ 的图象.

2. 探索 $\omega (\omega > 0)$ 对 $y = \sin (\omega x + \varphi)$ 图象的影响

下面，仍然通过数学实验来探索．如图5.6-5，取圆的半径 $A = 1$ ，为了研究方便，不妨令 $\varphi = \frac{\pi}{6}$ 当 $\omega = 1$ 时得到 $y = \sin \left(x + \frac{\pi}{6}\right)$ 的图象.

![](../../%E8%B5%84%E6%BA%90/images/part002_04ff80f31df50fdd8c34b48864599c7ebdd797189851302917c7124a127ecb32.jpg)  
图5.6-5


探究

取 $\omega = 2$ ，图象有什么变化？取 $\omega = \frac{1}{2}$ 呢？取 $\omega = 3$ ， $\omega = \frac{1}{3}$ ，图象又有什么变化？当 $\omega$ 取任意正数呢？

取 $\omega = 2$ 时，得到函数 $y = \sin \left(2x + \frac{\pi}{6}\right)$ 的图象.

进一步，在单位圆上，设以 $Q_{1}$ 为起点的动点，当 $\omega = 1$ 时到达点 $P$ 的时间为 $x_{1}\mathrm{s}$ ，当 $\omega = 2$ 时到达点 $P$ 的时间为 $x_{2}\mathrm{s}$ 。因为 $\omega = 2$ 时动点的转速是 $\omega = 1$ 时的2倍，所以 $x_{2} = \frac{1}{2} x_{1}$ 。这样，设 $G(x, y)$ 是函数 $y = \sin \left(x + \frac{\pi}{6}\right)$ 图象上的一点，那么 $K\left(\frac{1}{2} x, y\right)$ 就是函数 $y = \sin \left(2x + \frac{\pi}{6}\right)$ 图象上的相应点，如图5.6-5所示。这说明，把 $y = \sin \left(x + \frac{\pi}{6}\right)$ 的图象上所有点的横坐标缩短到原来的 $\frac{1}{2}$ （纵坐标不变），就得到 $y = \sin \left(2x + \frac{\pi}{6}\right)$ 的图象。 $y = \sin \left(2x + \frac{\pi}{6}\right)$ 的周期为 $\pi$ ，是 $y = \sin \left(x + \frac{\pi}{6}\right)$ 的周期的 $\frac{1}{2}$ 。

同理，当 $\omega = \frac{1}{2}$ 时，动点的转速是 $\omega = 1$ 时的 $\frac{1}{2}$ ，以 $Q_{1}$ 为起点，到达点 $P$ 的时间是 $\omega = 1$ 时的2倍。这样，把 $y = \sin \left(x + \frac{\pi}{6}\right)$ 图象上所有点的横坐标伸长到原来的2倍（纵坐标不变），就得到 $y = \sin \left(\frac{1}{2} x + \frac{\pi}{6}\right)$ 的图象。 $y = \sin \left(\frac{1}{2} x + \frac{\pi}{6}\right)$ 的周期为 $4\pi$ ，是 $y = \sin \left(x + \frac{\pi}{6}\right)$ 的周期的2倍。

$$
\omega = \frac {1}{3}
$$

一般地，函数 $y = \sin (\omega x + \varphi)$ 的周期是 $\frac{2\pi}{\omega}$ ，把 $y = \sin (x + \varphi)$ 图象上所有点的横坐标缩短（当 $\omega > 1$ 时）或伸长（当 $0 < \omega < 1$ 时）到原来的 $\frac{1}{\omega}$ 倍（纵坐标不变），就得到 $y = \sin (\omega x + \varphi)$ 的图象.


下面通过数学实验探索 A 对函数图象的影响. 为了研究方便, 不妨令 $\omega=2,\quad\varphi=\frac{\pi}{6}$ .
当 A=1 时，如图 5.6-6，可得 $y=\sin\left(2x+\frac{\pi}{6}\right)$ 的图象.

![](../../%E8%B5%84%E6%BA%90/images/part002_68e95e7938973fde5a50b08b4589f242f7f5511e931c1586eaf193f8c2b8a212.jpg)  
图5.6-6

探究

改变 $A$ 的取值，使 $A$ 取 $2, \frac{1}{2}, 3, \frac{1}{3}$ 等，你发现图象有什么变化？当 $A$ 取任意正数呢？

当 A=2 时，得到函数 $y=2\sin\left(2x+\frac{\pi}{6}\right)$ 的图象.

进一步，设射线 $O_{1}Q_{1}$ 与以 $O_{1}$ 为圆心、2为半径的圆交于 $T_{1}$ 。如果单位圆上以 $Q_{1}$ 为起点的动点，以 $\omega = 2$ 的转速经过 $x$ s到达圆周上点 $P$ ，那么点 $P$ 的纵坐标是 $\sin \left(2x + \frac{\pi}{6}\right)$ ；相应地，点 $T_{1}$ 在以 $O_{1}$ 为圆心、2为半径的圆上运动到点 $T$ ，点 $T$ 的纵坐标是 $2\sin \left(2x + \frac{\pi}{6}\right)$ 。这样，设 $K(x, y)$ 是函数 $y = \sin \left(2x + \frac{\pi}{6}\right)$ 图象上的一点，那么点 $N(x, 2y)$ 就是函数 $y = 2\sin \left(2x + \frac{\pi}{6}\right)$ 图象上的相应点，如图5.6-6所示。这说明，把 $y = \sin \left(2x + \frac{\pi}{6}\right)$ 图象上所有点的纵坐标伸长到原来的2倍（横坐标不变），就得到 $y = 2\sin \left(2x + \frac{\pi}{6}\right)$ 的图象。

同理，把 $y = \sin \left(2x + \frac{\pi}{6}\right)$ 图象上所有点的纵坐标缩短到原来的 $\frac{1}{2}$ （横坐标不变），就得到 $y = \frac{1}{2}\sin \left(2x + \frac{\pi}{6}\right)$ 的图象.

$$
A = 3, A = \frac {1}{3}
$$

一般地，函数 $y=A\sin(\omega x+\varphi)$ 的图象，可以看作是把 $y=\sin(\omega x+\varphi)$ 图象上所有点的纵坐标伸长（当 A>1 时）或缩短（当 0<A<1 时）到原来的 A 倍（横坐标不变）而得到。从而，函数 $y=A\sin(\omega x+\varphi)$ 的值域是 $[-A, A]$ ，最大值是 A，最小值是 -A。

思考

你能总结一下从正弦函数图象出发，通过图象变换得到 $y = A \sin(\omega x + \varphi)$ (A > 0, $\omega > 0$ ) 图象的过程与方法吗？

一般地，函数 $y = A\sin (\omega x + \varphi)(A > 0, \omega > 0)$ 的图象，可以用下面的方法得到：先画出函数 $y = \sin x$ 的图象；再把正弦曲线向左（或右）平移 $|\varphi|$ 个单位长度，得到函数 $y = \sin (x + \varphi)$ 的图象；然后把曲线上各点的横坐标变为原来的 $\frac{1}{\omega}$ 倍（纵坐标不变），得到函数 $y = \sin (\omega x + \varphi)$ 的图象；最后把曲线上各点的纵坐标变为原来的 $A$ 倍（横坐标不变），这时的曲线就是函数 $y = A\sin (\omega x + \varphi)$ 的图象.

这一过程的步骤如下：

![](../../%E8%B5%84%E6%BA%90/images/part002_4b2334ece815cb92e5d433e54df352f4ace38c72a7798f66842686083f43a389.jpg)


补全步骤 2 和 3 的函数及图象.

从上述步骤可以清楚地看到，参数 $A$ ， $\omega$ ， $\varphi$ 是如何对函数图象产生影响的.
