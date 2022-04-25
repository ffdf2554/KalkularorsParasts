from argparse import MetavarTypeHelpFormatter
from ast import operator
from distutils import command
from tkinter import*
from math import*
mansLogs=Tk()
mansLogs.title("Kalkulators")
#mansLogs.geometry("300x300")

def btnClick(number):
    current=e.get()#nolasa skaitli
    e.delete(0,END)#dzeš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#izvade displejs
    return 0

def btnCommand(command):
    global num1
    global mathOp 
    mathOp= command
    num1=float(e.get())
    e.delete(0,END)
    return 0

def btnVienads():
    global num2
    num2=(int(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def notirit():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

def sakne():
    global operator
    global num1
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0

def loga():
    global operator
    global num1
    num1=(float(e.get()))
    num1=log(num1,10)
    e.delete(0,END)
    e.insert(0,num1)
    return 0

e=Entry(mansLogs,width=15,font=("Arial Black",20))

bnt0=Button(mansLogs,text="0",padx="40",pady="20",command=lambda:btnClick(0))
bnt1=Button(mansLogs,text="1",padx="40",pady="20",command=lambda:btnClick(1))
bnt2=Button(mansLogs,text="2",padx="40",pady="20",command=lambda:btnClick(2))
bnt3=Button(mansLogs,text="3",padx="40",pady="20",command=lambda:btnClick(3))
bnt4=Button(mansLogs,text="4",padx="40",pady="20",command=lambda:btnClick(4))
bnt5=Button(mansLogs,text="5",padx="40",pady="20",command=lambda:btnClick(5))
bnt6=Button(mansLogs,text="6",padx="40",pady="20",command=lambda:btnClick(6))
bnt7=Button(mansLogs,text="7",padx="40",pady="20",command=lambda:btnClick(7))
bnt8=Button(mansLogs,text="8",padx="40",pady="20",command=lambda:btnClick(8))
bnt9=Button(mansLogs,text="9",padx="40",pady="20",command=lambda:btnClick(9))

btnSum=Button(mansLogs,text="+",padx="40",pady="20",command=lambda:btnCommand("+"))
btnMin=Button(mansLogs,text="-",padx="40",pady="20",command=lambda:btnCommand("-"))
btnDel=Button(mansLogs,text="C",padx="40",pady="20",command=notirit)
btnDal=Button(mansLogs,text="/",padx="40",pady="20",command=lambda:btnCommand("/"))
btnReiz=Button(mansLogs,text="*",padx="40",pady="20",command=lambda:btnCommand("*"))
btnVien=Button(mansLogs,text="=",padx="40",pady="20",command=btnVienads)
btnKv=Button(mansLogs,text="x²",padx="40",pady="20")
btnSak=Button(mansLogs,text="√",padx="40",pady="20",command=sakne)
btnLog=Button(mansLogs,text="log",padx="40",pady="20",command=loga)
bnt7.grid(row=1,column=0)
bnt8.grid(row=1,column=1)
bnt9.grid(row=1,column=2)
bnt4.grid(row=2,column=0)
bnt5.grid(row=2,column=1)
bnt6.grid(row=2,column=2)
bnt1.grid(row=3,column=0)
bnt2.grid(row=3,column=1)
bnt3.grid(row=3,column=2)
bnt0.grid(row=4,column=1)


btnSum.grid(row=3,column=4)
btnMin.grid(row=4,column=4)
btnDel.grid(row=4,column=0)
btnVien.grid(row=4,column=2)
btnDal.grid(row=1,column=4)
btnReiz.grid(row=2,column=4)
btnSak.grid(row=1,column=5)
btnKv.grid(row=2,column=5)
btnLog.grid(row=3,column=5)

e.grid(row=0,column=0,columnspan=6)


mansLogs.mainloop()