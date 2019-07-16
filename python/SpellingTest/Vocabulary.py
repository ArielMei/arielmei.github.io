import tkinter as tk
from tkinter import font
import pygame

import glob
import os

from random import shuffle

import numpy as np
import pandas as pd
#------------------------------------------------
""" check """
def check():
    global current_question
    global entry_time
    entry_time += 1
    data = answer_Box.get()
    
    corrt_answer = listing[current_question][:-4]
    ind_word = "'" + corrt_answer + "'"
    if corrt_answer == data:
        current_question += 1
        if current_question < len(listing):
            string_to_display="Correct. \n  "
        else:
            string_to_display="Correct. \n The End!"
    else:
        string_to_display="Incorrect. \n It is \n Please Retry! "

    label_answer0['text'] = string_to_display
    label_answer['text'] = corrt_answer
    label_definition['text'] = df.at[corrt_answer,'definition']
    label_example['text'] = df.at[corrt_answer,'example']
    score['text'] = "Total question: %d \n Correct answer: %d \n Try time: %d \n Youre socer is: %d" \
                    %(len(listing),current_question,entry_time,current_question/entry_time * 100)
    answer_Box.delete(0, 'end')

"""Play audio"""
def play(file):
    global locate_path
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(locate_path,file))
    pygame.mixer.music.play()

""" Get word list in path """
def word_list(path):
    List = []
    print("path lenght",len(path))
    for name in glob.glob(os.path.join(path,'*.mp3')):
        List.append(name[len(path):])
    return List
#------------------------------------------------
foldernames = os.listdir('mp3Data')
foldernames.remove(".DS_Store")
print("Exsiting folders are:")
print(foldernames)

folder_name = input("Please choose folder: ")

locate_path = 'mp3Data/' + folder_name +'/'
listing = word_list(locate_path)
shuffle(listing)       # shuffle the word list

current_question = 0   # create global variable
entry_time = 0
#------------------------------------------------
df = pd.read_excel(locate_path + folder_name + '.xlsx')
df = df.set_index('words')
#------------------------------------------------

HEIGHT = 600
WIDTH = 1000

root = tk.Tk()
root.title("Spell Test")

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='spelling.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

#""" Folder Choose window """
#top_frame = tk.Frame(root,bg='#3399ff',bd=5)
#top_frame.place(relx=0.5,rely=0.01,relwidth=0.75,relheight=0.15,anchor='n')
#
#folder_list = tk.Label(top_frame,font=('Courier',15),fg='blue',anchor='nw',justify='left',bd=4)
#folder_list.place(relwidth=0.6,relheight=1)
#folder_list['text'] = "Choose Foder list below: \n Grade1"
#
#folder_Box = tk.Entry(top_frame,font=('Courier',18))
#folder_Box.place(relx=0.65,relwidth=0.33,relheight=0.5)
#
#get_folderBtn = tk.Button(top_frame, text="Choose",font=('Courier',18),command=lambda:print(folder_Box.get()))
#get_folderBtn.place(relx=0.65,rely=0.5,relwidth=0.33,relheight=0.5)

#----------------------------------------------------
""" Main window """
frame = tk.Frame(root,bg='#3399ff',bd=5)
frame.place(relx=0.5,rely=0.04,relwidth=0.75,relheight=0.1,anchor='n')

button1 = tk.Button(frame, text="Play",font=('Courier',18),command=lambda:play(listing[current_question]))
button1.place(relwidth=0.2,relheight =1)

answer_Box = tk.Entry(frame,font=('Courier',18))
answer_Box.place(relx=0.25,relwidth=0.5,relheight=1)

button2 = tk.Button(frame, text="Submit",font=('Courier',18),command=lambda:check())
button2.place(relx=0.8,relwidth=0.2,relheight =1)

""" Interactive window """
lower_frame = tk.Frame(root,bg='#3399ff',bd=10)
lower_frame.place(relx=0.5, rely=0.18,relwidth=0.75,relheight=0.5, anchor='n')

label_answer0 = tk.Label(lower_frame,font=('Courier',30),fg='red',anchor='nw',justify='left',bd=4)
label_answer0.place(relwidth=1,relheight=0.2)

label_answer = tk.Label(lower_frame,font=('Courier',30),fg='red',anchor='nw',justify='left',bd=4)
label_answer.place(rely=0.2,relwidth=1,relheight=0.2)

label_definition0 = tk.Label(lower_frame,font=('Courier',20),fg='blue',anchor='nw',justify='left',bd=4,text= 'Definition:')
label_definition0.place(rely=0.4, relwidth=1,relheight=0.15)

label_definition = tk.Label(lower_frame,font=('Courier',15),anchor='nw',justify='left',bd=4)
label_definition.place(rely=0.55, relwidth=1,relheight=0.15)

label_example0 = tk.Label(lower_frame,font=('Courier',20),fg='blue',anchor='nw',justify='left',bd=4,text= 'Example:')
label_example0.place(rely=0.7, relwidth=1,relheight=0.15)


label_example = tk.Label(lower_frame,font=('Courier',15),anchor='nw',justify='left',bd=4)
label_example.place(rely=0.85, relwidth=1,relheight=0.15)

""" Score """
score_frame = tk.Frame(root,bg='#3399ff',bd=5)
score_frame.place(relx=0.5, rely=0.73,relwidth=0.75,relheight=0.2, anchor='n')

score = tk.Label(score_frame,font=('Courier',15),fg='blue',anchor='nw',justify='left',bd=4)
score.place(relwidth=1,relheight=1)


root.mainloop()







