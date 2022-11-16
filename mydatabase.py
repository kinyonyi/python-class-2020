import psycopg2

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


cur = conn.cursor()  # creating a cursor

def createTable():
    cur.execute("""
    CREATE TABLE Employee
    (
        ID SERIAL,
        NAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL
    )
    """)

    # commit the changes
    conn.commit()
    print("Table Created successfully")
    
def insertData():
    cur.execute("""
        INSERT INTO Employee (NAME,EMAIL) VALUES
        ('Alan Walker','awalker@gmail.com'),
        ('Steve Jobs','sjobs@gmail.com'),
        ('Steve Jobs','sjobs@gmail.com'),
        ('Steve Jobs','sjobs@gmail.com'),
        ('Steve Jobs','sjobs@gmail.com'),
    """)
    print("data inserted")
    conn.commit()
    
def allData():
    cur.execute("SELECT * FROM Employee")
    rows = cur.fetchall()
    for data in rows:
        print("ID :" + str(data[0]))
        print("NAME :" + data[1])
        print("EMAIL :" + data[2])
    
    print('Data fetched successfully')
    conn.close()

def updateData():
    cur = conn.cursor()
    cur.execute("UPDATE Employee set EMAIL = 'updated@gmail.com' WHERE ID = 1 ")
    conn.commit()
    print("Data updated Successfully")
    print("Total row affected "+str(cur.rowcount))
    
def deleteData():
    cur = conn.cursor()
    cur.execute("DELETE FROM Employee WHERE ID =1 ")
    conn.commit()
    #conn.rollback()
    print("Data deleted Successfully")
    print("Total row affected "+str(cur.rowcount))
    
insertData()
deleteData()
allData()
"""
The main entry points of Psycopg are:
The connect() function creates a new database session and returns a new instance of connection.
The class connection encloses a database session. It allows to :
create new cursor instance
terminate transaction using commit() or rollback() methods.
The cursor allows interaction with the database:
send commands to the database using execute() and executemany() methods.
retrieve data from the database using methods such as fetchone(), fetchmany(), fetchall(), or by iteration.
"""