## 1. 等差数列的前 $\mathbf{n}$ 项和公式

公式①: $S_{n} = \frac{n(a_{1} + a_{n})}{2}$ ; ② $S_{n} = na_{1} + \frac{n(n - 1)}{2} d$ .

## 证明①:倒序相加法

$$
S _ {n} = a _ {1} + a _ {2} + a _ {3} + \dots + a _ {n - 1} + a _ {n} (1)
$$

$$
S _ {n} = a _ {n} + a _ {n - 1} + a _ {n - 2} + \dots + a _ {2} + a _ {1} \tag {②}
$$

$$
① + ②: 2 S _ {n} = \left(a _ {1} + a _ {n}\right) + \left(a _ {2} + a _ {n - 1}\right) + \left(a _ {3} + a _ {n - 2}\right) + \dots + \left(a _ {n} + a _ {1}\right)
$$

因为 $a_1 + a_n = a_2 + a_{n - 1} = a_3 + a_{n - 2} = \dots\dots = a_n + a_1$

所以 $2S_{n} = n(a_{1} + a_{n})$

由此得: $S_{n} = \frac{n(a_{1} + a_{n})}{2}$

证明②: 将 $a_{n}=a_{1}+(n-1)d$ 代入 $S_{n}=\frac{n(a_{1}+a_{n})}{2}$ 可得: $S_{n}=na_{1}+\frac{n(n-1)d}{2}$
