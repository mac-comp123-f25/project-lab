import tkinter as tk
from trivia_questions import TRIVIA_QUESTIONS

category = "Football"
questions = [TRIVIA_QUESTIONS[category][i]["question"] for i in range(1, 6)]
correct_answers = [TRIVIA_QUESTIONS[category][i]["answer"].lower() for i in range(1, 6)]

def check_answers():
    for i in range(5):
        user_answer = entries[i].get().strip().lower()
        if user_answer == correct_answers[i]:
            entries[i].config(bg="green")
        else:
            entries[i].config(bg="red")

root = tk.Tk()
root.title("Football Trivia")
root.geometry("500x300")

title = tk.Label(root, text="Football", font=("Arial", 16))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

entries = []

for i, question_text in enumerate(questions):
    row = tk.Frame(frame)
    row.pack(pady=4, anchor="w")

    label = tk.Label(row, text=f"{i+1}. {question_text}", wraplength=400, justify="left")
    label.pack(side="left")

    entry = tk.Entry(row, width=20)
    entry.pack(side="left", padx=10)
    entries.append(entry)

button = tk.Button(root, text="Submit", command=check_answers)
button.pack(pady=10)

root.mainloop()



