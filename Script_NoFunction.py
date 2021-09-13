#NOT using a function
import mysql.connector

#Establishing the connection with the database, in this case: host = localhost, name of the database = school, user and pass = root
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='school',
                                         user='root',
                                         password='root')
#Inserting the same commands as workbench or cmd, INSERT INTO tableName(.....)
#VALUES(........), in this case we assign it to a variable
    mySql_insert_query = """INSERT INTO classroom1 (id, name, last_name, age) 
                           VALUES  (108,'Martin','Hermitage',20) """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into classroom1 table")
    cursor.close()
#If connection fails
except mysql.connector.Error as error:
    print("Failed to insert record into classroom1 table {}".format(error))
#If connection success
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
