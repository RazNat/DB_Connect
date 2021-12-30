import mysql.connector
import yaml
import pandas as pd

db = yaml.safe_load(open('db.yaml'))
config ={
    'user':         db['user'],
    'password':     db['pwrd'],
    'host':         db['host'],
    'database':     db['db'],
    'auth_plugin':  'mysql_native_password'
}
cnx = mysql.connector.connect(**config)
query = 'select Name from Colleges'
df = pd.read_sql(query, con = cnx)
print(df)