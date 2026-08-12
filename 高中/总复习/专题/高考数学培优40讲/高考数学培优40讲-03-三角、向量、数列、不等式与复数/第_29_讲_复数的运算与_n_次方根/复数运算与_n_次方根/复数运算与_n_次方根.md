## 复数的运算与 $n$ 次方根

在传统的观念中,复数在高考数学中所占的比重很小,难度简单且内容单调,随着新高考的深入,复数这部分内容的考查方式越来越灵活,具有常考常新、活而不难的特点.

复数不是一个孤立的内容, 它在三角、几何、代数中的应用非常广泛. 复数具有代数和三角两种形式, 它又与复平面的点之间建立起一一对应的关系, 即复数的实部与虚部是一对实变量, 那么对应的点在复平面上就是动点. 如果变量按某种条件变化, 那么复平面上对应点就构成具有某种特征的点的集合或轨迹, 这使得复数问题与平面向量、解析几何问题可相互转化, 成为数形结合的重要桥梁.

除此之外,复数还可以成为我们强有力的解题工具.根据题目特征,适当构造出一个与题目情景相应的“复数模型”,进而利用复数的性质,常可简捷地解决一些非复数问题.

本讲重点讲述复数的运算、复数三角形式乘除的几何意义、复数最值、 $n$ 次方根等问题, 揭示了复数与三角、向量、解析几何等知识的内在联系. 希望同学们通过本讲的学习, 对复数有全新的认识与领会, 并掌握好复数这一解题工具.

![](../../images/combined/part-001/157e627e228c08121394a5a100fb3daac104d39c2c32658fe1e4a1c26e1b0504.jpg)

## 研究密钥

## 1. 复数的定义和表示形式

(1) 复数代数形式: $z = a + b\mathrm{i}(a, b \in \mathbf{R})$ .

(2)三角形式： $z=r(\cos\theta+\mathrm{i}\sin\theta)$ ，其中 $r\geqslant0$ .

(3) 指数形式: $z = r e ^ { i \theta }$ , 其中 $r \geqslant 0$ ; 欧拉公式 $e^{i \theta} = \cos \theta + i \sin \theta$ , 其中 $\theta \in \mathbb{R}$ ; 数学最“美”的公式 $e^{i \pi} + 1 = 0$ .

(4)特殊复数：

①周期性： $i^{2}=-1,i^{4}=1,i^{n+4}=i^{n}(n\in\mathbf{Z})$ .

②1 的虚立方根 $\omega: \omega = -\frac{1}{2} \pm \frac{\sqrt{3}}{2} \mathrm{i}, \omega^3 = 1, \omega^2 + \omega + 1 = 0, \omega^2 = \overline{\omega}$ .

③恒等式： $a^{3}+b^{3}+c^{3}-3abc=(a+b+c)(a+\omega b+\omega^{2}c)(a+\omega^{2}b+\omega c)$ .

## 2. 模与共轭的性质

(1)运算性质： $|z|^{2}=\overline{z}z$ ，特别地， $|z|=1\Leftrightarrow\overline{z}=\frac{1}{z}$ .

(2)三角形不等式: $||z_1| - |z_2|| \leqslant |z_1 + z_2| \leqslant |z_1| + |z_2|$ , 其中左式取“=”的条件是 $\overrightarrow{OZ_1}$ 与 $\overrightarrow{OZ_2}$ 反向, 即 $|\arg z_1 - \arg z_2| = \pi$ , 亦即 $z_1 = -\lambda z_2 (\lambda > 0)$ ; 右式取“=”的条件是 $\overrightarrow{OZ_1}$ 与 $\overrightarrow{OZ_2}$ 同向, 即 $\arg z_1 = \arg z_2$ , 亦即 $z_1 = \lambda z_2 (\lambda > 0)$ .

(3) 平行四边形恒等式: $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$ .

