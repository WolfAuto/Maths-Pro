import tkinter as tk
from tkinter import ttk


class MathsPro(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "Maths Pro")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def qf(stringtoprint):
    print(stringtoprint)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="blue")
        label = tk.Label(self, text="Start Page", font=("Times New Roman", 20))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Visit Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=("Times New Roman", 20))
        label.grid(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.grid()

        button2 = ttk.Button(self, text="Visit page two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.grid()

        button3 = ttk.Button(self, text="Visit page three",
                             command=lambda: controller.show_frame(PageThree))
        button3.grid()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=("Times New Roman", 20))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Visit page one",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three Graph Page",
                         font=("Times New Roman", 20))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Visit page one",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


root = MathsPro()
root.geometry("1000x700")
root.mainloop()


app = tk.Tk()
app.geometry('500x500')
app.title("Maths Pro - Registration Form 1")

label_0 = tk.Label(app, text="Reigstration Form 1",
                   width=20, font=("bold", 10))
label_0.place(x=90, y=53)

label_1 = tk.Label(app, text="First Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = tk.Entry(app)
entry_1.place(x=240, y=130)

label_2 = tk.Label(app, text="Gender", width=20, font=("bold", 10))
label_2.place(x=70, y=230)
var = tk.IntVar()
tk.Radiobutton(app, text="Male", padx=5, variable=var,
               value=1).place(x=235, y=230)
tk.Radiobutton(app, text="Female", padx=20,
               variable=var, value=2).place(x=290, y=230)
