from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("484x470")
def click1(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        # screen.update()
    elif text=="C":
        scvalue.set("")
        # screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        # screen.update()

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30 bold").pack(fill=X,padx=8,pady=10)
f1=Frame(root,bg="grey")
b1=Button(f1,text="9",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="8",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="7",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="C",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

f1.pack()



f1=Frame(root,bg="grey")
b1=Button(f1,text="6",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="5",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="4",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="+",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)
f1.pack()



f1=Frame(root,bg="grey")
b1=Button(f1,text="3",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="2",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="1",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="=",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=12,pady=5)
b1.bind("<Button-1>", click1)
f1.pack()


f1=Frame(root,bg="grey")
b1=Button(f1,text="0",padx=24,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=13,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="-",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=13,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="*",padx=23,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=13,pady=5)
b1.bind("<Button-1>", click1)

b1=Button(f1,text="/",padx=26,pady=12,font="lucida 20 bold")
b1.pack(side=LEFT,padx=13,pady=5)
b1.bind("<Button-1>", click1)
f1.pack()


root.mainloop()