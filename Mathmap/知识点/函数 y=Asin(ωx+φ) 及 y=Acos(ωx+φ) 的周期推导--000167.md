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

# 函数 y=Asin(ωx+φ) 及 y=Acos(ωx+φ) 的周期推导

函数 $y = A\sin (\omega x + \varphi)$ 及函数 $y = A\cos (\omega x + \varphi)$ 的周期

从前面的例子中可以看出，函数

$$
y = A \sin (\omega x + \varphi), x \in \mathbf {R}
$$

及函数

$$
y = A \cos (\omega x + \varphi), x \in \mathbf {R}
$$

（其中 $A, \omega, \varphi$ 为常数，且 $A \neq 0, \omega > 0$ ）的周期仅与自变量的系数有关。那么，如何用自变量的系数表示上述函数的周期呢？

事实上，令 $z = \omega x + \varphi$ ，那么由 $x\in \mathbf{R}$ 得 $z\in \mathbf{R}$ ，且函数 $y = A\sin z$ ， $z\in \mathbf{R}$ 及函数 $y = A\cos z$ ， $z\in \mathbf{R}$ 的周期都是 $2\pi$

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

的周期 $T = \frac{2\pi}{\omega}$

根据这个结论，我们可以由这类函数的解析式直接写出函数的周期.

想一想：上述求函数 $y = A \sin(\omega x + \varphi)$ ， $x \in R$ 及函数 $y = A \cos(\omega x + \varphi)$ ， $x \in R$ 周期的方法是否能推广到求一般周期函数的周期？即命题 “如果函数 $y = f(x)$ 的周期是 T，那么函数 $y = f(\omega x) (\omega > 0)$ 的周期是 $\frac{T}{\omega}$ ” 是否成立？

## 所属组织

- [探究与发现 函数 y = A sin(ωx + φ) 及 函数 y = A cos(ωx + φ) 的周期](../%E7%9F%A5%E8%AF%86%E4%B8%B2%E8%81%94/%E4%BA%BA%E6%95%99A-%E5%BF%85%E4%BF%AE%E7%AC%AC%E4%B8%80%E5%86%8C/%E7%AC%AC%E4%BA%94%E7%AB%A0%20%E4%B8%89%E8%A7%92%E5%87%BD%E6%95%B0/5.4%20%E4%B8%89%E8%A7%92%E5%87%BD%E6%95%B0%E7%9A%84%E5%9B%BE%E8%B1%A1%E4%B8%8E%E6%80%A7%E8%B4%A8/5.4.2%20%E6%AD%A3%E5%BC%A6%E5%87%BD%E6%95%B0%E3%80%81%E4%BD%99%E5%BC%A6%E5%87%BD%E6%95%B0%E7%9A%84%E6%80%A7%E8%B4%A8/%E6%8E%A2%E7%A9%B6%E4%B8%8E%E5%8F%91%E7%8E%B0%20%E5%87%BD%E6%95%B0%20y%20%3D%20A%20sin%28%CF%89x%20%2B%20%CF%86%29%20%E5%8F%8A%20%E5%87%BD%E6%95%B0%20y%20%3D%20A%20cos%28%CF%89x%20%2B%20%CF%86%29%20%E7%9A%84%E5%91%A8%E6%9C%9F.md)

## 相关练习组织（范围关联）

- [5.4.2 正弦函数、余弦函数的性质](../%E9%A2%98%E5%9E%8B/%E4%BA%BA%E6%95%99A-%E5%BF%85%E4%BF%AE%E7%AC%AC%E4%B8%80%E5%86%8C/%E7%AC%AC%E4%BA%94%E7%AB%A0%20%E4%B8%89%E8%A7%92%E5%87%BD%E6%95%B0/5.4%20%E4%B8%89%E8%A7%92%E5%87%BD%E6%95%B0%E7%9A%84%E5%9B%BE%E8%B1%A1%E4%B8%8E%E6%80%A7%E8%B4%A8/5.4.2%20%E6%AD%A3%E5%BC%A6%E5%87%BD%E6%95%B0%E3%80%81%E4%BD%99%E5%BC%A6%E5%87%BD%E6%95%B0%E7%9A%84%E6%80%A7%E8%B4%A8/5.4.2%20%E6%AD%A3%E5%BC%A6%E5%87%BD%E6%95%B0%E3%80%81%E4%BD%99%E5%BC%A6%E5%87%BD%E6%95%B0%E7%9A%84%E6%80%A7%E8%B4%A8.md)
