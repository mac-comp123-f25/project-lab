import tkinter as tk

questions = [
    "Question 1:",
    "Question 2:",
    "Question 3:",
    "Question 4:",
    "Question 5:"
] # INPUT ACTUAL QUESTIONS 

correct_answers = ["a", "b", "c", "d", "e"] # INPUT ACTUAL ANSWERS

def check_answers():
    score = 0

    for i in range(5):
        user_answer = entries[i].get().strip().lower()
        if user_answer == correct_answers[i]:
            entries[i].config(bg="green")
            score += 1
        else:
            entries[i].config(bg="red")

    root.after(700, lambda: show_result(score))

def show_result(score):
    percent = int((score / 5) * 100)

    quiz_frame.pack_forget()

    for widget in result_frame.winfo_children():
        widget.destroy()

    if score == 5:
        result_frame.config(bg="green")
    else:
        result_frame.config(bg=root.cget("bg"))

    result_label = tk.Label(result_frame,
                            text=f"Your Score: {percent}%",
                            font=("Arial", 20),
                            bg=result_frame.cget("bg"))
    result_label.pack(pady=30)

    back_button = tk.Button(result_frame,
                            text="Go Back",
                            font=("Arial", 12),
                            command=go_back)
    back_button.pack()

    result_frame.pack(fill="both", expand=True)

def go_back():
    result_frame.config(bg=root.cget("bg"))
    result_frame.pack_forget()

    for entry in entries:
        entry.delete(0, tk.END)
        entry.config(bg="white")

    quiz_frame.pack()

root = tk.Tk()
root.title("Football Trivia")
root.geometry("350x300")


quiz_frame = tk.Frame(root)
quiz_frame.pack()

title = tk.Label(quiz_frame, text="Football", font=("Arial", 16))
title.pack(pady=10)

frame = tk.Frame(quiz_frame)
frame.pack()

entries = []

for i, q in enumerate(questions):
    row = tk.Frame(frame)
    row.pack(pady=4)

    label = tk.Label(row, text=f"{i+1}. {q}", width=15, anchor="w")
    label.pack(side="left")

    entry = tk.Entry(row, width=10)
    entry.pack(side="left")
    entries.append(entry)

button = tk.Button(quiz_frame, text="Submit", command=check_answers)
button.pack(pady=10)

result_frame = tk.Frame(root)

root.mainloop()



