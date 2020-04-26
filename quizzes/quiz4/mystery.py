def mystery(a, b):
    if b == 0:
        return 0
    elif b % 2 == 0:
        return mystery(a + a, b / 2)
    else:
        return a + mystery(a + a, b / 2)

