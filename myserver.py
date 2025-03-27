import mysql.connector
try:
    
    # Replace with your actual credentials
    mydb = mysql.connector.connect(
        host="localhost",
        user="EMIO24",  # Your MySQL username
        password="Passion13.@1",  # Your MySQL password
    )

    my_cursor = mydb.cursor()
    my_cursor = mydb.cursor("CREATE DATABASE Book_store")
    my_cursor.execute("")
    
except:
    print("except mysql.connector.Error")
