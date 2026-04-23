# main.py
import random  # это стандартная библиотека, не нужно ничего устанавливать

print("Привет! Давай сыграем в монетку!")

coin = random.randint(0, 1)  # 0 или 1

if coin == 0:
    print("Выпала РЕШКА! 🪙")
else:
    print("Выпал ОРЁЛ! 🪙")

# main.py (добавь в конец)

def guess_number():                     # новая функция
    secret = random.randint(1, 5)
    print("Угадай число от 1 до 5!")
    guess = int(input("Твой ответ: "))
    if guess == secret:
        print("УРА! Ты угадал! 🎉")
    else:
        print(f"Не угадал. Было число {secret}")

# Вызываем функцию
guess_number()