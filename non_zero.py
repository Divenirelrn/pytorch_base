import torch


a = torch.rand(2, 5)
print(a)

conf_mask = torch.nonzero(a[:, 4]).squeeze()

a = a[conf_mask].view(-1, 5)
print(a)