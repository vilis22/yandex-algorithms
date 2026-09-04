class Number:
    x = None


list_integers = list(map(int, input().split()))
Number.x = max(list_integers)
