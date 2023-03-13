import tkinter as tk

def count_symbols(event):
    # Get the text entered by the user
    text = entry.get()
    # Update the label with the count of symbols
    label.config(text=f"Number of symbols: {len(text)}")

root = tk.Tk()

# Create the input box
entry = tk.Entry(root)
entry.pack()

# Create the label that displays the count of symbols
label = tk.Label(root)
label.pack()

# Bind the count_symbols function to the "Key" press event
entry.bind("<Key>", count_symbols)

root.mainloop()
