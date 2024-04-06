import mysql.connector

# MySQL server connection details
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'pynews'
}


def user_connect(username, password):

    try:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(**config)

        if conn.is_connected():
            print('Connected to MySQL server')

            cursor = conn.cursor()

            query = "SELECT * FROM USERS WHERE username = %s AND password = %s;"
            cursor.execute(query, (username, password))

            # checking if the database returns the result
            row = cursor.fetchall()

            # Close cursor and connection
            cursor.close()
            conn.close()

            if row:  # user exists if true
                print('Data exists')
                return True

            else:
                print('Data not found')
                return False

    except mysql.connector.Error as e:
        print(f'Error connecting to MySQL server: {e}')
        return False


def add_data():
    try:
        conn = mysql.connector.connect(**config)

        if conn.is_connected():
            print('connect established')

        cursor = conn.cursor()

        insert_query = """
        INSERT INTO USERS (username, password) VALUES
        ('Shahid', 'shahid@123'),
        ('Imran', 'imran@123'),
        ('Salman', 'salman@123')
        """
        cursor.execute(insert_query)
        print('query inserted')

        # Commit the transaction
        conn.commit()

        cursor.execute('SELECT * FROM USERS;')
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print('Error while connecting ', e)


def print_all():
    try:
        conn = mysql.connector.connect(**config)

        if conn.is_connected():
            print('connect established')

        cursor = conn.cursor()

        cursor.execute('SELECT * FROM USERS;')

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print('Error while connecting ', e)

# user_connect('shahid', 'shahid@123')
print_all()