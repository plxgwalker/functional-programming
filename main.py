from numpy import arctan, sin, cos
from random import randint

# Варіант 15.

"""
Завдання 1.

1. З допомогою позиційних параметрів функції скласти програму обчислення
коренів рівняння f(x)=0 з точністю EPS = 0,0001.

"""


def function_15(x: float) -> float:
    """Функція репрезентує функцію 15 варінту.

    Arguments:
        x(float): значення x.

    Return:
        Вичислене значення функції 15 варінту.

    """
    return arctan(x) + x - 1


def newton_method(a: int, b: int, eps: float, f: function_15) -> float:
    """Функція репрезентує метод Ньютона.

    Arguments:
        a(int): початок проміжка.
        b(int): кінець проміжка.
        eps(float): значення точності.
        f(function_15): функція мого варіанту.

    Return:
        Значенння x на проміжку a та b з точністю eps.

    """
    while b - a > eps:
        x = (a + b) / 2
        fx = f(x)
        fa = f(a)
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
        else:
            b = x

    return x


print(f"Task 1:")
print(newton_method(-10, 10, 0.0001, function_15))


"""
Завдання 2.

2. З допомогою іменованих (ключових) параметрів функції дослідити з кроком
h функцію на певному проміжку (табулювання) у=arctg(x + 3,1); х[–6; 1], h =
0,2

"""


def tabulation_15(x: float) -> float:
    """
    Arguments:
        x(float): значення x.

    Return:
        Вичислене значення функції 15 варінту.

    """
    return sin(x**2) + cos(x)


def tabulation(left: float, right: float, h: float, f: tabulation_15) -> None:
    """
     Arguments:
        left(float): початок проміжка.
        right(float): кінець проміжка.
        h(float): значення крока.
        f(tabulation_15): функція мого варіанту.

    Return:
        Нічого.

    """
    x = left
    while x <= right:
        print(f"x = {x:.1f}\t|\ty = {tabulation_15(x):.4f}\t|")
        x += h


print(f"\nTask 2:")
tabulation(-4, 10, 0.4, tabulation_15)


"""Завдання 3:
    
    За допомогою функції генератора створити масив (N>50) з цілих додатних та
    від‘ємних чисел, які лежать в діапазоні від – 10 до 10 включно і передати його
    другій функції, яка здійснює визначення кількості елементів, що передують
    першому від‘ємному елементу та їх значення належить проміжку [1, 5].
    
"""

randomized_arr = [randint(-20, 70) for i in range(50)]


def generator_15(arr: randomized_arr) -> str:
    """
    Arguments:
        arr(randomized_arr): Array.

    Return:
         str: String of sorted array and how much 2-digit numbers is sorted array.

    """
    sorted_array = []
    two_decimal_nums = 0

    for i in arr:
        if i >= 0:
            sorted_array.append(i)
            if len(str(i)) == 2:
                two_decimal_nums += 1
    return f"Sorted array: {sorted(sorted_array)}" \
           f"\nAmount of two decimal numbers: {two_decimal_nums}"


def sort_arr(arr: randomized_arr) -> list:
    """
        Arguments:
            arr(randomized_arr): Array.

        Return:
             list: Sorted array. Example: [0, 3, 7].

    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(f"\nTask 3:")
print(f"Not sorted array: {randomized_arr}")
print(generator_15(sort_arr(randomized_arr)))