(4)共轭运算： $\overline{(z)}=z$ （相互性）， $z+\overline{z}=2Rez$ ，或 $Rez=\frac{z+\overline{z}}{2}$ ; $z-\overline{z}=2iImz$ ，或 $Imz=\frac{z-\overline{z}}{2i}$ .

(5)复数属性判别： $z\in R\Leftrightarrow\bar{z}=z,z$ 是纯虚数 $\Leftrightarrow\bar{z}=-z\neq0.$

(6)运算性质： $\overline{(z)}=z,\overline{z_{1}\pm z_{2}}=\overline{z_{1}}\pm\overline{z_{2}},\overline{z_{1}}\overline{z_{2}}=\overline{z_{1}}\overline{z_{2}},\overline{\left(\frac{z_{1}}{z_{2}}\right)}=\frac{z_{1}}{\overline{z_{2}}}$ ;一般地, $f(z)\in\mathbf{R}\Rightarrow\overline{f(z)}=f(z)$ .

(7) 复数不等式: $|z| \geqslant \max \{|Rez|, |Imz|\} \geqslant \max \{Rez, Imz\}$ .

(8) 对称表示: $\operatorname{Re} z_{1} \overline{z_{2}} = \frac{1}{2} (\overline{z_{1}} z_{2} + z_{1} \overline{z_{2}}), \operatorname{Im}(z_{1} \overline{z_{2}}) = \frac{1}{2 \mathrm{i}} (z_{1} \overline{z_{2}} - \overline{z_{1}} z_{2})$ .

## 3. 复数的运算与几何意义

## (1) 加法与减法

复数的加减法适合代数形式运算 $(a+bi)\pm(c+di)=(a\pm c)+(b\pm d)i$ ，其几何意义是分别作出复数 $z_{1}$ 和复数 $z_{2}$ 对应的向量 $\overrightarrow{OZ_{1}}$ 与 $\overrightarrow{OZ_{2}}$ ，则向量 $\overrightarrow{OZ_{1}}+\overrightarrow{OZ_{2}}$ 对应复数 $z_{1}+z_{2}$ ，向量 $\overrightarrow{OZ_{1}}-\overrightarrow{OZ_{2}}$ 对应复数 $z_{1}-z_{2}$ .

## (2)乘法与除法

复数的乘法与除法也适合用代数形式运算 $(a+bi)(c+di)=(ac-bd)+(ad+bc)i$ ，但用三角形式作复数的乘法非常简洁。

$r_{1}(\cos\theta_{1}+\mathrm{i}\sin\theta_{1})\cdot r_{2}(\cos\theta_{2}+\mathrm{i}\sin\theta_{2})=r_{1}r_{2}[\cos(\theta_{1}+\theta_{2})+\mathrm{i}\sin(\theta_{1}+\theta_{2})]$ ，并有鲜明的几何意义：设 $z_{1}=r_{1}(\cos\theta_{1}+\mathrm{i}\sin\theta_{1}),z_{2}=r_{2}(\cos\theta_{2}+\mathrm{i}\sin\theta_{2})$ ，其中 $r_{1}>0,r_{2}>0$ ，作出复数 $z_{1}$ 对应的向量 $\overrightarrow{OZ_{1}}$ ，先把向量 $\overrightarrow{OZ_{1}}$ 的模“伸长”到 $r_{2}$ 倍，得到一个向量 $\overrightarrow{OZ^{\prime}}$ ，再把向量 $\overrightarrow{OZ^{\prime}}$ 按逆时针 $(\theta_{2}>0)$ 或顺时针 $(\theta_{2}<0)$ 旋转一个角 $|\theta_{2}|$ ，得到的向量 $\overrightarrow{OZ}$ 对应复数 $z_{1}z_{2}$ ；先把向量 $\overrightarrow{OZ_{1}}$ 的模“缩短”到 $\frac{1}{r_{2}}$ 倍，得到一个向量 $\overrightarrow{OZ^{\prime}}$ ，再把向量 $\overrightarrow{OZ^{\prime}}$ 按顺时针 $(\theta_{2}>0)$ 或逆时针 $(\theta_{2}<0)$ 旋转一个角 $|\theta_{2}|$ ，得到的向量 $\overrightarrow{OZ}$ 对应复数 $\frac{z_{1}}{z_{2}}$ 。

