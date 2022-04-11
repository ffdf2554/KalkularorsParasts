from tkinter import*
mansLogs=Tk()
mansLogs.title("Kalkulators")
#mansLogs.geometry("300x300")

bnt0=Button(mansLogs,text="0",padx="40",pady="20")
bnt1=Button(mansLogs,text="1",padx="40",pady="20")
bnt2=Button(mansLogs,text="2",padx="40",pady="20")
bnt3=Button(mansLogs,text="3",padx="40",pady="20")
bnt4=Button(mansLogs,text="4",padx="40",pady="20")
bnt5=Button(mansLogs,text="5",padx="40",pady="20")
bnt6=Button(mansLogs,text="6",padx="40",pady="20")
bnt7=Button(mansLogs,text="7",padx="40",pady="20")
bnt8=Button(mansLogs,text="8",padx="40",pady="20")
bnt9=Button(mansLogs,text="9",padx="40",pady="20")

btnSum=Button(mansLogs,text="+",padx="40",pady="20")
btnMin=Button(mansLogs,text="-",padx="40",pady="20")
btnDel=Button(mansLogs,text="c",padx="40",pady="20")
btnDal=Button(mansLogs,text="/",padx="40",pady="20")
btnReiz=Button(mansLogs,text="x",padx="40",pady="20")
btnVien=Button(mansLogs,text="=",padx="40",pady="20")

bnt7.grid(row=1,column=0)
bnt8.grid(row=1,column=1)
bnt9.grid(row=1,column=2)
bnt4.grid(row=2,column=0)
bnt5.grid(row=2,column=1)
bnt6.grid(row=2,column=2)
bnt1.grid(row=3,column=0)
bnt2.grid(row=3,column=1)
bnt3.grid(row=3,column=2)
bnt0.grid(row=4,column=0)


btnSum.grid(row=3,column=4)
btnMin.grid(row=4,column=4)





mansLogs.mainloop()