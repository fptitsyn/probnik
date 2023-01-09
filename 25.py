n = 0
for x in range(200_000_000, 700_000_000):
    d = set()
    for k in range(2, int(x ** 0.5) + 1):
        if x % k == 0:
            d.add(k)
            d.add(x // k)
    if len(d) < 5:
        p = 0
    else:
        a = sorted(d)
        p = a[0] * a[1] * a[2] * a[3] * a[4]
        if p % 10 == 1 and p <= x:
            n += 1
            print(x, p, a[4])
    if n == 5:
        break