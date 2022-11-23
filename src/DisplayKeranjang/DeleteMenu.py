import psycopg2

def DeleteMenu():
    try:
        connection = psycopg2.connect(
                    database="DataRestoran",
                    user="postgres",
                    password="123",
                    host="127.0.0.1",
                    port=5432)

        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = "DELETE FROM datapesanancustomer"
        cursor.execute(sql_delete_query)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

#test
#DeleteMenu()
