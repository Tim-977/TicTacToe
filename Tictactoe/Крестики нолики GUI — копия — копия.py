from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
# from tkinter.ttk import *
import random
from time import sleep

def g1():
    global stat
    b1['state'] = DISABLED
    grid[0][0] = stat
    hod = 1
#     n += 1
    b1.configure(bg = 'red') if stat == 1 else b1.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        return
    if b2["state"] == DISABLED and b3["state"] == DISABLED and\
       b4["state"] == DISABLED  and b5["state"] == DISABLED and\
       b6["state"] == DISABLED  and b7["state"] == DISABLED and\
       b8["state"] == DISABLED  and b9["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    

def g2():
    global stat
    b2['state'] = DISABLED
    grid[0][1] = stat
    hod = 2
    b2.configure(bg = 'red') if stat == 1 else b2.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
    if b1["state"] == DISABLED and b3["state"] == DISABLED and\
       b4["state"] == DISABLED  and b5["state"] == DISABLED and\
       b6["state"] == DISABLED  and b7["state"] == DISABLED and\
       b8["state"] == DISABLED  and b9["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
        b1['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    
def g3():
    global stat
    b3['state'] = DISABLED
    hod = 3
    grid[0][2] = stat
    b3.configure(bg = 'red') if stat == 1 else b3.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
        b2['state'] = DISABLED
        b1['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        return
    if b2["state"] == DISABLED and b1["state"] == DISABLED and\
       b4["state"] == DISABLED  and b5["state"] == DISABLED and\
       b6["state"] == DISABLED  and b7["state"] == DISABLED and\
       b8["state"] == DISABLED  and b9["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    
def g4():
    global stat
    b4['state'] = DISABLED
    hod = 4
    grid[1][0] = stat
    b4.configure(bg = 'red') if stat == 1 else b4.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b1['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        return
    if b2["state"] == DISABLED and b3["state"] == DISABLED and\
       b1["state"] == DISABLED  and b5["state"] == DISABLED and\
       b6["state"] == DISABLED  and b7["state"] == DISABLED and\
       b8["state"] == DISABLED  and b9["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    
def g5():
    global stat
    b5['state'] = DISABLED
    hod = 5
    grid[1][1] = stat
    b5.configure(bg = 'red') if stat == 1 else b5.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b1['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        return
    if b2["state"] == DISABLED and b3["state"] == DISABLED and\
       b4["state"] == DISABLED  and b1["state"] == DISABLED and\
       b6["state"] == DISABLED  and b7["state"] == DISABLED and\
       b8["state"] == DISABLED  and b9["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    
def g6():
    global stat
    b6['state'] = DISABLED
    hod = 6
    grid[1][2] = stat
    b6.configure(bg = 'red') if stat == 1 else b6.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b1['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        return
    if b2["state"] == DISABLED and b3["state"] == DISABLED and\
       b4["state"] == DISABLED  and b5["state"] == DISABLED and\
       b1["state"] == DISABLED  and b7["state"] == DISABLED and\
       b8["state"] == DISABLED  and b9["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    
def g7():
    global stat
    b7['state'] = DISABLED
    hod = 7
    grid[2][0] = stat
    b7.configure(bg = 'red') if stat == 1 else b7.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b1['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        return
    if b2["state"] == DISABLED and b3["state"] == DISABLED and\
       b4["state"] == DISABLED  and b5["state"] == DISABLED and\
       b6["state"] == DISABLED  and b1["state"] == DISABLED and\
       b8["state"] == DISABLED  and b9["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    
def g8():
    global stat
    b8['state'] = DISABLED
    hod = 8
    grid[2][1] = stat
    b8.configure(bg = 'red') if stat == 1 else b8.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b1['state'] = DISABLED
        b9['state'] = DISABLED
        return
    if b2["state"] == DISABLED and b3["state"] == DISABLED and\
       b4["state"] == DISABLED  and b5["state"] == DISABLED and\
       b6["state"] == DISABLED  and b7["state"] == DISABLED and\
       b1["state"] == DISABLED  and b9["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    
def g9():
    global stat
    b9['state'] = DISABLED
    hod = 9
    grid[2][2] = stat
    b9.configure(bg = 'red') if stat == 1 else b9.configure(bg = 'cyan')
    if grid[0][0] == grid[0][1] == grid[0][2] != '-' or grid[1][0] == grid[1][1] == grid[1][2] != '-' or grid[2][0] == grid[2][1] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][0] == grid[2][0] != '-' or grid[0][1] == grid[1][1] == grid[2][1] != '-' or grid[0][2] == grid[1][2] == grid[2][2] != '-' or\
       grid[0][0] == grid[1][1] == grid[2][2] != '-' or grid[0][2] == grid[1][1] == grid[2][0] != '-':
        winstat = True
        if stat == 1:
            lbl.configure(text='ПОБЕДИЛИ КРЕСТИКИ', fg = 'white', bg = 'red', font=('Arial Bold', 27))
        else:
            lbl.configure(text='ПОБЕДИЛИ НОЛИКИ', fg = 'black', bg = 'cyan', font=('Arial Bold', 30))
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b1['state'] = DISABLED
        return
    if b2["state"] == DISABLED and b3["state"] == DISABLED and\
       b4["state"] == DISABLED  and b5["state"] == DISABLED and\
       b6["state"] == DISABLED  and b7["state"] == DISABLED and\
       b8["state"] == DISABLED  and b1["state"] == DISABLED:
        lbl.configure(text='НИЧЬЯ!', fg = 'white', bg = 'Royalblue', width = 18, font=('Arial Bold', 29))
        return
    stat += 1
    stat %= 2
    lbl.configure(text='Ход Крестиков') if stat == 1 else lbl.configure(text='Ход Ноликов')
    

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
#     global n
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global hod
#     global stat
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
#     n = 0
#-------------------BACKEND---------------------
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
global stat
global winstat
# n = 0
stat = 1
hods = set()
win = False



#-------------------GUI-------------------------
window = Tk()  
window.title("Крестики-Нолики")
window.resizable(0,0)
lbl = Label(window, text="Крестики-Нолики",fg = 'navy', font = ("Arial Bold", 33))  
lbl.grid(column=0, row=0)
btn = Button(window, text="ИГРАТЬ", width = 9, height = 2, bg = '#390879', fg = '#b8df10', font = ("Arial Bold", 50), command=start)  
btn.grid(column=0, row=1)
tag = Label(window, text='Made by Tim#8661')
tag.grid(column=0, row=2)

window.mainloop()
