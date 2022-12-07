import numpy as np
from my_module import count


def f_15_1(arr) -> list:
    multiples_2 = []

    for element in arr:
        if element % 2 == 0:
            multiples_2.append(element)

    return multiples_2


if __name__ == "__main__":
    amount = input(f"Initialize amount of elements in array: ")
    randomized_array = np.random.randint(1, 101, int(amount))

    print(f"Randomized array: {randomized_array}")
    print(f"Elements multiples 2: {f_15_1(randomized_array)}")

    new_file = open("file.txt", "wb")
    new_file.write(bytearray(randomized_array))
    new_file.close()

    print(f"Randomized elements was written to 'file.txt'")

    new_file = open("file.txt", "ab")
    new_file.write(bytearray(f_15_1(randomized_array)))
    new_file.close()

    print(f"Elements multiples '2' was written to 'file.txt'")

    print(f"Amount of lines in 'user_file': {count}")
