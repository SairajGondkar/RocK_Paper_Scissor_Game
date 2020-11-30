import random
import tkinter as tk
window = tk.Tk()
window.geometry("245x250")
window.configure(bg='purple')
window.title("Rock Paper Scissors Game")
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""
def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def random_computer_choice():
    return random.choice(['rock','paper','scissor'])
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        m = "ITS A TIE"

    elif((user-comp)%3==1):
        m = "WINNER WINNER CHICKEN DINNER"

        USER_SCORE+=1
    else:
        m = "YOU LOST THE GAME"
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#FF99FF",font='Helvetica')
    text_area.grid(column=0,row=4)
    answer = "You Selected : {uc} \nComputer Selected : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)
    text_area.insert(tk.END,answer)
    message = tk.Message(master=window, text=m,bg='pink',font='TimesNewRoman')
    message.grid(column=0, row=4)
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissor'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

button1 = tk.Button(text="       ROCK       ",bg="green",command=rock,height=4,width=50)
button1.grid(column=0,row=1)
button2 = tk.Button(text="       PAPER      ",bg="yellow",command=paper,height=4,width=50)
button2.grid(column=0,row=2)
button3 = tk.Button(text="      SCISSOR     ",bg="orange",command=scissor,height=4,width=50)
button3.grid(column=0,row=3)

window.mainloop()
