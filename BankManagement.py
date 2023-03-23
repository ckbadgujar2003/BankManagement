from tkinter import *
import os
from PIL import ImageTk, Image

# Main window
window = Tk()
window.title('MyBank')

# App name and Image insertion
img = Image.open('img.png')
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)
Label(window, text='MyBank', font=("Times", 22, "bold italic")).grid()
Label(window, text="Your money is safe with us!", font=("Times", 16)).grid()
Label(window, image=img, background='black').grid()
Label(window, text=" ").grid()


# Register window
def register():
    global registerWindow
    global registerUsername
    global registerAge
    global registerGender
    global registerEmail
    global registerMobile
    global registerPassword
    global forgotPassword
    global a

    registerUsername = StringVar()
    registerAge = StringVar()
    registerGender = StringVar()
    registerEmail = StringVar()
    registerMobile = StringVar()
    registerPassword = StringVar()
    forgotPassword = StringVar()

    registerWindow = Toplevel(window)
    registerWindow.title("Register window")
    Label(registerWindow, text='Registration', justify=CENTER, font=("Times", 22, "bold italic")).grid(columnspan=5)
    l = Label(registerWindow, text="Enter your details")
    l.grid(row=1, column=1, columnspan=2, padx=15, pady=15)
    l = Label(registerWindow, text="Username:")
    l.grid(row=2, column=1, sticky=W, padx=15)
    e = Entry(registerWindow, textvariable=registerUsername)
    e.grid(row=2, column=2, padx=15, pady=10)
    l = Label(registerWindow, text="Age:")
    l.grid(row=3, column=1, sticky=W, padx=15)
    e = Entry(registerWindow, textvariable=registerAge)
    e.grid(row=3, column=2, padx=15, pady=10)
    l = Label(registerWindow, text="Gender:")
    l.grid(row=4, column=1, sticky=W, padx=15)
    e = Entry(registerWindow, textvariable=registerGender)
    e.grid(row=4, column=2, padx=15, pady=10)
    l = Label(registerWindow, text="Email ID:")
    l.grid(row=5, column=1, sticky=W, padx=15)
    e = Entry(registerWindow, textvariable=registerEmail)
    e.grid(row=5, column=2, padx=15, pady=10)
    l = Label(registerWindow, text="Mobile No.:")
    l.grid(row=6, column=1, sticky=W, padx=15)
    e = Entry(registerWindow, textvariable=registerMobile)
    e.grid(row=6, column=2, padx=15, pady=10)
    l = Label(registerWindow, text="Password:")
    l.grid(row=7, column=1, sticky=W, padx=15)
    e = Entry(registerWindow, show="*", textvariable=registerPassword)
    e.grid(row=7, column=2, padx=15, pady=10)
    l = Label(registerWindow, text="Security Q: What is your favorite color?")
    l.grid(row=8, column=1, sticky=W, padx=15)
    e = Entry(registerWindow, textvariable=forgotPassword)
    e.grid(row=8, column=2, padx=15, pady=10)
    b = Button(registerWindow, text="Register", font=("Times", 10),bg='light green',activebackground= 'green', width=10, height=1, command=click_reg)
    b.grid(row=9, column=1, pady=10)
    b = Button(registerWindow, text="Close", font=("Times", 10,'bold'), bg='pink',activebackground= 'red', width=10, height=1, command=registerWindow.destroy)
    b.grid(row=9, column=2, pady=10)
    a = Label(registerWindow)
    a.grid(row=10, columnspan=5, padx=10, pady=10)


def click_reg():
    username = registerUsername.get()
    age = registerAge.get()
    gender = registerGender.get()
    email = registerEmail.get()
    mobile = registerMobile.get()
    password = registerPassword.get()
    forgot = forgotPassword.get()
    account = os.listdir()

    if username == '' or age == '' or gender == '' or email == '' or mobile == '' or password == '' or forgot == '':
        a.config(fg='red', text='*All fields required*')
        return

        # while (True):
        #     try:
        #         email.split('@')
        #     except:
        #         a.config(text="Enter proper email id")

        for check_email in account:
            if email == check_email:
                a.config(fg='red', text='Account already exists')
            return
        else:
            file = open(email, 'w')
            file.write(username + '\n')
            file.write(age + '\n')
            file.write(gender + '\n')
            file.write(email + '\n')
            file.write(mobile + '\n')
            file.write(password + '\n')
            file.write(forgot + '\n')
            file.write('0.0')
            file.close()
            a.config(text='Account created successfully :)', fg='green')


