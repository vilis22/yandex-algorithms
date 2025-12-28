def add(coefficients_x: list, coefficients_y: list, degree_x: int, degree_y: int) -> list:
    if degree_x > degree_y:
        long, short = coefficients_x, coefficients_y
    else:
        long, short = coefficients_y, coefficients_x

    result = long[:]
    length_short = len(short)

    for i in range(1, length_short + 1):
        result[-i] += short[-i]

    return result


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    res = add(a, b, n, m)
    print(max(n, m))
    print(*res)
