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
college = input('Enter college name: ')
students = input('Enter student population: ')
city = input('Enter city name: ')
state = input('Enter state name: ')
country = input('Enter country name: ')
query = (f'INSERT INTO `Colleges` VALUES (22,"{college}",{students},"{city}","{state}","{country}")')

cursor.execute(query)
# printing the rows in the table

query=("select * from colleges")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()
