import mysql.connector 


mydb = mysql.connector.connect(
    host = "hostnameDummy",
    user="userDummy",
    password="passwordDummy",
    use_pure = True
)

cursor = mydb.cursor()
query = "SELECT * FROM doraaudit.processcomis;"
cursor.execute(query)

result = cursor.fetchall()
for row in result:
    print(row)