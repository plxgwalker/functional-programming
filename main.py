import random


randomized_list1 = []
randomized_list2 = []
n = int(input("Enter amount elements in lists: "))

for i in range(n):
    randomized_list1.append(random.randint(-10, 10))
    randomized_list2.append(random.randint(-10, 10))


def minimal(list1: list, list2: list) -> int:
    minimal_n = 0
    for i in list1:
        if i not in list2:
            if i < minimal_n:
                minimal_n = i
    return minimal_n


print(f"List 1: {randomized_list1}")
print(f"List 2: {randomized_list2}")
print(f"Minimal number: {minimal(randomized_list1, randomized_list2)}")
