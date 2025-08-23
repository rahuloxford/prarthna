from mysql.connector import connect

mydb = connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password", database="worker")

cursor = mydb.cursor()

insert_query = "INSERT INTO worker_details(id, name, salary) VALUES(%s, %s, %s)"
many_data = [(3, "Kimi", 356.68), (4, "Linda", 975.26), (5, "Zoya", 687.25)]

cursor.executemany(insert_query, many_data)

mydb.commit()