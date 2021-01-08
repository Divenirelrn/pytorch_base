import torch


a = torch.ones(2,3)
print(a)

print("---------copy_-----------")
b = torch.randn(2,3)
b.copy_(a)
b[0,0] = 0
print(a)
print(b)

print("-----------clone----------")
c = a.clone()
c[0,0] = 0
print(a)
print(c)