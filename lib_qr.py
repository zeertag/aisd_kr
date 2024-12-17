import numpy as np

np.set_printoptions(suppress=True)


def qr_algorithm(matrix, tol=1e-10, max_iterations=1000):
    A = matrix
    for i in range(max_iterations):
        Q, R = np.linalg.qr(A)
        A_next = R @ Q
        if np.allclose(A, A_next, atol=tol):
            break
        A = A_next
    else:
        print("Выполнено максимальное количество итераций")
    return A
