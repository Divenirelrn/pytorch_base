import torch

a = torch.full([8], 1.)
#norm
b = a.view(2,4)
c = a.view(2,2,2)
print(a.norm(1), b.norm(1), c.norm(1))
print(a.norm(2), b.norm(2), c.norm(2))

#mean/sum
a = torch.arange(8).view(2,4).float()
print(a.sum())
print(a.mean())

#max/min(默认先打平再返回,可用keepdim保持维度)
print(a.max(dim=1, keepdim=True))
print(a.min())

#argmax/argmin
print(a.argmax(dim=1))
print(a.argmin())

#top-k/k-th
a = torch.rand(4, 10)
print(a.topk(3, dim=1))
print(a.kthvalue(8, dim=1))


