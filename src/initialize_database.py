from database_connection import get_database_connection


def create_users_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        create table if not exists users (
            username text primary key,
            password text
        );
    """)

    connection.commit()


def drop_users_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)

    connection.commit()


def create_subject_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        create table if not exists subjects (
            id integer primary key,
            username text,
            name text,
            mastery_level text,
            time int
            );  
        """)
    connection.commit()


def drop_subject_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists subjects;
        """)

    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_users_table(connection)
    drop_subject_table(connection)
    create_users_table(connection)
    create_subject_table(connection)

    cursor = connection.cursor()

# Check the table schema
    tab = "subjects"
    cursor.execute(f"PRAGMA table_info({tab});")
    columns = cursor.fetchall()

    # Check if 'time' column exists
    if not any(column[1] == 'time' for column in columns):
        print("Adding 'time' column to the table...")
        cursor.execute(f"ALTER TABLE {tab} ADD COLUMN time TEXT;")
        connection.commit()
        print("'time' column added successfully!")
    else:
        print("'time' column already exists.")

    # Close the connection
    connection.close()

