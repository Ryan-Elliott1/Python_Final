"""
Program: client_gui.py
Author: Ryan Elliott
Last date modified: 08/2/2020
Client gui and database
"""
import sqlite3
from sqlite3 import Error
from tkinter import *


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):

    sql_create_client_table = """ CREATE TABLE IF NOT EXISTS client (
                                        id integer PRIMARY KEY,
                                        lastname text NOT NULL,
                                        firstname text NOT NULL,
                                        phonenumber text NOT NULL,
                                        address text NOT NULL,
                                        appointment text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create client table
        create_table(conn, sql_create_client_table)
    else:
        print("Unable to connect to " + str(database))


def create_client(conn, client):
    """Create a new client for table
    :param conn:
    :param client:
    """
    client = (entry_last_name.get(), entry_first_name.get(), entry_phone_number.get(), entry_address.get(), entry_appointment_time.get())
    sql = ''' INSERT INTO client(lastname,firstname,phonenumber,address,appointment)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, client)
    return cur.lastrowid # returns the row id of the cursor object, the person id


def create_all():
    create_tables("pythonsqlite.db")
    conn = create_connection("pythonsqlite.db")


def select_all_clients(conn):
    """Query all rows of client table
    :param conn: the connection object
    """
    label_display.config(text="")
    cur = conn.cursor()
    cur.execute("SELECT lastname,firstname,phonenumber,address,appointment FROM client")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        label_display.config(text=label_display.cget('text') + convert_tuple(row))


def select_appointment_times(conn):
    """Query firstname, lastname and appointment of client table
    :param conn: the connection object
    """
    label_display.config(text="")
    cur = conn.cursor()
    cur.execute("SELECT firstname, lastname, appointment FROM client")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        label_display.config(text=label_display.cget('text') + convert_tuple(row))
        

def convert_tuple(tuple):
    """converts a tuple into a string
    :param tuple: the tuple database object
    """
    str =  ''.join(tuple)
    return str


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")

    m = Tk()
    m.title('Client GUI')
    # create database button and label
    create_database_and_table = Button(m, text="Create Database", width=15, command=create_all, state="normal")
    create_database_and_table.grid(row = 9, column = 1, pady = 2)

    # first name label and entry box
    label_first_name = Label(m, text="Firstname:")
    label_first_name.grid(row=1, column = 0, sticky = W, pady = 2)
    entry_first_name = Entry(m)
    entry_first_name.grid(row = 1, column = 1, pady = 2)

    # last name label and entry box
    label_last_name = Label(m, text="Lastname:")
    label_last_name.grid(row=2, column = 0, sticky = W, pady = 2)
    entry_last_name = Entry(m)
    entry_last_name.grid(row = 2, column = 1, pady = 2)

    # phone number label and entry box
    label_phone_number = Label(m, text="Phone Number:")
    label_phone_number.grid(row=3, column = 0, sticky = W, pady = 2)
    entry_phone_number = Entry(m)
    entry_phone_number.grid(row = 3, column = 1, pady = 2)

    # address label and entry box
    label_address = Label(m, text="Address:")
    label_address.grid(row=4, column = 0, sticky = W, pady = 2)
    entry_address = Entry(m)
    entry_address.grid(row = 4, column = 1, pady = 2)

    # appointment label and entry box
    label_appointment_time = Label(m, text="Appointment Time:")
    label_appointment_time.grid(row=5, column = 0, sticky = W, pady = 2)
    entry_appointment_time = Entry(m)
    entry_appointment_time.grid(row = 5, column = 1, pady = 2)

    # create client button
    client_add = (entry_last_name.get(), entry_first_name.get(), entry_phone_number.get(), entry_address.get(), entry_appointment_time.get())
    button_create_client = Button(m, text="Add Client", width=15, command=lambda : create_client(conn, client_add), state="normal")
    button_create_client.grid(row = 6, column = 1, pady = 2)

    # view client label and button
    button_view_client_table = Button(m, text="View Client Table", width=15, command=lambda : select_all_clients(conn), state="normal")
    button_view_client_table.grid(row = 7, column = 1, pady = 2)

    # view client appointments label and button
    button_view_appointments = Button(m, text="View Appointments", width=15, command=lambda : select_appointment_times(conn), state="normal")
    button_view_appointments.grid(row = 8, column = 1, pady = 2)

    label_display = Label(m, text="")
    label_display.grid(row=1, column = 2, sticky = W, pady = 2)

    # exit button
    exit_button = Button(m, text='Exit', width=15, command=m.destroy)
    exit_button.grid(row = 10, column = 1, pady = 2)
    m.mainloop()
