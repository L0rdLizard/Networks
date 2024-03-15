import numpy as np
from scipy.special import comb


# def calculate_error_probability(g, l, eps):
#     poly = np.poly1d(g)
#
#     error_probability = 0
#     for i in range(l):
#         error_probability += poly(i) * (1 - eps) ** i * eps ** (l - i)
#
#     upper_bound = min(1, error_probability + eps)
#
#     return error_probability, upper_bound


# def calculate_error_probability(g, l, eps):
#     # Инициализация многочлена с помощью NumPy
#     poly = np.poly1d(g)
#
#     # Вычисление точной вероятности ошибки
#     error_probability = 0
#     for i in range(l + 1):
#         error_probability += poly(i) * eps ** i * (1 - eps) ** (l - i)
#
#     # Верхняя оценка вероятности ошибки
#     upper_bound = 0
#     for i in range(l + 1):
#         upper_bound += comb(l, i) * (eps ** i) * ((1 - eps) ** (l - i))
#
#     return error_probability, upper_bound

def calculate_error_probability(g, l, eps):
    # Инициализация многочлена с помощью NumPy
    poly = np.poly1d(g)

    # Вычисление точной вероятности ошибки
    i = np.arange(l + 1)
    error_probability = np.sum(poly(i) * (eps ** i) * (1 - eps) ** (l - i))

    # Верхняя оценка вероятности ошибки
    upper_bound = np.sum(comb(l, i) * (eps ** i) * ((1 - eps) ** (l - i)))

    return error_probability, upper_bound


g = [1, 0, 1]
l = 12
eps = 0.01

error_probability, upper_bound = calculate_error_probability(g, l, eps)
print(f"Вероятность ошибки: {error_probability}")
print(f"Верхняя оценка вероятности ошибки: {upper_bound}")
