def f_15(n: float, i: int, result=0) -> float:
    if n - i == 1:
        summary = (1 / (1 + 1 / 2)) + result
        return summary

    result += 1 / (n - i + f_15(n, i + 1, result))
    return result


x = float(input("Enter n: "))

print(f"y({x}): {f_15(x, 0):.6f}")
