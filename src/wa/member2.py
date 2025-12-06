import tkinter as tk
import random
from tkinter import messagebox
from trivia_questions import TRIVIA_QUESTIONS

class TriviaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Trivia Game")
        self.root.geometry("900x450")

        self.category = None
        self.questions = []
        self.answers = []
        self.correct_display = []
        self.current_index = 0
        self.score = 0
        self.results = []

        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.clear_window()
        title_label = tk.Label(self.root, text="Welcome to Sports Trivia!", font=("Arial", 20, "bold"))
        title_label.pack(pady=30)

        start_btn = tk.Button(self.root, text="Start Game", font=("Arial", 16), command=self.show_category_screen)
        start_btn.pack(pady=20)

    def show_category_screen(self):
        self.clear_window()
        label = tk.Label(self.root, text="Select Trivia Category", font=("Arial", 16))
        label.pack(pady=20)

        for category in TRIVIA_QUESTIONS.keys():
            btn = tk.Button(self.root, text=category, font=("Arial", 14), width=20,
                            command=lambda c=category: self.start_category(c))
            btn.pack(pady=5)

    def start_category(self, category):
        self.category = category

        self.questions = []
        self.answers = []
        self.correct_display = []
        self.results = []
        self.current_index = 0
        self.score = 0

        qa_pairs = []
        for i in range (1, 6):
            q = TRIVIA_QUESTIONS[category][i]["question"]
            ans = TRIVIA_QUESTIONS[category][i]["answer"]

            if isinstance(ans, dict):
                display_answer = ans["display"]
                normalized = [a.lower() for a in ans["accepted"]]

            elif isinstance(ans, list):
                display_answer = ans[0]
                normalized = [a.lower() for a in ans]
            else:
                display_answer = ans
                normalized = ans.lower()

            qa_pairs.append((q, normalized, display_answer))

        random.shuffle(qa_pairs)

        self.questions = [q for (q, norm, disp) in qa_pairs]
        self.answers = [norm for (q, norm, disp) in qa_pairs]
        self.correct_display = [disp for (q, norm, disp) in qa_pairs]

        self.show_question()

    def show_question(self):
        self.clear_window()
        if self.current_index >= len(self.questions):
            self.show_summary_screen()
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

    def check_answer(self):
        user = self.entry.get().strip()
        user_answer = user.lower()

        correct = self.answers[self.current_index]
        display_correct = self.correct_display[self.current_index]

        if isinstance(correct, list):
            is_correct = user_answer in correct
        else:
            is_correct = user_answer == correct

        if is_correct:
            self.entry.config(bg="green")
            self.correct_label.config(text="")
            self.score += 1
        else:
            self.entry.config(bg="red")
            self.correct_label.config(text=f"Correct Answer: {display_correct}")

        self.results.append({
            "question": self.questions[self.current_index],
            "user_answer": user if user else "(blank)",
            "correct_answer": display_correct,
            "is_correct": is_correct
        })

        self.root.after(1500, self.next_question)


    def next_question(self):
        self.current_index += 1
        self.show_question()

    def show_summary_screen(self):
        self.clear_window()

        title = tk.Label(self.root, text="Game Over!", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        score_label = tk.Label(
            self.root,
            text=f"Your score: {self.score}/{len(self.questions)}",
            font=("Arial", 14)
        )
        score_label.pack(pady=5)

        summary_frame = tk.Frame(self.root)
        summary_frame.pack(pady=10, fill="both", expand=True)

        headers = ["Q#", "Question", "Your Answer", "Correct Answer", "Result"]
        widths = [5, 50, 20, 30, 10]

        for col, (header, width) in enumerate(zip(headers, widths)):
            tk.Label(
                summary_frame,
                text=header,
                font=("Arial", 12, "bold"),
                borderwidth=1,
                relief="solid",
                width=width,
                wraplength=300
            ).grid(row=0, column=col, padx=1, pady=1)

        # Table rows
        for idx, res in enumerate(self.results, start=1):
            question = res["question"]
            user_ans = res["user_answer"]
            correct_ans = res["correct_answer"]
            result_text = "Correct" if res["is_correct"] else "Incorrect"
            color = "green" if res["is_correct"] else "red"

            row_data = [
                str(idx),
                question,
                user_ans,
                correct_ans if not res["is_correct"] else "",
                result_text
            ]

            for col, value in enumerate(row_data):
                tk.Label(
                    summary_frame,
                    text=value,
                    font=("Arial", 11),
                    fg=color if col == 4 else "black",
                    borderwidth=1,
                    relief="solid",
                    width=widths[col],
                    wraplength=300,
                    justify="center"
                ).grid(row=idx, column=col, padx=1, pady=1)

        back_btn = tk.Button(
            self.root,
            text="Back to Categories",
            font=("Arial", 14),
            command=self.show_category_screen
        )
        back_btn.pack(pady=15)


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop()