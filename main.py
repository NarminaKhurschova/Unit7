from functions import *

user_name = input("Введите свое имя")

words_list = read_words_file()

users_points = 0
for word in words_list:
    shuffled_word = letters_shuffle(word)
    user_answer = input(f"Угадайте слово:{shuffled_word}")
    points = words_compare(word, user_answer)
    if points > 0:
        users_points += 10
        print("Верно! Вы получаете 10 очков.")
    else:
        print(f"Неверно! Верный ответ – {word}.")

history_of_users(user_name, users_points)


