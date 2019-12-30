#Connect to MySQL
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername", #replace yourusername with your user name
    password="yourpassword", #replace yourpassword with your password
    auth_plugin="mysql_native_password",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS inventory")

mycursor.execute("SHOW DATABASES")

print("Your existing databases are:")
for database in mycursor:
    print(database)