#!/usr/bin/env python3

import tkinter
# The controller.
def click_up(): 
    counter.set(counter.get() + 1)
def click_down(): 
    counter.set(counter.get() - 1)

if __name__ == '__main__': 
    window = tkinter.Tk()
    # The model.
    counter = tkinter.IntVar() 
    counter.set(0)
    # The views.
    frame = tkinter.Frame(window)
    frame.pack()
    button = tkinter.Button(frame, text='Up', command=click_up) 
    button.pack()
    button = tkinter.Button(frame, text='Down', command=click_down) 
    button.pack()
    label = tkinter.Label(frame, textvariable=counter)
    label.pack()
    # Start the machinery!
    window.mainloop()




window = tkinter.Tk()
# The model.
counter = tkinter.IntVar()
counter.set(0)
# General controller.
def click(var, value): 
    var.set(var.get() + value)
# The views.
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=lambda: click(counter, 1)) 
button.pack()
button = tkinter.Button(frame, text='Down', command=lambda: click(counter, -1)) 
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()
window.mainloop()



window = tkinter.Tk()
button = tkinter.Button(window, text='Hello',font=('Courier', 14, 'bold italic'))
button.pack()
window.mainloop()

window = tkinter.Tk()
button = tkinter.Label(window, text='Hello', bg='green', fg='white') 
button.pack()
window.mainloop()




def change(widget, colors):
    """ Update the foreground color of a widget to show the RGB color value
    stored in a dictionary with keys 'red', 'green', and 'blue'.  Does
    *not* check the color value.
    """
    new_val = '#'
    for name in ('red', 'green', 'blue'):
        new_val += colors[name].get() 
    widget['bg'] = new_val
# Create the application.
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
# Set up text entry widgets for red, green, and blue, storing the 
# # associated variables in a dictionary for later use.
colors = {}
for (name, col) in (('red', '#FF0000'),('green', '#00FF00'),('blue', '#0000FF')): 
    colors[name] = tkinter.StringVar()
    colors[name].set('00')
    entry = tkinter.Entry(frame, textvariable=colors[name], bg=col,fg='white')
    entry.pack()

# Display the current color.
current = tkinter.Label(frame, text=' ', bg='#FFFFFF') 
current.pack()
# Give the user a way to trigger a color update.
update = tkinter.Button(frame, text='Update',command=lambda: change(current, colors))
update.pack()
tkinter.mainloop()




window = tkinter.Tk()
frame = tkinter.Frame(window) 
frame.pack()
label = tkinter.Label(frame, text='Name') 
label.pack(side='left')
entry = tkinter.Entry(frame) 
entry.pack(side='left')
window.mainloop()



def cross(text):
    text.insert(tkinter.INSERT, 'X')
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
text = tkinter.Text(frame, height=3, width=10)
text.pack()
button = tkinter.Button(frame, text='Add', command=lambda: cross(text)) 
button.pack()
window.mainloop()



window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
red = tkinter.IntVar()
green = tkinter.IntVar()
blue = tkinter.IntVar()
for (name, var) in (('R', red), ('G', green), ('B', blue)): 
    check = tkinter.Checkbutton(frame, text=name, variable=var) 
    check.pack(side='left')
def recolor(widget, r, g, b): 
    color = '#'
    for var in (r, g, b):
        color += 'FF' if var.get() else '00'
    widget.config(bg=color)
label = tkinter.Label(frame, text='[ ]') 
button = tkinter.Button(frame, text='update',command=lambda: recolor(label, red, green, blue))
button.pack(side='left') 
label.pack(side='left') 
window.mainloop()




import tkinter.filedialog as dialog
def save(root, text):
    data = text.get('0.0', tkinter.END) 
    filename = dialog.asksaveasfilename(
        parent=root, 
        filetypes=[('Text', '*.txt')], 
        title='Save as...')
    writer = open(filename, 'w') 
    writer.write(data) 
    writer.close()

def quit(root): 
    root.destroy()

window = tkinter.Tk()
text = tkinter.Text(window)
text.pack()
menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label='Save', command=lambda : save(window, text)) 
filemenu.add_command(label='Quit', command=lambda : quit(window))
menubar.add_cascade(label = 'File', menu=filemenu) 
window.config(menu=menubar)
window.mainloop()