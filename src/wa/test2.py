import tkinter as tk
import random
from tkinter import messagebox
from trivia_questions import TRIVIA_QUESTIONS


class TriviaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Trivia Game")
        self.root.geometry("1000x600")
        self.root.configure(bg="#1e1e2f")

        self.category = None
        self.questions = []
        self.answers = []
        self.correct_display = []
        self.current_index = 0
        self.score = 0
        self.results = []

        self.show_welcome_screen()

    # ---------- UI HELPERS ----------
    def card(self):
        frame = tk.Frame(self.root, bg="#2c2c44", padx=40, pady=30)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        return frame

    def big_button(self, parent, text, command):
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Helvetica", 20, "bold"),
            bg="#0057FF",
            fg="white",
            activebackground="#003FCC",
            activeforeground="white",
            relief="solid",
            borderwidth=3,
            highlightthickness=0,
            cursor="hand2",
            padx=40,
            pady=16,
            width=24
        )

    # ---------- SCREENS ----------
    def show_welcome_screen(self):
        self.clear_window()
        frame = self.card()

        title_label = tk.Label(
            frame,
            text="🏆 Welcome to Sports Trivia!",
            font=("Helvetica", 28, "bold"),
            bg="#2c2c44",
            fg="white"
        )
        title_label.pack(pady=20)

        start_btn = self.big_button(frame, "Start Game", self.show_category_screen)
        start_btn.pack(pady=20)

    def show_category_screen(self):
        self.clear_window()
        frame = self.card()

        label = tk.Label(
            frame,
            text="Select Trivia Category",
            font=("Helvetica", 22, "bold"),
            bg="#2c2c44",
            fg="white"
        )
        label.pack(pady=15)

        for category in TRIVIA_QUESTIONS.keys():
            btn = self.big_button(
                frame,
                category,
                lambda c=category: self.start_category(c)
            )
            btn.pack(pady=10)

    def start_category(self, category):
        self.category = category

        self.questions = []
        self.answers = []
        self.correct_display = []
        self.results = []
        self.current_index = 0
        self.score = 0

        qa_pairs = []
        for i in range(1, 6):
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

        frame = self.card()
        question_text = self.questions[self.current_index]

        self.label = tk.Label(
            frame,
            text=f"Q{self.current_index + 1}: {question_text}",
            wraplength=750,
            font=("Helvetica", 18),
            bg="#2c2c44",
            fg="white",
            justify="center"
        )
        self.label.pack(pady=20)

        self.entry = tk.Entry(
            frame,
            width=30,
            font=("Helvetica", 18),
            relief="solid",
            borderwidth=2,
            justify="center",
            bg="black",
            fg="white",
            insertbackground="white"
        )
        self.entry.pack(pady=15)
        self.entry.focus()

        self.correct_label = tk.Label(
            frame,
            text="",
            font=("Helvetica", 14),
            bg="#2c2c44",
            fg="#ff7070"
        )
        self.correct_label.pack(pady=8)

        submit_btn = self.big_button(frame, "Submit Answer", self.check_answer)
        submit_btn.pack(pady=20)

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
            self.entry.config(bg="#7CFC90")
            self.correct_label.config(text="✅ Correct!")
            self.score += 1
        else:
            self.entry.config(bg="#ffb3b3")
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
        frame = self.card()

        title = tk.Label(
            frame,
            text="🎉 Game Over!",
            font=("Helvetica", 26, "bold"),
            bg="#2c2c44",
            fg="white"
        )
        title.pack(pady=10)

        score_label = tk.Label(
            frame,
            text=f"Your score: {self.score}/{len(self.questions)}",
            font=("Helvetica", 16),
            bg="#2c2c44",
            fg="#bbbbbb"
        )
        score_label.pack(pady=5)

        summary_frame = tk.Frame(frame, bg="#2c2c44")
        summary_frame.pack(pady=15, fill="both", expand=True)

        headers = ["Q#", "Question", "Your Answer", "Correct Answer", "Result"]
        widths = [5, 40, 18, 25, 10]

        for col, (header, width) in enumerate(zip(headers, widths)):
            tk.Label(
                summary_frame,
                text=header,
                font=("Helvetica", 12, "bold"),
                bg="#3a3a5c",
                fg="white",
                borderwidth=1,
                relief="solid",
                width=width
            ).grid(row=0, column=col, padx=2, pady=2)

        for idx, res in enumerate(self.results, start=1):
            color = "#7CFC90" if res["is_correct"] else "#ff9999"
            result_text = "Correct" if res["is_correct"] else "Incorrect"

            row_data = [
                str(idx),
                res["question"],
                res["user_answer"],
                "" if res["is_correct"] else res["correct_answer"],
                result_text
            ]

            for col, value in enumerate(row_data):
                tk.Label(
                    summary_frame,
                    text=value,
                    font=("Helvetica", 11),
                    bg="#2c2c44",
                    fg=color if col == 4 else "white",
                    borderwidth=1,
                    relief="solid",
                    width=widths[col],
                    wraplength=300,
                    justify="center"
                ).grid(row=idx, column=col, padx=1, pady=1)

        back_btn = self.big_button(frame, "Back to Categories", self.show_category_screen)
        back_btn.pack(pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop()


