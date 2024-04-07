import sqlite3
import pandas as pd


# Select the title of the table entered using json
import json
# JSON read file
with open('entry.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    

databank = json_object['databank']
table = json_object['table']
name = json_object['name'].upper()
surname = json_object['surname'].upper()
age = json_object['age'].upper()
gender = json_object['gender'].upper()
email = json_object['email'].upper()
number = json_object['number'].upper()


# Connects with the file
database = sqlite3.connect(f'{databank}.db')
cursor = database.cursor()

def read_column():
    # Select an item according to the column name
    nm = pd.read_sql_query(f"SELECT {name} from {table}", database)
    sm = pd.read_sql_query(f"SELECT {surname} from {table}", database)
    ag = pd.read_sql_query(f"SELECT {age} from {table}", database)
    gd = pd.read_sql_query(f"SELECT {gender} from {table}", database)
    em = pd.read_sql_query(f"SELECT {email} from {table}", database)
    nb = pd.read_sql_query(f"SELECT {number} from {table}", database)

    # Verify that result of SQL query is stored in the dataframe
    for i in nm:
        global r_name
        r_name = i

    for i in sm:
        global r_surname
        r_surname = i

    for i in ag:
        global r_age
        r_age = i

    for i in gd:
        global r_gender
        r_gender = i
        
    for i in em:
        global r_email
        r_email = i

    for i in nb:
        global r_number
        r_number = i
read_column()


# select data from table
def read_name():
    data_name = f"SELECT {name} from {table}"
    cursor.execute(data_name)
    global name_row1
    name_row1 = cursor.fetchone()
    global name_row2
    name_row2 = cursor.fetchone()
    global name_row3
    name_row3 = cursor.fetchone()
    global name_row4
    name_row4 = cursor.fetchone()
    global name_row5
    name_row5 = cursor.fetchone()
    global name_row6
    name_row6 = cursor.fetchone()
    global name_row7
    name_row7 = cursor.fetchone()
    global name_row8
    name_row8 = cursor.fetchone()
    global name_row9
    name_row9 = cursor.fetchone()    
    global name_row10
    name_row10 = cursor.fetchone()
read_name()


def read_surname():
    data_surname = f"SELECT {surname} from {table}"
    cursor.execute(data_surname)

    global surname_row1
    surname_row1 = cursor.fetchone() 
    global surname_row2
    surname_row2 = cursor.fetchone()
    global surname_row3
    surname_row3 = cursor.fetchone()
    global surname_row4
    surname_row4 = cursor.fetchone()
    global surname_row5
    surname_row5 = cursor.fetchone()
    global surname_row6
    surname_row6 = cursor.fetchone()    
    global surname_row7
    surname_row7 = cursor.fetchone() 
    global surname_row8
    surname_row8 = cursor.fetchone() 
    global surname_row9
    surname_row9 = cursor.fetchone()
    global surname_row10
    surname_row10 = cursor.fetchone() 
read_surname()


def read_age():
    data_age = f"SELECT {age} from {table}"
    cursor.execute(data_age)

    global age_row1
    age_row1 = cursor.fetchone()
    global age_row2
    age_row2 = cursor.fetchone()
    global age_row3
    age_row3 = cursor.fetchone()
    global age_row4
    age_row4 = cursor.fetchone()
    global age_row5
    age_row5 = cursor.fetchone()
    global age_row6
    age_row6 = cursor.fetchone()
    global age_row7
    age_row7 = cursor.fetchone()
    global age_row8
    age_row8 = cursor.fetchone()
    global age_row9
    age_row9 = cursor.fetchone()
    global age_row10
    age_row10 = cursor.fetchone()
read_age()


def read_gender():
    data_gender = f"SELECT {gender} from {table}"
    cursor.execute(data_gender)

    global gender_row1
    gender_row1 = cursor.fetchone()
    global gender_row2
    gender_row2 = cursor.fetchone()
    global gender_row3
    gender_row3 = cursor.fetchone()
    global gender_row4
    gender_row4 = cursor.fetchone()
    global gender_row5
    gender_row5 = cursor.fetchone()
    global gender_row6
    gender_row6 = cursor.fetchone()
    global gender_row7
    gender_row7 = cursor.fetchone()
    global gender_row8
    gender_row8 = cursor.fetchone()
    global gender_row9
    gender_row9 = cursor.fetchone()
    global gender_row10
    gender_row10 = cursor.fetchone()
read_gender()


def read_email():
    data_email = f"SELECT {email} from {table}"
    cursor.execute(data_email)

    global email_row1
    email_row1 = cursor.fetchone()
    global email_row2
    email_row2 = cursor.fetchone()
    global email_row3
    email_row3 = cursor.fetchone()
    global email_row4
    email_row4 = cursor.fetchone()
    global email_row5
    email_row5 = cursor.fetchone()
    global email_row6
    email_row6 = cursor.fetchone()
    global email_row7
    email_row7 = cursor.fetchone()
    global email_row8
    email_row8 = cursor.fetchone()
    global email_row9
    email_row9 = cursor.fetchone()
    global email_row10
    email_row10 = cursor.fetchone()
read_email()

def read_number():
    data_number = f"SELECT {number} from {table}"
    cursor.execute(data_number)

    global number_row1
    number_row1 = cursor.fetchone()
    global number_row2
    number_row2 = cursor.fetchone()
    global number_row3
    number_row3 = cursor.fetchone()
    global number_row4
    number_row4 = cursor.fetchone()
    global number_row5
    number_row5 = cursor.fetchone()
    global number_row6
    number_row6 = cursor.fetchone()
    global number_row7
    number_row7 = cursor.fetchone()
    global number_row8
    number_row8 = cursor.fetchone()
    global number_row9
    number_row9 = cursor.fetchone()
    global number_row10
    number_row10 = cursor.fetchone()
read_number()



# def read_one():
#     column = str(input("Column name: ")).lower()

#     # select an item according to the column name
#     df = pd.read_sql_query(f"SELECT {column} from partners", database)

#     # Verify that result of SQL query is stored in the dataframe
#     print(df.head())
#     return read_one
# read_one()

