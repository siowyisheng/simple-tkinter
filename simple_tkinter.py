import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkmessagebox
from random import randint
from PIL import Image, ImageTk
import sys, os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class App(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.configure_gui()
        self.create_menu()

        def hello():
            tkmessagebox.showinfo("Say Hello", "Hello World")

        def sel():
            selection = "You selected the option " + str(var.get())
            self.label.config(text=selection)

        def hello2():
            n = randint(1, 4)
            health_int = int(health.get().replace('Health: ', ''))
            new_health = f'Health: {health_int - n}'
            health.set(new_health)
            ttk.Label(self.master, text=f'You cut it for {n} damage').pack()

        left = ttk.Frame(self.master)
        left.pack(side=tk.LEFT)

        ttk.Button(left, text="Say Hello", command=hello).pack()

        load = Image.open(resource_path("parrot.png"))
        render = ImageTk.PhotoImage(load)
        img = ttk.Label(left, image=render)
        img.image = render  # keep this line for use in garbage collection
        img.pack()

        tk.Message(
            left,
            text=
            'William Shakespeare (bapt. 26 April 1564 – 23 April 1616)[a] was an English poet, playwright, and actor, widely regarded as the greatest writer in the English language and the world\'s greatest dramatist.[2][3][4] He is often called England\'s national poet and the "Bard of Avon" (or simply "the Bard").',
            width=300).pack()

        health = tk.StringVar(value='Health: 20')
        style = ttk.Style()
        style.configure("BW.TLabel",
                        foreground="red",
                        font=('helvetica', 12, 'bold'))
        ttk.Label(
            left,
            textvariable=health,
            style='BW.TLabel',
        ).pack()

        self.radio_frame = ttk.Frame(left)
        self.radio_frame.pack()
        var = tk.IntVar()
        ttk.Radiobutton(self.radio_frame,
                        text="Option 1",
                        variable=var,
                        value=1,
                        command=sel).pack(side=tk.LEFT)

        ttk.Radiobutton(self.radio_frame,
                        text="Option 2",
                        variable=var,
                        value=2,
                        command=sel).pack(side=tk.LEFT)

        ttk.Radiobutton(self.radio_frame,
                        text="Option 3",
                        variable=var,
                        value=3,
                        command=sel).pack(side=tk.LEFT)

        self.label = ttk.Label(left)
        self.label.pack()

        self.checkbox_frame = tk.Frame(left)
        self.checkbox_frame.pack()

        CheckVar1 = tk.IntVar()
        ttk.Checkbutton(self.checkbox_frame, text="Music",
                        variable=CheckVar1).pack(side=tk.LEFT)

        CheckVar2 = tk.IntVar()
        ttk.Checkbutton(self.checkbox_frame, text="Video",
                        variable=CheckVar2).pack(side=tk.LEFT)

        middle = ttk.Frame(self)
        middle.pack(side=tk.LEFT)

        v = tk.IntVar()
        ttk.Scale(middle, from_=0, to=100, orient=tk.HORIZONTAL,
                  variable=v).pack()

        F = ttk.Frame(middle)
        F.pack()
        scrollbar = ttk.Scrollbar(F)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        mylist = tk.Listbox(F, yscrollcommand=scrollbar.set)
        for line in range(100):
            mylist.insert(tk.END, "This is line number " + str(line))

        mylist.pack(side=tk.LEFT)
        scrollbar.config(command=mylist.yview)

        mb = ttk.Menubutton(middle, text="condiments")
        mb.pack()
        mb.menu = tk.Menu(mb, tearoff=0)
        mb["menu"] = mb.menu

        mayoVar = tk.IntVar()
        ketchVar = tk.IntVar()

        mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
        mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

        text = tk.Text(
            middle, font='Helvetica', height=3, width=20
        )  # height is in lines and width is in number of characters
        text.insert(tk.INSERT, "Hello.....")
        text.config(state=tk.DISABLED)
        text.pack()

        w = ttk.Spinbox(middle, from_=0, to=10)
        w.pack()

        F = ttk.Frame(middle)
        F.pack()
        L1 = ttk.Label(F, text="User Name")
        L1.pack(side=tk.LEFT)
        E1 = ttk.Entry(F)
        E1.pack(side=tk.RIGHT)

        group = ttk.LabelFrame(middle, text="Group")
        group.pack(padx=10, pady=10)

        w = ttk.Entry(group)
        w.pack()

        variable = tk.StringVar()
        variable.set("one")  # default value

        w = tk.OptionMenu(middle, variable, "one", "two", "three")
        w.pack()

        ttk.Button(middle, text='Click Me', command=hello2).pack()

        right = ttk.Frame(self)
        right.pack(side=tk.LEFT)

        ttk.Combobox(right,
                     values=('Eiffel Tower', 'Statue of Liberty',
                             'Colossus')).pack()

        self.notebook = ttk.Notebook(right, height=50, width=200)
        self.notebook.add(ttk.Button(text='Push Me'), text='Button1')
        self.notebook.add(ttk.Button(text='Prod Me'), text='Button2')
        self.notebook.add(ttk.Button(text='Poke Me'), text='Button3')
        self.notebook.pack()

        ttk.Label(right, text='Progress Label').pack()
        pbar1 = ttk.Progressbar(right, mode='determinate')
        pbar1.pack()
        pbar1.start()

        pbar2 = ttk.Progressbar(right, mode='indeterminate')
        pbar2.pack()

    def configure_gui(self):
        self.master.title("Widget Showcase")
        # self.master.geometry("500x500")
        self.master.resizable(True, True)

    def create_menu(self):
        def donothing():
            filewin = tk.Toplevel(self.master)
            button = ttk.Button(filewin, text="Do nothing button")
            button.pack()

        def show_about():
            top = tk.Toplevel(self.master)
            top.title("About")
            top.geometry("150x100")

            f = ttk.Frame(top, height=800, width=800)
            f.pack()

            msg = tk.Message(f, text='Made by Siow Yi Sheng')
            msg.pack()

            button = ttk.Button(f, text="Dismiss", command=top.destroy)
            button.pack()

        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.master.quit)
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

        self.master.config(menu=menubar)


if __name__ == "__main__":
    root = tk.Tk()
    App(root).pack()
    root.mainloop()

root.mainloop()