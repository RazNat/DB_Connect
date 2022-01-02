import mysql.connector
import yaml
import pandas as pd
import numpy as np
import os
from flask import Flask, render_template

db_user = os.environ["root"]
db_pass = os.environ["3umP3LecFgn53c5l"]
db_name = os.environ["education"]
db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
instance_connection_name = os.environ["dbcloud-336721:northamerica-northeast2:bogle2022"]

pool = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL.create(
        drivername="mysql+pymysql",
        username=db_user,  # e.g. "my-database-user"
        password=db_pass,  # e.g. "my-database-password"
        database=db_name,  # e.g. "my-database-name"
        query={
            "unix_socket": "{}/{}".format(
                db_socket_dir,  # e.g. "/cloudsql"
                instance_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
        }
    ),
    **db_config
)
query = 'select Name from Colleges'
df = pd.read_sql(query, con = pool)
print(df)
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
