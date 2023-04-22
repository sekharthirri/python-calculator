from tkinter import *

mw = Tk()
mw.title ('Calculator')




def clear():
    db.delete(0, END)

def btn_clk(num): 
    cur_num =db.get()
    clear()
    f_num = cur_num + num
    db.insert(0,f_num)



Frist_num = 0

def calc(math_type):
    global Frist_num , math
    math = math_type
    Frist_num = db.get()
    clear()
    
    
def eqaul():
    result = ''
    global Frist_num
    second_Num  = db.get()
    clear()
    if math == 'add':
        result = int(Frist_num) + int(second_Num)  
    elif math == 'sub':
        result = int(Frist_num) - int(second_Num)  
    elif math == 'mul':
        result = int(Frist_num) * int(second_Num)  
    elif math == 'div':
        result = int(Frist_num) / int(second_Num)  
    db.insert(0 , str(result))  





# Creating Widgets
db = Entry(mw,font=('Arial',28),width=14,justify=RIGHT)

btn_0 = Button(text='0',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('0'))
btn_1 = Button(text='1',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('1'))
btn_2 = Button(text='2',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('2'))
btn_3 = Button(text='3',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('3'))
btn_4 = Button(text='4',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('4'))
btn_5 = Button(text='5',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('5'))
btn_6 = Button(text='6',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('6'))
btn_7 = Button(text='7',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('7'))
btn_8 = Button(text='8',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('8'))
btn_9 = Button(text='9',padx=36,pady=10,font=('Arial',14) , command=lambda:btn_clk('9'))


btn_Clear = Button(text='clear',padx=74,pady=10,font=('Arial',14), command=clear)

btn_Div = Button(text='/',padx=38,pady=10,font=('Arial',14),command=lambda:calc('div'))
btn_mul = Button(text='*',padx=38,pady=10,font=('Arial',14),command=lambda:calc('mul'))
btn_sub = Button(text='-',padx=38,pady=10,font=('Arial',14),command=lambda:calc('sub'))
btn_add = Button(text='+',padx=36,pady=10,font=('Arial',14),command=lambda:calc('add'))
btn_equal = Button(text='=',padx=38,pady=40,font=('Arial',14),command=eqaul)


# Displaying widgets 

btn_equal.grid(row=5,rowspan=2, column=2,padx=2,pady=2)

btn_Div.grid(row=5,column=0,padx=2,pady=2)
btn_mul.grid(row=5,column=1,padx=2,pady=2)
btn_sub.grid(row=6,column=0,padx=2,pady=2)
btn_add.grid(row=6,column=1,padx=2,pady=2)



btn_Clear.grid(row=4,column=1, columnspan=2, padx=2,pady=2)


btn_0.grid(row=4,column=0,padx=2,pady=2)

btn_1.grid(row=3,column=0,padx=2,pady=2)
btn_2.grid(row=3,column=1,padx=2,pady=2)
btn_3.grid(row=3,column=2,padx=2,pady=2)

btn_4.grid(row=2,column=0,padx=2,pady=2)
btn_5.grid(row=2,column=1,padx=2,pady=2)
btn_6.grid(row=2,column=2,padx=2,pady=2)

btn_7.grid(row=1,column=0,padx=2,pady=2)
btn_8.grid(row=1,column=1,padx=2,pady=2)
btn_9.grid(row=1,column=2,padx=2,pady=2)

db.grid(row=0,column=0, columnspan=3, padx=10,pady=10)


mw.mainloop()
