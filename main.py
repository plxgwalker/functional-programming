import math


def f(x):
    return math.e**(1+x)


def tailor(x: float, eps: float):
    x += 1
    sum = 1+x
    term = x
    n = 2
    while term*term > eps*eps:
        term *= x/n
        n += 1
        sum += term
    return sum


a = float(input("Enter a: "))
b = float(input("Enter b: "))
eps = float(input("Enter eps: "))
step = (b-a)/10
error = f(a) - tailor(a, eps)

print(f"\n     x\t  |    _f(x)\t|    f(x)\t\t|    error\t|\n"
      f"---------------------------------------------------------")

while a <= b:
    print(
        f"    {a:.2f}  |    {tailor(a, eps):.4f}\t|    {f(a):.4f}\t|    {error:.4f}\t|")
    a += step
