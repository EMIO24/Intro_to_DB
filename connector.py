import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Replace these with your MySQL credentials
        connection = mysql.connector.connect(
            host="localhost",
            user="EMIO24",          # Your MySQL username
            password="Passion13.@1", # Your MySQL password
            database="alx_book_store" # Your database name
        )

        if connection.is_connected():
            print("Successfully connected to MySQL database!")
            
            # Test query (optional)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print(f"You're connected to database: {db_name[0]}")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function
connect_to_mysql()
