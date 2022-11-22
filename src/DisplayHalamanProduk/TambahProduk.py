import psycopg2

def TambahProduk(id_barang, jumlah_barang, nama_barang, harga_barang):
    try:
        connection = psycopg2.connect(database="DataRestoran",
                    user="postgres",
                    password="123",
                    host="127.0.0.1",
                    port=5432)

        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO datapesanancustomer (id_barang, jumlah_barang, nama_barang, harga_barang) VALUES (%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, (id_barang, jumlah_barang, nama_barang, harga_barang))

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into datapesanancustomer")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into datapesanancustomer", error)


# if __name__ == "__main__":
    # TambahProduk(1, 2, "Teh Hangat", 5000.0)
