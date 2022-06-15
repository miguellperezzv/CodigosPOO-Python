import tkinter  as tk
from threading import Timer

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)



class FrameContador:

   

    def __init__(self, root):
        self.root = root
        self.root.geometry("500x200")
        self.master_frame = tk.Frame(root)
        self.master_frame.pack(fill=tk.BOTH, expand=True)
        self.root.title("Contador")
        btnContar = tk.Button(self.master_frame, text="Contar")
        btnParar = tk.Button(self.master_frame, text="Parar")
        btnContar.pack()
        btnParar.pack()