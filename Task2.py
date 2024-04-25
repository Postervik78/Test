def divisor(arr):
    tarr= []
    tarr1 = []
    for i in range(0, len(arr)):
        for j in range(1, arr[i]):
            if arr[i] % j == 0:
                tarr.append(j)
    for i in range(0, len(tarr)):
        if tarr.count(i) >= 2:
            tarr1.append(i)
    print(tarr1)


arr1 = [42, 12, 18]
divisor(arr1)
