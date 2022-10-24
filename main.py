def f_15(n: float, i: int, summary=0) -> float:
    """Function represents a 15 variant of task.

        :param n: value of function.
        :param i: value which minus n in formula.
        :param summary: sum of 1/(((n-i)+(1)/(n-i++)))

        :returns:
            'Result' if n-i = 1.
            'Summary' in common case.

    """
    check_if_negative(n)

    if n - i == 1:
        result = (1 / (1 + 1 / 2)) + summary
        return result

    summary += 1 / (n - i + f_15(n, i + 1, summary))
    return summary


def check_if_negative(n: float) -> None:
    """Function represents a check if 'n' is not negative.

        :param n: Number which we want to check.
        :raise ValueError: If 'n' is negative.

    """
    if n < 1:
        raise ValueError("'N' can't be negative")


x = float(input("Enter n: "))
print(f"y({x}): {f_15(x, 0):.6f}")
