# Для трех заданных точек 𝑀1(𝑥1;𝑦1);𝑀2(𝑥2;𝑦2);𝑀3(𝑥3;𝑦3)  вычислить:

# 1. Периметр треугольника 𝑀1𝑀2𝑀3
# 2. 𝐶𝑜𝑠α ,  α  угол между прямыми  𝑀1𝑀2  и  𝑀2𝑀3
# 3. Найти площадь треугольника  𝑀1𝑀2𝑀3

import math as m

# Координаты точек M1, M2, M3.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())


# x1=0;y1=0;x2=3;y2=0;x3=3;y3=4;

# Периметр треугольника M1M2M3.
def l(x1, y1, x2, y2):
    l = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** (1 / 2)
    return l


a = l(x1, y1, x2, y2)
b = l(x1, y1, x3, y3)
c = l(x2, y2, x3, y3)

l = a + b + c
print(l)

# cos(a) и a между M1M2 и M2M3
v1 = x2 - x1
u1 = y2 - y1

v2 = x3 - x2
u2 = y3 - y2


def cos(v1, u1, v2, u2):
    r = (v1 * v2 + u1 * u2) / (((v1 ** 2 + u1 ** 2) ** (1 / 2)) * ((v2 ** 2 + u2 ** 2) ** (1 / 2)))
    return r


cos = cos(v1, u1, v2, u2)
print(cos, m.acos(cos))

# Площадь треугольника
p = l / 2
s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

print(s)
