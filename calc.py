from tkinter import *
from random import randint
import time;


def btnclick(numbers):
	global oparator
	oparator= oparator + str(numbers)
	textInput.set(oparator)

def btnclear():
	global oparator
	oparator=""
	textInput.set("")

def equal():
	global oparator
	total=str(eval(oparator))
	textInput.set(total)
	oparator=""

def receipt_no():
	global number 
	number=randint(100000,999999)
	receipt.set(number)
	oparator=""

def reset():
	juice.set("")
	fries.set("")
	chiken.set("")
	total.set("")
	receipt.set("")
	jtotal.set("")
	ftotal.set("")
	ctotal.set("")

def exit():
	calc.destroy()

def G_total():
	CoJ=float(juice.get())
	Cof=float(fries.get())
	Coc=float(chiken.get())


		

	costjuice=CoJ*70
	costfries=Cof*100
	costchiken=Coc*120


	jtotal.set(costjuice)
	ftotal.set(costfries)
	ctotal.set(costchiken)

	add_T= (costjuice+ costfries+ costchiken)
	total.set(add_T)

	



calc=Tk()

calc.geometry("1600x800+0+0")

calc.title("Restaurant Calculator")

#Variables---------
oparator=""
textInput=StringVar()
receipt=StringVar()

#-----------------------------

#Frames
f1=Frame(calc, width=1600,height=50, relief=SUNKEN)
f1.pack(side=TOP)

f2=Frame(calc, width=800, height=700, relief=SUNKEN)
f2.pack(side=LEFT)

f3=Frame(calc, width=300,height=700, bg="sky blue", relief=SUNKEN)
f3.pack(side=RIGHT)
#----------------------------------

#time
localtime=time.asctime(time.localtime(time.time()))
#-------------------------------------------


l1=Label(f1, text="Four Points", font=("Times New Roam", 40, "bold"), anchor="w")
l1.grid(column=0, row=0)

l1=Label(f1, text=localtime, font=("Times New Roam", 20, "bold"), anchor="w")
l1.grid(column=0, row=1)

#Calculator-----------------------
e1= Entry(f3,textvariable=textInput, font=("Times New Roam", 20,"bold"), bd=30, justify="right")
e1.grid(columnspan=4)

#Buttons
b9=Button(f3, text="9", padx=20, pady=20, fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(9))
b9.grid(column=0, row=1)

b8=Button(f3,text="8", padx=20, pady=20,fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(8))
b8.grid(column=1, row=1)

b7=Button(f3,text="7", padx=20, pady=20,fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(7))
b7.grid(column=2, row=1)

b6=Button(f3,text="6", padx=20, pady=20, fg="black",bg="sky blue",bd=10, font=(20), command=lambda:btnclick(6))
b6.grid(column=0, row=2)

b5=Button(f3,text="5", padx=20, pady=20,fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(5))
b5.grid(column=1, row=2)

b4=Button(f3,text="4", padx=20, pady=20,fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(4))
b4.grid(column=2, row=2)

b3=Button(f3,text="3", padx=20, pady=20,fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(3))
b3.grid(column=0, row=3)

b2=Button(f3,text="2", padx=20, pady=20,fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(2))
b2.grid(column=1, row=3)

b1=Button(f3,text="1", padx=20, pady=20,fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(1))
b1.grid(column=2, row=3)

b0=Button(f3,text="0", padx=20, pady=20,fg="black",bg="sky blue", bd=10, font=(20), command=lambda:btnclick(0))
b0.grid(column=1, row=4)

ba=Button(f3,text="+", padx=20, pady=20, bd=10, font=(20), command=lambda:btnclick("+"))
ba.grid(column=3, row=1)

bb=Button(f3,text="-", padx=20, pady=20, bd=10, font=(20), command=lambda:btnclick("-"))
bb.grid(column=3, row=2)

bc=Button(f3,text="*",padx=20, pady=20, bd=10, font=(20), command=lambda:btnclick("*"))
bc.grid(column=3, row=3)

bd=Button(f3,text="=", padx=20, pady=20, bd=10, font=(20), command=lambda:equal())
bd.grid(column=3, row=4)

be=Button(f3, text="DEL", padx=20, pady=20, bd=10, font=(20), command=lambda:btnclear())
be.grid(column=2, row=4)

#--------------------------------------------------------------------------------------------------------------------
juice=StringVar()
fries=StringVar()
chiken=StringVar()
total=StringVar()
jtotal=StringVar()
ftotal=StringVar()
ctotal=StringVar()



l2=Label(f2, text="Receit NO",font=(50))
l2.grid()
la=Entry(f2, bd=5, justify="right" , textvariable=receipt)
la.grid(column=1, row=0)

l3=Label(f2, text="juice",font=(50))
l3.grid(column=0, row=1)
lb=Entry(f2, bd=5,textvariable=juice, justify="right")
lb.grid(column=1, row=1)

l4=Label(f2, text="fries",font=(50))
l4.grid(column=0, row=2)
lc=Entry(f2, bd=5,textvariable=fries, justify="right")
lc.grid(column=1, row=2)

l5=Label(f2, text="chiken",font=(50))
l5.grid(column=0, row=3)
ld=Entry(f2, bd=5,textvariable=chiken, justify="right")
ld.grid(column=1, row=3)

l6=Label(f2, text="Total Cost",font=(50))
l6.grid(column=2, row=5)
le=Entry(f2, bd=5,textvariable=total, justify="right")
le.grid(column=3, row=5)

l7=Label(f2, text="Total", font=(50))
l7.grid(column=2, row=1)
lg=Entry(f2, bd=5, justify="right", textvariable=jtotal,width=30)
lg.grid(column=3,row=1)

l8=Label(f2, text="Total", font=(50))
l8.grid(column=2, row=2)
lh=Entry(f2, bd=5, justify="right", width=30, textvariable=ftotal)
lh.grid(column=3,row=2)

l9=Label(f2, text="Total", font=(50))
l9.grid(column=2, row=3)
li=Entry(f2, bd=5, justify="right", width=30, textvariable=ctotal)
li.grid(column=3,row=3)

bf=Button(f2, text="receipt", padx=5, pady=2, bd=15,font=(30), command=lambda:receipt_no())
bf.grid(column=1, row=7)

bh=Button(f2, text="Total", padx=5, pady=2, bd=15, font=(30),command=G_total) #command=lambda:grand_total() )
bh.grid(column=2, row=7)

bi=Button(f2, text="Reset", padx=5, pady=2, bd=15, font=(30), command=reset)
bi.grid(column=3, row=7)

bj=Button(f2, text="exit", padx=5, pady=2, bd=15, font=(30) ,command=exit)
bj.grid(column=4, row=7)
















calc.mainloop()