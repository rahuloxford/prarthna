from mysql.connector import connect

mydb = connect(host="localhost", user="root", password="root", auth_plugin="mysql_native_password")

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE worker")