import torch

X = torch.arange(12).view(4,3)
mask = torch.zeros((4,3), dtype=torch.bool)
mask[0,0] = 1
mask[1,1] = 1
mask[3,2] = 1

# apply mask
X[mask] = 0

print(X)

## from http://juditacs.github.io/2018/12/27/masked-attention.html