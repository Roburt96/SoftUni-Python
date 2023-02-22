import tkinter as tk

# Step 3: create the main window
root = tk.Tk()
root.title("Travel App")
root.geometry("400x300")

# Step 4: create the widgets
label = tk.Label(root, text="Where do you want to go?")
entry = tk.Entry(root)
button = tk.Button(root, text="Search")

options = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar(value=options[0])
# Step 5: add functionality to the widgets
def search():
    query = entry.get()
    # code to search for the query
    if query == 'Dubai':
        show_dubai()

def show_dubai():
    text = 'Hello to Dubai!'
    label.config(text=text)
    label.text = text
button.config(command=search)

# Step 6: organize the widgets
label.pack()
entry.pack()
button.pack()
option_menu = tk.OptionMenu(root, selected_option, *options)
option_menu.pack()
# Step 7: add functionality to the app
# add code here to retrieve data or perform calculations

# Step 8: test and refine the app
root.mainloop()

