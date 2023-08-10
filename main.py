# ---------------------------- IMPORTS ------------------------------- #
from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
from tkinter.ttk import Combobox
import ctypes
import math
import winsound
from random import shuffle
import pyautogui

from question_model import Question
from quiz_brain import QuizBrain

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
TEAL = "#2EC4B6"
TIMER = None

winsound.PlaySound("quiz_brain_music.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# ---------------------------- FUNCTIONS ------------------------------- #
def reset_button_images():
    canvas.itemconfig(true_button, image=true_image_unclicked)
    canvas.itemconfig(false_button, image=false_image_unclicked)
    canvas.tag_bind(true_button, "<Button-1>", lambda _: check_answer("True"))
    canvas.tag_bind(false_button, "<Button-1>", lambda _: check_answer("False"))

def show_messagebox(title, message):
    pyautogui.alert(text=message, title=title)

# Function to load questions based on the selected category
def load_questions(category):
    """Loads questions from selected category and shuffles them."""
    
    # Dynamically import question data based on category.
    # Depending on the category chosen, a different module is imported.
    if category == "Python":
        from python_questions import question_data
    elif category == "Movies and TV Shows":
        from movies_and_tv_shows_questions import question_data
    elif category == "History":
        from history_questions import question_data
    elif category == "Geography":
        from geography_questions import question_data
    elif category == "Pop Culture":
        from pop_culture_questions import question_data
    elif category == "Sports":
        from sports_questions import question_data
    elif category == "Science":
        from science_questions import question_data
    elif category == "Math":
        from math_questions import question_data
    # More categories can be added following the same pattern.
    
    # If the category does not match any of the above, return an empty list.
    else:
        return []

    # Shuffle the list of questions to randomize their order.
    shuffle(question_data)
    
    # Convert the list of question dictionaries into a list of Question objects and return this list.
    return [Question(item["question"], item["correct_answer"]) for item in question_data]

def start_game():
    global quiz, true_button, false_button

    # Create the true and false buttons when the game starts
    true_button = canvas.create_image(position_x_true, position_y_true, anchor="center", image=true_image_unclicked)
    false_button = canvas.create_image(position_x_false, position_y_false, anchor="center", image=false_image_unclicked)
    canvas.tag_bind(true_button, "<Button-1>", lambda _: check_answer("True"))
    canvas.tag_bind(false_button, "<Button-1>", lambda _: check_answer("False"))

    selected_category = category_combobox.get()
    question_bank = load_questions(selected_category)

    if not question_bank:
        return

    canvas.itemconfig(score_label, text="Score: 0/0")
    reset_timer()

    quiz = QuizBrain(question_bank)
    quiz.next_question()

    canvas.itemconfig(question_label, text=quiz.current_question.question)

def reset_timer():
    global TIMER
    if TIMER is not None:
        window.after_cancel(TIMER)
    count_down(11)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        end_game_with_sound()

def end_game_with_sound():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("game_over.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    show_messagebox(title="GAME OVER!", message=f"Your score is: {quiz.score}/{quiz.question_number}")
    window.quit()

def display_instructions():
    # Change the image to clicked state
    canvas.itemconfig(instructions_button, image=instructions_image_clicked)
    window.update_idletasks()
    window.after(1000, lambda: canvas.itemconfig(instructions_button, image=instructions_image_unclicked))
    
    instructions = """
    Welcome to the Quiz Brain Game!
    
    In this quiz game, you will be presented with a series of questions from different categories. 
    Your goal is to select the correct answer for each question.
    
    - Use the drop-down menu to choose a category.
    - Read the question and choose either "True" or "False" as your answer.
    - The timer will count down for each question.
    - If you answer a question correctly, your score will increase and the timer will reset.
    - If you answer a question incorrectly, the timer will keep going down!
    - The game ends when you reach 10 correct answers or when you either run out of time, or get 5 wrong answers.
    
    Good luck and have fun!
    """
    messagebox.showinfo(title="Instructions", message=instructions)


def check_answer(user_answer):
    if user_answer == "True":
        canvas.itemconfig(true_button, image=true_image_clicked)
    else:
        canvas.itemconfig(false_button, image=false_image_clicked)

    window.update_idletasks()
    window.after(1000, reset_button_images)

    is_correct = quiz.check_answer(user_answer)

    if is_correct:
        reset_timer()

    if quiz.score == 10:
        show_messagebox(title="Congratulations!", message="Congratulations, you have reached 10 correct answers. YOU WIN!")
        window.quit()
        return

    elif (quiz.question_number - quiz.score) == 5:
        end_game_with_sound()
        return

    feedback = "Correct!" if is_correct else "Wrong!"
    show_messagebox(title="Result", message=feedback)

    canvas.itemconfig(score_label, text=f"Score: {quiz.score}/{quiz.question_number}")

    if quiz.still_has_questions():
        quiz.next_question()
        canvas.itemconfig(question_label, text=quiz.current_question.question)
    else:
        final_score = f"Your final score: {quiz.score}/{quiz.question_number}"
        show_messagebox(title="Quiz Complete", message=final_score)
        window.after_cancel(TIMER)
        window.quit()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Quiz Brain")
window.config(bg=TEAL)

canvas = Canvas(window, width=400, height=800, bg=TEAL)
border_img = PhotoImage(file="trivia_border.png")
canvas.create_image(200, 400, image=border_img)
canvas.grid(column=0, row=2, columnspan=2, rowspan=10)

brain_img = PhotoImage(file="quizbrain_logo.png")
canvas.create_image(200, 200, image=brain_img)
canvas.grid(column=0, row=2)

timer_text = canvas.create_text(200, 81, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
score_label = canvas.create_text(93, 36, text="Score: 0/0", fill="white", font=(FONT_NAME, 18, "bold"))

# ---------------------------- UI COMPONENTS SETUP ------------------------------- #
question_label = canvas.create_text(200, 300, text="", font=(FONT_NAME, 15, "bold"), width=200, anchor="n")

categories = ["Python", "Movies and TV Shows", "History", "Geography", "Pop Culture", "Sports", "Science", "Math"]
category_combobox = Combobox(window, values=categories)
category_combobox.set("Select Category")
category_combobox.grid(column=1, row=2)
category_combobox.bind("<<ComboboxSelected>>", lambda _: start_game())

# Making sure the images are loaded before creating the canvas items
true_image_unclicked = PhotoImage(file="true_unclicked.png")
true_image_clicked = PhotoImage(file="true_clicked.png")
false_image_unclicked = PhotoImage(file="false_unclicked.png")
false_image_clicked = PhotoImage(file="false_clicked.png")

instructions_image_unclicked = PhotoImage(file="instructions_unclicked.png")
instructions_image_clicked = PhotoImage(file="instructions_clicked.png")

position_x_true = 100
position_y_true = 700
position_x_false = 300
position_y_false = 700

# Instructions Button as Canvas Item:
instructions_button_position = (200, 750)  # Adjust position as needed
instructions_button = canvas.create_image(*instructions_button_position, image=instructions_image_unclicked, anchor="center")
canvas.tag_bind(instructions_button, "<Button-1>", lambda _: display_instructions())

window.mainloop()


