# Longevity
# Demonstrates text and entry widgets, and the Grid layout manager
from tkinter import *
class Application(Frame):
    """ GUI application which can reveal the secret of longevity. """
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


def create_widgets(self):
    """ Create button, text, and entry widgets. """
    # create instruction label
    self.inst_lbl = Label(self, text = "Enter password for the secret of longevity")
    self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

