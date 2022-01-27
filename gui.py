from tkinter import *

window = Tk()
window.title("VREMENSKA PROGNOZA")
window.geometry('500x300')

emptylabel = Label(window, text="VREMENSKA PROGNOZA")
emptylabel.grid( row=10, column=1,sticky=W)

label1 = Label(window, text='Enter city name', fg='blue', font=('Arial', 14))
label1.grid(row=0, column=0, padx=5, pady=10)

data = StringVar()
data2 = data
data2 = open('temp1.txt', 'r')


textbox1 = Entry(window, textvariable=data, fg='blue', font=('Arial', 14))
textbox1.grid(row=0, column=1)



def myfunction():
    city_info = data.get()
    a1 = open('city.dat', 'w')
    a1.write(data.get())
    a1.close()
    print(city_info)
    print(data2.read())
    import os
    os.system('python main.py')
    with open("temp1.txt", "r") as t:
        emptylabel.config(text=t.read())



button1 = Button(window, command=myfunction(), text='Check weather',fg='blue', font=('Arial', 14))
button1.grid(row=0, column=2, sticky=W)




window.mainloop()