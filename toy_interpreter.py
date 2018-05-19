class Apply(object):
    def __init__(self, var=None, func=None):
        # TODO, 解析var定义变量
        if var is None:
            var = {}
        if func is None:
            func = {}

        self.var = var
        self.func = func

    def plus(self, l):
        r = self.apply(l[1])

        for i, e in enumerate(l):
            if i < 2:
                continue
            r += self.apply(e)

        return r

    def minus(self, l):
        r = self.apply(l[1])
        for i, e in enumerate(l):
            if i < 2:
                continue
            r -= self.apply(e)
        return r

    def times(self, l):
        r = self.apply(l[1])
        for i, e in enumerate(l):
            if i < 2:
                continue
            r *= self.apply(e)
        return r

    def divide(self, l):
        r = self.apply(l[1])
        for i, e in enumerate(l):
            if i < 2:
                continue
            r /= self.apply(e)
        return r

    def apply(self, l):
        ops = {
            '+': self.plus,
            '-': self.minus,
            '*': self.times,
            '/': self.divide,
        }

        if type(l) == list:
            op = l[0]
            r = ops[op](l)
        else:
            r = l
        return r


if __name__ == '__main__':
    a = Apply()
    print(a.apply(['+', 1, 2]))
    print(a.apply(['-', 1, 2]))
    print(a.apply(['*', 1, 2]))
    print(a.apply(['/', 1, 2]))

    print(a.apply(['+', 1, ['-', 2, 3]]))
