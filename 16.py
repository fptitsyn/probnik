def f(n):
    global k
    k += (n * n)
    if n > 1:
        k += (2 * n + 1)
        f(n - 2)
        f(n // 3)


for n in range(1, 10000):
    k = 0
    f(n)
    if k > 3200000:
        print(n, k)
        break

