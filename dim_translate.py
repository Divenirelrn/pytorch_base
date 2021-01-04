import torch

#view/reshape（两方法效果等价）
a = torch.rand(4,1,28,28)
print(a.view(4, 1* 28 * 28))

#squeeze/unsqueeze
print(a.unsqueeze(0).shape)
print(a.unsqueeze(-1).shape)
print(a.squeeze().shape)

#expand/repeate
b = torch.randn(1, 3, 1, 1)
print(b.expand(16, 3, 28, 28).shape) #按维度
print(b.repeat(16,1,28,28).shape) #按重复次数

#transpose/permute
b = torch.rand(2,3)
print(b.t()) #只适用于二维张量

#b ,c ,h ,w -> b, w, h, c ->  b, w * h * c ->
b = a.transpose(1,3).contiguous().view(4, 28 * 28 * 1).view(4, 28, 28, 1).transpose(1,3)
print(torch.all(torch.eq(b, a)))
c = a.transpose(1,3).contiguous().transpose(1,3)
print(torch.all(torch.eq(c, a)))

b = a.permute(0,2,3,1)
print(b.shape)