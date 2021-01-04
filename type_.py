import torch

"""
基本数据类型：
torch.IntTensor
torch.FloatTensor
torch.ByteTensor
"""

#类型判断
a = torch.randn(2,3)
print(a.type())
print(isinstance(a, torch.FloatTensor))
print(type(a))

#属性
print(a.dim())
print(a.shape)
print(a.size())
print(a.numel()) #元素个数

#0-d tensor(应用：loss计算(.item(), .detach()))
a = torch.tensor(1.)
print(a)

#1-d张量(应用： bias)
a = torch.tensor([1.0])
print(a)

#2-d张量(应用：linear nn Input)
a = torch.FloatTensor(2,3)
print(a)

#3-d张量
a = torch.rand(1,2,3)
print(a)

#4-d张量
a = torch.randn(2, 3, 28, 28)
print(a)



