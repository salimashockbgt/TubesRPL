import psycopg2

def get_connection():
    try:
        return psycopg2.connect(
            database="DataRestoran",
            user="postgres",
            password="123",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False
  
conn = get_connection()
  
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")


conn = get_connection()
curr = conn.cursor()
print("------------------MENU------------------")
curr.execute("SELECT * FROM datamenurestoran;")
data = curr.fetchall()
for row in data:
    print(row)
conn.close()

