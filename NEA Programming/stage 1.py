import tkinter as tk
import ttk


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

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.config(bg="green")
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page", font=("Times New Roman", 20))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=("Times New Roman", 20))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        label_0 = tk.Label(root, text="Reigstration Form 1", width=20, font=("bold", 10))
        label_0.place(x=90, y=53)

        label_1 = tk.Label(root, text="First Name", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)

        entry_1 = tk.Entry(root)
        entry_1.place(x=240, y=130)

        label_2 = tk.Label(root, text="Gender", width=20, font=("bold", 10))
        label_2.place(x=70, y=230)
        var = tk.IntVar()
        tk.Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
        tk.Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

        label_3 = tk.Label(self, text="Student or Teacher", width=20, font=("bold", 10))
        label_3.place(x=240, y=180)
        var1 = tk.IntVar()
        tk.Radiobutton(self, text="Student", padx=5, variable=var1, value=1).place(x=235, y=280)
        tk.Radiobutton(self, text="Teacher", padx=5, variable=var1, value=2).place(x=290, y=280)


root = MathsPro()
root.geometry("1280x800")
root.mainloop()
