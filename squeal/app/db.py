import sqlite3


class Database:

    """ Creates a database instance - Simplifies database operations
        I wrote most of this so it can be reused in future projects. """

    def __init__(self, db_file: str):
        self.__db_file = db_file
        self.__db_conn = self.__connect_db()

    def __connect_db(self):

        """ Private Method: Opens the database file. """

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

        """ Private Method: Open's and closes the cursor """

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

    def search_user(self, table: str, return_columns: str, where_like: tuple = None):

        """ issues the following statement to the SQLite db items in brackets are optional

            SELECT column FROM table (WHERE key like '%search_string%')
                                        ( OR key like '%search_string%') """

        sql_statement = f"SELECT {return_columns} FROM {table}"
        if where_like:  # if parameter passed execute this
            sql_statement += f" WHERE {where_like[0]} like '%{where_like[1]}%';"
        try:
            rows = self.__cursor(sql_statement, fetch=True)
            return rows
        except sqlite3.Error as error:
            print(" !", str(error).capitalize())

    def add_user(self, *user_details):
        sql_statement = "INSERT INTO users (first_name, last_name, email_address, role, username, password)"\
            f"VALUES (?,?,?,?,?,?);"
        try:
            self.__cursor(sql_statement, user_details)
            self.__db_conn.commit()
        except sqlite3.Error as e:
            print(f" * {e}")
        print(" * Record added.")

