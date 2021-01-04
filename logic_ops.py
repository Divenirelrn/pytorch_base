import torch

a = torch.rand(2,3)
b = torch.rand(2,3)
#>, <, ==, >=, <=, !=
#eq, ge（大于等于）
print(a > 0.5)

print(torch.eq(a, b))
print(torch.equal(a,b)) #只返回True或False