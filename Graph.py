import matplotlib.pyplot as plt
import numpy as np

lstgred, lstxdrp, n0 = [], [], []

with open("data/results.txt", "r") as file:
    a = file.readline().strip()
    while len(a) > 0:
        a = a.split(" ")
        n0.append(int(a[0]))
        lstgred.append(int(a[3][:-2]))
        lstxdrp.append(int(a[2][:-2]))
        a = file.readline().strip()

plt.xlabel("Кількість елементів в послідовності")
plt.ylabel("Значення T'")
plt.title("Порівняння результатів для X-drop та Greedy алгоритмів")

gred = np.array(lstgred)
xdrp = np.array(lstxdrp)
n = np.array(n0)
plt.text(3000, 9000, "X-DROP")
plt.text(2300, 11000, "Greedy")
plt.plot(n, gred, n, gred, "ro")
plt.plot(n, xdrp, n, xdrp, "ro")

plt.grid(True)
plt.show()