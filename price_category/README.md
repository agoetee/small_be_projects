# Task prompt:

Create a PostgreSQL database and two tables:

products table with columns:

id (SERIAL, Primary Key)
name (VARCHAR(255))
price (NUMERIC(10,2))
category_id (INTEGER)
created_at (TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)

categories table with columns:

id (SERIAL, Primary Key)
name (VARCHAR(100))
Additional Requirements:

Create an index on the 'name' column of the 'products' table.
Establish a FOREIGN KEY constraint on the 'category_id' column of the 
'products' table, referencing the 'id' column of the 'categories' table.
Implement a trigger to automatically update the 'created_at' column of the '
products' table with the current timestamp whenever a new product is inserted.

2i.
Create functions to perform CRUD operations on the 'products' and 'categories' tables you created earlier.

Specific Requirements:

Product Management:

Create a function to add a new product, requiring product name, price, and category ID as input.
Create a function to search for products by name, allowing for partial matches.
Create a function to list all products with details.
(Optional) Create a function to delete a product by its ID.
Category Management:

Create a function to add a new category, requiring category name as input.
Create a function to list all categories.
Additional Considerations:

Ensure proper error handling and data validation for all functions.
Consider performance optimization techniques for search and listing functions, especially when dealing with large datasets.
Explore the use of stored procedures or views to encapsulate complex logic and improve performance.
