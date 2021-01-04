import torch

a = torch.randn(16, 3, 28, 28)
print(a)

#取第一张图片
print(a[0])

#取第一个channel
print(a[0, 0, :, :]) #：可写可不写

#select bu steps
print(a[:,:,0:28:2, 0:28:2])

#select by specific index
print(a.index_select(0, torch.tensor([0, 2]))) #第一个维度，取第0与第2张图片

#...
print(a[0, ...])

#torch.masked_select()
#torch.take()

