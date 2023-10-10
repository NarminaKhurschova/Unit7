import os.path
from random import shuffle


def read_words_file():
    with open(os.path.join('words.txt'), 'r') as file:
        words_content = file.read().split("\n")
        only_words =[]
        for word in words_content:
            if word != '':
                only_words.append(word)
            else:
                pass
        return only_words


def letters_shuffle(word):
    letters_list = [letter for letter in word]
    return letters_list


def words_compare(word, user_answer):
    if word == user_answer:
        return print(f'Верно! Вы получаете 10 очков')
    else:
        return print(f'Неверно! Верный ответ – {word}')


def history_of_users(user_name, points):
    with open(os.path.join('history.txt'), "a") as f:
        user = f.write(f'{user_name} {points}')
        return user

history_of_users("Narmina", 56)