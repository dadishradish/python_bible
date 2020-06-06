from random import choice

questions = [
    "Why do dogs bark?: ",
    "How many leaves grow on trees?: ",
    "Why can't babies talk?: "
    ]

question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh...Okay")
