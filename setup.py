import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('form_data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store form data
cursor.execute('''
CREATE TABLE IF NOT EXISTS form_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    carpet_area TEXT,
    super_area TEXT,
    rent_carpet TEXT,
    rent_super TEXT,
    cam_area TEXT,
    city_name TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
