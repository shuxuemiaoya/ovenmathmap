## 32.1 角度 1: $d \to f(n)$

研究密钥

(1) 若 $d \to n$ , 如 $a_{n+1} - a_n = n (n \in \mathbb{N}^*)$ , $a_1 = 1$ , 求 $\{a_n\}$ 的通项公式.

由题意得 $\left\{\begin{aligned}a_{n}-a_{n-1}&=n-1\\ a_{n-1}-a_{n-2}&=n-2\\ \vdots\\ a_{2}-a_{1}&=1\end{aligned}\right.$ ，求和可得 $a_{n}-a_{1}=(n-1)+(n-2)+\cdots+1=\frac{n(n-1)}{2}$ ，所

以 $a_{n} = \frac{n(n - 1)}{2} +1.$

(2) 若 $d \to \frac{1}{n(n+1)}$ , 如 $a_{n+1} - a_n = \frac{1}{n(n+1)} (n \in \mathbb{N}^*)$ , $a_1 = 1$ , 求 $\{a_n\}$ 的通项公式.

$$
a _ {n} - a _ {n - 1} = \frac {1}{(n - 1) n} = \frac {1}{n - 1} - \frac {1}{n}
$$

由题意得 $\left\{ \begin{array}{l} a_{n-1} - a_{n-2} = \frac{1}{(n-2)(n-1)} = \frac{1}{n-2} - \frac{1}{n-1} \\ \vdots \\ a_2 - a_1 = 1 - \frac{1}{2} \end{array} \right.$ ，求和可得 $a_n - a_1 = 1 - \frac{1}{n}$ ，所

以 $a_{n}=2-\frac{1}{n}.$

(3) 若 $d \to 2^n$ , 如 $a_{n+1} - a_n = 2^n (n \in \mathbb{N}^*)$ , $a_1 = 1$ , 求 $\{a_n\}$ 的通项公式.

由题意得 $\left\{\begin{aligned}a_{n}-a_{n-1}&=2^{n-1}\\ a_{n-1}-a_{n-2}&=2^{n-2}\\ \vdots\\ a_{2}-a_{1}&=2^{1}\end{aligned}\right.$ ，求和可得 $a_{n}-a_{1}=2^{1}+2^{2}+\cdots+2^{n-1}=\frac{2^{1}-2^{n}}{1-2}=2^{n}-2$ ，所以 $a_{n}=2^{n}-1.$

(4) 若 $d \to \ln \frac{n + 1}{n}$ , 如 $a_{n+1} - a_n = \ln \frac{n + 1}{n} (n \in \mathbb{N}^*)$ , $a_1 = 1$ , 求 $\{a_n\}$ 的通项公式. 由题意得 $\left\{ \begin{array}{l} a_n - a_{n-1} = \ln \frac{n}{n-1} = \ln n - \ln (n-1) \\ a_{n-1} - a_{n-2} = \ln \frac{n-1}{n-2} = \ln (n-1) - \ln (n-2) \\ \vdots \\ a_2 - a_1 = \ln \frac{2}{1} = \ln 2 - \ln 1 \end{array} \right.$ , 求和可得 $a_n - a_1 = \ln n - \ln 1 =$ 所以 $a_n = \ln n + 1$ .

$$
\ln n
$$

![[高中/总复习/专题/高考数学培优40讲/高考数学培优40讲-03-三角、向量、数列、不等式与复数/第32讲_由递推数列求通项公式/递推关系__a__n_1__a_n_d__的拓展/32_1_角度1___d_to_f_n__/例题/Q00019987.md]]
![[高中/总复习/专题/高考数学培优40讲/高考数学培优40讲-03-三角、向量、数列、不等式与复数/第32讲_由递推数列求通项公式/递推关系__a__n_1__a_n_d__的拓展/32_1_角度1___d_to_f_n__/例题/Q00019988.md]]
