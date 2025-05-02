import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
# List to store feedbacks (optional)
feedback_storage = []

# --- Functions ---
def display_message(sender, message):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"{sender}: {message}\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def bot_typing(message):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "Bot: ")
    for char in message:
        chat_display.insert(tk.END, char)
        chat_display.update()
        time.sleep(0.03)
    chat_display.insert(tk.END, "\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def handle_rating(rating):
    display_message("You", f"My rating: {rating}")
    threading.Thread(target=bot_typing, args=(f"Thanks for rating us {rating} star(s)! ⭐",)).start()
    feedback_storage.append({"rating": rating})

def analyze_comment(comment):
    comment = comment.lower()
    negative_keywords = ["bad", "poor", "slow", "hate", "worst", "delay", "broken", "buggy", "terrible"]
    positive_keywords = ["good", "great", "awesome", "excellent", "love", "fast", "smooth", "amazing", "perfect"]

    positive_responses = [
        "Yay! We're glad you loved it! Thanks for your kind words! 💖",
        "That's awesome to hear! We're thrilled to know you liked it! 🎉",
        "Thank you so much! Your positive feedback means a lot. 🙏",
        "We appreciate your love and support! 😊",
        "Your feedback made our day! 💫"
    ]

    negative_responses = [
        "We're sorry to hear that. We'll work on improving the quality of our product. 🛠️",
        "Thank you for your honesty — we’re always looking to improve. 🙇",
        "We apologize for the inconvenience. Our team will look into it. ⚙️",
        "Noted! We'll make sure to fix that. Thanks for telling us. 🔧",
        "We're sorry it didn't meet your expectations. We'll do better! 📉"
    ]

    if any(word in comment for word in negative_keywords):
        return random.choice(negative_responses)
    elif any(word in comment for word in positive_keywords):
        return random.choice(positive_responses)
    else:
        return "Thanks for your feedback! We'll use it to improve your experience. 😊"


def submit_comment():
    comment = comment_input.get().strip()
    if comment:
        display_message("You", comment)
        response = analyze_comment(comment)
        feedback_storage.append({"comment": comment})
        bot_typing(response)
        comment_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Comment", "Please type something before submitting.")

def start_feedback():
    bot_typing("Hi there! We'd love your feedback. How would you rate your experience?.")
    bot_typing("Click a rating below (1 - Worst, 5 - Best), and feel free to write a comment anytime!")

# --- GUI Setup ---
root = tk.Tk()
root.title("FeedbackBot")
root.geometry("500x580")
root.configure(bg="#E8F0FE")

title = tk.Label(root, text="💬 FeedbackBot – Your Opinion Matters!", font=("Helvetica", 16, "bold"), bg="#E8F0FE")
title.pack(pady=10)

# Chat Display
chat_display = tk.Text(root, width=60, height=20, font=("Consolas", 11), state=tk.DISABLED, wrap=tk.WORD, bg="white")
chat_display.pack(padx=10, pady=5)

# Rating Buttons
rating_frame = tk.Frame(root, bg="#E8F0FE")
rating_frame.pack(pady=5)

rating_label = tk.Label(rating_frame, text="Rate us:", font=("Arial", 12), bg="#E8F0FE")
rating_label.pack(side=tk.LEFT)

for i in range(1, 6):
    btn = tk.Button(rating_frame, text=str(i), width=3, bg="#AED6F1", font=("Arial", 11),
                    command=lambda rating=i: handle_rating(rating))
    btn.pack(side=tk.LEFT, padx=4)

# Comment Box
comment_label = tk.Label(root, text="Any comments?", font=("Arial", 12), bg="#E8F0FE")
comment_label.pack(pady=(15, 5))

comment_input = tk.Entry(root, width=40, font=("Arial", 12))
comment_input.pack()

submit_btn = tk.Button(root, text="Submit Comment", command=submit_comment, bg="#D6EAF8", font=("Arial", 12))
submit_btn.pack(pady=10)

# Auto-start the feedback conversation
root.after(1000, start_feedback)

root.mainloop()
