"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    #ограничиваем зону поиска загаданного значения 50 значениями
    if number > predict:
      count += 1
      predict += 50
    else:
      count += 1
      predict -= 50
      
    #ограничиваем зону поиска загаданного значения 25 значениями из 50 отобраных выше в коде
    if number > predict:
      count += 1
      predict += 25
    else:
      count += 1
      predict -= 25

    #ограничиваем зону поиска загаданного значения 10 значениями из 25 отобраных выше в коде
    if number > predict:
      count += 1
      predict += 10
    else:
      count += 1
      predict -= 10
      
    #ограничиваем зону поиска загаданного значения 5 значениями из 10 отобраных выше в коде  
    if number > predict:
      count += 1
      predict += 5
    else:
      count += 1
      predict -= 5
      
    #производится перебор значений из 5 отобранных выше
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
