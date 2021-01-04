import torch

#torch.where(condition, x, y)
"""
 Return a tensor of elements selected from either x or y, depending on condition 
"""
cond = torch.tensor([[0.6789, 0.7271],
                     [0.8884, 0.4163]])
a = torch.zeros(2,2)
b = torch.ones(2,2)
c = torch.where(cond > 0.5, a, b)
print(c)

#torch.gether(input, dim, index, out=None)
"""
 input: 表格
 dim: 维度
 index； 下标, 选择表格中的第几个
"""
prob = torch.randn(4, 10)
idx = prob.topk(k=3, dim=1)[1] #4,3
print(idx)
label = torch.arange(10) + 100
print(label.expand(4, 10))
out = torch.gather(label.expand(4, 10), dim=1, index=idx.long())
print(out)

