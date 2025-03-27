import mysql.connector
from mysql.connector import Error

print("=== Script started ===")  # Debugging line

try:
    print("Attempting to connect to MySQL...")  # Debugging line
    mydb = mysql.connector.connect(
        host="localhost",
        user="EMIO24",
        password="Passion13.@1",
    )
    print("Connected to MySQL server!")  # Debugging line

    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' ensured.")  # Debugging line

except Error as e:
    print(f"MySQL Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")

input("Press Enter to exit...")  # Pause to see output
    