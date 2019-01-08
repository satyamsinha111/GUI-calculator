from tkinter import*


def fun():
	e1['state']='normal'
	e1.insert(END,btn1['text'])
	e1['state']='disabled'
def fun2():
	e1['state'] = 'normal'
	e1.insert(END,btn2['text'])
	e1['state'] = 'disabled'
def fun3():
	e1['state'] = 'normal'
	e1.insert(END,btn3['text'])
	e1['state'] = 'disabled'
def fun4():
	e1['state'] = 'normal'
	e1.insert(END, btn4['text'])
	e1['state'] = 'disabled'
def fun5():
	e1['state'] = 'normal'
	e1.insert(END, btn5['text'])
	e1['state'] = 'disabled'
def fun6():
	e1['state'] = 'normal'
	e1.insert(END, btn6['text'])
	e1['state'] = 'disabled'
def fun7():
	e1['state'] = 'normal'
	e1.insert(END, btn7['text'])
	e1['state'] = 'disabled'
def fun8():
	e1['state'] = 'normal'
	e1.insert(END, btn8['text'])
	e1['state'] = 'disabled'
def fun9():
	e1['state'] = 'normal'
	e1.insert(END, btn9['text'])
	e1['state'] = 'disabled'
def fun0():
	e1['state'] = 'normal'
	e1.insert(END, btn0['text'])
	e1['state'] = 'disabled'
def funadd():
	e1['state'] = 'normal'
	e1.insert(END,add['text'])
	e1['state'] = 'disabled'
def pro():
	e1['state'] = 'normal'
	e1.insert(END,multiply['text'])
	e1['state'] = 'disabled'
def div():
	e1['state'] = 'normal'
	e1.insert(END,Divide['text'])
	e1['state'] = 'disabled'
def sub():
	e1['state'] = 'normal'
	e1.insert(END,subtract['text'])
	e1['state'] = 'disabled'
def clear():
	e1['state'] = 'normal'
	e1.delete(0,END)
	e1['state'] = 'disabled'
def result():
	e1['state'] = 'normal'
	str=e1.get()
	e1.delete(0,END)
	if '+' in str:
		o = str.find('+')
		num1 = str[0:o]
		num2 = str[o + 1:]
		sum=float(num1)+float(num2)
		e1.insert(0,sum)
	elif '-' in str:
		o = str.find('-')
		num1 = str[0:o]
		num2 = str[o + 1:]
		diff = float(num1) - float(num2)
		e1.insert(0, diff)
	elif 'x' in str:
		o = str.find('x')
		num1 = str[0:o]
		num2 = str[o + 1:]
		diff = float(num1) * float(num2)
		e1.insert(0, diff)
	elif '/' in str:
		o = str.find('/')
		num1 = str[0:o]
		num2 = str[o + 1:]
		diff = float(num1) / float(num2)
		e1.insert(0, diff)
	e1['state'] = 'disabled'


window=Tk()
window.config(bg='Black')
window.geometry('10x120')
window.title('My todo list')

frm1=Frame(window,height=50,width=20)
frm1.pack(side=TOP)
e1=Entry(frm1,state='disabled')
e1.grid(row=0,columnspan=4)
btn1 = Button(frm1,text='1',width=3,height=1,command=fun)
btn1.grid(row=1,column=0)
btn2 = Button(frm1,text='2',width=3,height=1,command=fun2)
btn2.grid(row=1,column=1)
btn3 = Button(frm1,text='3',width=3,height=1,command=fun3)
btn3.grid(row=1,column=2)
multiply=Button(frm1,text='x',width=3,height=1,command=pro)
multiply.grid(row=1,column=3)

btn4 = Button(frm1,text='4',width=3,height=1,command=fun4)
btn4.grid(row=2,column=0)
btn5 = Button(frm1,text='5',width=3,height=1,command=fun5)
btn5.grid(row=2,column=1)
btn6 = Button(frm1,text='6',width=3,height=1,command=fun6)
btn6.grid(row=2,column=2)
Divide=Button(frm1,text='/',width=3,height=1,command=div)
Divide.grid(row=2,column=3)

btn7 = Button(frm1,text='7',width=3,height=1,command=fun7)
btn7.grid(row=3,column=0)
btn8 = Button(frm1,text='8',width=3,height=1,command=fun8)
btn8.grid(row=3,column=1)
btn9 = Button(frm1,text='9',width=3,height=1,command=fun9)
btn9.grid(row=3,column=2)
subtract=Button(frm1,text='-',width=3,height=1,command=sub)
subtract.grid(row=3,column=3)


btn0=Button(frm1,text='0',width=3,height=1,command=fun0)
btn0.grid(row=4,column=0)
add=Button(frm1,text='+',width=3,height=1,command=funadd)
add.grid(row=4,column=1)
equal=Button(frm1,text='=',width=3,height=1,command=result)
equal.grid(row=4,column=2)
clear=Button(frm1,text='clr',width=3,height=1,command=clear)
clear.grid(row=4,column=3)
window.mainloop()

