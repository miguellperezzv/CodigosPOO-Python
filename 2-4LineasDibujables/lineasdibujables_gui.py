import tkinter  as tk 




class GUI():
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.master_frame = tk.Frame(root)