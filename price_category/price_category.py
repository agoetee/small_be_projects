import mysql.connector
import datetime
import time

myConn = mysql.connector.connect(
    host = "localhost",
    username = "root",
    passwd = "1990Charles.",
    database = "alx_be"
)


myCursor = myConn.cursor()
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
    ask = "INSERT INTO categories (name) VALUES (%s)"
    give = (name,)
    myCursor.execute(ask, give)
    myConn.commit()

# category = input("Enter new category: ")
# add_category(category)

def list_categories():
    myCursor.execute("SELECT * FROM categories")
    results = myCursor.fetchall()
    if results:
        print("Categories Available")
        for item in results:
            print(item)
    else:
        print("No categories found")
# list_categories()

def add_product(name, price, category_id):
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
        myConn.commit()
# prod_name = input("Enter product name: ")
# price = int(input("Price: "))
# cat_id = int(input("Enter category id: "))
# add_product(prod_name, price, cat_id)

def search_product(search_item):
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

    
search = input("Enter search item: ")
search_product(search)

def search_all_products():
    myCursor.execute("SELECT * FROM products")
    results = myCursor.fetchall()
    if results:
        print("All Entries now: ")
        for item in results:
            print(item)
    else:
        print("Nothing to show")
    myCursor.close()
# search_all_products()
     



myCursor.close()
myConn.close()

# Next Is to populate table with rows

#Recent: Checked is Category Id entered exists in list of category_ids
# Currently: Searched all products and also partial search
# Main menu: