import mysql.connector
import get_planet_data
from mysql.connector import errorcode
from get_planet_data import get_planet_data

try:
    # open the database
    cnx = mysql.connector.connect(user='root', password='mypassword', database="scraping")
    insert_sql = ("INSERT INTO Planets (Name, Mass, Radius, Description) VALUES (%s, %s, %s, %s)")
    
    planet_data = get_planet_data()
    
    # loop through all planets executing INSERT for each with the cursor
    cursor = cnx.cursor()
    for planet in planet_data:
        print("Storing data for %s" %(planet['Name']))
        cursor.execute(insert_sql, (planet['Name'], planet['Mass'], planet['Radius'], planet['Description']))
        
    # commit the new records
    cnx.commit()
    
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username and password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
        
else:
    cnx.close()
