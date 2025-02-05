import mysql.connector

# Replace with your actual credentials
mydb = mysql.connector.connect(
    host="localhost",
    user="EMIO24",  # Your MySQL username
    password="Passion13.@1",  # Your MySQL password
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully!")
