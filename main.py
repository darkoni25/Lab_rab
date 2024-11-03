print("Завдання 1")
def modify_list():
    user_input = input("Введіть елементи списку, розділені пробілами: ")
    user_list = user_input.split()
    element = input("Введіть елемент для вставки: ")
    position = int(input("Введіть позицію для вставки елемента (починаючи з 0): "))
    if 0 <= position <= len(user_list):
        user_list.insert(position, element)
        result = " ".join(user_list)
        print(f"Оновлений список: {result}.")
    else:
        print("Помилка: Позиція поза межами списку.")
    find_sequence(user_list)
def find_sequence(user_list):
    print("Завдання 2")
    sequence_input = input("Введіть послідовність для пошуку, розділену пробілами: ")
    sequence = sequence_input.split()
    seq_len = len(sequence)
    found = False
    for i in range(len(user_list) - seq_len + 1):
        if user_list[i:i + seq_len] == sequence:
            found = True
            print(f"Послідовність {sequence} знайдена на позиції {i}.")
            break
    if not found:
        print(f"Послідовність {sequence} не знайдена у списку.")
modify_list()
print("Завдання 3")
def analyze_text(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    letters = set(c.lower() for c in text if c.isalpha())
    vowels_in_text = letters & vowels
    consonants_in_text = letters - vowels
    vowel_count = sum(1 for c in text.lower() if c in vowels)
    consonant_count = sum(1 for c in text.lower() if c.isalpha() and c not in vowels)
    print(f"Унікальні літери у тексті (множина): {letters}")
    if vowel_count > consonant_count:
        print("Голосних більше.")
    elif consonant_count > vowel_count:
        print("Приголосних більше.")
    else:
        print("Кількість голосних і приголосних однакова.")
    if not letters:
        letters = set(list(letters))
        print(f"Результуюча множина (через перетворення): {letters}")
user_text = input("Введіть текст: ")
analyze_text(user_text)
