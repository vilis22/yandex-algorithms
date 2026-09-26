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
