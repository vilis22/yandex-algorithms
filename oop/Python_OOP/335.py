import copy


class CrazyList:
    def __init__(self, lst=None):
        self.lst = [] if lst is None else lst

    def __str__(self):
        return f"CrazyList({self.lst})"

    @staticmethod
    def _subtract(source, other):
        result = copy.deepcopy(source)

        for item in other:
            for index, value in enumerate(result):
                if type(value) is type(item) and value == item:
                    result.pop(index)
                    break

        return result

    def __sub__(self, other):
        other_lst = other.lst if isinstance(other, CrazyList) else other
        return CrazyList(self._subtract(self.lst, other_lst))

    def __rsub__(self, other):
        return self._subtract(other, self.lst)

    def __isub__(self, other):
        other_lst = other.lst if isinstance(other, CrazyList) else other
        self.lst[:] = self._subtract(self.lst, other_lst)
        return self


x_1 = CrazyList([0, 1, "1", 0, 1, 2, "0", True, "True", 6, 8, "False", False, {1: 0, 2: 0}])
x_1_id = id(x_1)
print(x_1)  # CrazyList([0, 1, '1', 0, 1, 2, '0', True, 'True', 'False', False, {1: 0, 2: 0}])
x_2 = CrazyList([1, "1", 0, 1, 2, True, "False", "0", {1: 0}, 6, 9, 1])
print(x_2)  # CrazyList([1, '1', 0, 1, 2, True, 'False', '0', {1: 0}, 6, 9, 1])
x_2_id = id(x_2)
x_3 = x_1 - x_2
print(x_3)  # CrazyList([0, 'True', 8, False, {1: 0, 2: 0}])
assert x_1_id == id(x_1) and isinstance(x_3, CrazyList) and id(x_3) != x_1_id, (
    'при операции "-" создается новый объект, \
уменьшаемый объект не должен менять своего id'
)
assert x_2_id == id(x_2), "вычитаемый объект не должен менять своего id"
