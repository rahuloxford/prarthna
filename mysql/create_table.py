from mysql.connector import connect

mydb = connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password", database="worker")

cursor = mydb.cursor()

cursor.execute("CREATE TABLE worker_details(id INT, name VARCHAR(20), salary DECIMAL(6, 2))")