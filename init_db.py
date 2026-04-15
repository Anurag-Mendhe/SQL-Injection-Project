import sqlite3

conn = sqlite3.connect('products.db')
c = conn.cursor()

# Create table FIRST
c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# Clear old data (prevents duplicates)
c.execute("DELETE FROM products")

# Sample data
products = [
    ("Laptop", "Dell XPS 13", 999.99),
    ("Smartphone", "Samsung Galaxy S21", 799.99),
    ("Headphones", "Sony WH-1000XM4", 349.99),
    ("Shoes", "Nike Air Max", 129.99),
    ("Watch", "Fossil Gen 5 Smartwatch", 199.99),
    ("Tablet", "iPad 10th Gen", 499.99),
    ("Camera", "Canon EOS 1500D", 549.99)
]

# Insert data
c.executemany(
    'INSERT INTO products (name, description, price) VALUES (?, ?, ?)',
    products
)

conn.commit()
conn.close()

print("Database initialized with fresh sample data.")