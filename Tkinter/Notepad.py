from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import os
def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    Textarea.delete(1.0,END)
def openFile():
    global file
    file=askopenfile(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file==None:
        file=asksaveasfile(initialfile="Untitled",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
    else:
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()
        
def quitApp():
    root.destroy()
def about():
    showinfo("About Notepad","Notepad by Abhi")
def cut():
    Textarea.event_generate("<<Cut>>")      #kinter handle it internally
def copy():
    Textarea.event_generate("<<Copy>>")
def paste():
    Textarea.event_generate("<<Paste>>")
if __name__ == '__main__':
    root=Tk()
    root.title("Notepad")
    root.geometry("600x600")

    Textarea=Text(root,font="lucida 13")
    file=None
    Textarea.pack(expand=True,fill=BOTH,)
    # Crete a menubar
    Menubar=Menu(root)

    # File menu start here----------------------------------------
    Filemenu=Menu(Menubar,tearoff=0)
    # Open a new file
    Filemenu.add_command(label="New",command=newFile)

    # to open alerdy existing file
    Filemenu.add_command(label="Open", command=openFile)

    # To save the current file
    Filemenu.add_command(label="Save",command=saveFile)
    Filemenu.add_separator()

    Filemenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=Filemenu)
    # File menu end here

    # Edit menu starts
    EditMenu=Menu(Menubar,tearoff=0)
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    Menubar.add_cascade(label="Edit",menu=EditMenu)
    # Edit menu end here

    # Help menu starts here
    HelpMenu=Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="About",command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)
    # Help menu end here
    root.config(menu=Menubar)
    Scroll=Scrollbar(Textarea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)
    root.mainloop()