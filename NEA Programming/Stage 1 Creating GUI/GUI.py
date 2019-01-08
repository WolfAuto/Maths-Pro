import tkinter as tk
from tkinter import ttk
# c:\users\kymani mcgregor\appdata\local\programs\python\python37-32\lib\site-packages


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

        for F in (MainMenu, RegistrationForm1, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Maths Pro", font=("Times New Roman", 70))
        label.grid(row=0, column=1, columnspan=2)
        label.grid_rowconfigure(0, weight=1)
        label.grid_columnconfigure(0, weight=1)

        button1 = ttk.Button(self, text="Register",
                             command=lambda: controller.show_frame(RegistrationForm1))
        button1.grid(row=4, column=4)

        button2 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=4, column=5)


class RegistrationForm1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")

        
        label = tk.Label(self, text="Reigstration Form 1", font=("Times New Roman", 50))
        label.pack(pady=10, padx=10)

        label_0 = tk.Label(self, text="Reigstration Form 1", width=20, font=("bold", 10))
        label_0.place(x=90, y=103)

        label_1 = tk.Label(self, text="First Name", width=20, font=("bold", 10))
        label_1.place(x=550, y=230)

        label_a = tk.Label(self, text="Surname", width=20, font=("bold", 10))
        label_a.place(x=575, y=280)

        entry_a = tk.Entry(self)
        entry_a.place(x=740, y=280)

        entry_1 = tk.Entry(self)
        entry_1.place(x=740, y=230)

        label_2 = tk.Label(self, text="Gender", width=20, font=("bold", 10))
        label_2.place(x=570, y=330)

        var = tk.IntVar()
        tk.Radiobutton(self, text="Male", padx=5, variable=var, value=1).place(x=735, y=330)
        tk.Radiobutton(self, text="Female", padx=20, variable=var, value=2).place(x=790, y=330)
        label_b = tk.Label(self, text="Student or Teacher", width=20, font=("bold", 10))
        label_b.place(x=570, y=380)
        var1 = tk.IntVar()
        tk.Radiobutton(self, text="Student", padx=3, variable=var1, value=1).place(x=735, y=380)
        tk.Radiobutton(self, text="Teacher", padx=20, variable=var1, value=2).place(x=800, y=380)
        button1 = ttk.Button(self, text="Back to home", width=50,
                             command=lambda: controller.show_frame(MainMenu))
        button1.place(x=800, y=700)

        button2 = ttk.Button(self, text="Visit page two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Enter details", command=None)

        button3.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=("Times New Roman", 50))
        label.grid(pady=10, padx=10, sticky="n")

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(MainMenu))
        button1.grid()

        button2 = ttk.Button(self, text="Visit page one",
                             command=lambda: controller.show_frame(RegistrationForm1))
        button2.grid()


root = MathsPro()
root.geometry("1080x900")

root.mainloop()
