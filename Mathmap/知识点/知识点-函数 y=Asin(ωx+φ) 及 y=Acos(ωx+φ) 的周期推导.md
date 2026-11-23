---
id: "Ke236641b1ebca6"
kind: "knowledge"
title: "函数 y=Asin(ωx+φ) 及 y=Acos(ωx+φ) 的周期推导"
source_id: "rja-required-1"
source: "人教A版高中数学·必修第一册"
source_files: ["原子层/知识点/函数 y=Asin(ωx+φ) 及 y=Acos(ωx+φ) 的周期推导--000086.md", "原子层/公式/0011-F.md"]
source_node_keys: ["atom-6485bf3f8bf32e51", "atom-derived-7be077fc8f4ec7c4"]
knowledge_number: 167
learning_objective: "从代数定义出发严谨推导并证明函数 y=Asin(ωx+φ) 与 y=Acos(ωx+φ)（A≠0,ω>0）的最小正周期 T=2π/ω。"
---
对于函数

$$
y = A \sin (\omega x + \varphi), x \in \mathbf {R}
$$

及函数

$$
y = A \cos (\omega x + \varphi), x \in \mathbf {R}
$$

（其中 $A, \omega, \varphi$ 为常数，且 $A \neq 0, \omega > 0$ ），它们的周期仅与自变量的系数 $\omega$ 有关。下面推导用 $\omega$ 表示这些函数周期的一般公式。

令 $z = \omega x + \varphi$ ，那么由 $x\in \mathbf{R}$ 得 $z\in \mathbf{R}$ ，且函数 $y = A\sin z$ ， $z\in \mathbf{R}$ 及函数 $y = A\cos z$ ， $z\in \mathbf{R}$ 的周期都是 $2\pi$ .

因为

$$
z + 2 \pi = (\omega x + \varphi) + 2 \pi = \omega \left(x + \frac {2 \pi}{\omega}\right) + \varphi ,
$$

所以，对于任意 $x$ ，当自变量 $x$ 增加 $\frac{2\pi}{\omega}$ 时，函数值就重复出现；并且当增加量小于 $\frac{2\pi}{\omega}$ 时，函数值不会总重复出现。即

$$
T = \frac {2 \pi}{\omega}
$$

是使等式

$$
A \sin [ \omega (x + T) + \varphi ] = A \sin (\omega x + \varphi),
$$

$$
A \cos [ \omega (x + T) + \varphi ] = A \cos (\omega x + \varphi)
$$

成立的最小正数。从而，函数

$$
y = A \sin (\omega x + \varphi), x \in \mathbf {R}
$$

及函数

$$
y = A \cos (\omega x + \varphi), x \in \mathbf {R}
$$

的周期为 $T = \frac{2\pi}{\omega}$ .

根据这个结论，我们可以由这类函数的解析式直接写出函数的周期.
