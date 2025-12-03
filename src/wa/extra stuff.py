window = tk.Tk()
#welcome_window.title("Welcome to Game On: Sports Trivia Challenge!")
#welcome_window.geometry("450x250")

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

