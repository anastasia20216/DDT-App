import tkinter as tk

def BtnClicked(button, id, names):
    print(f"Button {id} clicked with text {names[id]}")

# Initialize the main window 
root = tk.Tk()
root.title("Buttons with Scrollbar")

# Create a Canvas widget
canvas = tk.Canvas(root)
canvas.pack(side='left', fill='both', expand=True)

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Create a Frame to hold the buttons
button_frame = tk.Frame(canvas)

# Create a window on the Canvas to hold the button_frame
canvas.create_window((0, 0), window=button_frame, anchor='nw')

# Configure the Canvas to use the Scrollbar
canvas.config(yscrollcommand=scrollbar.set)

# Example data
rep_name = ["Button1", "Button2", "Button3", "Button4", "Button5", "Button6", "Button7", "Button8", "Button9", "Button10", "Button11", "Button12"]
image_refs = [None] * len(rep_name)  # Placeholder for images
buttons = []

# Variables to position buttons
x = 0.18
y = 0.1

# Add buttons to the button_frame
for i in range(12):
    if i < len(rep_name):
        idx = i
        rep_button = tk.Button(button_frame, text=rep_name[i], relief="flat", borderwidth=0, compound=tk.TOP, bg='#F5F2EB', font=("Helvetica", 10), padx=5, pady=5)
        rep_button.grid(row=i//4, column=i%4, padx=5, pady=5, sticky="ew")  # Using grid instead of place for simplicity
        rep_button.config(command=lambda b=rep_button, id=idx, v=rep_name: BtnClicked(b, id, v))
        buttons.append(rep_button)

# Update the Canvas scroll region to encompass the button_frame
button_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

# Start the Tkinter event loop
root.mainloop()
