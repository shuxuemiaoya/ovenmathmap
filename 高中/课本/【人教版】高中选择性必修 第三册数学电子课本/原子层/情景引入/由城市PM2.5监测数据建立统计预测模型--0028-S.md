---
title: 由城市PM2.5监测数据建立统计预测模型
atom_type: "scenario"
atom_key: "atom-c7a8f9f91a5c59e4"
owner_key: "node-toc-028"
source: "【人教版】高中选择性必修 第三册数学电子课本.pdf"
source_pdf: "【人教版】高中选择性必修 第三册数学电子课本.pdf"
source_sha256: "2f556770f33e5c8491482a769e8318ef098bb57b6733b629421c05678c4d82a1"
source_range: [5558, 5577]
used_by:
  - "普通高中教科书 数学 选择性必修 第三册"
  - "数学建模 建立统计模型进行预测"
organizers:
  - "普通高中教科书 数学 选择性必修 第三册"
  - "数学建模 建立统计模型进行预测"
updated_at: "2026-10-30"
review_status: "passed"
estimated_learning_minutes: 10
difficulty: "introductory"
importance: "context"
learning_objectives:
  - "说明本节学习动机与问题背景"
scenario_role: "section-introduction"
---

在现实世界中有许多随机现象需要研究。已有的学习告诉我们，研究随机现象，就是要在明确研究对象和问题的基础上，通过收集数据、整理数据、提取信息、构建数学模型，再利用模型进行推断，得出结论。通过这样的研究所得出的结论，可以为我们作出决策提供有力的依据。

下面我们看一个通过建立统计模型进行随机现象的分析和决策的实际事例.

背景 大气污染物 $PM_{2.5}$ （大气中直径小于或等于 $2.5 \mu m$ 的颗粒物）的浓度超过一定的限度会影响人的身体健康。为了研究 $PM_{2.5}$ 的浓度是否受到汽车流量、气候状况等因素的影响，研究人员选择了 24 个社会经济发展水平相近的城市，在每个城市选择一个交通点建立监测点，统计每个监测点 24 h 内过往的汽车流量（单位：千辆），同时在低空相同的高度测定每个监测点该时间段的平均气温（单位：℃）、风速（单位：m/s）、空气湿度（绝对湿度，单位： $g/m^{3}$ ）以及空气中 $PM_{2.5}$ 的平均浓度（单位： $\mu g/m^{3}$ ），得到的数据如表 1 所示。

表 1 24 个城市交通点空气中 ${\mathrm{{PM}}}_{2.5}$ 浓度监测数据

<table><tr><td>城市编号</td><td>汽车流量</td><td>平均气温</td><td>空气湿度</td><td>风速</td><td> $PM_{2.5}$ 浓度</td><td>城市编号</td><td>汽车流量</td><td>平均气温</td><td>空气湿度</td><td>风速</td><td> $PM_{2.5}$ 浓度</td></tr><tr><td>1</td><td>1.300</td><td>20.0</td><td>80</td><td>0.45</td><td>66</td><td>13</td><td>0.948</td><td>22.5</td><td>69</td><td>2.00</td><td>35</td></tr><tr><td>2</td><td>1.444</td><td>23.0</td><td>57</td><td>0.50</td><td>76</td><td>14</td><td>1.440</td><td>21.5</td><td>79</td><td>2.40</td><td>58</td></tr><tr><td>3</td><td>0.786</td><td>26.5</td><td>64</td><td>1.50</td><td>21</td><td>15</td><td>1.084</td><td>28.5</td><td>59</td><td>3.00</td><td>29</td></tr><tr><td>4</td><td>1.652</td><td>23.0</td><td>84</td><td>0.40</td><td>170</td><td>16</td><td>1.844</td><td>26.0</td><td>73</td><td>1.00</td><td>140</td></tr><tr><td>5</td><td>1.756</td><td>29.5</td><td>72</td><td>0.90</td><td>156</td><td>17</td><td>1.116</td><td>35.0</td><td>92</td><td>2.80</td><td>43</td></tr><tr><td>6</td><td>1.754</td><td>30.0</td><td>76</td><td>0.80</td><td>120</td><td>18</td><td>1.656</td><td>20.0</td><td>83</td><td>1.45</td><td>69</td></tr><tr><td>7</td><td>1.200</td><td>22.5</td><td>69</td><td>1.80</td><td>72</td><td>19</td><td>1.536</td><td>23.0</td><td>57</td><td>1.50</td><td>87</td></tr><tr><td>8</td><td>1.500</td><td>21.8</td><td>77</td><td>0.60</td><td>120</td><td>20</td><td>0.960</td><td>24.8</td><td>67</td><td>1.50</td><td>45</td></tr><tr><td>9</td><td>1.200</td><td>27.0</td><td>58</td><td>1.70</td><td>100</td><td>21</td><td>1.784</td><td>23.3</td><td>83</td><td>0.90</td><td>222</td></tr><tr><td>10</td><td>1.476</td><td>27.0</td><td>65</td><td>0.65</td><td>129</td><td>22</td><td>1.496</td><td>27.0</td><td>65</td><td>0.65</td><td>145</td></tr><tr><td>11</td><td>1.820</td><td>22.0</td><td>83</td><td>0.40</td><td>135</td><td>23</td><td>1.060</td><td>26.0</td><td>58</td><td>1.83</td><td>34</td></tr><tr><td>12</td><td>1.436</td><td>28.0</td><td>68</td><td>2.00</td><td>99</td><td>24</td><td>1.436</td><td>28.0</td><td>68</td><td>2.00</td><td>105</td></tr></table>

数学建模 建立统计模型进行预测

我们希望通过这些数据，定量探究与 $\mathrm{PM}_{2.5}$ 浓度相关的影响因素，为作出控制空气污染的决策提供依据.

建立统计模型进行预测的一般流程如图 1 所示. 我们按照这个流程, 对上述问题进行研究.

![](高中/课本/【人教版】高中选择性必修%20第三册数学电子课本/资源/images/part001_4aa52607e05691baeea53126b9399e0864b50c1d050338b21cd54643ae0d78b1.jpg)  
图1
