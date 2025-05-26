import sqlite3

# get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personalData = (firstName, lastName, age)

# execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?,?,?)", personalData)

print(personalData)