# Login window
def login():
    global loginUsername
    global loginPassword
    global a
    global loginWindow

    loginUsername = StringVar()
    loginPassword = StringVar()

    loginWindow = Toplevel(window)
    loginWindow.title("Login Window")
    Label(loginWindow, text='Login', justify=CENTER, font=("Times", 22, "bold italic")).grid(columnspan=5)
    Label(loginWindow, text="Enter login credentials").grid(row=1, columnspan=2, pady=12, padx=12)
    Label(loginWindow, text="E-mail ID:").grid(row=2, column=0, padx=12)
    Label(loginWindow, text="Password:").grid(row=3, column=0, padx=12)

    Entry(loginWindow, textvariable=loginUsername).grid(row=2, column=1, pady=12, padx=10)
    Entry(loginWindow, textvariable=loginPassword, show='*').grid(row=3, column=1, pady=12, padx=10)

    loginButton = Button(loginWindow, text="Login", font=("Times", 10), activebackground='green',bg='light green', width=13, height=1, command=click_login)
    loginButton.grid(row=4, column=0, padx=15, pady=10)
    b = Button(loginWindow, text="Forgot Password", font=("Times", 10), activebackground='yellow',bg='light yellow', width=13, height=1, command=forgot_password)
    b.grid(row=4, column=1, padx=5, pady=10)
    b = Button(loginWindow, text="Close", font=("Times", 10,'bold'), bg='pink',activebackground= 'red', width=10, height=1, command=loginWindow.destroy)
    b.grid(row=5, column=0, columnspan=5, pady=10)
    a = Label(loginWindow)  # Empty Label
    a.grid(row=6, columnspan=5, padx=10, pady=10)


def accDetailsWindowCall():
    loginWindow.destroy()
    accDetailsWindow = Toplevel(window)
    accDetailsWindow.title('Account Details')

    Label(accDetailsWindow, text='Account Details', justify=CENTER, font=("Times", 22, "bold italic")).grid(
        columnspan=5, padx=10)
    Label(accDetailsWindow, text="Welcome to MyBank", justify=CENTER, font=("Times", 15)).grid(pady=10,
                                                                                               padx=10)
    Label(accDetailsWindow, text='Select your choice:', justify=CENTER, font=("Times", 11)).grid(padx=5)
    Label(accDetailsWindow, text="").grid()
    Button(accDetailsWindow, text="Personal Details", font=("Times", 12), width=15, height=1, command=personal).grid(
        column=0, columnspan=2, pady=4)
    Button(accDetailsWindow, text="Deposit", font=("Times", 12), width=15, height=1, command=deposit).grid(column=0,columnspan=2,pady=4)
    Button(accDetailsWindow, text="Withdraw", font=("Times", 12), width=15, height=1, command=withdraw).grid(column=0,columnspan=2,pady=4)
    Button(accDetailsWindow, text="Transfer", font=("Times", 12), width=15, height=1, command=transfer).grid(column=0,columnspan=2,pady=4)


def click_login():
    global username
    username = loginUsername.get()
    password = loginPassword.get()
    accounts = os.listdir()

    if username == '' or password == '':
        a.config(text="*Enter all credentials*", fg='red')
        return

    for name in accounts:
        if name == username:
            file = open(name, "r")
            data = file.read()
            data = data.split('\n')
            isPassword = data[5]

            # Account Details Window
            if isPassword == password:
                accDetailsWindowCall()
                return
            else:
                a.config(text='*Incorrect username or password!*', fg='red')
                return
    a.config(text='*No account found!*', fg='red')


def forgot_password():
    global forgotpasswordWindow
    global entry2
    global entry
    forgotpasswordWindow = Toplevel(window)
    forgotpasswordWindow.title("Forgot Password")
    Label(forgotpasswordWindow, text='Forgot Password', justify=CENTER, font=("Times", 22, "bold italic")).grid(row=0, column=0,columnspan=5)
    l = Label(forgotpasswordWindow, text='Email ID: ')
    l.grid(row=1, column=0, padx=10)
    entry2 = Entry(forgotpasswordWindow)
    entry2.grid(row=2, column=1, padx=10)
    Label(forgotpasswordWindow,text='')
    l.grid(row=2, column=0, padx=10)
    l = Label(forgotpasswordWindow, text='Security Q:', fg='red', font=('Times', 8))
    l.grid(row=3, column=0, padx=10)
    l = Label(forgotpasswordWindow, text="What is your favorite color?")
    l.grid(row=4, column=0, padx=10)
    entry = Entry(forgotpasswordWindow)
    entry.grid(row=4, column=1, columnspan=8)
    b = Button(forgotpasswordWindow, text='Done', command=click_forgot)
    b.grid(row=5, columnspan=8, pady=10)


