#Bailey Garrett Final

# Create a GUI price check
import tkinter as tk 

#create a window
window = tk.Tk()
window.title("Price Checker")

#create a label for the title
title_label = tk.Label(window, text="Price Checker", font=("Arial", 20))
title_label.pack()

def exit():
    window.destroy()

def clear_history():
    history_label.config(text = "")

#hide history page 
def open_window():
    window2.withdraw()

#unhide/show history page
def open_window2():
    window2.deiconify()

#clear user input
def clear_input():
    amount_entry.delete(0, tk.END)
    units_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

#Function to calc ppu
def calc_ppu():
    items = float(amount_entry.get())
    unit = float(units_entry.get())
    price = float(price_entry.get())
    #calc ppu
    totalunit = unit * items
    ppu =  (price/totalunit)
    #round 2 decimal places... removed to avoid saying $0 for items worth less than 1 cent
    #ppu=round(ppu,2)
    #display result to wondow
    result_label.config(text=" The Price Per Unit is: $" + str(ppu))

    #display to history page... this took forever
    current_text = history_label.cget("text")
    new_text =  "\n"+ str(items)+" items with "+str(unit)+" units each at $"+str(price)+" is $"+str(ppu) +" a unit"
    updated_text = current_text + new_text
    history_label.config(text = updated_text)

    


#history window
#open history window

window2 = tk.Toplevel(window)
window2.title("History")
#hides window
window2.withdraw() 

#window header
history_text = tk.Label(window2, text="History")
history_text.pack()

#append text to add all history
history_label = tk.Label(window2, text="")
history_label.pack()

#button to clear history
button3 = tk.Button(window2, text="Clear history", command=clear_history)
button3.pack()

#button to exit history window by hiding it
button2 = tk.Button(window2, text="Close history", command=open_window)
button2.pack()

#main window
#Create a label for the amount entry
amount_label = tk.Label(window, text="Enter Amount of Items:")
amount_label.pack()

#Create an entry for the user to enter their amount
amount_entry = tk.Entry(window)
amount_entry.pack()

#Create a label for the units entry
units_label = tk.Label(window, text="Enter Amount of Units Per Single Item:")
units_label.pack()

#Create an entry for the user to enter their units
units_entry = tk.Entry(window)
units_entry.pack()

#Create a label for the price entry
price_label = tk.Label(window, text="Enter Price:")
price_label.pack()

#Create an entry for the user to enter their price
price_entry = tk.Entry(window)
price_entry.pack()

#Create a button to calc PPU
calc_button = tk.Button(window, text="Calculate Price per unit", command=calc_ppu)
calc_button.pack()

#create a label for the result
result_label = tk.Label(window, text="")
result_label.pack()

#button to clear user input
clear_button = tk.Button(window, text="Clear inputs", command=clear_input)
clear_button.pack()

#button to open history window
button = tk.Button(window, text="Open History", command=open_window2)
button.pack()

#exit button to end program
button4 = tk.Button(window, text="Exit", command=exit)
button4.pack()







#Start the event loop
window.mainloop()