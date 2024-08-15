from tkinter import *
root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
mylabel = Label(root, text="This is second page")
mylabel.pack()
print("im second")
root.mainloop()