import torch
import torch.nn as nn
from torch import matmul, exp

import numpy as np


X = torch.rand((4, 10))
linear = nn.Linear(10, 3)

Y = linear(X)

W, b = linear.parameters()
print(f"=====")
print(f"W: {W.shape}")
item_val = W.shape
print(f"b: {b.shape}")
print(f"Y: {Y.shape}")
print(f"\nY torch val: \n{Y}")
print("=====\n\n")


# calculate matrix multiplication
Z = matmul(X, W.T) + b
Y_after_sigmoid = 1/1+exp(-Z)

print(f"=== calculate matrix multiplication ===")

print(f"Z: {Z.shape}")
print(f"Z val: \n{Z}")
print(f"Y_after_sigmoid: {Y_after_sigmoid.shape}")
print(f"Y_after_sigmind val: \n{Y_after_sigmoid}")
print(f"=======================================")


# calculate dot product
Y_man_vec = np.zeros(shape=(4, 3))
for x_idx in range(4):
  x = X[x_idx]
  for w_idx in range(3):
    w = W[w_idx]
    b_temp = b[w_idx]

    z = torch.sum(x * w.T) + b_temp
    Y_man_vec[x_idx, w_idx] = z.item()

print(f"=== calculate dot product ===")
print(Y_man_vec)
print("=============================")