def click_forgot():
    global a1
    global username
    a1 = Label(forgotpasswordWindow, text='')
    a1.grid(column=0,row=7, columnspan=2, pady=10)
    global forgetpassword
    accounts = os.listdir()
    username = entry2.get()
    if username == '' or entry == '':
        a1.config(text="*Enter your details*", fg='red')
        return
    for name in accounts:
        if name == username:
            file = open(name, "r")
            data = file.read()
            data = data.split('\n')
            forgetpassword = data[6]

            # Account Details Window
            if forgetpassword == entry.get():
                forgotpasswordWindow.destroy()
                accDetailsWindowCall()
                return
            else:
                a1.config(text='*Incorrect username or answer!*', fg='red')
                return
        else:
            a1.config(text='           *No account found!*           ', fg='red')


def personal():
    file = open(username, "r")
    data = file.read()
    accDetails = data.split('\n')
    accDetails_username = accDetails[0]
    accDetails_age = accDetails[1]
    accDetails_gender = accDetails[2]
    accDetails_email = accDetails[3]
    accDetails_mobile = accDetails[4]
    accDetails_balance = accDetails[7]

    personalDetailsWindow = Toplevel(window)
    personalDetailsWindow.title('Personal Details')
    Label(personalDetailsWindow, text='Personal Details', font=("Times", 22, "bold italic")).grid(padx=15)
    Label(personalDetailsWindow, text="Username :\t" + accDetails_username).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="Age :\t\t" + accDetails_age).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="Gender :\t\t" + accDetails_gender).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="E-mail :\t\t" + accDetails_email).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="Mobile :\t\t" + accDetails_mobile).grid(sticky=W, padx=10)
    Label(personalDetailsWindow, text="Balance :\t\t\u20B9 " + accDetails_balance).grid(sticky=W, padx=10)


def deposit():
    global amt
    global l1
    global l3
    amt = StringVar()
    depositWindow = Toplevel(window)
    depositWindow.title("Deposit Window")
    Label(depositWindow, text='Deposit', justify=CENTER, font=("Times", 22, "bold italic")).grid(columnspan=5)
    file = open(username, "r")
    data = file.read()
    accDetails = data.split('\n')
    l1 = Label(depositWindow, text="Current Balance:\t\t\u20B9 " + accDetails[7])
    l1.grid(row=2, column=1, sticky=W, padx=10)
    l2 = Label(depositWindow, text="Amount to deposit:\t\u20B9 ")
    l2.grid(row=3, column=1, sticky=W, padx=10)
    e1 = Entry(depositWindow, width=15, borderwidth=2, textvariable=amt)
    e1.grid(row=3, column=2, sticky=W, padx=10)
    b = Button(depositWindow, text="Deposit", height=1, width=6, justify=CENTER, command=done_deposit)
    b.grid(row=4, columnspan=4)
    l3 = Label(depositWindow, justify=CENTER)
    l3.grid(row=5, columnspan=4)


def done_deposit():
    file = open(username, "r+")  # r+ to open file in read and write mode
    data = file.read()
    accDetails = data.split('\n')
    old_balance = accDetails[7]
    # new_balance = old_balance
    if amt.get() == "" or float(amt.get()) <= 0:
        l3.config(text="*Amount cannot be deposited*\n*Please enter proper figure*", fg="red")
        return
    new_balance = float(old_balance) + float(amt.get())
    data = data.replace(old_balance, str(new_balance))
    file.seek(0)
    file.truncate(0)
    file.write(data)
    file.close()

    l1.config(text="Current Balance:\t\tRs." + str(new_balance), fg="purple")
    l3.config(text="Transaction successful :) ", fg="green")


def withdraw():
    global amt
    global l1
    global l3
    amt = StringVar()
    withdrawWindow = Toplevel(window)
    withdrawWindow.title("Withdraw Window")
    Label(withdrawWindow, text='Withdraw', justify=CENTER, font=("Times", 22, "bold italic")).grid(columnspan=5)
    file = open(username, "r")
    data = file.read()
    accDetails = data.split('\n')
    l1 = Label(withdrawWindow, text="Current Balance:\t\t\u20B9 " + accDetails[7])
    l1.grid(row=2, column=1, sticky=W, padx=10)
    l2 = Label(withdrawWindow, text="Amount to withdraw:\t\u20B9 ")
    l2.grid(row=3, column=1, sticky=W, padx=10)
    e1 = Entry(withdrawWindow, width=15, borderwidth=2, textvariable=amt)
    e1.grid(row=3, column=2, sticky=W, padx=10)
    b = Button(withdrawWindow, text="Withdraw", height=1, width=8, justify=CENTER, command=done_withdraw)
    b.grid(row=4, columnspan=4)
    l3 = Label(withdrawWindow, justify=CENTER)
    l3.grid(row=5, columnspan=4)


