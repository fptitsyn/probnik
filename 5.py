def f(n):
    b = bin(n)[2:]
    a = "0" * (8 - len(b)) + b
    