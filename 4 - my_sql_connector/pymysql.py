import pymysql

# set to true to test locally using Cloud SQL proxy listening on a TCP port
DEBUG = False

mysql_config = {
    "user": "root",
    "password": "cars",
    "host": "localhost",
    "database": "cars_database",
    "port": 3306,
}

# Create SQL connection globally to enable reuse
# PyMySQL does not include support for connection pooling
mysql_conn = None


def get_cursor():
    """
    Helper function to get a cursor
      PyMySQL does NOT automatically reconnect,
      so we must reconnect explicitly using ping()
    """
    if not mysql_conn.open:
        mysql_conn.ping(reconnect=True)
    return mysql_conn.cursor()


def init_conn():
    global mysql_conn

    if not mysql_conn:
        mysql_conn = pymysql.connect(**mysql_config)
