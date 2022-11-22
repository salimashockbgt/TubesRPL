import psycopg2

class DisplayKeranjang:
    def displayKeranjang():
        def getKeranjang():
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

        conn = getKeranjang()
        curr = conn.cursor()
        curr.execute("SELECT * FROM datapesanancustomer;")
        data = curr.fetchall()
        for row in data:
            print(row)
        conn.close()
#test

    displayKeranjang()
