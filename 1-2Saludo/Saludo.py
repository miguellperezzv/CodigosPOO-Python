import tkinter as tk
from tkinter import messagebox


def Saludador():
    
    messagebox.showinfo("Message", "Hola " + INnombre.get())
    master.quit()

if __name__ == "__main__":
    master = tk.Tk()
    tk.Label(master, text="Ingresa tu nombre").grid(row=0)


    INnombre = tk.Entry(master)
    INnombre.grid(row=0, column=1)

    tk.Button(master, text='Show', command=Saludador).grid(row=3, column=1, sticky=tk.W, pady=4)

    tk.mainloop()
