from .ConfigDB.Database import Database


def main():
    query_line = []
    db = Database("Demo01")
    cnx = db.Connect()
    query = "select * from dbo.category"
    cursor = cnx.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    while row:
        query_line.append(row[0].rstrip() + '\n')
        row = cursor.fetchone()

    db.Close()
    return query_line


if __name__ == "__main__":
    main()
