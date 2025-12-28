from itertools import chain


def curved_sum(line_a: str, line_b: str, line_length: int) -> str:
    return "".join(chain.from_iterable(zip(line_a, line_b)))


if __name__ == "__main__":
    import sys

    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = input_data[1]
    b = input_data[2]
    print(curved_sum(a, b, n))
