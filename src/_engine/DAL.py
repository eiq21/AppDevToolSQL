from Database import Database


def main():
    query_line = []
    db = Database("Demo01")
    cnx = db.Connect()
    query = "select * from dbo.category"
    cursor = cnx.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    while row:
        query_line.append(str(row[1]) + '\n')
        row = cursor.fetchone()

    db.Close()
    return query_line


if __name__ == "__main__":
    main()
