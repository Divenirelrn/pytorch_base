import torch

#一般tensor传数据，Tensor传shape
a = torch.tensor([1,2,3])
print(a)
a = torch.Tensor(3) #相当于FloatTensor
print(a)

#uninitialized
print(torch.empty(2,3))
print(torch.FloatTensor(2,3))

#random
print(torch.rand(2,3)) #x ~ u(0,1)
print(torch.randn(2,3)) #x ~ N(0,1)
print(torch.randint(1, 10, [2,3]))
a = torch.empty(2,3)
print(torch.rand_like(a))
print(torch.randperm(10))

#full
print(torch.full([2,3], 5))

#range
print(torch.arange(1, 10))
print(torch.linspace(1, 10, 10))
print(torch.logspace(0, 1, 10))

#special
print(torch.ones(2,3))
print(torch.zeros(2,3))
print(torch.eye(2,3))

#tensor.new()
a = torch.rand(3,2)
print(a.new(3,4).fill_(128))


