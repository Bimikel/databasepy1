import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import pandas

df = pandas.read_csv('username.csv')

def get_current_time_string():
    current_time = datetime.now()
    time_string = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    return time_string

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="asdfwefa",
        database="june3db"
    )
    mycursor = mydb.cursor()
    print("Connection to MySQL established.")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    exit(1)

tablename = "usernames4"

create_table_query = f"""
CREATE TABLE IF NOT EXISTS {tablename} (
    Username VARCHAR(50),
    Identifier INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
)
"""

mycursor.execute(create_table_query)

insert_query = f"""
INSERT INTO {tablename} (Username, Identifier, FirstName, LastName)
VALUES (%s, %s, %s, %s)
"""

for i, row in df.iterrows():
    mycursor.execute(insert_query, tuple(row))
  
mydb.commit()

print(f"The number of columns is: {df.shape[1]}.")
print(df)

column_types = df.dtypes
print('\nData types of each column:')
print(column_types)

# csv file is automatically closed now
mycursor.close()
mydb.close()
