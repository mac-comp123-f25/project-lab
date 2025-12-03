import tkinter as tk
from tkinter import messagebox
from trivia_questions import TRIVIA_QUESTIONS

class TriviaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Trivia Game")
        self.root.geometry("600x300")

        self.category = None
        self.questions = []
        self.answers = []
        self.current_index = 0
        self.score = 0

        self.show_welcome_screen()

    # ---------- Welcome Screen ---------- #
    def show_welcome_screen(self):
        self.clear_window()
        title_label = tk.Label(self.root, text="Welcome to Sports Trivia!", font=("Arial", 20, "bold"))
        title_label.pack(pady=30)

        start_btn = tk.Button(self.root, text="Start Game", font=("Arial", 16), command=self.show_category_screen)
        start_btn.pack(pady=20)

    # ---------- Category Selection ---------- #
    def show_category_screen(self):
        self.clear_window()
        label = tk.Label(self.root, text="Select Trivia Category", font=("Arial", 16))
        label.pack(pady=20)

        for category in TRIVIA_QUESTIONS.keys():
            btn = tk.Button(self.root, text=category, font=("Arial", 14), width=20,
                            command=lambda c=category: self.start_category(c))
            btn.pack(pady=5)

    # ---------- Start Selected Category ---------- #
    def start_category(self, category):
        self.category = category
        self.questions = [TRIVIA_QUESTIONS[category][i]["question"] for i in range(1, 6)]
        self.answers = []
        for i in range(1, 6):
            ans = TRIVIA_QUESTIONS[category][i]["answer"]
            if isinstance(ans, list):
                self.answers.append([a.lower() for a in ans])
            else:
                self.answers.append(ans.lower())
        self.current_index = 0
        self.score = 0
        self.show_question()

    # ---------- Show One Question ---------- #
    def show_question(self):
        self.clear_window()
        if self.current_index >= len(self.questions):
            messagebox.showinfo("Game Over", f"Your score: {self.score}/{len(self.questions)}")
            self.show_category_screen()
            return

        question_text = self.questions[self.current_index]

        self.label = tk.Label(self.root, text=f"Q{self.current_index + 1}: {question_text}", wraplength=500, font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root, width=30, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.focus()

        self.correct_label = tk.Label(self.root, text="", font=("Arial", 12), fg="green")
        self.correct_label.pack(pady=5)

        submit_btn = tk.Button(self.root, text="Submit Answer", font=("Arial", 14), command=self.check_answer)
        submit_btn.pack(pady=10)

    # ---------- Check Answer and Move Next ---------- #
    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        correct = self.answers[self.current_index]

        if isinstance(correct, list):
            is_correct = user_answer in correct
            correct_text = ", ".join(correct)
        else:
            is_correct = user_answer == correct
            correct_text = correct

        if is_correct:
            self.entry.config(bg="green")
            self.correct_label.config(text="")  # No label if correct
            self.score += 1
        else:
            self.entry.config(bg="red")
            self.correct_label.config(text=f"Correct Answer: {correct_text}")  # SHOW correct answer

        # Wait a short moment then move to next question
        self.root.after(1500, self.next_question)

    def next_question(self):
        self.current_index += 1
        self.show_question()

    # ---------- Utility ---------- #
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ------------------- RUN APP ------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop()
