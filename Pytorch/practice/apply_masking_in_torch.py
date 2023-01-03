import torch

# 1.
X = torch.arange(12).view(4,3)
mask = torch.zeros((4,3), dtype=torch.bool)
mask[0,0] = 1
mask[1,1] = 1
mask[3,2] = 1

## apply mask
X[mask] = 0

print(f"1번 방법 결과 : {X}")

## from http://juditacs.github.io/2018/12/27/masked-attention.html

# 2.
def make_mask_tensor(input_tensor:torch.Tensor, mask_value:int=0):
    mask_tensor = torch.eq(torch.tensor(mask_value).int(), input_tensor)

    return mask_tensor

def apply_masking(input_tensor:torch.Tensor, mask:torch.BoolTensor):
    input_tensor[mask] = -1e6

    return input_tensor

input_tensor = torch.tensor([1,2,3,4,0,0])
mask_tensor = make_mask_tensor(input_tensor=input_tensor)

applied_mask_result = apply_masking(input_tensor=input_tensor, mask=mask_tensor)
print(f"2번 방법 결과 : {applied_mask_result}")