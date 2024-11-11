
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
   
   
def select_word(file_path, used_words):
   with open(file_path, "r", encoding="utf-8") as f:
      lines = f.readlines()
   
   while True: # гипотетически бесконечный
      word = random.choice(lines)
      if word in used_words:
         word = random.choice(lines) 
      else:
         break
   
   return word


def get_input():
   # только буквы, все остальное - ошибка
   # если вводит правильную, но которую уже вводил, говорим "давай другую", ошибкой не считается
   # список для введенных правильных и список для введенных неправильных
   # если вводит НЕправильную, но которую уже вводил, говорим "давай другую", ошибкой не считается
   pass
       

# TODO
def main():
   # Приветствие
   # Выбрать слово
   # Получаем инпут от пользователя (+ защита от дурака)
   # Проверка буквы в слове (+ счетчик)
   # Вывод промежуточных результатов с картиночкой
   # Продолжаем играть?
   file_path="hangman_words.txt"
   used_words = []
   
   print_introduction()
   
   lines = select_word(file_path, used_words)
   print(lines)

if __name__ == "__main__":
   main()

