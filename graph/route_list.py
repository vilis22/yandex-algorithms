def main():
    n, m = map(int, input().split())
    matrix_1 = [[0 for _ in range(n)] for _ in range(n)]
    matrix_2 = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        data = list(map(int, input().split()))
        k = data[0]
        route = data[1:]

        for i in range(k - 1):
            u, v = route[i], route[i + 1]
            matrix_1[u - 1][v - 1] = 1
            matrix_1[v - 1][u - 1] = 1

        for i in range(k):
            for j in range(i + 1, k):
                u, v = route[i], route[j]
                matrix_2[u - 1][v - 1] = 1
                matrix_2[v - 1][u - 1] = 1

    for _ in range(n):
        print(*matrix_1[_])

    for _ in range(n):
        print(*matrix_2[_])


if __name__ == "__main__":
    main()
