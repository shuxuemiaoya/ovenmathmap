---
title: "函数 y=Asin(ωx+φ) 及 y=Acos(ωx+φ) 的周期推导"
atom_type: "knowledge"
atom_key: "atom-6485bf3f8bf32e51"
owner_key: "node-toc-049"
source: "【人教版】高中必修 第一册数学电子课本.pdf"
source_pdf: "【人教版】高中必修 第一册数学电子课本.pdf"
source_sha256: "7f72df7a79284ad2b10d8bfaf58065e74b24f237bf6b7ad750a46bf557eb9051"
source_range: [8185, 8243]
used_by:
  - "普通高中教科书 数学 必修 第一册"
  - "第五章 三角函数"
  - "5.4 三角函数的图象与性质"
  - "5.4.2 正弦函数、余弦函数的性质"
  - "探究与发现 函数 y = A sin(ωx + φ) 及 函数 y = A cos(ωx + φ) 的周期"
organizers:
  - "普通高中教科书 数学 必修 第一册"
  - "第五章 三角函数"
  - "5.4 三角函数的图象与性质"
  - "5.4.2 正弦函数、余弦函数的性质"
  - "探究与发现 函数 y = A sin(ωx + φ) 及 函数 y = A cos(ωx + φ) 的周期"
updated_at: "2026-11-13"
review_status: "passed"
estimated_learning_minutes: 30
difficulty: "advanced"
importance: "core"
learning_objectives:
  - "从代数定义出发严谨推导并证明函数 y=Asin(ωx+φ) 与 y=Acos(ωx+φ)（A≠0,ω>0）的最小正周期 T=2π/ω。"
knowledge_number: 88
knowledge_granularity: "complete-teaching-unit"
is_definition_card: false
prerequisites:
  - "正弦函数、余弦函数的奇偶性"
defined_concepts: []
keywords:
  - "函数 y=Asin(ωx+φ) 及 y=Acos(ωx+φ) 的周期推导"
---

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