## (3)乘方与开方

①复数乘方: $(a + b\mathrm{i})^n = \sum_{r=0}^{n} \mathrm{i}^r \mathrm{C}_n^r a^{n-r} b^r$ ，当正整数 $n$ 较大时就不方便；用三角形式就十分简捷，即 $[r(\cos \theta + \mathrm{i}\sin \theta)]^n = r^n (\cos n\theta + \mathrm{i}\sin n\theta)$ .

②复数开方:已知复数 z, 求复数 w, 使之满足 $w^{n}=z$ , 这个计算过程叫复数开方; 当开方次数 n 较低时, 用代数形式还是比较方便的, 但次数较高时就应用三角形式 $w^{n}=r(\cos\theta+\mathrm{i}\sin\theta)$ , $w_{k}=\sqrt[n]{r}\left(\cos\frac{\theta+2k\pi}{n}+\mathrm{i}\sin\frac{\theta+2k\pi}{n}\right)$ , $w_{k}=w_{0}\left(\cos\frac{2\pi}{n}+\mathrm{i}\sin\frac{2\pi}{n}\right)^{k}$ .

其中 $k=0,1,2,\cdots,n-1$ . 其几何意义是复数 $w_{0}, w_{1}, \cdots, w_{n-1}$ 在复平面上均匀地分布在圆 $|z|=r$ 上.

## (4)复数系内解方程

①代数基本定理：n 次方程 $a_{0}x^{n}+a_{1}x^{n-1}+\cdots+a_{n-1}x+a_{n}=0(a_{0}\neq0)$ 有 n 个根（重根按重数计算），实系数高次方程虚根按共轭成对出现。

②开方解方程:方程 $(x-a)^{n}=b$ 的解析.

设 $b=r(\cos\theta+\mathrm{i}\sin\theta)(r>0)$ ，则 $x_{k}=a+\sqrt[n]{r}\left(\cos\frac{\theta+2k\pi}{n}+\mathrm{i}\sin\frac{\theta+2k\pi}{n}\right)(k=0,1,2,\cdots,n-1)$ .

几何意义: $n$ 个根 $x_0, x_1, \cdots, x_{n-1}$ 对应的复数均匀地分布在以 $a$ 为圆心, 以 $\sqrt[n]{r}$ 为半径的圆周上, 这些点恰好是一个正 $n$ 边形的顶点. 反之, 一个正 $n$ 边形的 $n$ 个顶点对应的复数可以用 $(x - a)^{n} = b$ ( $a$ 为该正多边形的中心) 的根来刻画.

![[高中/总复习/专题/高考数学培优40讲/高考数学培优40讲-03-三角、向量、数列、不等式与复数/第_29_讲_复数的运算与_n_次方根/复数运算与_n_次方根/29_1_复数的代数运算/29_1_复数的代数运算.md]]
![[高中/总复习/专题/高考数学培优40讲/高考数学培优40讲-03-三角、向量、数列、不等式与复数/第_29_讲_复数的运算与_n_次方根/复数运算与_n_次方根/29_2_复数三角形式的运算与几何意义/29_2_复数三角形式的运算与几何意义.md]]
![[高中/总复习/专题/高考数学培优40讲/高考数学培优40讲-03-三角、向量、数列、不等式与复数/第_29_讲_复数的运算与_n_次方根/复数运算与_n_次方根/29_3_复数模的最值问题/29_3_复数模的最值问题.md]]
![[高中/总复习/专题/高考数学培优40讲/高考数学培优40讲-03-三角、向量、数列、不等式与复数/第_29_讲_复数的运算与_n_次方根/复数运算与_n_次方根/29_4_三次单位根与_n_次单位根/29_4_三次单位根与_n_次单位根.md]]
