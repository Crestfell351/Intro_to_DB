import mysql.connector
from mysql.connector import Error

# Replace with your actual connection details
try:
  mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="T7k$8jL#Z9mR%2dX",
      auth_plugin='mysql_native_password'
  )
  if connection.isconnected():
    curser = connection.curser()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except Error as e:
        print(f"Error: '{e}' occurred")

if connection.is_connected():
  cursor.close()
  connection.close()
  print("MySQL connection is closed")
