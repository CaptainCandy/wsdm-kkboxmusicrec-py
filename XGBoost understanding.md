# 在了解XGBoost之前

- 了解监督性学习

  监督学习，就是两步，一是定出模型确定参数，二是根据训练数据找出最佳的参数值

- 了解classification and regression trees (CART)决策树
- 如何找出最佳参数？

  需要目标函数来帮助我们来确定参数是否是最佳的
  目标函数通常由损失项+正则项组成：obj(θ)=L(θ)+Ω(θ)
    通常是：obj = ∑i(sigmoid(∑jθj*xij) - yi)^2 + ∑j(θj^2)
  目标函数可以设为MSE（mean squared error）函数：L(θ)=∑i(yi−y^i)2，这个函数通常被用作回归问题（最小二乘法）
  而对数损失函数通常被用做分类问题：L(θ)=∑i[yiln(1+e−y^i)+(1−yi)ln(1+ey^i)]

- 
