import psycopg2

class DisplayMenu:
    def displayMenu():
        def getMenu():
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

        conn = getMenu()
        curr = conn.cursor()
        curr.execute("SELECT * FROM datamenurestoran;")
        data = curr.fetchall()
        for row in data:
            print(row)
        conn.close()
#test
    displayMenu()
