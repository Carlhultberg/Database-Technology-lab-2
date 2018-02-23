import psycopg2
import pprint

class Database():

    def __init__(self, host, dbname, user, password):

        conn_string = "host='"+host+"' dbname='"+dbname+"' user='"+user+"' password='"+password+"'"
        self.connection = psycopg2.connect(conn_string)
        self.cursor = self.connection.cursor()


    def select(self, command):

        self.cursor.execute(command)
        return self.cursor.fetchall()


db = Database("localhost", "dbname", "hejsan", "1234")
pprint.pprint(db.select("SELECT * FROM dbname"))
