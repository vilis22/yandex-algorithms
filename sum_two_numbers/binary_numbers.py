import sys


def main():
    data = sys.stdin.read().split()
    sys.stdout.write(f"{int(data[0], 2) + int(data[1], 2):b}\n")


if __name__ == "__main__":
    main()
