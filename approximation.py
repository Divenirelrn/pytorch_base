import torch

a = torch.rand(2,3)
print(a.floor())
print(a.ceil())
print(a.trunc(), a.frac())
print(a.round())