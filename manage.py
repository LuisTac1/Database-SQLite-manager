import sqlite3
import pandas as pd

# connects with the file
database = sqlite3.connect('partners_list.db')
cursor = database.cursor()

# create the file
sql_query = "CREATE TABLE IF NOT EXISTS partners (name TEXT, surname TEXT, age INT, phone TEXT, e_mail TEXT)"
cursor.execute(sql_query)


def type_inf():
    # create columns and index
    first_name = str(input('Type first name:').capitalize())
    last_name = str(input('Type last name: ').capitalize())
    age = str(input('Type age: ').capitalize())
    phone = str(input('Type phone number: ').capitalize())
    e_mail = str(input('Type e-mail: ').capitalize())

    # add columns and index in file
    sql_query = "INSERT INTO partners (name, surname, age, phone, e_mail) VALUES (?,?,?,?,?)"
    cursor.execute(sql_query, (first_name, last_name, age, phone, e_mail))
    database.commit()
    return type_inf


def read_all():
    # Read sqlite query results into a pandas DataFrame
    df = pd.read_sql_query("SELECT * from partners", database)

    # Verify that result of SQL query is stored in the dataframe
    print(df.head())
    return read_all


def read_one():
    column = str(input("Column name: ")).lower()

    # select an item according to the column name
    df = pd.read_sql_query(f"SELECT name from partners", database)

    # Verify that result of SQL query is stored in the dataframe
    print(df.head())
    return read_one

import gui
