import mysql.connector as mc


connection = mc.connect(
    host='localhost',
    user='root',
    password='Football12345!',
    database='menagerie'
)


cursor = connection.cursor()
cursor.execute("SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner")


print("Number of pets per owner: ")
for record in cursor:
    print(record)


connection.close()
