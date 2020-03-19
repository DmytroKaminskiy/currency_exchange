import random
from time import sleep


def save_info(array: list) -> None:
    with open('workua2.txt', 'a') as file:
        for line in array:
            file.write(' | '.join(line) + '\n')


def random_sleep():
    sleep(random.randint(1, 4))
