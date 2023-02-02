def divide(a, b):
    print(a/b)
    return a/b


divide(56, 2.2)


def divide(a, b):
    if b == 0:
        return "DON'T DIVIDE BY ZERO!"
    return a/b


print(divide(6, 0))
