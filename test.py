import numpy as np
import time
import os

from main import QR
from lib_qr import qr_algorithm

times = []
det_value = []
check = []
a = QR()

tests = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for size in tests:
    t = 0
    mx_det = -1
    mn_det = 1
    a_det = 0
    check_count = 0
    for i in range(10):
        a.set_data(size, 2)
        B = np.copy(a.A)

        mx_det = max(mx_det, np.linalg.det(B))
        mn_det = min(mx_det, np.linalg.det(B))
        a_det += np.linalg.det(B)

        start = time.time()
        my_A = a.QR_algorithm()
        end = time.time()
        t += end - start

        lib_A = qr_algorithm(B)

        print(np.round(np.diag(my_A), 5), "- собственные числа (мои)")
        print(np.round(np.diag(lib_A), 5), "- собственные числа (с помощью библиотеки)")
        print(np.allclose(np.diag(my_A), np.diag(lib_A)), "\n")

        if np.allclose(np.diag(my_A), np.diag(lib_A)):
            check_count += 1

    det_value.append([mx_det, a_det, mn_det])
    check.append(check_count * 10)
    times.append(t / 10)

with open("times.txt", "w", encoding="utf-8") as file:
    file.write("Зависимость скорости выполнения QR алгоритма, от размера матрицы (тест по 10 замеров):\n\n")
    for i in range(len(tests)):
        file.write(f"{tests[i]} элементов: {times[i]} секунд\n")
        file.write(
            f"Максимально значение определителя - {det_value[i][0]}; среднее - {det_value[i][1]}; минимальное - {det_value[i][2]}\n")
        file.write(f"Совпадение собственных чисел для моего кода и библиотеки - {check[i]}%\n\n")
