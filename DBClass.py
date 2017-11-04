import mysql.connector as connector
class DbClass:
    def __init__(self):

        self.__dsn = {
            "host": "localhost",
            "user": "vitalonga",
            "passwd": "1830YAF532",
            "db": "vitalongadb"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()


    def getCapsules(self):
        # Query met parameters
        sqlQuery = "SELECT naam, beschrijving FROM KoffieSoort ORDER BY KoffieSoortID"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def storeCapsules(self, keuze1, keuze2, keuze3, keuze4):
        self.__cursor.execute("TRUNCATE  koffieDispenser")
        self.__connection.commit()
        query = "INSERT INTO vitalongadb.koffieDispenser(naam, beschrijving) " \
                "VALUES ('" + keuze1 + "', beschrijving ),('" + keuze2 + "', beschrijving)," \
                "('" + keuze3 + "', beschrijving),('"+ keuze4 + "', beschrijving)"

        self.__cursor.execute(query)
        # data comitten
        self.__connection.commit()

    def chosenCapsules(self):
        # Query met parameters
        sqlQuery = "SELECT * FROM koffieDispenser"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def chosenCapsule(self, product_name):
        # Query met parameters
        sqlQuery = "SELECT * FROM koffieDispenser WHERE koffieDispenserID ='" + product_name + "'"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def storekoffie(self):
        # Query met parameters
        sqlQuery = "INSERT INTO vitalongadb.gebruik(naam) VALUES('KOFFIE')"
        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result
