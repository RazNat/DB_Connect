import mysql.connector

def connection():
    cnx = mysql.connector.connect(user='root',
    password = 'MySQL366#',
    host = '127.0.0.1',
    database = 'education',
    auth_plugin = 'mysql_native_password')
    return cnx

cnx = connection()

cursor = cnx.cursor()
query=("select * from colleges")
cursor.execute(query)

#print all rows
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()    