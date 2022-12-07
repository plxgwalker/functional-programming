from names import get_full_name


zodiac_sign = [{
        "f_l_name": f"{get_full_name()}",
        "zodiac_sign": "The Ram",
        "birthday": [4, 5, 1990]
    },
    {
        "f_l_name": f"{get_full_name()}",
        "zodiac_sign": "The Bull",
        "birthday": [1, 12, 1997]
    },
    {
        "f_l_name": f"{get_full_name()}",
        "zodiac_sign": "The Twins",
        "birthday": [4, 3, 1986]
    },
    {
        "f_l_name": f"{get_full_name()}",
        "zodiac_sign": "The Crab",
        "birthday": [25, 8, 2000]
    },
    {
        "f_l_name": f"{get_full_name()}",
        "zodiac_sign": "The Lion",
        "birthday": [28, 12, 2003]
    },
    {
        "f_l_name": f"{get_full_name()}",
        "zodiac_sign": "The Virgin",
        "birthday": [20, 6, 1987]
    },
    {
        "f_l_name": f"{get_full_name()}",
        "zodiac_sign": "The Balance",
        "birthday": [24, 2, 1992]
    },
    {
        "f_l_name": f"{get_full_name()}",
        "zodiac_sign": "The Scorpion",
        "birthday": [16, 12, 1987]
    }]


def input_info() -> None:
    f_l_name = input(f"First and last name: ")
    sign = input(f"Zodiac sign: ")
    temp = input(f"Birthday: ")

    birthday = temp.split()
    birthday = [int(i) for i in birthday]

    new_user = {
        "f_l_name": f_l_name,
        "zodiac_sign": sign,
        "birthday": birthday
    }

    zodiac_sign.append(new_user)


if __name__ == "__main__":
    input_info()

    print(f"\nNot sorted list: ")
    for user in range(8+1):
        print(zodiac_sign[user])

    sorted_dict = sorted(zodiac_sign, key=lambda d: d["birthday"])

    print(f"\nSorted list: ")
    for user in range(8+1):
        print(sorted_dict[user])

    print(f"\nLast added user: \n{zodiac_sign[8]}")
