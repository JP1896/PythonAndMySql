#USING a function
import mysql.connector

def insert_variables(id,name,last_name,age):

#Establishing the connections with the database in MySql.....USER AND PASS : root
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='school',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO classroom1(id,name,last_name,age)
                                 VALUES (%s, %s, %s, %s) """



        record = (id,name,last_name,age)
        cursor.execute(mySql_insert_query,record)

        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into classroom1 table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into classroom1 table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

insert_variables(110,'Camila','Donovan',21)
