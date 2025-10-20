def book_word_count(text):
   words = text.split()
   return len(words)

def char_count(text):
    char_count_table = {}
    for char in text:
        char = char.lower()
        char_count_table[char] = char_count_table.get(char, 0) +1
    return char_count_table

def sort_on(items):
    return items["num"]

def sorted_list_dict(text):
    char_count_table = char_count(text)
    dict_list = []
    for key, value in char_count_table.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list