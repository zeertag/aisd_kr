import matplotlib.pyplot as plt
import os


def make_graphs(sizes, times, filename="graph.png", save_path="Test_data"):
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, times, 'o-', markersize=8)
    plt.title('Скорость работы QR алгоритма, в завимости от размера матрицы', fontsize=14)
    plt.xlabel('Размер квадратной матрицы', fontsize=12)
    plt.ylabel('Время выполнения алгоритма (сек)', fontsize=12)
    plt.grid()
    plt.tight_layout(pad=2.0)

    save_file_path = os.path.join(save_path, filename)
    plt.savefig(save_file_path)