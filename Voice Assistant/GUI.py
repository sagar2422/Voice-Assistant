from tkinter import *


class Widget:

    def __init__(self):
        root = Tk()

        root.title('Natasha')
        root.geometry('520x320')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Natasha', font=('Railways', 24,
                                                           'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black',
                      fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')

        btn = Button(root, text='Speak', font=('railways', 10, 'bold'), bg='red', fg='white').pack(fill='x',
                                                                                                     expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='yellow', fg='black',
                      command=root.destroy).pack(fill='x', expand='no')
        root.mainloop()


W = Widget()
