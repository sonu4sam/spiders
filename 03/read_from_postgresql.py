import psycopg2

try:
    conn = psycopg2.connect("dbname='scraping' host='localhost' user='postgres' password='1234'")
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Planets"')
    rows = cur.fetchall()
    print(rows)
    
    cur.close()
    conn.close()
    
except Exception as ex:
    print(ex)
    
    