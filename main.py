import sqlite3
from pandas import DataFrame
from tkinter import Tk,messagebox,Frame,LEFT,RIGHT,Label,Entry,Button,Text,END

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS cases(
ID integer PRIMARY KEY,
name text NOT NULL,
time text NOT NULL,
address text NOT NULL,
phone text NOT NULL,
doctor text NOT NULL,
disease text NOT NULL,
insurance text NOT NULL,
sessions integer,
payment integer,
description text NOT NULL);""")

class case:
    def __init__(self, master):
        self.master = master
        self.left = Frame(master, width=1200, height=720, bg='medium sea green')
        self.left.pack(side=LEFT)

        # Labels
        self.search_name = Label(master, text="Search Patient's Name",fg='black', font=('arial 16 bold'), bg='medium sea green')
        self.search_name.place(x=0, y=40)

        self.name = Label(self.left, text="1.Name", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.name.place(x=0, y=100)

        self.time = Label(self.left, text="2.Time", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.time.place(x=0, y=140)

        self.address = Label(self.left, text="3.Address", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.address.place(x=0, y=180)

        self.phone = Label(self.left, text="4.Phone Number", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.phone.place(x=0, y=220)

        self.doctor = Label(self.left, text="5.Doctor", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.doctor.place(x=0, y=260)

        self.disease = Label(self.left, text="6.Type of Disease", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.disease.place(x=0, y=300)

        self.insurance = Label(self.left, text="7.Type of Insurance", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.insurance.place(x=0, y=340)

        self.sessions = Label(self.left, text="8.Number of Sessions", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.sessions.place(x=0, y=380)
                 
        self.payment = Label(self.left, text="9.Payment", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.payment.place(x=0, y=420)

        self.description = Label(self.left, text="10.Description", font=('arial 16 bold'), fg='black', bg='medium sea green')
        self.description.place(x=0, y=480)

        # Entries
        self.search_name_ent = Entry(master, width=30, font=('arial 16 bold'))
        self.search_name_ent.place(x=250, y=40)

        self.name_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.name_ent.place(x=250, y=100)

        self.time_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.time_ent.place(x=250, y=140)

        self.address_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.address_ent.place(x=250, y=180)

        self.phone_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.phone_ent.place(x=250, y=220)

        self.doctor_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.doctor_ent.place(x=250, y=260)
        
        self.disease_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.disease_ent.place(x=250, y=300)

        self.insurance_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.insurance_ent.place(x=250, y=340)

        self.sessions_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.sessions_ent.place(x=250, y=380)

        self.payment_ent = Entry(self.left, width=30,font='arial 16 bold')
        self.payment_ent.place(x=250, y=420)

        self.description_ent = Text(self.left, width=50,font='arial 16 bold')
        self.description_ent.place(x=0, y=520)

        self.id_list = []
        self.name_list = []
        self.time_list = []
        self.address_list = []
        self.phone_list = []
        self.doctor_list = []
        self.disease_list = []
        self.insurance_list = []
        self.sessions_list = []
        self.payment_list = []
        self.description_list = []
        
        res = c.execute("SELECT * FROM cases")
        for r in res:
            self.id_list.append(r[0])
            self.name_list.append(r[1])
            self.time_list.append(r[2])
            self.address_list.append(r[3])
            self.phone_list.append(r[4])
            self.doctor_list.append(r[5])
            self.disease_list.append(r[6])
            self.insurance_list.append(r[7])
            self.sessions_list.append(r[8])
            self.payment_list.append(r[9])
            self.description_list.append(r[10])

        self.data = {'ids' : self.id_list, 'names': self.name_list, 'time': self.time_list, 'address': self.address_list,
        'phone':self.phone_list ,'doctor': self.doctor_list, 'disease': self.disease_list, 'insurance': self.insurance_list,
        'sessions' :self.sessions_list, 'payments' :self.payment_list, 'description' : self.description_list}

        # search_db button
        self.search = Button(master, text="Search", width=8, height=1, 
        bg='RoyalBlue1', font=('arial 12 bold'), command=self.search_db)
        self.search.place(x=650, y=40)

        # update_db button
        self.update = Button(self.master, text="Update", width=8, height=1, font=('arial 12 bold'), 
        bg='dark orange', command=self.update_db)
        self.update.place(x=800, y=40)

        # delete_db button
        self.delete = Button(self.master, text="Delete", width=8, height=1, font=('arial 12 bold'), 
        bg='red', command=self.delete_db)
        self.delete.place(x=950, y=40)

        #clear_db button
        self.clear = Button(self.master, text="Clear", width=8, height=1, font=('arial 12 bold'), 
        bg='cyan', command=self.clear_db)
        self.clear.place(x=1100, y=40)

        # export_to_xslx button
        self.export = Button(self.left, text="Export to xlsx", width=12, height=1, bg='SlateBlue1',
        font='arial 12 bold', command=self.export_to_xlsx)
        self.export.place(x=650, y=100)

        # export_to_html button
        self.export = Button(self.left, text="Export to html", width=12, height=1, bg='SlateBlue3',
        font='arial 12 bold', command=self.export_to_html)
        self.export.place(x=850, y=100)

        # copy_to_clipboard button
        self.export = Button(self.left, text="Clipboard", width=12, height=1, bg='SlateBlue4',
        font='arial 12 bold', command=self.copy_to_clipboard)
        self.export.place(x=1050, y=100)

        # add_case button
        self.submit = Button(self.left, text="Add Case", width=10, height=1, bg='green',
        font='arial 20 bold', command=self.add_case)
        self.submit.place(x=650, y=640)

    def add_case(self):
        self.var1 = self.name_ent.get()
        self.var2 = self.time_ent.get()
        self.var3 = self.address_ent.get()
        self.var4 = self.phone_ent.get()
        self.var5 = self.doctor_ent.get()
        self.var6 = self.disease_ent.get()
        self.var7 = self.insurance_ent.get()
        self.var8 = self.sessions_ent.get()
        self.var9 = self.payment_ent.get()

        self.var10 = self.description_ent.get(1.0, "end-1c")
        if self.var1 == '' and self.var2 == '' and self.var3 == '' and self.var4 == '' and self.var5 == '' and self.var6 == '':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            sql = """INSERT INTO 'cases' (name,time,address,phone,doctor,disease,insurance,sessions,payment,description)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            c.execute(sql, (self.var1, self.var2, self.var3, self.var4, self.var5, 
            self.var6, self.var7, self.var8, self.var9,self.var10))
            conn.commit()
            messagebox.showinfo("Success", "Case for " +str(self.var1) + " has been created" )

    def search_db(self):
        self.input = self.search_name_ent.get()

        sql = "SELECT * FROM cases WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name = self.row[1]
            self.time = self.row[2]
            self.address = self.row[3]
            self.phone = self.row[4]
            self.doctor = self.row[5]
            self.disease = self.row[6]
            self.insurance = self.row[7]
            self.sessions = self.row[8]
            self.payment = self.row[9]
            self.description = self.row[10]
        
        self.name_ent.insert(END, str(self.name))
        self.time_ent.insert(END, str(self.time))
        self.address_ent.insert(END, str(self.address))
        self.phone_ent.insert(END, str(self.phone))
        self.doctor_ent.insert(END, str(self.doctor))
        self.disease_ent.insert(END, str(self.disease))
        self.insurance_ent.insert(END, str(self.insurance))
        self.sessions_ent.insert(END, str(self.sessions))
        self.payment_ent.insert(END, str(self.payment))
        self.description_ent.insert(END, str(self.description))

    def update_db(self):
        self.var1 = self.name_ent.get()
        self.var2 = self.time_ent.get()
        self.var3 = self.address_ent.get()
        self.var4 = self.phone_ent.get()
        self.var5 = self.doctor_ent.get()
        self.var6 = self.disease_ent.get()
        self.var7 = self.insurance_ent.get()
        self.var8 = self.sessions_ent.get()
        self.var9 = self.payment_ent.get()
        self.var10 = self.description_ent.get(1.0, "end-1c")

        query = """UPDATE cases SET name=?, time=?, address=?, phone=?, doctor=?, 
        disease=?, insurance=?, sessions=?, payment=?, description=? WHERE name LIKE ?"""
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6,
        self.var7, self.var8, self.var9, self.var10, self.search_name_ent.get(),))
        conn.commit()

        messagebox.showinfo("Updated", "Successfully Updated.")

    def delete_db(self):
        sql = "DELETE FROM cases WHERE name LIKE ?"
        c.execute(sql, (self.search_name_ent.get(),))
        conn.commit()

        messagebox.showinfo("Success", "Deleted Successfully")

    def clear_db(self):
        self.name_ent.delete(0,'end')
        self.time_ent.delete(0,'end')
        self.address_ent.delete(0,'end')
        self.phone_ent.delete(0,'end')
        self.doctor_ent.delete(0,'end')
        self.disease_ent.delete(0,'end')
        self.insurance_ent.delete(0,'end')
        self.sessions_ent.delete(0,'end')
        self.payment_ent.delete(0,'end')
        self.description_ent.delete('1.0','end')

    def export_to_xlsx(self):
        df = DataFrame(self.data)
        df.to_excel('HAVIN.xlsx',encoding="utf-8", index=False)
        messagebox.showinfo("File Saved", "xlsx has been saved")

    def export_to_html(self):
        df = DataFrame(self.data)
        df.to_html('HAVIN.html',encoding="utf-8", index=False)
        messagebox.showinfo("File Saved", "html has been saved")

    def copy_to_clipboard(self):
        df = DataFrame(self.data)
        df.to_clipboard('HAVIN.json', index=False)
        messagebox.showinfo("Copied", "All case has been copied")

#1------------------------------------------------------------------------
# show the case window
root = Tk()
case(root)
root.title('HAVIN')
root.geometry("1200x720+10+10")
root.resizable(False,False)
root.mainloop()
