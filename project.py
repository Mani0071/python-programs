#connecting MYSQL with python
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='Mani123',database='student')
#checking connected succesfully or not
if con.is_connected():
    print('connected succesfully')

#funtions for inserting a data into a table
def insert(name, age, city):
    res = con.cursor()
    sql = "insert into users (name,age,city) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")

#functions for update the existing data in a table
def update(name, age, city,id):
    res = con.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city,id)
    res.execute(sql, user)
    con.commit()
    print("Data Update Success")

#functions for selecting a particular column in a table
def select():
    res = con.cursor()
    sql = "SELECT ID,NAME,AGE,CITY from users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))

#functions for delete the unwanted data
def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data Delete Success")

#using loop to select the choice
while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
#calling a functions insert
    if choice == 1:
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        city = input("Enter City : ")
        insert(name, age, city)
#calling a functions update
    elif choice == 2:
        id = input("Enter The Id : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        update(name, age, city,id)
#calling a functions select
    elif choice == 3:
        select()
#invoking a functions delete
    elif choice == 4:
        id = input("Enter The Id to Delete : ")
        delete(id)
#exiting the loop if no choice is selected
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection . Please Try Again !")


