import tkinter as tk

TRIVIA_QUESTIONS = {
    "Football": {
        1: {"question":"Which nfl team became the first team to win six superbowls?",
            "answer":"Steelers"},
        2: {"question":"Who holds the nfl record for most career passing yards?",
            "answer":"Chicago"},
        3: {"question":"What year did the first superbowl take place?",
            "answer":"1967"},
        4: {"question":"Which player is known for the famous immaculate reception?",
            "answer":"Franco Harris"},
        5: {"question":"Which nfl franchise has the most regular season wins in franchise history?",
            "answer":"Chicago"}
    }
}

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



