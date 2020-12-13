import psycopg2
from datetime import datetime

def create_connection():
    conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='',
    password='',
    database='',
    sslmode='require')
    return conn

def post_search_data(userID,Keyword):
    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute("Insert into public.searches Values('{}','{}','{}'))".format(
    userID,Keyword,
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()

def fetch_search_data(userID,Keyword):
    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute("Select * from public.seaches where userID='{}' Keyword like '%'".format(userID)+Keyword+"%")
    results = cursor.fetchall()
    conn.close()
    return results
