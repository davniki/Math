# Вводится число  𝑁   (1<𝑁<106) .
# Напечатать  𝑁 -ую цифру числа,
# составленного из написанных подряд последовательных натуральных чисел, начиная с 1.

n = int(input())
s = ''

if 1 < n < 106:
    for i in range(1, n + 1):
        s += str(i)

a = int(s)
print((a // (10 ** int(len(str(a)) - n))) % 10)