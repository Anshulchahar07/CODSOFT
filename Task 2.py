# Python Quiz Game
# Store all the questions in a tuple
questions = ("Philology is the ",
             "Satellite launching station is located at ",
             "What is the most abundant gas in the earth's atmosphere? ",
             "The 'Black flag' signifies ",
             "Rana Pratap Sagar (Rajasthan) is famous for ")

options = (("A. study of bones", "B. study of muscles", "C. study of architecture", "D. science of language"),
           ("A. Sriharikotta (Andhra pradesh)", "B. Solapur (Maharashtra)", "C. Salem (Tamilnadu)", "D. Warangal (Telangana)"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydragen"),
           ("A. revolution/danger", "B. peace", "C. protest", "D. truce"),
           ("A. hydropower generation", "B. aluminum industry", "C. brassware", "D. sports goods"))

answers = ("D", "A", "A", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------------")
print("          Results           ")
print("----------------------------")

print("Correct answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")