from mysql.connector import connect

mydb = connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password", database="worker")

cursor = mydb.cursor()

delete_query = "DELETE FROM worker_details WHERE id = 4"

cursor.execute(delete_query)

mydb.commit()