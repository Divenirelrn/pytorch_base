import torch

#cat/stack
a = torch.rand(4,32,8)
b = torch.rand(4,32,8)
print(torch.cat([a,b], 1).shape)
print(torch.stack([a,b], 1).shape)

#split/chunk
a = torch.rand(2,32,8)
aa, bb = a.split([1,1], dim=0) #按长度分割
print(aa.shape, bb.shape)
aa, bb = a.chunk(2, dim=0) #按块数分割
print(aa.shape, bb.shape)