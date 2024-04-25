def simple(n1, n2):
    for i in range(n1, n2 + 1):
        if i == 0 or i == 1:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i, ' ', end='')


n1 = int(input())
n2 = int(input())
simple(n1, n2)
