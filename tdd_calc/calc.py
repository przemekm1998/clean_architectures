from functools import reduce


class Calc:

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        result = reduce(lambda x, y: x * y, args)
        return result

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'inf'

    def avg(self, it, ut=None, lt=None):

        try:
            if ut is None:
                ut = max(it)
            if lt is None:
                lt = min(it)
            _it = [x for x in it if ut >= x >= lt]
            return sum(_it) / len(_it)
        except ValueError:
            return 0
        except ZeroDivisionError:
            return 0
