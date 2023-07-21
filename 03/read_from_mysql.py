import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='mypassword', host='127.0.0.1', database='scraping')
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM scraping.Planets")
    
    for row in cursor:
        print(row)
        
    # close the cursor and connection
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Please check your username and password.")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Databases does not exist")
    else:
        print(err)
finally:
    cnx.close()