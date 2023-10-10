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
    shuffle(letters_list)

    return "".join(letters_list)


def words_compare(word, user_answer):
    points = 0
    if word == user_answer:
        points += 10
    else:
        pass
    return points
    

def history_of_users(user_name, points):
    with open(os.path.join('history.txt'), "a") as f:
        user = f.write(f'{user_name} {points}\n')
        return user

