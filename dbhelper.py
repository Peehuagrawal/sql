import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hit-db-demo"
            )
            self.mycursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print("Some error occurred. Could not connect to database:", e)
            sys.exit(0)
        else:
            print("connected to database")

    def register(self, name, email, password):
        try:
            sql = """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
            """
            self.mycursor.execute(sql, (name, email, password))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print("Error inserting user:", e)
            return False
        
    def search(self, email,password):
        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'""".format(email,password))
        data= self.mycursor.fetchall()
        return data
            