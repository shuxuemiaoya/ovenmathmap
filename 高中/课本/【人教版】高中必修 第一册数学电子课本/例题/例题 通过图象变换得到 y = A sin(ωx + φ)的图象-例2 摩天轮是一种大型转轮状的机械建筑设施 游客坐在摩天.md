---
来源: 2019 人教A 数学 必修一
年级: 高一
节点类型: 例题
章节: 第五章 三角函数
所属知识点: "[[mathmap/知识点/通过图象变换得到 y = A sin(ωx + φ)的图象]]"
难度: 难
重要程度: 必须深度理解
---

> [!example]- 例 2 摩天轮是一种大型转轮状的机械建筑设施，游客坐在摩天轮的座舱里慢慢地往上转，可以从高处俯瞰四周景色。如图 5.6-9，某摩天轮最高点距离地面高度为 120 m，转盘直径为 110 m，设置有 48 个座舱，开启后按逆时针方向匀速旋转，游客在座舱转到距离地面最近的位置进舱，转一周大约需要 30 min。
>
> <div align="center">
>   <img src="/高中/课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/bb0e703a6803eb000215afaa6475c25a9d3bdb81e55eeceb9ab470790a3ce566.jpg" width="55%" />
>   <br />
>   图5.6-9
> </div>
>
> （1）游客甲坐上摩天轮的座舱，开始转动 $t \min$ 后距离地面的高度为 $H \mathrm{~m}$ ，求在转动一周的过程中， $H$ 关于 $t$ 的函数解析式；
> （2） 求游客甲在开始转动 5 min 后距离地面的高度;
> （3）若甲、乙两人分别坐在两个相邻的座舱里，在运行一周的过程中，求两人距离地面的高度差 h （单位：m）关于 t 的函数解析式，并求高度差的最大值（精确到 0.1）.
>
> > [!tip]- 分析：
> > 摩天轮上的座舱运动可以近似地看作质点在圆周上做匀速旋转。在旋转过程中，游客距离地面的高度 $H$ 呈现周而复始的变化，因此可以考虑用三角函数来刻画。
>
> > [!success]- 解：
> > 如图 5.6-10，设座舱距离地面最近的位置为点 P，以轴心 O 为原点，与地面平行的直线为 x 轴建立直角坐标系.
> > （1）设 $t = 0\mathrm{min}$ 时，游客甲位于点 $P(0, -55)$ ，以 $OP$ 为终边的角为 $-\frac{\pi}{2}$ ；根据摩天轮转一周大约需要 $30\mathrm{min}$ ，可知座舱转动的角速度约为 $\frac{\pi}{15}\mathrm{rad / min}$ ，由题意可得
> >
> > <div align="center">
> >   <img src="/高中/课本/【人教版】高中必修%20第一册数学电子课本/知识点/images/8a77869e70a8841a08939287801581fe2a1090585aa8c33df0d8e17103efd7c5.jpg" width="55%" />
> >   <br />
> >   图5.6-10
> > </div>
> >
> > $H = 5 5 \sin \left(\frac {\pi}{1 5} t - \frac {\pi}{2}\right) + 6 5, 0 \leqslant t \leqslant 3 0.$
> > （2） 当 t=5 时，
> > $H = 5 5 \sin \left(\frac {\pi}{1 5} \times 5 - \frac {\pi}{2}\right) + 6 5 = 3 7. 5.$
> > 所以，游客甲在开始转动 5 min 后距离地面的高度约为 37.5 m.
> > （3）如图5.6-10，设甲、乙两人的位置分别用点 $A$ ， $B$ 表示，则 $\angle AOB = \frac{2\pi}{48} = \frac{\pi}{24}$ 经过 $t\min$ 后甲距离地面的高度为 $H_{1} = 55\sin \left(\frac{\pi}{15} t - \frac{\pi}{2}\right) + 65$ ，点 $B$ 相对于点 $A$ 始终落后 $\frac{\pi}{24}\mathrm{rad}$ ，此时乙距离地面的高度为 $H_{2} = 55\sin \left(\frac{\pi}{15} t - \frac{13\pi}{24}\right) + 65.$ 则甲、乙距离地面的高度差
> > $h = \left| H _ {1} - H _ {2} \right| = 5 5 \left| \sin \left(\frac {\pi}{1 5} t - \frac {\pi}{2}\right) - \sin \left(\frac {\pi}{1 5} t - \frac {1 3 \pi}{2 4}\right) \right| = 5 5 \left| \sin \left(\frac {\pi}{1 5} t - \frac {\pi}{2}\right) + \sin \left(\frac {1 3 \pi}{2 4} - \frac {\pi}{1 5} t\right) \right|,$
> >
> > 利用 $\sin \theta +\sin \varphi = 2\sin \frac{\theta + \varphi}{2}\cos \frac{\theta - \varphi}{2}$ ，可得
> > $h = 1 1 0 \left| \sin \frac {\pi}{4 8} \sin \left(\frac {\pi}{1 5} t - \frac {\pi}{4 8}\right) \right|, 0 \leqslant t \leqslant 3 0.$
> > 当 $\frac{\pi}{15} t - \frac{\pi}{48} = \frac{\pi}{2}\left(\text{或} \frac{3\pi}{2}\right)$ ，即 $t \approx 7.8$ (或22.8)时， $h$ 的最大值为 $110\sin \frac{\pi}{48} \approx 7.2$ .
> > 所以，甲、乙两人距离地面的高度差的最大值约为 7.2 m.
