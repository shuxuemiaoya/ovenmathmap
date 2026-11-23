---
id: "K46fd35e7b07b15"
kind: "knowledge"
title: "R软件生成随机数"
knowledge_number: 327
learning_objective: "理解R软件生成随机数，掌握其对象、条件与推理结论。"
---
1. 用 runif（）函数产生区间 $[0, 1]$ 内的随机数

例如，要产生 100 个区间 [0, 1] 内的随机数，在命令窗口中输入 “runif (100)” 即可（图 1）.

2. 用 sample（）函数产生区间 $[a, b]$ 内的整数随机数

例如，在命令窗口中输入“sample (1: 712, 100, T)”，就产生了100个区间[1, 712]内的可重复的整数随机数。如果希望随机数不可重复，只要把sample函数中的参数T改为F即可。

![](attachments/1e/1e65192bc4055adf4455fb58452da5bf84bef8e094a88e8b0499dff263661b16.jpg)  
图1
