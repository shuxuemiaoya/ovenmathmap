---
id: "K8c7a453b4830eb"
kind: "knowledge"
title: "用R软件sample函数进行随机抽样"
knowledge_number: 328
learning_objective: "理解用R软件sample函数进行随机抽样，掌握其对象、条件与推理结论。"
---
例如，从一组数据 1, 2, 3, 3, 4, 4, 5, 6 中，抽取一个容量为 5 的样本。如果是有放回的抽取，在命令窗口中输入

$$
\begin{array}{l} \hline \mathrm{x< -c(1, 2, 3, 3, 4, 4, 5, 6)} \\ \text {sample(x, 5, T)} \end{array}
$$

如果是不放回的抽取，只要把 sample 函数中的参数 T 改为 F 即可.
