import torch

#+/-/*//
a = torch.rand(2,3)
b = torch.rand(3,2)
#torch.add(a, b) <-> a + b
#torch.sub(a, b) <-> a - b
#torch.mul(a, b) <-> a * b
#torch.div(a, b) <-> a / b

#matrix multiply
print(torch.mm(a,b)) #只适用于2-d张量
print(torch.matmul(a,b))
print(a @ b)

#pow/sqrt
print(a.pow(2))
print(a.sqrt())
print(a ** 0.5) #通用写法
print(a.abs())

#exp/log
print(torch.exp(a))
print(torch.log(a))