import sys


def solve():
    input_data = sys.stdin.read().split()
    data_iter = map(int, input_data)
    n = next(data_iter)
    m = next(data_iter)
    matrix_a = [[next(data_iter) for _ in range(m)] for _ in range(n)]

    for i in range(n):
        row_res = []
        for j in range(m):
            row_res.append(matrix_a[i][j] + next(data_iter))
        print(*row_res)


if __name__ == "__main__":
    solve()
