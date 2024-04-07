from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkcalendar import * # install tkcalendar

import sqlite3
import pandas as pd # install pandas
import json

import manage

class MainWindow(Frame):

    def __init__(self):
        super().__init__()
        self.init_bar()
        self.frame_up()
        self.frame_right()
        self.frame_bottom()
        self.layar_right()
        self.layar_left()
        self.btn_bottom()
        self.table()


    def init_bar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar, tearoff="off")
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New File", compound='left', underline=0)
        fileMenu.add_command(label="Open File", compound='left', underline=0, command=self.openFile)
        fileMenu.add_command(label="Save", compound='left', underline=0)
        fileMenu.add_command(label="Exit", command=self.onExit)


    def onExit(self):
        self.quit()

    def openFile(self):
        self.filename = fd.askopenfilename()
        return self.openFile


    def frame_up(self):
        Fup = LabelFrame(self.master, bd=0.5, bg="#DCDEDE", height=330, width=280, text='Create database', font=('System', 12) )
        Fup.pack(side='top', anchor=NW)


    def frame_right(self):
        Fup = LabelFrame(self.master, bd=0.5, bg="#DCDEDE", height=330, width=320, text='Form data', font=('System', 12) )
        Fup.place(x=280,y=0)


    def frame_bottom(self):
        Fup = LabelFrame(self.master, bd=0.5, bg="#DCDEDE", height=50, width=320, text='Complete', font=('Arian', 8) )
        Fup.pack(side=BOTTOM, fill='both')

    def layar_right(self):

        # function to validate
        def only_numbers(char):
            return char.isdigit()
        validation = self.master.register(only_numbers)


        def clear_text():
            E1.delete(0, 'end')
            E2.delete(0, 'end')
            # E3.delete(0, 'end')
            E4.delete(0, 'end')
            E5.delete(0, 'end')


        def send():
            v_name = E1.get()
            v_sur = E2.get()
            v_age = E3.get()
            v_gender = output
            v_mail = E4.get()
            v_numb = E5.get()
            
            print(v_name, v_sur, v_age, v_gender, v_mail, v_numb)

            # add columns and index in file
            sql_query = f"INSERT INTO {tb_name} ({cl_name1}, {cl_name2}, {cl_name3}, {cl_name4}, {cl_name5}, {cl_name6}) VALUES (?,?,?,?,?,?)"
            cursor.execute(sql_query, (v_name, v_sur, v_age, v_gender, v_mail, v_numb))
            database.commit() 
                

        def selection():
            selected = self.var.get()
            if selected == 1:
                global output
                output = "Male"
            elif selected == 2:
                output =  "Femele"
            elif selected == 3:
                output =  "N/specify"
            # L4.config(text=output)


        L1 = Label(self.master, bg="#DCDEDE", text="First name", font=('System', 9))
        L1.place(x=290,y=40)
        E1 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a', )
        E1.insert(END, 'Billy')
        E1.place(x=390,y=40)

        L2 = Label(self.master, bg="#DCDEDE", text="Last name", font=('System', 9))
        L2.place(x=290,y=80)
        E2 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a', )
        E2.insert(END, 'Antom')
        E2.place(x=390,y=80,)

        L3 = Label(self.master, bg="#DCDEDE", text="Age", font=('System', 9))
        L3.place(x=290,y=120)
        E3 = DateEntry(self.master, width=18, font=('Arial', 12), data_patern='mm/dd/yy')
        E3.place(x=390,y=120,)

        L4 = Label(self.master, bg="#DCDEDE", text="Gender", font=('System', 9))
        L4.place(x=290,y=160)
        self.var = IntVar()
        R1 = Radiobutton(self.master, bg="#DCDEDE", text="Male", variable=self.var, value=1, command=selection)
        R2 = Radiobutton(self.master, bg="#DCDEDE", text="Female", variable=self.var, value=2, command=selection)
        R3 = Radiobutton(self.master, bg="#DCDEDE", text="N/specify", variable=self.var, value=3, command=selection)
        R1.place(x=390,y=160,)
        R2.place(x=445,y=160,)
        R3.place(x=515,y=160,)

        L5 = Label(self.master, bg="#DCDEDE", text="E-mail", font=('System', 9))
        L5.place(x=290,y=200)
        E4 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a',)
        E4.insert(END, 'exemple@emal')
        E4.place(x=390,y=200,)

        L6 = Label(self.master, bg="#DCDEDE", text="Number", font=('System', 9))
        L6.place(x=290,y=240)
        E5 = Entry(self.master, validate="key", validatecommand=(validation, '%S'), bd=1, font=('Arial', 12), fg='#8a8a8a',)
        E5.insert(END, '7888985')
        E5.place(x=390,y=240,)


        B2 = Button(self.master, text='Clear', font=('System', 9), bd=0, width=10, bg='#c7c7c7', command=clear_text)
        B2.place(x=510,y=300,)


        B1 = Button(self.master, text='Send', font=('System', 9), bd=0, width=10, bg='#c7c7c7', command=send)
        B1.place(x=415,y=300)


    def layar_left(self):
        
        def send():
            global db_name
            db_name = E1.get()
            global tb_name
            tb_name = E2.get()

            global cl_name1
            cl_name1 = Eb1.get()
            global cl_name2
            cl_name2 = Eb2.get()
            global cl_name3
            cl_name3 = Eb3.get()
            global cl_name4
            cl_name4 = Eb4.get()
            global cl_name5
            cl_name5 = Eb5.get()
            global cl_name6
            cl_name6 = Eb6.get()

            print(db_name, tb_name, cl_name1, cl_name2, cl_name3, cl_name4, cl_name5, cl_name6)
            
            # connects with the file
            global database
            database = sqlite3.connect(f'{db_name}.db')
            global cursor
            cursor = database.cursor()
            # create the file
            sql_query = f"CREATE TABLE IF NOT EXISTS {tb_name} ({cl_name1} TEXT, {cl_name2} TEXT, {cl_name3} TEXT, {cl_name4} TEXT, {cl_name5} TEXT, {cl_name6} TEXT)"
            cursor.execute(sql_query)

            dictionary = {
                "databank": db_name,
                "table": tb_name,
                "name": cl_name1,
                "surname": cl_name2,
                "age": cl_name3,
                "gender": cl_name4,
                "email": cl_name5,
                "number": cl_name6,
            }
            with open('entry.json', 'w') as openfile:
                # Reading from json file
                json_object = json.dump(dictionary, openfile)
            

        L1 = Label(self.master, bg="#DCDEDE", text="Database name", font=('System', 9))
        L1.place(x=3,y=30)
        E1 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a',)
        E1.insert(END, 'my_partners')
        E1.place(x=3,y=55)

        L2 = Label(self.master, bg="#DCDEDE", text="Table name", font=('System', 9))
        L2.place(x=5,y=80)
        E2 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a',)
        E2.insert(END, 'partners')
        E2.place(x=5,y=105,)

        L3 = Label(self.master, bg="#DCDEDE", text="Columns name", font=('System', 9))
        L3.place(x=5,y=140)
        Eb1 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a', width=8,)
        Eb1.insert(END, 'name')
        Eb1.place(x=5,y=175,)

        Eb2 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a', width=8)
        Eb2.insert(END, 'surname')
        Eb2.place(x=5,y=200,)

        Eb3 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a', width=8)
        Eb3.insert(END, 'age')
        Eb3.place(x=5,y=225,)

        Eb4 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a', width=8)
        Eb4.insert(END, 'gender')
        Eb4.place(x=130,y=175,)

        Eb5 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a', width=8)
        Eb5.insert(END, 'e_mail')
        Eb5.place(x=130,y=200,)

        Eb6 = Entry(self.master, bd=1, font=('Arial', 12), fg='#8a8a8a', width=8)
        Eb6.insert(END, 'number')
        Eb6.place(x=130,y=225,)

        B1 = Button(self.master, text='Create', font=('System', 9), bd=0, width=10, bg='#c7c7c7', command=send)
        B1.place(x=190,y=300)


    def btn_bottom(self):
        B1 = Button(self.master, text='Save', font=('System', 9), bd=0, width=10, bg='#c7c7c7')
        B1.place(x=5,y=670)


    def table(self):
        tbl_frame = Frame(self.master, height=400, width=200)
        tbl_frame.pack(side='top', fill='both')
        tbl = ttk.Treeview(tbl_frame, height=15)
        tbl['columns'] = ('people_id', 'first_name', 'last_name', 'age', 'gender', 'e_mail', 'number')
        

        tbl.column("#0", width=0,  stretch=NO)
        tbl.column("people_id", anchor=CENTER, width=40,)
        tbl.column("first_name", anchor=CENTER, width=100)
        tbl.column("last_name", anchor=CENTER, width=100)
        tbl.column("age", anchor=CENTER, width=80)
        tbl.column("gender", anchor=CENTER, width=60)
        tbl.column("e_mail", anchor=CENTER, width=120)
        tbl.column("number", anchor=CENTER, width=100)

        tbl.heading("#0", text="", anchor=CENTER)
        tbl.heading("people_id", text="Id", anchor=CENTER)
        tbl.heading("first_name", text=manage.r_name, anchor=CENTER)
        tbl.heading("last_name", text=manage.r_surname,anchor=CENTER)
        tbl.heading("age", text=manage.r_age, anchor=CENTER)
        tbl.heading("gender", text=manage.r_gender, anchor=CENTER)
        tbl.heading("e_mail", text=manage.r_email, anchor=CENTER)
        tbl.heading("number", text=manage.r_number, anchor=CENTER)
    
        tbl.insert(parent='', index='end', iid=0, text='',
        values=('', manage.name_row1, manage.surname_row1, manage.age_row1, manage.gender_row1, manage.email_row1, manage.number_row1))

        tbl.insert(parent='',index='end',iid=1, text='',
        values=('', manage.name_row2, manage.surname_row2, manage.age_row2, manage.gender_row2, manage.email_row2, manage.number_row2))

        tbl.insert(parent='', index='end', iid=2, text='',
        values=('', manage.name_row3, manage.surname_row3, manage.age_row3, manage.gender_row3, manage.email_row3, manage.number_row3))

        tbl.insert(parent='', index='end', iid=3, text='',
        values=('', manage.name_row4, manage.surname_row4, manage.age_row4, manage.gender_row4, manage.email_row4, manage.number_row4))

        tbl.insert(parent='',index='end',iid=4, text='',
        values=('', manage.name_row5, manage.surname_row5, manage.age_row5, manage.gender_row5, manage.email_row5, manage.number_row5))

        tbl.insert(parent='', index='end', iid=5, text='',
        values=('', manage.name_row6, manage.surname_row6, manage.age_row6, manage.gender_row6, manage.email_row6, manage.number_row6))

        tbl.insert(parent='', index='end', iid=6, text='',
        values=('', manage.name_row7, manage.surname_row7, manage.age_row7, manage.gender_row7, manage.email_row7, manage.number_row7))

        tbl.insert(parent='',index='end',iid=7, text='',
        values=('', manage.name_row8, manage.surname_row8, manage.age_row8, manage.gender_row8, manage.email_row8, manage.number_row8))

        tbl.insert(parent='', index='end', iid=8, text='',
        values=('', manage.name_row9, manage.surname_row9, manage.age_row9, manage.gender_row9, manage.email_row9, manage.number_row9))

        tbl.insert(parent='', index='end', iid=9, text='',
        values=('', manage.name_row10, manage.surname_row10, manage.age_row10, manage.gender_row10, manage.email_row10, manage.number_row10))

        tbl.place(x=0, y=0)

def main():
    root = Tk()
    root.geometry("600x700")
    root.title("Databese manage")
    app = MainWindow()
    root.resizable(False, False)

    p1 = PhotoImage(file="master\icons\person.png")
    root.iconphoto(False, p1)
    

    root.mainloop()

if __name__ == '__main__':
    main()
