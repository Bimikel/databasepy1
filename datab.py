import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysecret",
  database="june3db"
)

def get_current_time_string():
    current_time = datetime.now()
    time_string = current_time.strftime("%Y_%m_%d_%H_%M_%S")
    return time_string

# Example usage
tname = get_current_time_string()

mycursor = mydb.cursor()

command = "CREATE TABLE table_" + tname + "(name VARCHAR(255), address VARCHAR(255))"

mycursor.execute(command)

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mycursor.close()
mydb.close()