# passmaker gui
from tkinter import *
from turtle import width
from generator import Generator as gen
# from pil import ..........

class Page:
    def __init__(self) -> None:
        # colors
        self.gray = "#333333"
        self.text_color = "#999999"
        self.button_color = "#8b8878"

        # main page
        self.page = Tk() #main page
        self.page.geometry("600x500") #set the page size
        self.page.resizable(False,False) #disable resizing
        self.page.attributes("-alpha", 0.93) #a better background
        self.page.title("Passmaker") # set the page name
        self.page.configure(bg=self.gray)

    def strong_pass (self): # generating strong password by generator.py
        passw = gen.generate_hard() 
        self.pass_show.configure(text=passw)

    def medium_pass_m (self): # generating medium quality password by generator.py
        passw = gen.generate_medium()
        self.pass_show.configure(text=passw)

    def weak_pass_m (self): # generating weak password by generator.py
        passw= gen.generate_weak()
        self.pass_show.configure(text=passw)

    def dashboard (self):
        self.name_tag = Label(self.page, font=("bold" , 18) , text="🔒maker" , bg=self.gray , fg=self.text_color).place(x=10 , y=8)
        self.pass_show  = Label(self.page, font=("italich", 20) , text="password" , bg="#a9a9a9" , width=30)
        self.pass_show.place(x=56 , y=60)

        # buttons
        self.strong_pass = Button(self.page , bg=self.button_color , text="💪Strong Password💪" , font=("italich" , 15) , width=30 , command=self.strong_pass).place(x=127 , y=170)
        self.medium_pass = Button(self.page , bg=self.button_color , text="🟡Medium Password🟡" , font=("italich" , 15) , width=30 , command=self.medium_pass_m).place(x=127 , y=250)
        self.weak_pass = Button(self.page , bg=self.button_color , text="📉Weak Password📉" , font=("italich" , 15) , width=30 , command=self.weak_pass_m).place(x=127 , y=320)

    def run (self): # for runnnig the gui
        self.dashboard()
        self.page.mainloop()

# running
page=Page()
page.run()