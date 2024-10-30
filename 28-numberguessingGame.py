import random

lowest_num = 1
highest_num = 50
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("number guessing game")
print(f"choose a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("enter your guess: ")
    
    if guess.isdigit():
         guess = int(guess)
         guesses += 1
         
         if guess < lowest_num or guess > highest_num:
             print("the number is out of range")
             print(f"choose a number between {lowest_num} and {highest_num}")
         elif guess < answer:
             print("too low, try again!")
         elif guess > answer:
             print("too high, try again!")
         else:
             print(f"correct! the answer was {answer}")
             print(f"number of guesses: {guesses}")
             is_running = False
    else:
        print("invlid guess!")
        print(f"choose a number between {lowest_num} and {highest_num}")
