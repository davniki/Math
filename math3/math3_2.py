# Границы водохранилища представляют собой простой многоугольник (то есть такой, в котором любые две стороны имеют не
# более одной общей точки, причём стороны имеют одну общую точку, только если у них есть общая вершина).

# Требуется по заданным границам водохранилища определить его площадь.

# Input. В первой строке одно число  𝑁(3≤𝑁≤105).  Каждая из  𝑁  последующих строк содержит два целых числа  𝑥𝑖  и
# 𝑦𝑖  — координаты очередной вершины водохранилища. Вершины идут в порядке обхода по часовой стрелке или против
# часовой стрелки. Все координаты — целые числа, по абсолютной величине не превосходящие  107 .

# Output. Одно число — величина площади приведённого многоугольника с абсолютной погрешностью не хуже  10−16 .

N = int(input())  # кол-во вершин простого многоуголника

# по формуле |((x1y2-y1x1)+...+(xny1-ynx1))/2| вычисли площадь s

x0 = int(input())
y0 = int(input())
a = 0
x1 = x0
y1 = y0
for i in range(N - 1):
    x2 = int(input())
    y2 = int(input())
    a = a + x1 * y2 - y1 * x2
    x1 = x2
    y1 = y2

s = abs(a / 2)
print(s)
