import numpy as np
import matplotlib.pylab as plt

def numerical_differentiation(f, x):
    delta_x = 1e-5
    # 전진 차분
      # return (f(x + delta-x) - f(x)) / delta_x
    # 중앙 차분
    return (f(x+delta_x) - f(x-delta_x)) / (delta_x * 2)
    # 후진 차분
      # return (f(x) - f(x - delta_x)) / delta_x

def f(x):
    return x ** 3 + x ** 2

def f_analytic(x):
    return 3 * (x ** 2) + 2 * x

x = np.arange(0, 10, 0.01)

plt.plot(x, f(x), label = 'f(x)')
plt.plot(x, numerical_differentiation(f, x), label = 'f(x)_numerical_differentiation')
plt.plot(x, f_analytic(x), linestyle = '--', label = 'f(x)_analytic_differentiation')

plt.ylim(0, 300)
plt.legend()
plt.show()