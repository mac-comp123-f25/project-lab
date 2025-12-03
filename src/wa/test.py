import tkinter as tk
from tkinter import messagebox
from trivia_questions import TRIVIA_QUESTIONS

# ------------------- MAIN APP CLASS ------------------- #
class TriviaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game On: Sports Trivia Challenge!")
        self.root.geometry("600x450")
        self.entries = []
        self.correct_answers = []

        self.show_welcome_screen()

    # ---------- Welcome Screen ---------- #
    def show_welcome_screen(self):
        self.clear_window()

        title_label = tk.Label(
            self.root,
            text="Welcome to the Sports Trivia Game!",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=30)

        start_button = tk.Button(
            self.root,
            text="Start Game",
            font=("Arial", 16),
            width=15,
            command=self.show_category_screen
        )
        start_button.pack(pady=20)

    # ---------- Category Selection ---------- #
    def show_category_screen(self):
        self.clear_window()

        label = tk.Label(self.root, text="Select Trivia Category", font=("Arial", 16))
        label.pack(pady=20)

        for category in TRIVIA_QUESTIONS.keys():
            btn = tk.Button(
                self.root,
                text=category,
                font=("Arial", 14),
                width=20,
                command=lambda c=category: self.show_questions(c)
            )
            btn.pack(pady=5)

    # ---------- Question Screen ---------- #
    def show_questions(self, category):
        self.clear_window()
        self.entries = []
        self.correct_answers = []

        questions = [TRIVIA_QUESTIONS[category][i]["question"] for i in range(1, 6)]
        for i in range(1, 6):
            ans = TRIVIA_QUESTIONS[category][i]["answer"]
            # Normalize answers to lowercase
            if isinstance(ans, list):
                self.correct_answers.append([a.lower() for a in ans])
            else:
                self.correct_answers.append(ans.lower())

        title_label = tk.Label(self.root, text=f"{category} Trivia", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        for i, question_text in enumerate(questions):
            row = tk.Frame(frame)
            row.pack(pady=5, anchor="w")

            label = tk.Label(row, text=f"{i+1}. {question_text}", wraplength=500, justify="left")
            label.pack(side="left")

            entry = tk.Entry(row, width=25)
            entry.pack(side="left", padx=10)
            self.entries.append(entry)

        submit_btn = tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.check_answers)
        submit_btn.pack(pady=20)

    # ---------- Check Answers ---------- #
    def check_answers(self):
        score = 0
        for i, entry in enumerate(self.entries):
            user_answer = entry.get().strip().lower()
            correct = self.correct_answers[i]

            if isinstance(correct, list):
                is_correct = user_answer in correct
            else:
                is_correct = user_answer == correct

            entry.config(bg="green" if is_correct else "red")
            if is_correct:
                score += 1

        messagebox.showinfo("Score", f"You scored {score}/{len(self.entries)}!")

    # ---------- Utility ---------- #
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ------------------- RUN APP ------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop()
