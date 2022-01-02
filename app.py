import mysql.connector
import yaml
import pandas as pd
import numpy as np
import os
from flask import Flask, render_template

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
#print(df)
"""
A sample Hello World server.

"""

# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

# x = pd.DataFrame(np.random.randn(20, 5))
    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision, data = df.to_html())

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