def done_withdraw():
    file = open(username, "r+")  # r+ to open file in read and write mode
    data = file.read()
    accDetails = data.split('\n')
    old_balance = accDetails[7]
    # new_balance = old_balance
    if amt.get() == "" or float(amt.get()) <= 0:
        l3.config(text="*Amount cannot be withdrawn*\n*Please enter proper figure*", fg="red")
        return

    elif float(old_balance) < float(amt.get()):
        l3.config(text="*Amount cannot be withdrawn*\n*Insufficient Balance*", fg="red")
        return

    else:
        new_balance = float(old_balance) - float(amt.get())
        data = data.replace(old_balance, str(new_balance))
        file.seek(0)
        file.truncate(0)
        file.write(data)
        l1.config(text="Current Balance:\t\tRs." + str(new_balance), fg="purple")
        l3.config(text="Transaction successful :) ", fg="green")
        file.close()

def transfer():
    global l1
    global l4
    global amt
    global username_recipient
    username_recipient = StringVar()
    amt = StringVar()
    transferWindow = Toplevel(window)
    transferWindow.title("Transfer Window")
    Label(transferWindow, text='Transfer', justify=CENTER, font=("Times", 22, "bold italic")).grid(columnspan=5)
    file = open(username, "r")
    data = file.read()
    accDetails = data.split('\n')
    l1 = Label(transferWindow, text="Current Balance:\t\tRs." + accDetails[7])
    l1.grid(row=2, column=1, sticky=W, padx=10)
    l3 = Label(transferWindow, text="E-mail ID of recipient:")
    l3.grid(row=3, column=1, sticky=W, padx=10)
    e2 = Entry(transferWindow, width=15, borderwidth=2, textvariable=username_recipient)
    e2.grid(row=3, column=2, sticky=W, padx=10)
    l2 = Label(transferWindow, text="Amount to tranfer:\tRs.")
    l2.grid(row=4, column=1, sticky=W, padx=10)
    e1 = Entry(transferWindow, width=15, borderwidth=2, textvariable=amt)
    e1.grid(row=4, column=2, sticky=W, padx=10)
    b = Button(transferWindow, text="Transfer", height=1, width=8, justify=CENTER, command=done_transfer)
    b.grid(row=5, columnspan=4)
    l4 = Label(transferWindow, justify=CENTER)
    l4.grid(row=6, columnspan=4)


def done_transfer():
    accounts = os.listdir()
    recipient = username_recipient.get()
    for names in accounts:
        if names == recipient:
            file = open(username, "r+")  # r+ to open file in read and write mode
            data = file.read()
            accDetails = data.split('\n')
            old_balance = accDetails[7]
            new_balance = old_balance
            new_balance = float(new_balance) - float(amt.get())
            if amt.get() == "" or float(amt.get()) <= 0:
                l4.config(text="Amount cannot be transfered\nPlease enter proper figure", fg="red")
                return
            if float(amt.get()) > float(new_balance):
                l4.config(text="Amount cannot be withdrawn\nInsufficient Balance", fg="red")
                return
            if username_recipient.get() == '':
                l4.config(text="Enter proper details", fg="red")

            data = data.replace(old_balance, str(new_balance))
            file.seek(0)
            file.truncate(0)
            file.write(data)
            file.close()

            l1.config(text="Current Balance:\t\tRs." + str(new_balance), fg="purple")
            l4.config(text="Transaction successful :) ", fg="green")
            file1 = open(recipient, "r+")  # r+ to open file in read and write mode
            data1 = file1.read()
            accDetails = data1.split('\n')
            old_balance = accDetails[7]
            new_balance = old_balance
            new_balance = float(new_balance) + float(amt.get())
            data1 = data1.replace(old_balance, str(new_balance))
            file1.seek(0)
            file1.truncate(0)
            file1.write(data1)
            file1.close()
            return

    l4.config(text="No account found", fg="red")


# Buttons
Button(window, text="Login", font=('Times', 18), width=20, borderwidth=5,activebackground= 'sky blue', command=login).grid()
Label(window, text="Not registered yet?\nGet registered here", fg='red', font=('Calibri', 10)).grid()
Button(window, text="Register", font=('Times', 18), width=20,activebackground= 'crimson', borderwidth=5, command=register).grid()

window.mainloop()