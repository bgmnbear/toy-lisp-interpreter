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

    def calc_common(self, l, t):
        for i, e in enumerate(l):
            # print('i, e', i, e)
            if e in t:
                # print('if in')
                token = self.apply([e, l[i - 1], l[i + 1]])
                r = l[:i - 1] + [token] + l[i + 2:]
                # print('r', r)
                return r

    def calc_list(self, l):
        for i, e in enumerate(l):
            # print('i, e', i, e)
            if type(e) == list:
                t = self.calc(['calc', e])
                r = l[:i] + [t] + l[i + 1:]
                return r

    def calc_apply(self, l):
        for i, e in enumerate(l):
            if type(e) == list:
                r = self.calc_list(l)
                return r
        if ('*' in l) or ('/' in l):
            r = self.calc_common(l, ['*', '/'])
            return r
        elif ('+' in l) or ('-' in l):
            r = self.calc_common(l, ['+', '-'])
            return r

    def calc(self, l):
        f = l[1]
        if len(f) > 1:
            t = self.calc_apply(f)
            r = self.calc(['calc', t])
        else:
            r = f[0]
        return r

    def define_variable(self, l):
        v = self.apply(l[2])
        k = l[1]
        r = {
            k: v,
        }
        self.var.update(r)
        # print(self.var)
        return 'N/A'

    def call_variable(self, name):
        return self.var[name]

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

    l1 = ['calc', [1, '+', 2, '-', 3]]
    l2 = ['calc', [1, '+', 2, '*', 3, '/', 2]]
    l3 = ['calc', [1, '+', 2, '*', [1, '+', [1, '+', 1]], '/', 2]]

    print(Apply().calc(l1))
    print(Apply().calc(l2))
    print(Apply().calc(l3))
