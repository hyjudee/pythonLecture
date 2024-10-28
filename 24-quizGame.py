questions = ("from where do we get solar energy?: ",
             "where is the captial city of south of korea?: ",
             "what do they sing about in a song from rose and bruno?: ")

options = (("A. the sun", "B. the earth", "C. the mars"), 
           ("A. busan", "B. jeju", "C. seoul"),
           ("A. house", "B. apt", "C. flat"))

answers = ("A", "C", "B")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("-" * 25)
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct!")
    else:
        print("incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-" * 26)
print(("-" * 10) + "result" + ("-" * 10))
print("-" * 26)

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")