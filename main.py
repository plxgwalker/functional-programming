from random_word import RandomWords
r = RandomWords()


def largest_word(temp: list) -> str:
    max_word = ""

    for word in temp:
        if len(word) > len(max_word):
            max_word = word

    return max_word


def vowels_in_largest_word(max_word: str) -> str:
    vowel_o_counter = 0
    vowel_u_counter = 0
    vowel_a_counter = 0
    vowel_e_counter = 0
    vowel_i_counter = 0

    for letter in max_word:
        match letter:
            case "i":
                vowel_i_counter += 1
            case "o":
                vowel_o_counter += 1
            case "u":
                vowel_u_counter += 1
            case "a":
                vowel_a_counter += 1
            case "e":
                vowel_e_counter += 1

    return f"\nLargest word: {max_word}\nCounts: i: {vowel_i_counter}, o: {vowel_o_counter}, u: {vowel_u_counter}, " \
           f"a: {vowel_a_counter}, e: {vowel_a_counter}\n"


def list_insert() -> None:
    randomized_list = []
    generator = (r.get_random_word() for i in range(0, 10))

    for i in range(0, 10):
        randomized_list.append(next(generator))

    print(f"Randomized list: {randomized_list}")
    print(f"{vowels_in_largest_word(largest_word(randomized_list))}")

    randomized_list.remove(largest_word(randomized_list))
    print(f"Randomized list: {randomized_list}")


if __name__ == "__main__":
    list_insert()
