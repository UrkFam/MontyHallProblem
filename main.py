from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

import DoorScript
from DoorScript import generate


class MyGUI:

    def __init__(self):
        self.window = Tk()

        self.window.geometry("800x500")
        self.window.title("Monty Hall Problem")

        self.title = Label(self.window, text="Explaining the Monty Hall Problem", font=('Helvetica', 18))
        self.title.pack(padx=20, pady=20)

        self.textbox = Text(self.window, height=1, width=5, font=('Helvetica', 12))
        self.textbox.pack(padx=10, pady=10)

        self.generateIterations = Button(self.window, text="Generate Iterations", font=('Helvetica', 14),
                                         command=self.genIterations)
        self.generateIterations.pack(padx=10, pady=10)
        # self.generateIterations.bind("<Return>", self.genIterations)

        self.window.mainloop()

    def genIterations(self):
        getIterations = DoorScript.generate(self.textbox.get("1.0", END))
        messagebox.showinfo(title="Results", message=getIterations)


# Display
MyGUI()
