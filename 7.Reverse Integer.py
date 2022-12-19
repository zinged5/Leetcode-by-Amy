def reverse(self, x: int) -> int:
    d = list(str(x))
    ln = -2 ** 31
    lh = 2 ** 31 - 1
    if d.count('-') > 0:
        d.remove('-')
        d = list(reversed(d))
        d.insert(0, '-')
        n = int(''.join(d))
        if ln <= n <= lh:
            return n
        else:
            return (0)
    else:
        n = int(''.join(list(reversed(d))))
        if ln <= n <= lh:
            return n
        else:
            return (0)