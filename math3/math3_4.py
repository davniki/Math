# Построить 4 графика используюя subplot для фунции
# 𝑦=(7+𝑥^2)/𝑥

# Сплошная линия зеленого цвета
# Пунктирная линия красного цвета
# Линия "Пунктир-точка" желтого цвета
# Линия, состоящая из точек черного цвета

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
y = (7 + x ** 2) / x  # наша функция

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle('4 графика')
ax1.plot(x, y, 'g', label='first')
ax2.plot(x, y, 'r--', label='second')
ax3.plot(x, y, 'y-.', label='third')
ax4.plot(x, y, 'k.', label='fourth')

for ax in fig.get_axes():
    ax.label_outer()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
