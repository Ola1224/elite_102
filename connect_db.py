import mysql.connector 

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Tenamm24!!',
        database = 'elite_bank'

    )
    

import tkinter as tk

mydb = connect_to_db()

# create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# create the main window
window = tk.Tk()
window.title("Halal Bank")

# create the labels and entry widgets for the username and balance
username_label = tk.Label(window, text="Username:")
username_label.grid(column=0, row=0)
username_entry = tk.Entry(window)
username_entry.grid(column=1, row=0)

balance_label = tk.Label(window, text="Balance:")
balance_label.grid(column=0, row=1)
balance_value = tk.StringVar()
balance_value.set("0")
balance_entry = tk.Entry(window, textvariable=balance_value, state="readonly")
balance_entry.grid(column=1, row=1)

# function to retrieve the user's balance from the database
def get_balance():
    # execute the SQL query to retrieve the user's balance
    mycursor.execute("SELECT balance FROM users WHERE username = %s", (username_entry.get(),))
    result = mycursor.fetchone()

    # update the balance entry widget with the user's balance
    if result:
        balance_value.set(result[0])
        return result[0]

# function to update the user's balance in the database
def update_balance(amount):
    # get the current balance from the balance entry widget
    balance = int(get_balance())

    # calculate the new balance
    new_balance = balance + amount

    # update the balance entry widget with the new balance
    balance_value.set(new_balance)

    # execute the SQL query to update the user's balance in the database
    mycursor.execute("UPDATE users SET balance = %s WHERE username = %s", (new_balance, username_entry.get()))

    # commit the changes to the database
    mydb.commit()

# create the deposit and withdrawal buttons
deposit_button = tk.Button(window, text="Deposit", command=lambda: update_balance(int(deposit_entry.get())))
deposit_button.grid(column=0, row=2)

deposit_entry = tk.Entry(window)
deposit_entry.grid(column=1, row=2)

withdraw_button = tk.Button(window, text="Withdraw", command=lambda: update_balance(-int(withdraw_entry.get())))
withdraw_button.grid(column=0, row=3)

withdraw_entry = tk.Entry(window)
withdraw_entry.grid(column=1, row=3)

# create the get balance button
balance_button = tk.Button(window, text="Get Balance", command=get_balance)
balance_button.grid(column=2, row=1)

# run the main loop of the GUI
window.mainloop()
