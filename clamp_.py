import torch

a = torch.rand(3,4)
print(a.clamp(0.2, 0.8))