
import random


# играющий сдаётся, если он вводит одно из этих слов
EXIT_WORDS = ["quit", "exit", "сдаюсь", "выход"]

HANGMAN_PICS =  ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O  |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']


def print_introduction():
   print("Добро пожаловать в Виселицу! Ты не можешь ошибиться больше 7 раз! Вводи по одной букве и смотри результаты.")
   print("Для выхода из игры введи одно из слов: {}".format(", ".join(EXIT_WORDS)))
   
   
def select_word(file_path="hangman_words.txt"):
   with open(file_path, "r", encoding="utf-8") as f:
      lines = f.readlines()
   return lines

# TODO
def main():
   # Приветствие
   # Выбрать слово
   # Получаем инпут от пользователя (+ защита от дурака)
   # Проверка буквы в слове (+ счетчик)
   # Вывод промежуточных результатов с картиночкой
   # Продолжаем играть?
   print_introduction()
   lines = select_word()
   print(lines)

if __name__ == "__main__":
   main()

