from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')

def calculate_bmi():
    try:
        w = float(weight_tf.get())
        h = float(height_tf.get()) / 100
        bmi = w / (h * h)
        bmi = round(bmi, 1)
        bmi_index(bmi)
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numerical values for height and weight.')

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Result', f'Your BMI: {bmi}\nYou are Underweight')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo('BMI Result', f'Your BMI: {bmi}\nYou have Normal weight')
    elif 24.9 <= bmi < 29.9:
        messagebox.showinfo('BMI Result', f'Your BMI: {bmi}\nYou are Overweight')
    else:
        messagebox.showinfo('BMI Result', f'Your BMI: {bmi}\nYou are Obese')

# Create main window
ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x300')
ws.config(bg='#686e70')

# Create a frame
frame = Frame(ws, padx=10, pady=10, bg='#b5c3c5')  # Changed background color
frame.pack(expand=True)

# Labels and Entry for age
age_lb = Label(frame, text='Enter Age(2-100)', bg='#b5c3c5')  # Updated label background color
age_lb.grid(row=1, column=1)
age_tf = Entry(frame)
age_tf.grid(row=1, column=2, pady=5)

# Gender Selection
gen_lb = Label(frame, text='Select Gender', bg='#b5c3c5')  # Updated label background color
gen_lb.grid(row=2, column=1)
frame2 = Frame(frame, bg='#b5c3c5')  # Updated frame background color
frame2.grid(row=2, column=2, pady=5)
var = IntVar()
male_rb = Radiobutton(frame2, text='Male', variable=var, value=1, bg='#b5c3c5')  # Updated radio button background color
male_rb.pack(side=LEFT)
female_rb = Radiobutton(frame2, text='Female', variable=var, value=2, bg='#b5c3c5')  # Updated radio button background color
female_rb.pack(side=RIGHT)

# Labels and Entry for height and weight
height_lb = Label(frame, text='Enter height in cm:', bg='#b5c3c5')  # Updated label background color
height_lb.grid(row=3, column=1)
weight_lb = Label(frame, text='Enter weight in kg:', bg='#b5c3c5')  # Updated label background color
weight_lb.grid(row=4, column=1)
height_tf = Entry(frame)
height_tf.grid(row=3, column=2, pady=5)
weight_tf = Entry(frame)
weight_tf.grid(row=4, column=2, pady=5)

# Buttons
frame3 = Frame(frame, bg='#b5c3c5')  # Updated frame background color
frame3.grid(row=5, columnspan=3, pady=10)
cal_btn = Button(frame3, text='Calculate', command=calculate_bmi)
cal_btn.pack(side=LEFT)
reset_btn = Button(frame3, text='Reset', command=reset_entry)
reset_btn.pack(side=LEFT)
exit_btn = Button(frame3, text='Exit', command=ws.destroy)
exit_btn.pack(side=RIGHT)

# Adding an image
photo = PhotoImage(file="image.png")  # Change "image.png" to your actual image file
image_label = Label(frame, image=photo, bg='#b5c3c5')
image_label.grid(row=6, columnspan=3, pady=10)

# Start the GUI
ws.mainloop()
