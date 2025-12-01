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

# --------------------- WELCOME SCREEN --------------------- #
welcome_window = tk.Tk()
welcome_window.title("Welcome to Game On: Sports Trivia Challenge!")
welcome_window.geometry("450x250")

title_label = tk.Label(
    welcome_window,
    text="Welcome to the Sports Trivia Game!",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=30)

start_button = tk.Button(
    welcome_window,
    text="Start Game",
    font=("Arial", 16),
    width=15,
    command=open_category_window
)
start_button.pack(pady=20)

welcome_window.mainloop()

# --------------------- CATEGORY WINDOW --------------------- #
def open_category_window():
    """Destroy welcome window and open category selection window."""
    welcome_window.destroy()

    category_window = tk.Tk()
    category_window.title("Select Trivia Category")
    category_window.geometry("400x300")

    label = tk.Label(category_window, text="Select Trivia Category", font=("Arial", 18))
    label.pack(pady=20)

    # Buttons for each category in TRIVIA_QUESTIONS
    for category in TRIVIA_QUESTIONS.keys():
        btn = tk.Button(
            category_window,
            text=category,
            font=("Arial", 14),
            width=20,
            command=lambda c=category: (category_window.destroy(), run_trivia(c))
        )
        btn.pack(pady=10)

    category_window.mainloop()