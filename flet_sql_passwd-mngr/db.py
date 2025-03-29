import sqlite3

# specify database here:
conn = sqlite3.connect("mngr.dat", check_same_thread=False)  # check_same_thread false: allows reload
cur = conn.cursor()

def initialize_db():
    """Creates the mypass table, if it doesn't exist yet."""
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mypass(id integer primary key autoincrement, service text, handle text, password text)
        """)
    
def close_db():
    conn.close()
    
def create_pass(service, handle, password):
    """Inserts a new password into mypass."""
    try:
        cur.execute("""
            INSERT INTO mypass(service, handle, password)
            VALUES(?, ?, ?)    
            """, (service, handle, password))
        conn.commit()
        return 0
    except:
        return 1
    
def change_pass(id, password):
    """Changes a password for a specific id"""
    try:
        cur.execute("""
            UPDATE mypass SET password = ?
            WHERE id = ?;
            """, (password, id))
        conn.commit()
        return 0
    except:
        return 1
    
def delete_pass(id):
    """Delete the specific entry from mypass"""
    try:
        cur.execute("""
            DELETE FROM mypass
            WHERE id = ?;
            """, (str(id))
        )
        conn.commit()            
        return 0
    except:
        return 1
    
def get_all():
    """Gets all rows and columns from mypass table"""
    cur.execute("""SELECT * FROM mypass""")
    return cur.fetchall()

def get_by_service(service):
    """Gets all rows and columns matching a specific service"""
    service = "%" + service + "%"
    cur.execute(
        """
        SELECT * FROM mypass
        WHERE service LIKE ?
        """,
        (service,)
    )
    return cur.fetchall()

def get_by_handle(handle):
    """Gets all rows and columns matching a specific handle"""
    handle = "%" + handle + "%"
    cur.execute(
        """
        SELECT * FROM mypass
        WHERE handle LIKE ?
        """, (handle,)
    )
    return cur.fetchall()

def get_by_id(id):
    """Fetches a specific mypass row by id"""
    cur.execute(
        """
        SELECT * FROM mypass
        WHERE id = ?
        """        , (str(id),)
    )
    return cur.fetchone()

