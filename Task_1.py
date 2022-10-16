def cool():
    a = 10
    b = 100
    c = 1000
    print(a, b, c)


print(cool.__code__.co_nlocals)
