import torch

x = torch.randn(3,4) #初始值，始终不变
print(x)

sorted, indices = torch.sort(x)  #按行从小到大排序
print(sorted)
print(indices)

sorted, indices = torch.sort(x, descending=True)  #按行从大到小排序 (即反序)
print(sorted)
print(indices)

sorted, indices = torch.sort(x, dim=0)  #按列从小到大排序
print(sorted)
print(indices)

sorted, indices = torch.sort(x, dim=0, descending=True)  #按列从大到小排序
print(sorted)
print(indices)