def table(n):
    for row in range(1, n + 1):
        for column in range(1, n + 1):
            print("%4d" % (row * column), end="")
        print()


n = 5
table(n)
