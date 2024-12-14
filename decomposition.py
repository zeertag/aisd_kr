import numpy as np


def qr_decomposition(A):
    R = np.zeros(A.shape)
    Q = np.zeros(A.shape)
    for i in range(A.shape[0]):
        v = A[:, i]
        for j in range(i):
            R[j, i] = np.dot(Q[:, j], v)
            v -= R[j, i] * Q[:, j]

        R[i, i] = np.linalg.norm(v)
        Q[:, i] = v / R[i, i]

    return Q, R


