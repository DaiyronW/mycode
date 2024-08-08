#!/usr/bin/python3

import html
import random

trivia = {
    "category": "Entertainment: Film",
    "type": "multiple",
    "question": "Which of the following is NOT a quote from the 1942 film Casablanca?",
    "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
    "incorrect_answers": [
        "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
        "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
        "&quot;Round up the usual suspects.&quot;"
    ]
}

question = html.unescape(trivia["question"])
correct_answer = html.unescape(trivia["correct_answer"])
incorrect_answers = [html.unescape(ans) for ans in trivia["incorrect_answers"]]

answers = incorrect_answers + [correct_answer]
random.shuffle(answers)

letters = ['A', 'B', 'C', 'D']

print(question)
for i, answer in enumerate(answers):
    print(f"{letters[i]}. {answer}")

user_answer = input("Enter your answer (A,B,C or D): ").upper()

if answers[letters.index(user_answer)] == correct_answer:
    print("you're right")

else:
    print("wrong")
