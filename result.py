import mysql.connector as mc


connection = mc.connect(
    host='localhost',
    user='root',
    password='Football12345!',
    database='menagerie'
)


cursor = connection.cursor()
cursor.execute("SELECT name, birth, MONTH(birth) AS birth_month FROM pet")


print("pets with birth month: ")
for record in cursor:
    print(record)

connection.close()
