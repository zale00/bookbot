def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count


def sort_on(dict_item):
    return dict_item["num"]


def sort_char_count(char_count_dict):
    sorted_list = []
    for char in char_count_dict:
        sorted_list.append({"char": char, "num": char_count_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list