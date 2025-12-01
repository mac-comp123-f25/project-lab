from questions import TRIVIA_QUESTIONS
import tkinter as tk

from TRIVIA_QUESTIONS import (
    football_questions,
    soccer_questions,
    baseball_questions,
    basketball_questions
)

def run_trivia(TRIVIA_QUESTIONS):
    score = 0
    total = len(TRIVIA_QUESTIONS)

    print("Welcome to Game On: Sports Trivia Challenge!")

    for question in TRIVIA_QUESTIONS.items():
        user = input(question).strip().lower()

        if user == answer.lower():
            print ("Correct!\n")
            score += 1
        else:
            print (f"Wrong. Correct answer: {answer}\n")

    print(f"Game over! Score:"
          f" {score}/{total}\n")

def choose_category(category):
    window.destroy()

    if category == "football":
        run_trivia(football_questions)
    elif category == "soccer":
        run_trivia(soccer_questions)
    elif category == "baseball":
        run_trivia(baseball_questions)
    else:
        run_trivia(basketball_questions)


# ------------------- GUI WINDOW ------------------- #
window = tk.Tk()
window.title("Select Trivia Category")
window.geometry("350x200")

label = tk.Label(window, text="Select Trivia Category")
label.pack(padx=20)

buttons = [
("Football", "football"),
    ("Soccer", "soccer"),
    ("Baseball", "baseball"),
    ("Basketball", "basketball"),
]


for text, cat in buttons:
    btn = tk.Button(
        window,
        text=text,
        font=("Arial", 12),
        width=15,
        command=lambda c=cat: choose_category(c)
    )
    btn.pack(pady=5)

window.mainloop()





