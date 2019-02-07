import tkinter as tk

large_font = ("Verdana", 12)
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container= tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage]= frame

        frame.grid(row=0, column=0, sticky="nsew")

        frame.grid(row=110, column=110, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.config(bg="grey")
        frame.tkraise()
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font = large_font)
        label.pack(pady=10,padx=10)
class PageOne(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)

app = SeaofBTCapp()
app.mainloop()
