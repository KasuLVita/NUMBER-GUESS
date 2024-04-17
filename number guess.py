import random

difficulty_lvl = {
    'e': 10,
    'm': 5,
    'h': 3
}

def check(number, result, lives):
    if number == result:
        print("You win!")
        return True
    elif number > result:
        print("Too high!")
    else:
        print("Too low!")
    return False

print("Welcome to the number guessing game!")
while True:
    print('Choose a difficulty: (e) easy, (m) medium, (h) hard')
    ans = input("Enter a difficulty: ").lower()
    if ans in difficulty_lvl:
        lives = difficulty_lvl[ans]
        result = random.randint(1, 100)
        while lives > 0:
            print(f"You have {lives} attempts remaining to guess the number.")
            number = int(input("Enter a number: "))
            if check(number, result, lives):
                break
            lives -= 1
        if lives == 0:
            print(f"You lose! The number was {result}")
        break
    else:
        print("Invalid difficulty level. Please enter 'e' for easy, 'm' for medium, or 'h' for hard.")
