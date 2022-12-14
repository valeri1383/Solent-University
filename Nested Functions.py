from random import randrange


def number_check(a, b):
    if a == b:
        return True
    return False


min_value = int(input("Please enter the minimum value: "))
max_value = int(input("Please enter the maximum value: "))
random_num = randrange(min_value, max_value)
current_attempt = 0
print(f"I am thinking of a number between {min_value} and {max_value}. Can you guess what it is?")


while True:
    user_number = int(input())
    state_vadidation = number_check(user_number, random_num)

    if state_vadidation:
        print("Congratulations! You guessed my number!")
        break

    # Logg file Recording
    with open("Error Log", "a") as file:
        current_attempt += 1
        file.write(f"Wrong number! Number of attempts {current_attempt}\n" + "-" * 35 + "\n")

    print("Try again:")