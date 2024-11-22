import mysql.connector as mc


connection = mc.connect(
    host='localhost',
    user='root',
    password='Football12345!'
)
cursor = connection.cursor()

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

connection.close()