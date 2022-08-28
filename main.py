from tkinter import *
from words import WORDS
from datetime import datetime
from datetime import timedelta


word_index = 0
user_index = 0
wpm = 0
high_wpm = 0


def update_display():
    global word_
    global word_index
    global user_index
    word_.destroy()
    word_index = 0
    for row_ in range(5):
        for column_ in range(8):
            word_ = Label(w_frame, text=WORDS[word_index], font=('', 16, 'bold'))
            word_.grid(column=column_, row=row_)
            if word_index == user_index:
                word_.config(bg='grey')
            word_index += 1


def start_clicked():
    global word_index
    global user_index
    global wpm
    global typed_wrong
    word_index = 0
    user_index = 0
    wpm = 0
    typed_wrong = 0
    update_display()
    type_area.bind('<Return>', enter_pressed)
    type_area.config(state=NORMAL)
    type_area.delete(0, END)
    type_area.focus_set()
    count_down()


def count_down():
    now = datetime.now()
    future = now + timedelta(seconds=61)
    remaining_secs = future - datetime.now()
    while remaining_secs.seconds > 0:
        remaining_secs = future - datetime.now()
        global secs
        secs.set(str(remaining_secs.seconds))

        root.update()

    # Disable typing and key bind
    type_area.config(state=DISABLED)
    type_area.bind('<Return>', lambda x: None)

    # Update stats in Entries
    # Update best score WPM
    global your_best_entry
    global wpm
    global error_entry
    global high_wpm
    if wpm > high_wpm:
        high_wpm = wpm
        your_best_entry.config(state=NORMAL)
        your_best_entry.delete(0, END)
        your_best_entry.insert(0, str(high_wpm))
        your_best_entry.config(state=DISABLED)

    # Update number of errors
    global typed_wrong
    error_entry.config(state=NORMAL)
    error_entry.delete(0, END)
    error_entry.insert(0, str(typed_wrong))
    error_entry.config(state=DISABLED)

    # Update WPM
    global wpm_entry
    wpm_entry.config(state=NORMAL)
    wpm_entry.delete(0, END)
    wpm_entry.insert(0, str(wpm))
    wpm_entry.config(state=DISABLED)


def enter_pressed(e):
    global typed_word
    global user_index
    global wpm
    global typed_wrong

    # print(type(typed_word.get()))
    if typed_word.get().strip() == WORDS[user_index]:
        # print(f"user_index: {user_index}")
        wpm += 1
        # print(f"WPM: {wpm}")
    else:
        # print(f"user_index: {user_index}")
        wpm += 1
        typed_wrong += 1
        # print(f"WPM: {wpm}")
        # print(f"errors: {typed_wrong}")

    user_index += 1
    type_area.delete(0, END)
    update_display()


def create_window():
    # Create Window
    global root
    root = Tk()
    root.title("Typing Test")
    root.geometry("900x700")

    # Your best score
    global your_best_entry
    your_best = Label(root)
    your_best.pack()
    your_best_label = Label(your_best, text='Your Best: ')
    your_best_label.grid(column=0, row=0)
    your_best_entry = Entry(your_best, width=5, state=DISABLED)
    your_best_entry.grid(column=1, row=0)

    # typed wrong
    global error_entry
    word_error = Label(root)
    word_error.pack()
    error_label = Label(word_error, text='Typed Wrong: ')
    error_label.grid(column=0, row=0)
    error_entry = Entry(word_error, width=5, state=DISABLED)
    error_entry.grid(column=1, row=0)


    # Word per min (WPM)
    global wpm_entry
    wpm = Label(root)
    wpm.pack()
    wpm_label = Label(wpm, text='WPM: ')
    wpm_label.grid(column=0, row=0)
    wpm_entry = Entry(wpm, width=5, state=DISABLED)
    wpm_entry.grid(column=1, row=0)

    # Time left
    global t_left_entry
    t_left = Label(root)
    t_left.pack()
    t_left_label = Label(t_left, text='Time Left: ')
    t_left_label.grid(column=0, row=0)

    global secs
    secs = StringVar()
    t_left_entry = Entry(t_left, width=5, textvariable=secs)
    # t_left_entry.insert(0, str(START_TIME))
    secs.set('60')
    t_left_entry.config(state=DISABLED)
    t_left_entry.grid(column=1, row=0)

    # display words
    global w_frame
    w_frame = LabelFrame(root, width=800, height=400, bd=2)
    w_frame.pack(padx=10, pady=10)
    # initial 40 words displayed
    global word_index
    global user_index
    global word_
    word_index = 0
    user_index = 0
    for row_ in range(5):
        for column_ in range(8):
            word_ = Label(w_frame, text=WORDS[word_index], font=('', 16, 'bold'))
            word_.grid(column=column_, row=row_)
            if word_index == user_index:
                word_.config(bg='grey')
            word_index += 1

    # start button
    start = Button(root, text='Start', command=start_clicked)
    start.pack()

    # User typing area
    global type_area
    global typed_word
    typed_word = StringVar()
    type_area = Entry(root, width=25, font=('Arial', 13, 'bold'), textvariable=typed_word)
    type_area.config(state=DISABLED)
    type_area.pack(padx=5, pady=5)
    type_area.bind('<Return>', enter_pressed)

    root.mainloop()


def run():
    create_window()


if __name__ == "__main__":
    run()
