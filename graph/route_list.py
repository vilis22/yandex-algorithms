def main():
    n, m = map(int, input().split())
    adjacency_matrix_1 = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        stops = list(map(int, input().split()))
        for i in range(1, stops[0]):
            adjacency_matrix_1[stops[i] - 1][stops[i + 1] - 1] = 1
            adjacency_matrix_1[stops[i + 1] - 1][stops[i] - 1] = 1

    for _ in range(n):
        print(*adjacency_matrix_1[_])


if __name__ == "__main__":
    main()
