import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = '12345',database = 'school')
mycur = mydb.cursor()
mycur.execute("create database if not exists school")

#CREATION OF A TABLE
def create():
    mycur.execute("create table if not exists student(Roll_no int primary key,Name varchar(20),age int,Class int,City varchar(20))")


#INSERTING DATA
def insert():
    while True:
        print("\nPress 1 for INSERING DATA")
        print("Press 2 for Home Page")
        p = int(input("\nENTER YOUR CHOICE:\t"))
        if p==1:
            s = int(input("\nEnter the Number of Rcords you want to Insert:\t"))
            for i in range(1,s+1):
                print("\nDATA - %d "%i)
                r = int(input("\nEnter the Roll Number:\t"))
                n = input("Enter the Name:\t")
                a = int(input("Enter Age:\t"))
                c = int(input("Enter Class:\t"))
                city = input("Enter City:\t")
                mycur.execute("INSERT INTO STUDENT VALUES ('"+str(r)+"','"+n+"','"+str(a)+"','"+str(c)+"','"+str(city)+"')")
                mydb.commit()
                print("Data Inserted Sucessfully")
                pass
        elif p==2:
            break
        else:
            print("WRONG KEY ENTERED!! ENTER AGAIN")
            continue

#FETCHING DATA

def fetch():
    while True:
        print("\nPress 1 for fetching by Fetchone method")
        print("Press 2 for fetching by Fetchall method")
        print("Press 3 for Home Page")
        l = int(input("\nENTER YOUR CHOICE:\t"))
        print("\n")
        if l==1:
            global row
            mycur.execute("SELECT * FROM STUDENT")
            row = mycur.fetchone()
            while row is not None:
                print(row)
                row = mycur.fetchone()
            if row is not None:
                print("\nDATA NOT FOUND")
        elif l==2:
            mycur.execute("SELECT * FROM STUDENT")
            records = mycur.fetchall()
            for i in records:
                print(i)
            if len(records)==0:
                print("\nDATA NOT FOUND")
        elif l==3:
            break
        else:
            print("WRONG KEY ENTERED!! ENTER AGAIN")
            continue

#FUNCTION FOR UPDATING THE DATA WHICH EXSITS
def up():
    global roll
    global status
    status = 1
    mycur.execute("SELECT * FROM STUDENT")
    row = mycur.fetchone()
    roll = int(input("\nEnter the ROLL NUMBER of the Record to be UPDATED:\t"))
    while row is not None:
        if row[0]==roll:
            mydb1 = mysql.connector.connect(host = 'localhost',user = 'root',password = '12345',database = 'school')
            mycur1 = mydb1.cursor()
            status = 0
        row = mycur.fetchone()
    if status==1:
        print("\nDATA NOT FOUND")

#FUNCTION FOR DELETING THE DATA WHICH EXSITS
def de():
    global rd
    global status
    status = 1
    mycur.execute("SELECT * FROM STUDENT")
    row = mycur.fetchone()
    rd = int(input("Enter the ROLL NUMBER of the Record to be DELETED:\t"))
    while row is not None:
        if row[0]==rd:
            mydb1 = mysql.connector.connect(host = 'localhost',user = 'root',password = '12345',database = 'school')
            mycur1 = mydb1.cursor()
            status = 0
        row = mycur.fetchone()
    if status==1:
        print("\nDATA NOT FOUND")


#UPDATING THE DATA
def update():
    while True:
        print("\nPress 1 for updating NAME")
        print("Press 2 for updating AGE")
        print("Press 3 for updating CLASS")
        print("Press 4 for updating CITY")
        print("Press 5 for Home Page")
        a = int(input("\nENTER YOUR CHOICE:\t"))
        if a==1:
            up()
            if status==0:
                updated_name = input("Enter NEW NAME:\t")
                query = "UPDATE STUDENT SET NAME = %s WHERE Roll_no = %s "
                mycur.execute(query,(updated_name,roll))
                mydb.commit()
                print("NAME UPDATED SUCESSFULLY")
        elif a==2:
            up()
            if status==0:
                updated_age = int(input("Enter NEW AGE:\t"))
                query = "UPDATE STUDENT SET AGE = %s WHERE Roll_no = %s "
                mycur.execute(query,(updated_age,roll))
                mydb.commit()
                print("AGE updated sucessfully")
        elif a==3:
            up()
            if status==0:
                updated_class = int(input("Enter NEW CLASS:\t"))
                query = "UPDATE STUDENT SET CLASS = %s WHERE Roll_no = %s "
                mycur.execute(query,(updated_class,roll))
                mydb.commit()
                print("CLASS updated sucessfully")
        elif a==4:
            up()
            if status==0:
                updated_city = input("Enter NEW CITY:\t")
                query = "UPDATE STUDENT SET CITY = %s WHERE Roll_no = %s "
                mycur.execute(query,(updated_city,roll))
                mydb.commit()
                print("CITY updated sucessfully")
        elif a==5:
            break
        else:
            print("WRONG KEY ENTERED!! ENTER AGAIN")
            continue

#DELETING DATA
def delete():
    while True:
        print("\nPress 1 for Deleting")
        print("Press 2 for Home Page")
        a = int(input("\nENTER YOUR CHOICE:\t"))
        if a==1:
            de()
            if status==0:
                query = "DELETE FROM STUDENT WHERE ROLL_NO = %s"%rd
                mycur.execute(query)
                mydb.commit()
                print("\nRecord DELETED Sucessfully")
        elif a==2:
            break
        else:
            print("WRONG KEY ENTERED!! ENTER AGAIN")
            continue
            

while True:
    print("\nPRESS 1 FOR INSERTING DATA")
    print("PRESS 2 FOR FETCHING DATA")
    print("PRESS 3 FOR UPDATING DATA")
    print("PRESS 4 FOR DELETING DATA")
    print("PRESS 5 FOR EXITING PROGRAM")
    m = int(input("\nEnter Your Choice:\t"))
    create()
    if m==1:
        insert()
    elif m==2:
        fetch()
    elif m==3:
        update()
    elif m==4:
        delete()
    elif m==5:
        #CLOSING DATABASE CONNECTION.
        if (mydb.is_connected()):
            mycur.close()
            mydb.close()
            print("Connection is Closed")
            print("THANKS FOR USING THE PROGRAM :)")
            break
    else:
        print("WRONG KEY ENTERD!! ENTER AGAIN")









