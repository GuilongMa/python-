# coding: utf-8

import functools


def is_use(flag):
    def memoize(fn):
        known = dict()
        if flag:
            @functools.wraps(fn)
            def memoizer(*args):
                if args not in known:
                    known[args] = fn(*args)
                return known[args]

            return memoizer
        return fn
    return memoize


@is_use(False)
def nsum(n):
    '''返回前n个数字的和'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)


@is_use(False)
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(10)', 'import': 'fibonacci',
                'func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum',
                                     'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import \
            {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time: \
            {}'.format(m['func'].__name__, m['func'].__doc__,
                       m['exec'], t.timeit()))
    # flag：True
    # name: fibonacci, doc: 返回斐波那契数列的第n个数, executing: fibonacci(100), time: 0.1689556
    # name: nsum, doc: 返回前n个数字的和, executing: nsum(200), time: 0.1376189

    # flag：False
    # name: fibonacci, doc: 返回斐波那契数列的第n个数, executing: fibonacci(10), time: 16.9971963
    # name: nsum, doc: 返回前n个数字的和, executing: nsum(200), time: 23.014836100000004