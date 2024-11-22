import mysql.connector as mc


connection = mc.connect(
    host='localhost',
    user='root',
    password='Football12345!',
    database='menagerie'
)


cursor = connection.cursor()
cursor.execute("SELECT name, birth FROM pet")


print("Name and Birth columns: ")
for record in cursor:
    print(record)


connection.close()
