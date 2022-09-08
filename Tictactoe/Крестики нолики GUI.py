from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import random
from time import sleep

def g1():
    grid[0][0] = stat
    b1.configure(text='X')
    print('DONE')
def g2():
    grid[0][1] = stat
def g3():
    grid[0][2] = stat
def g4():
    grid[1][0] = stat
def g5():
    grid[1][1] = stat
def g6():
    grid[1][2] = stat
def g7():
    grid[2][0] = stat
def g8():
    grid[2][1] = stat
def g9():
    grid[2][2] = stat

def start():
    global first
    global second
    btn.destroy()
    tag.destroy()
    lbl.configure(text='ВЫБОР РЕЖИМА', font = ("Arial Bold", 30))
    lbl.grid(column=0, row=0, columnspan=2)
    first = Button(window, text="1 игрок", width = 12, height = 1, bg = '#390879', fg = '#b8df10', font = ('Arial Bold', 25), command=p1)
    first.grid(column=0, row=1)
    second = Button(window, text="2 игрока", width = 12, height = 1, bg = '#390879', fg = '#b8df10', font = ('Arial Bold', 25), command=p2)
    second.grid(column=1, row=1)

def p1():
    messagebox.showwarning('ВНИМАНИЕ', 'Приношу извинения, пока не работает')
    
def p2():
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    first.destroy()
    second.destroy()
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    lbl.grid(column=0, row=0, columnspan=3)
    b1 = Button(window, width=20, height=7, command=g1)
    b2 = Button(window, width=20, height=7, command=g2)
    b3 = Button(window, width=20, height=7, command=g3)
    b4 = Button(window, width=20, height=7, command=g4)
    b5 = Button(window, width=20, height=7, command=g5)
    b6 = Button(window, width=20, height=7, command=g6)
    b7 = Button(window, width=20, height=7, command=g7)
    b8 = Button(window, width=20, height=7, command=g8)
    b9 = Button(window, width=20, height=7, command=g9)
    b1.grid(column=0, row=1)
    b2.grid(column=1, row=1)
    b3.grid(column=2, row=1)
    b4.grid(column=0, row=2)
    b5.grid(column=1, row=2)
    b6.grid(column=2, row=2)
    b7.grid(column=0, row=3)
    b8.grid(column=1, row=3)
    b9.grid(column=2, row=3)
#-------------------BACKEND---------------------
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
stat = 1
hods = set()
n = 9
win = False



#-------------------GUI-------------------------
window = Tk()  
window.title("Крестики-нолики")
# window.resizable(0,0)
lbl = Label(window, text="Крестики-Нолики",fg = 'navy', font = ("Arial Bold", 33))  
lbl.grid(column=0, row=0)
btn = Button(window, text="ИГРАТЬ", width = 9, height = 2, bg = '#390879', fg = '#b8df10', font = ("Arial Bold", 50), command=start)  
btn.grid(column=0, row=1)
tag = Label(window, text='Made by Tim#8661')
tag.grid(column=0, row=2)


window.mainloop()
