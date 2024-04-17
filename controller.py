import sqlite3 as sql

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE streamers(
        name text,
        followers integer,
        subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre,followers, subs):
   conn = sql.connect("streamers.db")
   cursor = conn.cursor()
   instruccion = f"INSERT INTO streamers VALUES('{nombre}',{followers}, {subs}) "
   cursor.execute(instruccion)
   conn.commit()
   conn.close()

def readRow():
   conn = sql.connect("streamers.db")
   cursor = conn.cursor()
   instruccion = f"SELECT * FROM streamers"
   cursor.execute(instruccion)
   datos = cursor.fetchall()
   conn.commit()
   conn.close()
   print(datos)

def insertRows(streamersList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES(?,?,?) "
    cursor.executemany(instruccion,streamersList)
    conn.commit()
    conn.close()


def readOrdered(field):
   conn = sql.connect("streamers.db")
   cursor = conn.cursor()
   instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
   cursor.execute(instruccion)
   datos = cursor.fetchall()
   conn.commit()
   conn.close()
   print(datos)

def search():
   conn = sql.connect("streamers.db")
   cursor = conn.cursor()
   instruccion = f"SELECT * FROM streamers WHERE name = 'Ibai'"
   cursor.execute(instruccion)
   datos = cursor.fetchall()
   conn.commit()
   conn.close()
   print(datos)

def updateFields():
   conn = sql.connect("streamers.db")
   cursor = conn.cursor()
   instruccion = f"UPDATE  streamers SET followers =7000000  WHERE name = 'Brains'"
   cursor.execute(instruccion)
   
   conn.commit()
   conn.close()
   
def deleteRow():
   conn = sql.connect("streamers.db")
   cursor = conn.cursor()
   instruccion = f"DELETE FROM streamers WHERE name = 'AuronPlay'"
   cursor.execute(instruccion)
   
   conn.commit()
   conn.close()
   

if __name__ == "__main__":
    streamers = [
        ('AuronPlay', 20000000, 1000000), 
        ('Midudev', 5000000, 3000000),
        ('Brains', 3000000, 3000000)
        ]
    deleteRow()