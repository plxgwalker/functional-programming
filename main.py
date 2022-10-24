import random


randomized_list1 = []
randomized_list2 = []
n = int(input("Enter amount elements in lists: "))

for i in range(n):
    randomized_list1.append(random.randint(-10, 10))
    randomized_list2.append(random.randint(-10, 10))


def minimal(*list) -> int:
    minimal_n = 0
    print(f"Lists: {list}")

    for i in list[0]:
        if i not in list[1]:
            if i < minimal_n:
                minimal_n = i
    return minimal_n


print(f"Minimal number: {minimal(randomized_list1, randomized_list2)}")
