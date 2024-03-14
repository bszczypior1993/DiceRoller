import random

print("Welcome to Dice Roller!")
walls = int(input("How many walls should your dice have? "))
dice_number = int(input(f"How many {walls} walled dice would you like to roll? "))
counter = 0

while dice_number > 0:
    roll = random.randint(1, walls)
    counter += 1
    print(f'The roll on your die no. {counter} is {roll}.')
    dice_number -= 1
