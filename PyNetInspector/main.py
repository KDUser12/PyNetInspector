######################################################################
# PyNetInspector est un inspecteur de réseau internet permetant de
# connaitre son niveau de débit mais aussi sur la fréquence et d'autre
# information utile à savoir sur son internet.
######################################################################

import tkinter as ttk
import sys


from packages.inspect import inspect_internet


class App:
    def __init__(self, window):
        self.title = window.title("PyNetInspector")
        self.minsize = window.minsize(width=350, height=150)
        self.maxsize = window.maxsize(width=350, height=150)

        self.button = ttk.Button(window, text="Inspecter", font=("Arial", 10), command=self.click_button)
        self.button.pack(pady=50)

        self.window = window

    def click_button(self):
        self.button.forget()
        self.label = ttk.Label(self.window, text="Loading...", font=("Arial", 12))
        self.label.pack(pady=50)

        inspect_internet(self)


if __name__ == "__main__":
    try:
        root = ttk.Tk()
        App(root)

        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)
