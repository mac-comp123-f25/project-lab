from trivia_questions import TRIVIA_QUESTIONS
import tkinter as tk

def run_trivia(TRIVIA_QUESTIONS):
    score = 0
    total = len(TRIVIA_QUESTIONS)

    print("Welcome to Game On: Sports Trivia Game!")
    print(f"There are {total_questions} questions.\n")

    for question in TRIVIA_QUESTIONS.items():
        user = input(question).strip().lower()

        if user == answer.lower():
            print ("Correct!\n")
            score += 1
        else:
            print (f"Wrong. Correct answer: {answer}\n")

    print(f"Game over! Final score: {score}/{total}")

if __name__ == "__main__":
    run_trivia()

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


# ------------------- GUI WINDOW ------------------- #
window = tk.Tk()
window.title("Select Trivia Category")
window.geometry("350x200")

label = tk.Label(window, text="Choose a category:", font=("Arial", 14))
label.pack(pady=20)

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




