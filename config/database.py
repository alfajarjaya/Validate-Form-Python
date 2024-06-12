import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="YOUR_HOST",
                user="YOUR_USER",
                password="YOUR_PASSWORD",
                database="YOUR_DATABASE"
            )
            self.mycursor = self.mydb.cursor()
        except Error as e:
            self.mydb = None
            self.mycursor = None
            raise Exception(f"Problem connecting to database: {e}")

    def create_users_table(self, email):
        try:
            self.mycursor.execute(
                f'''
                CREATE TABLE IF NOT EXISTS `{email}`(
                    email VARCHAR(255) PRIMARY KEY,
                    password VARCHAR(255) NOT NULL
                )
                '''
            )
            self.mydb.commit()
        except Error as e:
            self.mydb.rollback()
            raise Exception(f"Problem creating table: {e}")

    def insert(self, email, password):
        self.create_users_table(email)

        try:
            insert_query = f'''
                INSERT INTO `{email}` (email, password)
                VALUES (%s, %s)
            '''
            self.mycursor.execute(insert_query, (email, password))
            self.mydb.commit()
        except Error as e:
            self.mydb.rollback()
            raise Exception(f"Problem inserting data: {e}")

    def select(self, email, password):
        try:
            selection = f'''
                SELECT * FROM `{email}` WHERE email = %s AND password = %s
            '''
            self.mycursor.execute(selection, (email, password))
            result = self.mycursor.fetchall()
            return result
        except Error as e:
            self.mydb.rollback()
            raise Exception(f"Problem selecting data: {e}")
