from mysql.connector import connect

mydb = connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password", database="worker")

cursor = mydb.cursor()

select_query = "SELECT * FROM worker_details"

cursor.execute(select_query)

users = cursor.fetchall()

for user in users:
    print(user)