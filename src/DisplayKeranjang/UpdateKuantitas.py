import psycopg2

def updateKuantitas(id_barang, jumlah_barang):
    try:
        connection = psycopg2.connect(
                    database="DataRestoran",
                    user="postgres",
                    password="123",
                    host="127.0.0.1",
                    port=5432)

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from datapesanancustomer where id_barang = %s"""
        cursor.execute(sql_select_query, (id_barang,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update datapesanancustomer set jumlah_barang = %s where id_barang = %s"""
        cursor.execute(sql_update_query, (jumlah_barang, id_barang))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from datapesanancustomer where id_barang = %s"""
        cursor.execute(sql_select_query, (id_barang,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

if __name__ == "__main__":
    updateKuantitas(1,5)
