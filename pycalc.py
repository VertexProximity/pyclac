import tkinter as tk
from math import *

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Set the title and geometry of the window
        self.title("Scientific Calculator")
        self.geometry("270x380")

        # Create the display widget
        self.display = tk.Entry(self, font=("Helvetica", 16), relief=tk.RAISED, borderwidth=3)
        self.display.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create the buttons
        self.create_buttons()

        # Create the menu
        self.create_menu()

        # Create the status bar
        self.status_bar = tk.Label(self, text="", font=("Helvetica", 10), relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_buttons(self):
        # Create the buttons in a grid
        buttons = [
            ["AC", "C", "CE", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "±", "="],
        ]
        for row in buttons:
            for button in row:
                tk.Button(self, text=button, font=("Helvetica", 12), relief=tk.RAISED, borderwidth=3, command=lambda b=button: self.button_press(b)).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def create_menu(self):
        # Create the menu bar
        menu_bar = tk.Menu(self)

        # Create the File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Create the View menu
        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Standard", command=self.view_standard)
        view_menu.add_command(label="Scientific", command=self.view_scientific)
        menu_bar.add_cascade(label="View", menu=view_menu)

        # Create the Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Add the menu bar to the window
        self.config(menu=menu_bar)

    def view_standard(self):
        # Switch to standard view
        pass

    def view_scientific(self):
        # Switch to scientific view
        # Add scientific functions to the buttons
        scientific_buttons = [
            ["sin", "cos", "tan"],
            ["ln", "log", "e^x"],
            ["x^2", "x^3", "x^y"],
            ["√", "3√", "y√x"],
            ["π", "e", "φ"],
        ]
        for row in scientific_buttons:
            for button in row:
                tk.Button(self, text=button, font=("Helvetica", 12), relief=tk.RAISED, borderwidth=3, command=lambda b=button: self.button_press(b)).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def about(self):
        # Show the about dialog
        about_dialog = tk.Toplevel(self)
        about_dialog.title("About")
        about_dialog.geometry("200x100")

        tk.Label(about_dialog, text="Scientific Calculator").pack(side=tk.TOP)
        tk.Label(about_dialog, text="Version 1.0").pack(side=tk.TOP)
        tk.Label(about_dialog, text="Copyright 2022").pack(side=tk.TOP)

        tk.Button(about_dialog, text="Close", command=about_dialog.destroy).pack(side=tk.BOTTOM)

    def button_press(self, button):
        # Handle button press
        if button == "AC":
            self.display.delete(0, tk.END)
        elif button == "C":
            self.display.delete(len(self.display.get())-1, tk.END)
        elif button == "CE":
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
        elif button == "=":
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "sin":
            try:
                result = str(sin(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "cos":
            try:
                result = str(cos(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "tan":
            try:
                result = str(tan(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        elif button == "ln":
            try:
                result = str(log(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "log":
            try:
                result = str(log10(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "e^x":
            try:
                result = str(exp(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "x^2":
            try:
                result = str(pow(eval(self.display.get()), 2))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "x^3":
            try:
                result = str(pow(eval(self.display.get()), 3))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "x^y":
            self.display.insert(tk.END, "**")
        elif button == "√":
            try:
                result = str(sqrt(eval(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "3√":
            try:
                result = str(pow(eval(self.display.get()), 1/3))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button == "y√x":
            self.display.insert(tk.END, "**(1/)")
        elif button:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
        elif button == "π":
            self.display.insert(tk.END, "pi")
        elif button == "e":
            self.display.insert(tk.END, "e")
        elif button == "φ":
            self.display.insert(tk.END, "phi")
        else:
            self.display.insert(tk.END, button)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
