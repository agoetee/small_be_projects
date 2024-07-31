import mysql.connector
import datetime
import time

def db_connect():
    return  mysql.connector.connect(
    host = DB_HOST,
    username = DB_USERNAME,
    passwd = DB_PASSWORD,
    database = DB
)


ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# def create_table_categories():
#     ask = """
#         CREATE TABLE IF NOT EXISTS categories (
#         category_id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255)
#         )
#         """
#     myCursor.execute(ask)
#     print("Table created successfully")

# create_table_categories()

# def create_table_products():
#     ask = """
#         CREATE TABLE IF NOT EXISTS products (
#         product_id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255),
#         price NUMERIC(10, 3),
#         category_id INT,
#         created_at DATE,
#         FOREIGN KEY (category_id) REFERENCES categories(category_id),
#         INDEX (name(4))
#         )
#         """
#     myCursor.execute(ask)
#     print("Table created successfully")

# create_table_products()


# def describe_products():
#     myCursor.execute("DESCRIBE products")
#     print("Table products contain.....")
#     print([column[0] for column in myCursor.fetchall()])

# describe_products()

# def describe_categories():
#     myCursor.execute("DESCRIBE categories")
#     print("Table Categories contain...")
#     print([column[0] for column in myCursor.fetchall()])
# describe_products()

def add_category(name):
    db = db_connect()
    myCursor = db.cursor()
    ask = "INSERT INTO categories (name) VALUES (%s)"
    give = (name,)
    myCursor.execute(ask, give)
    db.commit()
    print(f"product {name} added successfully")
    myCursor.close()
    db.close()

# category = input("Enter new category: ")
# add_category(category)

def list_categories():
    db = db_connect()
    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM categories")
    results = myCursor.fetchall()
    if results:
        print("Categories Available")
        for item in results:
            print(item)
    else:
        print("No categories found")
    myCursor.close()
    db.close()


def add_product(name, price, category_id):
    db = db_connect()
    myCursor = db.cursor()
    ask = "INSERT INTO products (name, price, category_id, created_at) VALUES (%s, %s, %s, %s)"
    give = (name, price, category_id, timestamp)
    
    #Check if the category_id exists
    myCursor.execute("SELECT category_id FROM categories")
    checker = myCursor.fetchall()
    
    #Flatten the list of tupples to a list of category_id's
    present = [tup[0] for tup in checker]
    if category_id not in present:
        print(f"category ID {category_id} not present")
    else:
        myCursor.execute(ask, give)
        print(f"Product {name} added successfully")
        db.commit()
    myCursor.close()
    db.close()
# prod_name = input("Enter product name: ")
# price = int(input("Price: "))
# cat_id = int(input("Enter category id: "))
# add_product(prod_name, price, cat_id)

def search_product(search_item):
    db = db_connect()
    myCursor = db.cursor()
    ask = " SELECT name FROM products WHERE name LIKE %s"
    give = (f"%{search_item}%",)
    myCursor.execute(ask, give)
    result = myCursor.fetchall()
    if result:
        print(f"Name '{search_item}' matches:")
        for item in result:
            print(*item)
    else:
        print(f"No match for '{search_item}'")
    myCursor.close()
    db.close()


def list_all_products():
    db = db_connect()
    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM products")
    results = myCursor.fetchall()
    if results:
        print("All Entries now: ")
        for item in results:
            print(item)
    else:
        print("Nothing to show")
    myCursor.close()
    db.close()
     



# myCursor.close()
# myConn.close()

# Next Is to populate table with rows

#Recent: Checked is Category Id entered exists in list of category_ids
# Currently: Searched all products and also partial search
# Main menu:

def display_menu():
    print("Welcome to Price Category App")
    print("1. Add Category")
    print("2. List Categories")
    print("3. Add Product")
    print("4. Search for Products")
    print("5. List all products")
    print("6. Edit Product detail")
    print("7. Exit")

def main():
    while True:
        display_menu()
        display_menu_input = input("")
        match display_menu_input:
            case '1':
                print("Choice: Add category")
                category = input("Enter new category: ")
                add_category(category)
            case "2":
                print("Choice List Categories")
                list_categories()
            case "3":
                print("Choice Add Product")
                prod_name = input("Enter product name: ")
                price = int(input("Price: "))
                cat_id = int(input("Enter category id: "))
                add_product(prod_name, price, cat_id)
            case "4":
                print("Choice Search for Product")
                search = input("Enter search item: ")
                search_product(search)
            case '5':
                print("Choice List all Products")
                list_all_products()
            case '6':
                pass
            case "7":
                print("Thank you for using the service.. Bye")
                break
            case _:
                print("Invalid input. Try again")

main()