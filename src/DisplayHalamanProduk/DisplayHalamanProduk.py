import psycopg2

class DisplayHalamanProduk():
    def displayHalamanProduk():
        def getHalamanProduk():
            try:
                return psycopg2.connect(
                    database="DataRestoran",
                    user="postgres",
                    password="Kimjongin140194",
                    host="127.0.0.1",
                    port=5432,
                )
            except:
                return False
        
        conn = getHalamanProduk()
        curr = conn.cursor()
        curr.execute("SELECT * FROM datapesanancustomer;")
        data = curr.fetchall()
        for row in data:
            print(row)
        conn.close()
#test
    displayHalamanProduk()