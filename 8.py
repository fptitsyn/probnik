a = "АКСТУЬ"
c = 0
for a1 in a[:-1]:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    if ((a1 != a2 and a1 != a3 and a1 != a4 and a1 != a5) and
                            (a2 != a3 and a2 != a4 and a2 != a5) and
                            (a3 != a4 and a3 != a5) and
                            (a4 != a5)):
                        b = a1 + a2 + a3 + a4 + a5
                        if "СУК" not in b:
                            c += 1

print(c)

