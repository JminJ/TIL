import torch

X = torch.arange(12).view(4,3)
mask = torch.zeros((4,3), dtype=torch.bool)
mask[0,0] = 1
mask[1,1] = 1
mask[3,2] = 1

X[mask] = 0

print(X)