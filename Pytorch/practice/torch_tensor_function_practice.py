import torch

# Tensor 생성 함수들
print("===== Tensor 생성 함수들 =====")

print("torch.rand :")
rand_result = torch.rand((1, 3))
print(rand_result, "\n")

print("torch.rand_like :")
rand_like_result = torch.rand_like(rand_result)
print(rand_like_result, "\n")

print("torch.randn :")
randn_result = torch.randn((1, 3))
print(randn_result, "\n")

print("torch.randn_like :")
randn_like_result = torch.randn_like(rand_result)
print(randn_like_result, "\n")

print("torch.randint :")
randint_result = torch.randint(10, size=(1, 3))
print(randint_result, "\n")

print("torch.randint_like :")
randint_like_result = torch.randint_like(randint_result, high=10)
print(randint_like_result, "\n")

print("torch.randperm :")
randperm_result = torch.randperm(5)
print(randperm_result, "\n")


# 특수 값을 가지는 Tensor 생성 함수들
print("===== 특수 값을 가지는 Tensor 생성 함수 =====")

print("torch.arange :")
arange_result = torch.arange(10)
print(arange_result, "\n")

print("torch.ones :")
ones_result = torch.ones((1, 3))
print(ones_result, "\n")

print("torch.zeros :")
zeros_result = torch.zeros((1, 3))
print(zeros_result, "\n")

print("torch.ones_like :")
ones_like_result = torch.ones_like(ones_result)
print(ones_like_result, "\n")

print("torch.zeros_like :")
zeros_like_result = torch.zeros_like(zeros_result)
print(zeros_like_result, "\n")


print("torch.linspace :")
linspace_result = torch.linspace(start=0, end=10, steps=10)
print(linspace_result, "\n")

print("torch.logspace :")
logspace_result = torch.logspace(start=0, end=10, steps=10)
print(logspace_result, "\n")