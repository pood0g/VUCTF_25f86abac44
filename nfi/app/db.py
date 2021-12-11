from hashlib import sha256
import sqlite3

somepath = "s3cr3t/f1l3/p4th/flag2.txt"

class Database:

    def __init__(self, db_file: str):
        self.__db_file = db_file
        self.__db_conn = self.__connect_db()

    def __connect_db(self):
        try:
            db_conn = sqlite3.connect(self.__db_file, check_same_thread=False)
        except sqlite3.Error as error:  # unlikely but we need to handle this just in case
            print(" ! Database connection failed!")
            print(" ! ", error)
            return
        print(" * Database connection success!")
        print(" * SQLite version", sqlite3.version)
        return db_conn

    def __cursor(self, statement: str, values: tuple = None, fetch=False):
        cursor = self.__db_conn.cursor()
        cursor.execute(statement, values) if values else cursor.execute(statement)
        if fetch:
            rows = cursor.fetchall()
            cursor.close()
            return rows
        cursor.close()

    def db_close(self):
        self.__db_conn.close()
        print(" * Database closed cleanly.")

    def login(self, creds: tuple):
        try:
            if (salt := self.__cursor("SELECT salt FROM users WHERE username = ?", (creds[0],), fetch=True)):
                salted_password = sha256((salt[0][0] + creds[1]).encode()).hexdigest()
                sql_statement = "SELECT username, role FROM users WHERE username = ? and password = ?"
                row = self.__cursor(sql_statement, (creds[0], salted_password), fetch=True)
                if row:
                    return row[0]
        except sqlite3.Error as error:
            print(" !", str(error).capitalize())
