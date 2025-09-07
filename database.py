import sqlite3
import bcrypt # A library for hashing passwords

class Database:
    """A class to manage all database interactions."""

    def __init__(self, db_name='medical_chatbot.db'):
        """Initializes the database connection and creates tables if they don't exist."""
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        """Creates the necessary tables."""
        # User table with a securely hashed password
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_user(self, username, password):
        """Adds a new user with a hashed password. Returns True on success."""
        if not username or not password:
            return False
            
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        try:
            self.cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError: # This happens if the username already exists
            return False

    def check_user(self, username, password):
        """Checks if a user's credentials are correct."""
        self.cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        
        if result:
            stored_hash = result[0]
            # Check the provided password against the stored hash
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                return True
        return False

    def close(self):
        """Closes the database connection."""
        self.conn.close()