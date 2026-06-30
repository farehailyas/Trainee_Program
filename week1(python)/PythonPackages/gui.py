import tkinter as tk

# creates the main application
obj = tk.Tk()

# # add text on window
lab = tk.Label(obj , text = "Tkinter desktop Application" ,fg = "green" , width = 20, height = 20 )
lab.pack()
# add a button
button = tk.Button(obj , text = "Stop", command = obj.destroy )
# place the button on window
button.pack()

# tk.Label(obj, text="First Name").grid(row=0, column=0)
# tk.Label(obj, text="Last Name").grid(row=1, column=0)

# entry1 = tk.Entry(obj)
# entry2 = tk.Entry(obj)

# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)


# start the event loop and keeps the window responsive
obj.mainloop()