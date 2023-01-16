import torch.nn as nn
import torch.nn.functional as F
import torch.autograd as autograd

class STEFunction(autograd.Function):
    @staticmethod
    def forward(ctx, input):
        return (input > 0).float()

    @staticmethod
    def backward(ctx, grad_output):
        return F.hardtanh(grad_output) # gradient 값이 너무 커지지 않도록 제한을 걸어둔다.

class StraightThroughEstimator(nn.Module):
    def __init__(self):
        super(StraightThroughEstimator, self).__init__()

    def forward(self, x):
        x = STEFunction.apply(x)

        return x