import psycopg2
from get_planet_data import get_planet_data

try:
    #connect to postgres
    conn = psycopg2.connect("dbname='scraping' host='localhost' user='postgres' password='1234'")
        
    # the SQL INSERT statement we will use. 
    insert_sql = ('INSERT INTO public."Planets" (Name, Mass, Radius, Description, MoreInfo) VALUES (%s, %s, %s, %s, %s)')
    #open a cursor to access data
    cur = conn.cursor()
    
    #get the planets data and loop through each
    planet_data = get_planet_data()
    
    for planet in planet_data:
        #extract values from the dictionary in the correct order 
        planet_values = (planet['Name'], planet['Mass'], planet['Radius'], planet['Description'], planet['MoreInfo'])
        
        #write each record. 
        cur.execute(insert_sql, planet_values)
        
    # commit ther new changes 
    conn.commit()
    cur.close()
    conn.close()
    
    print("Successfully wrote the data to the database.")
    
except Exception as e:
    print(e)
