from trivia_questions import TRIVIA_QUESTIONS
import tkinter as tk

def run_trivia(TRIVIA_QUESTIONS):
    score = 0
    total = len(TRIVIA_QUESTIONS)

    for question in TRIVIA_QUESTIONS.items():
        user = input(question).strip().lower()

        if user == answer.lower():
            print ("Correct!\n")
            score += 1
        else:
            print (f"Wrong. Correct answer: {answer}\n")

    print(f"Game over! Score:"
          f" {score}/{total}\n")
    
window = tk.Tk()
welcome_window.title("Welcome to Game On: Sports Trivia Challenge!")
welcome_window.geometry("450x250")

def choose_category(category):
    window.destroy()

    if category == "football":
        run_trivia("Football")
    elif category == "soccer":
        run_trivia("Soccer")
    elif category == "baseball":
        run_trivia("Baseball")
    else:
        run_trivia("Basketball")


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





