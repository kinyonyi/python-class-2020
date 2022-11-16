import psycopg2
import json

DB_NAME = "david"
DB_USER = "postgres"
DB_PASS = "engdave"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
	conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT)
	print("Database connected successfully")
except:
	print("Database not connected successfully")
 
cursor = conn.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE customer(
        id SERIAL PRIMARY KEY,
        name VARCHAR(300),
        location VARCHAR(300)
        )
    """)
    conn.commit()
    print("table created")

def drop_table():
    cursor.execute("""
        DROP TABLE customer;
    """)
    conn.commit()
    print("table deleted")

def insert_data(name, location):
    cursor.execute(
        """
        INSERT INTO customer (name, location) VALUES('{name}','{location}');
        """.format(name = name, location = location)
    )
    conn.commit()
    print("data has been inserted into the database")

def retrieve_data():
    print("fetching all items ------>")
    cursor.execute("""
        SELECT * FROM customer;
    """)
    all_customers = cursor.fetchall()
    conn.commit()
    all_data = []
    for x in all_customers:
        all_data.append({
            "id":x[0],
            "name":x[1],
            "location":x[2]
        })
    
    print(json.dumps(all_data, indent=2))
    
def delete_item():
    cursor.execute(
        """
        DELETE FROM customer WHERE id = 5;
        """
    )
    conn.commit()
    print("item deleted!")
    
def one_item():
    print("fetching one item ------>")
    cursor.execute(
        """
        SELECT * FROM customer WHERE id = 3;
        """
    )
    all_data = cursor.fetchone()
    all_data_returned = {
        "id":all_data[0],
        "name":all_data[1],
        "location":all_data[2]
    }
    conn.commit()
    print(json.dumps(all_data_returned, indent=2))
    print("Fetch data successful")
    
def update_item():
    cursor.execute(
        """
        UPDATE customer SET name = 'jacinta', location = 'kansanga' WHERE id = 6;
        """
    )
    conn.commit()
    print("update for data successful")
name = input("Enter a name: ")
location = input("Enter your location: ")
insert_data(name = name, location=location)
#create_table()
#drop_table()
#insert_data()
#delete_item()
#update_item()
retrieve_data()
one_item()