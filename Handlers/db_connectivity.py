import mysql.connector


# MySQL server connection details
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'newsprism'
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

            if row:  # user exists if  true
                print('Data exists')
                return True

            else:
                print('Data not found')
                return False

    except mysql.connector.Error as e:
        print(f'Error connecting to MySQL server: {e}')
        return False


def add_user(name, username, password, pfp, bio):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query = """
        INSERT INTO USERS(name, username, password, profile_picture, bio) VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, username, password, pfp, bio))
        conn.commit()
        print('User added to the Database')

        return True

    except mysql.connector.Error as e:
        print('error while adding user: ', e)

        return False

    finally:
        cursor.close()
        conn.close()


def add_data():  # for testing only
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
        print('Error: ', e)


def add_article(article_picture, article_title, article_description, username):
    '''Adds data to the centralized Article table'''
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        print(article_picture, type(article_picture))

        insert_query = f"""
        INSERT INTO ARTICLES (article_picture, article_title, article_description, username)
        VALUES (%s, %s, %s, %s)
        """

# Bind data securely using placeholders and cursor.execute()
        cursor.execute(insert_query, (article_picture,
                    article_title, article_description, username))

        print('Article Added to the DB')

        conn.commit()

    except mysql.connector.Error as e:
        print('Error: ', e)

    finally:
        cursor.close()
        conn.close()


def retrive_user_articles(username):
    '''
    Retrives the articles based on username from the centralized Articles table
    '''
    try:
        conn = mysql.connector.connect(**config)
        
        cursor = conn.cursor()

        query = "SELECT  article_picture, article_title, article_description, published_date FROM ARTICLES WHERE username = %s"

        cursor.execute(query, (username,))
        articles = cursor.fetchall()

        return articles


    except mysql.connector.Error as e:
        print('error: ', e)

    finally:
        cursor.close()
        conn.close()


def retrive_all_verses():
    '''
    Retrives all the verses(articles) from centeralized table
    '''

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query = "SELECT article_picture, article_title, article_description, published_date, username FROM ARTICLES"
        cursor.execute(query)

        verses = cursor.fetchall()
        return verses

    except mysql.connector.Error as e:
        print('Error while retrieving verses: ', e)

    finally:
        cursor.close()
        conn.close()
    
def serve_profile_data(username):
    '''
    Retrives users' data such as their name, profile pic and bio (too lazy to add bio) and sends it to their profile page
    '''

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query = "SELECT name, bio, profile_picture FROM USERS WHERE username = %s"
        cursor.execute(query, (username,))

        user_profile_data = cursor.fetchall()
        user_profile_data = user_profile_data[0]
        print(user_profile_data)
        return user_profile_data

    except mysql.connector.Error as e:
        print('Error while fetching user data: ', e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    print(retrive_all_verses())