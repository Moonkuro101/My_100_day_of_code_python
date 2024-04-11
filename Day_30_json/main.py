from tkinter import *
from tkinter import messagebox
from random import shuffle , randint ,choice
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    #Password Generator Project
    Entry_Password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]


    # for char in range(nr_letters):
    #   password_list.append(choice(letters))

    # for char in range(nr_symbols):
    #   password_list += choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += choice(numbers)

    password_list = password_letter+password_symbols+password_numbers
    shuffle(password_list)

    delimiter = ""
    password = delimiter.join(password_list)
    Entry_Password.insert(0,password)
    pyperclip.copy(password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def Add():
    Web = Entry_web.get()
    Email = Entry_Email.get()
    Password = Entry_Password.get()
    data = { Web : 
                {"email" : Email , 
                 "Password" : Password
                 }
                }
    if not Web or not Email  or not Password:
        messagebox.showerror(title="You left something",message="Plese insert everything in the Entry")
    else:
    #     is_ok = messagebox.askokcancel(title="Want to save?",message=f"Do you want to save this \nwebsite : {Web}\nEmail : {Email}\nPassword : {Password}")
    # # messagebox.showinfo(title='Save',message='Do you what to save')
    #     if is_ok:
        try:
            with open("my_password.json",mode='r') as save_pass:
             #Read
             data_pass = json.load(save_pass)
        except FileNotFoundError:
            with open("my_password.json",mode='w') as save_pass:
                json.dump(data,save_pass,indent=4)
        #Update
        else:
            data_pass.update(data)
                #Writing
            with open("my_password.json",mode='w') as save_pass:
                json.dump(data_pass,save_pass,indent=4)
        
        Entry_web.delete(0,END)
        Entry_Password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
def search():
    try:
        with open("my_password.json",mode='r') as save_pass:
             #Read
             data_pass = json.load(save_pass)
    except FileExistsError:
        messagebox.showerror(title="You Didn't have this file",message="Let's create some password")
    else:
        Web = Entry_web.get()
        if not Web:
            messagebox.showerror(title="You left the Web",message="Insert the Web")
        else:
            try:
                Email = data_pass[Web]["email"]
                Password = data_pass[Web]["Password"]
                messagebox.showinfo(title="Your Email and Password",message= f"Email : { Email }\nPassword : { Password }")
                pyperclip.copy(Password)
            except KeyError:
                messagebox.showerror(title="There is no web in password",message=f"There no data {Web} find")

window = Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

Web = Label(text='Website',font=('Courier',10,'bold'))
Web.grid(column=0,row=1)

Entry_web = Entry(width=21)
Entry_web.grid(column=1,row=1,columnspan=1)
Entry_web.focus()

Email = Label(text='Email/Username',font=('Courier',10,'bold'))
Email.grid(column=0,row=2)

search = Button(text="Search",font=('Courier',10,'bold'),command=search,width=10)
search.grid(column=2,row=1,columnspan=2)


Entry_Email = Entry(width=35)
Entry_Email.grid(column=1,row=2,columnspan=2)
Entry_Email.insert(0,'songpontonku@gmail.com')

Password = Label(text='Password',font=('Courier',10,'bold'))
Password.grid(column=0,row=3)


Entry_Password = Entry(width=21)
Entry_Password.grid(column=1,row=3)

generate = Button(text="Genertate",font=('Courier',10,'bold'),command=generate)
generate.grid(column=2,row=3,columnspan=2)

add_button = Button(text="add",width=36,font=('Courier',10,'bold'),command=Add)
add_button.grid(column=1,row=4,columnspan=2)
window.mainloop()