# making hand dirty with matplotlib
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1968081)

csfont = {'fontname':'Comic Sans MS'}

N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
# print(x,y)
# print(np.random.rand(5))
area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
r = np.sqrt(x ** 2 + y ** 2)
print("random area = ", area)
print(c)
print(r)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
print(r < r0)
print(area1)

plt.axes().set_aspect('equal')
plt.title("Matplotlib", **csfont)
plt.scatter(x,y, s=area1, marker='^', c=c)
plt.scatter(x,y, s=area2, marker='o', c=c)
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta), c="r", linestyle = "--")
plt.savefig("plot1.png")