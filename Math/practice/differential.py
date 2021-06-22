import numpy as np
import matplotlib.pylab as plt

# 수치 미분
def numerical_differentiation(f, x):
    delta_x = 1e-5
    # 중앙 차분
    return (f(x+delta_x) - f(delta_x) / (delta_x * 2))

def f1(x):
    return x ** 2

def f2(x):
    return x ** 3 + x ** 2

x = np.arange(0, 10, 0.01)

plt.plot(x, f1(x), label = 'f1(x)')
plt.plot(x, numerical_differentiation(f1, x), label = 'f1(x)_derivative')

plt.plot(x, f1(x), label = 'f2(x)')
plt.plot(x, numerical_differentiation(f2, x), label = 'f2(x)_derivative')

plt.ylim(0, 300)
plt.legend()
plt.show()
