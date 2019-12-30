
#this script depends on having a working MySQL connection and MySQL connector installed
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername", #replace yourusername with your user name
    password="yourpassword", #replace yourpassword with your password
    auth_plugin="mysql_native_password",
    database="inventory", #create the database "inventory" using CreateDatabase.py
)

mycursor = mydb.cursor()

#create a table with the columns: id, item, quantity and location
mycursor.execute("CREATE TABLE IF NOT EXISTS inventory (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), quantity INT, location VARCHAR(255))")

#the following function allows the user to add an item to the table created above
def add_an_item():
    added_item_name = input("What item would you like to add? ")
    item_quant = int(input("What is the quantity of {}? ".format(added_item_name)))
    item_location = input("What location is associated with this item? ")
    sql = "INSERT INTO inventory (item, quantity, location) VALUES (%s, %s, %s)"
    val = (added_item_name, item_quant, item_location)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) added")
    menu_options()

#shows the user all items within the table, sorted by location
def show_all_items():
    mycursor.execute("SELECT location FROM inventory")
    mylocations = mycursor.fetchall()
    mylocations = list(dict.fromkeys(mylocations))
    for eachlocation in mylocations:
        sql = "SELECT item, quantity FROM inventory WHERE location = %s ORDER BY item"
        mycursor.execute(sql, eachlocation)
        myresult = mycursor.fetchall()
        print("***", str(eachlocation)[2:-3].upper(), "***")
        print("(Item Name, Quantity)")
        for row in myresult:
            print(row)
    menu_options()

#shows the user all items within the table, sorted by location, including id
def show_items_to_update():
    mycursor.execute("SELECT location FROM inventory")
    mylocations = mycursor.fetchall()
    mylocations = list(dict.fromkeys(mylocations))
    for eachlocation in mylocations:
        sql = "SELECT id, item, quantity FROM inventory WHERE location = %s ORDER BY item"
        mycursor.execute(sql, eachlocation)
        myresult = mycursor.fetchall()
        print("***", str(eachlocation)[2:-3].upper(), "***")
        print("(ID, Item Name, Quantity)")
        for row in myresult:
            print(row)

#allows the user to delete an item
def delete_an_item():
    show_items_to_update()
    deleted_item_name = (int(input("Enter the ID of the item you would like to delete: ")),)
    sql = "DELETE FROM inventory WHERE id = %s"
    mycursor.execute(sql, deleted_item_name)
    mydb.commit()
    if mycursor.rowcount == 0:
        print("No records found, please try again")
        delete_an_item()
    else:
        print(mycursor.rowcount, "record(s) deleted")
    menu_options()

#allows the user to update the name, quantity or location of an item
def update_an_item():
    show_items_to_update()
    item_to_update = int(input("Enter the ID of the item you would like to update: "),)
    column_to_update = input("""What would you like to update?
    A: Item name
    B: Quantity
    C: Location
    """)
    column_to_update = column_to_update.upper()
    if column_to_update == "A":
        new_item_name = input("What should the item be renamed? ")
        update_sql = "UPDATE inventory SET item = %s WHERE id = %s"
        update_val = (new_item_name, item_to_update)
        mycursor.execute(update_sql, update_val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
    elif column_to_update == "B":
        new_item_qty = int(input("What should the new quantity be? "))
        update_sql = "UPDATE inventory SET quantity = %s WHERE id = %s"
        update_val = (new_item_qty, item_to_update)
        mycursor.execute(update_sql, update_val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
    elif column_to_update == "C":
        new_item_loca = input("What should the new location be? ")
        update_sql = "UPDATE inventory SET location = %s WHERE id = %s"
        update_val = (new_item_loca, item_to_update)
        mycursor.execute(update_sql, update_val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
    else:
        print("Sorry, that's not an option. Please enter the letter associated with the action you'd like to take")
        update_an_item()
    menu_options()

#exits the program
def quit_inventory():
    print("Goodbye")
    quit()

#shows the user menu options
def menu_options():
    what_to_do = input("""What would you like to do?
    A: Add an item
    B: Delete an item
    C: Update an item
    D: View full list
    E: Exit
    """)
    what_to_do = what_to_do.upper()
    if what_to_do == "A":
        add_an_item()
    elif what_to_do == "B":
        delete_an_item()
    elif what_to_do == "C":
        update_an_item()
    elif what_to_do == "D":
        show_all_items()
    elif what_to_do == "E":
        quit_inventory()
    else:
        print("Sorry, that's not an option. Please enter the letter associated with the action you'd like to take")
        menu_options()

#welcome message
def welcome():
    print("Welcome to your inventory")
    menu_options()

welcome()


