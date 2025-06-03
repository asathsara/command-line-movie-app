import sqlite3

DB_NAME = 'movies.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            release_year INTEGER NOT NULL,
            genre TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_movie_db(movie_id, title, director, release_year, genre):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO movies VALUES (?, ?, ?, ?, ?)', (movie_id, title, director, release_year, genre))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_all_movies_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM movies')
    movies = c.fetchall()
    conn.close()
    return movies

def search_movies_db(search_title):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM movies WHERE LOWER(title) LIKE ?', (f'%{search_title.lower()}%',))
    results = c.fetchall()
    conn.close()
    return results

def update_movie_db(movie_id, title, director, release_year, genre):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        UPDATE movies SET title=?, director=?, release_year=?, genre=? WHERE id=?
    ''', (title, director, release_year, genre, movie_id))
    conn.commit()
    updated = c.rowcount
    conn.close()
    return updated > 0

def delete_movie_db(movie_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM movies WHERE id=?', (movie_id,))
    conn.commit()
    deleted = c.rowcount
    conn.close()
    return deleted > 0

# Call this at the start of your app to ensure the table exists
if __name__ == "__main__":
    init_db()
