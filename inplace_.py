import torch


a = torch.rand(2,3)
print(a)

print(a.clamp(0.2, 0.8)) #会复制一份, 原tensor不会改变
print(a)

print(a.clamp_(0.2, 0.8)) #直接操作原tensor，inplace操作
print(a)