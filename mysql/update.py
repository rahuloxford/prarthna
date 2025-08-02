from mysql.connector import connect

mydb = connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password", database="worker")

cursor = mydb.cursor()

update_query = "UPDATE worker_details SET salary = salary + (salary * 0.12)"

cursor.execute(update_query)

mydb.commit()