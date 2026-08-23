考点2：基于 $\cos x\sim 1 - \frac{1}{2} x^2$ 的放缩

## 例1 (2025·河南·三模)已知函数 $f(x) = m(2 - x^2) - \cos x (m \in \mathbb{R})$

(1) 当 m=1 时，求 $f(x)$ 的零点个数；

(2) 若 $\forall x \in \mathbb{R}$ , $f(x) \leqslant 0$ , 求 $m$ 的最大值;

(3)证明： $\forall n\in \mathbf{N}^*$ ， $n - 1 <   \sum_{i = 1}^{n}\cos {\frac{1}{i}}.$

## 解析 (1) $f(x)$ 有两个零点.

(2)由 $f(0)=2m-1\leqslant0$ ，得 $m\leqslant\frac{1}{2}$ ，下证当 $m=\frac{1}{2}$ 时， $\forall x\in\mathbb{R},f(x)\leqslant0$ ，令 $g(x)=\frac{1}{2}(2-x^{2})-\cos x$ ，则 $g'(x)=\sin x-x$ ，令 $\varphi(x)=\sin x-x$ ，则 $\varphi'(x)=\cos x-1\leqslant0$ ，所以 $\varphi(x)$ 在R上单调递减，又 $\varphi(0)=\sin0-0=0$ ，则 $g'(x)<0$ 的解集为 $(0,+\infty)$ ，则 $g'(x)>0$ 的解集为 $(-∞,0)$ ，所以 $g(x)$ 在区间 $(-∞,0)$ 上单调递增，在区间 $(0,+\infty)$ 上单调递减，所以 $g(x)\leqslant g(0)=\frac{1}{2}\times(2-0)-\cos0=0$ ，即 $f(x)\leqslant0$ ，所以m的最大值为 $\frac{1}{2}$ .

(3)证明：由(2)可得 $\cos x \geqslant 1 - \frac{1}{2}x^{2}$ ，当且仅当 x = 0 时取等号，所以 $\cos \frac{1}{i} > 1 - \frac{1}{2}\left(\frac{1}{i}\right)^{2}$ ，所以 $2\sum_{i=1}^{n}\cos \frac{1}{i} > 2n - \sum_{i=1}^{n}\left(\frac{1}{i}\right)^{2}$ ，且因为当 $i \geqslant 2$ 时， $\left(\frac{1}{i}\right)^{2} < \frac{1}{(i-1)i} = \frac{1}{i-1} - \frac{1}{i}$ ， $\sum_{i=1}^{n}\left(\frac{1}{i}\right)^{2} = 1 + \frac{1}{2^{2}} + \frac{1}{3^{2}} + \cdots + \frac{1}{n^{2}} < 1 + 1 - \frac{1}{2} + \frac{1}{2} - \frac{1}{3} + \cdots + \frac{1}{n-1} - \frac{1}{n} = 2 - \frac{1}{n} < 2$ ，所以 $2\sum_{i=1}^{n}\cos \frac{1}{i} > 2n - \sum_{i=1}^{n}\left(\frac{1}{i}\right)^{2} > 2n - 2$ ，即 $\forall n \in N^{*}$ ， $n - 1 < \sum_{i=1}^{n}\cos \frac{1}{i}$ .
