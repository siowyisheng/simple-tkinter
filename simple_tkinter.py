import tkinter as tk
import tkinter.messagebox as tkmessagebox
from random import randint
from PIL import Image, ImageTk
import sys, os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        def hello():
            tkmessagebox.showinfo("Say Hello", "Hello World")

        def donothing():
            filewin = tk.Toplevel(root)
            button = tk.Button(filewin, text="Do nothing button")
            button.pack()

        def show_about():
            top = tk.Toplevel()
            top.title("About")
            top.geometry("150x100")

            f = tk.Frame(top, height=800, width=800)
            f.pack()

            msg = tk.Message(f, text='Made by Siow Yi Sheng')
            msg.pack()

            button = tk.Button(f, text="Dismiss", command=top.destroy)
            button.pack()

        def sel():
            selection = "You selected the option " + str(var.get())
            label.config(text=selection)

        def hello2():
            n = randint(1, 4)
            health_int = int(health.get().replace('Health: ', ''))
            new_health = f'Health: {health_int - n}'
            health.set(new_health)
            tk.Label(root,
                     text=f'You cut it for {n} damage',
                     bg='#c8af6a',
                     fg='green',
                     font=('helvetica', 12, 'bold')).pack()
            root.update_idletasks()

        left = tk.Frame(root)
        left.pack(side=tk.LEFT)

        B1 = tk.Button(left, text="Say Hello", command=hello)
        B1.pack()

        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)
        editmenu.add_separator()

        C = tk.IntVar()
        C2 = tk.IntVar()
        editmenu.add_checkbutton(label="Show Video", variable=C)
        editmenu.add_radiobutton(label="Show Boop", variable=C2, value=1)
        editmenu.add_radiobutton(label="Show Bong", variable=C2, value=2)
        editmenu.add_radiobutton(label="Show Batter", variable=C2, value=3)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)

        load = Image.open(resource_path("parrot.png"))
        render = ImageTk.PhotoImage(load)
        img = tk.Label(left, image=render)
        img.image = render  # keep this line for use in garbage collection
        img.pack()

        tk.Message(
            left,
            text=
            'William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world\'s greatest dramatist.[2][3][4] He is often called England\'s national poet and the "Bard of Avon" (or simply "the Bard").',
            width=500).pack()

        health = tk.StringVar(value='Health: 20')
        tk.Label(left,
                 textvariable=health,
                 fg='red',
                 font=('helvetica', 12, 'bold')).pack()

        var = tk.IntVar()
        R1 = tk.Radiobutton(left,
                            text="Option 1",
                            variable=var,
                            value=1,
                            command=sel)
        R1.pack()

        R2 = tk.Radiobutton(left,
                            text="Option 2",
                            variable=var,
                            value=2,
                            command=sel)
        R2.pack()

        R3 = tk.Radiobutton(left,
                            text="Option 3",
                            variable=var,
                            value=3,
                            command=sel)
        R3.pack()

        label = tk.Label(left)
        label.pack()

        CheckVar1 = tk.IntVar()
        C1 = tk.Checkbutton(left, text="Music", variable=CheckVar1)
        C1.pack()

        CheckVar2 = tk.IntVar()
        C2 = tk.Checkbutton(left, text="Video", variable=CheckVar2)
        C2.pack()

        right = tk.Frame()
        right.pack(side=tk.RIGHT)

        v = tk.IntVar()
        tk.Scale(right,
                 from_=0,
                 to=100,
                 resolution=5,
                 orient=tk.HORIZONTAL,
                 variable=v).pack()

        F = tk.Frame()
        F.pack()
        scrollbar = tk.Scrollbar(F)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        mylist = tk.Listbox(F, yscrollcommand=scrollbar.set)
        for line in range(100):
            mylist.insert(tk.END, "This is line number " + str(line))

        mylist.pack(side=tk.LEFT)
        scrollbar.config(command=mylist.yview)

        mb = tk.Menubutton(right, text="condiments", relief=tk.RAISED)
        mb.pack()
        mb.menu = tk.Menu(mb, tearoff=0)
        mb["menu"] = mb.menu

        mayoVar = tk.IntVar()
        ketchVar = tk.IntVar()

        mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
        mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

        text = tk.Text(
            right, font='Helvetica', height=3, width=20
        )  # height is in lines and width is in number of characters
        text.insert(tk.INSERT, "Hello.....")
        text.config(state=tk.DISABLED)
        text.pack()

        w = tk.Spinbox(right, from_=0, to=10)
        w.pack()

        F = tk.Frame()
        F.pack()
        L1 = tk.Label(F, text="User Name")
        L1.pack(side=tk.LEFT)
        E1 = tk.Entry(F, bd=5)
        E1.pack(side=tk.RIGHT)

        group = tk.LabelFrame(right, text="Group", padx=5, pady=5)
        group.pack(padx=10, pady=10)

        w = tk.Entry(group)
        w.pack()

        variable = tk.StringVar()
        variable.set("one")  # default value

        w = tk.OptionMenu(right, variable, "one", "two", "three")
        w.pack()

        tk.Button(text='Click Me', command=hello2, bg='brown',
                  fg='white').pack(side=tk.BOTTOM)

        tk.Label(right, text='awesome game').pack()


if __name__ == "__main__":
    root = tk.Tk()
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

root.mainloop()