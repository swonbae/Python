from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title('Canada Province Flashcard Quiz App')
root.iconbitmap(r'')
root.geometry('500x650')

# Create a list of state names
PROVINCES = [
    'Alberta',
    'British Columbia',
    'Manitoba',
    'New Brunswick',
    'Newfoundland and Labrador',
    'Northwest Territories',
    'Nova Scotia',
    'Nunavut',
    'Ontario',
    'Prince Edward Island',
    'Quebec',
    'Saskatchewan',
    'Yukon',
]

# create randomizing state function
def randomState():
    # Generate a random number
    global rand_num
    rand_num = randint(0, len(PROVINCES)-1)
    state_filename = 'Images/States/' + PROVINCES[rand_num] + '.png'

    # Create our state images
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(state_filename))
    show_state.config(image = state_img, bg = 'white')

# Return lower no-space string
def trimString(string):
    return string.lower().strip().replace(" ", "")

# Create answer function
def stateAnswer():
    # answer = answer_input.get().title()
    # answer = answer_input.get().lower()
    # answer = answer.replace(" ", "")
    answer = trimString(answer_input.get())
    # answer_label.config(text = answer)

    # Determine if the answer is right or wrong
    if answer == trimString(PROVINCES[rand_num]):
        response = 'Correct! ' + PROVINCES[rand_num]
        # return True
    else:
        response = 'Incorrect! ' + PROVINCES[rand_num]
        # return False

    answer_label.config(text = response)

    # Clear the entry box
    answer_input.delete(0, END)
    
    randomState()

# Create State Flashcard Function
def states():
    # Hide previous frames
    hideAllFrames()

    state_frame.pack(fill = BOTH, expand = 1)

    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady = 15)

    randomState()

    # Create answer input box
    global answer_input
    answer_input = Entry(state_frame, font = ('Helvetica', 18), bd = 2)
    answer_input.pack(pady = 15)

    # Create button to randomize state images
    rand_button = Button(state_frame, text = 'Pass', command = states)
    rand_button.pack(pady = 5)

    # Create button to answer the question
    answer_button = Button(state_frame, text = 'Answer', command = stateAnswer)
    answer_button.pack(pady = 5)

    # Create a label to tell us if we got the answer right or not
    global answer_label
    answer_label = Label(state_frame, text = '', font = ('Helvetica', 18), bg = 'white')
    answer_label.pack(pady = 15)

# Create State Capital Flashcard Function
def stateCapitals():
    # Hide previous frames
    hideAllFrames()

    state_capitals_frame.pack(fill = BOTH, expand = 1)
    label = Label(state_capitals_frame, text = 'Capitals').pack()

# Hide all previous frames
def hideAllFrames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()
    state_capitals_frame.pack_forget()

# Create our menu
menuBar = Menu(root)
root.config(menu = menuBar)

# Create Geography menu items
states_menu = Menu(menuBar)
menuBar.add_cascade(label = 'Geography', menu = states_menu)
states_menu.add_command(label = 'States', command = states)
states_menu.add_command(label = 'State Capitals', command = stateCapitals)
states_menu.add_separator()
states_menu.add_command(label = 'Exit', command = root.quit)

# Create our Frames
state_frame = Frame(root, width = 500, height = 500, bg = 'white')
state_capitals_frame = Frame(root, width = 500, height = 500)

root.mainloop()