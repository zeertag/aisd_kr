import numpy as np

np.set_printoptions(suppress=True)


def qr_algorithm(matrix, tol=1e-10, max_iterations=1000):
    """
    Находит собственные числа матрицы с помощью QR-алгоритма.

    :param matrix: Квадратная матрица (numpy.ndarray)
    :param tol: Допустимая погрешность
    :param max_iterations: Максимальное количество итераций
    :return: Собственные числа матрицы
    """
    A = np.array(matrix, dtype=float)
    n = A.shape[0]
    for i in range(max_iterations):
        Q, R = np.linalg.qr(A)  # QR-разложение
        A_next = R @ Q  # Обновляем матрицу
        if np.allclose(A, A_next, atol=tol):  # Проверяем сходимость
            break
        A = A_next
    else:
        print("Предупреждение: алгоритм не сошелся за максимальное количество итераций")

    return A  # Собственные числа находятся на диагонали


# Пример использования
if __name__ == "__main__":
    matrix = np.random.randint(1, 10, size=(5, 5))  # Случайная матрица 4x4
    # matrix = [[6, 9, 9, 1], [1, 9, 4, 1], [3, 6, 2, 7], [1, 5, 6, 1]]
    print(f"Случайная матрица:\n{matrix}")

    A = qr_algorithm(matrix)
    print(A)
    eigenvalues = np.diag(A)
    print(f"Собственные числа: {eigenvalues}")
