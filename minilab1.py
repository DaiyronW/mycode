#!/usr/bin/python3
def ask_question(question, options):
    while True:
        print(question)
        for i in range(len(options)):
            print(f"{i + 1}. {options[i]}")
        try:
            choice = int(input("Choose an option (1, 2, 3, or 4): ").strip())
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the 'Which Disney Villain Are You?' Quiz!\n")

    scores = {
        "Maleficent": 0,
        "Scar": 0,
        "Ursula": 0,
        "Jafar": 0
    }

    questions = [
        {
            "question": "What motivates you the most?",
            "options": ["Power", "Revenge", "Wealth", "Chaos"],
            "scores": ["Jafar", "Scar", "Ursula", "Maleficent"]
        },
        {
            "question": "What's your greatest strength?",
            "options": ["Magic", "Cunning", "Manipulation", "Fear"],
            "scores": ["Maleficent", "Scar", "Ursula", "Jafar"]
        },
        {
            "question": "How do you deal with enemies?",
            "options": ["Curse them", "Outsmart them", "Intimidate them", "Destroy them"],
            "scores": ["Maleficent", "Scar", "Jafar", "Ursula"]
        },
        {
            "question": "What's your ultimate goal?",
            "options": ["Rule the world", "Personal Vendetta", "Unlimited Power", "To Be Feared"],
            "scores": ["Jafar", "Scar", "Maleficent", "Ursula"]
        },
        {
            "question": "What's your greatest fear?",
            "options": ["Failure", "Being Forgotten", "Being Outwitted", "Losing Control"],
            "scores": ["Jafar", "Maleficent", "Scar", "Ursula"]
        }
    ]

    for question in questions:
        choice = ask_question(question["question"], question["options"])
        chosen_villain = question["scores"][choice - 1]
        scores[chosen_villain] += 1

    max_score = max(scores.values())
    result = [villain for villain, score in scores.items() if score == max_score]

    print("\nYou are most like: ")
    for villain in result:
        print(f"- {villain}")

if __name__ == "__main__":
    main()

