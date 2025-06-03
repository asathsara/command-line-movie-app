# Movie App

A Python-based application for managing and exploring movies.

## Features

- **Browse and search movies:** Effortlessly explore the movie collection with intuitive browsing and powerful search capabilities, allowing users to quickly find movies by title, genre, or other attributes.
- **Add, edit, and delete movie entries:** Easily manage the movie database by adding new movies, updating existing entries, or removing movies as needed, ensuring the collection stays accurate and up to date.
- **User-friendly interface:** Enjoy a clean and intuitive interface designed for ease of use, making navigation and movie management straightforward for users of all experience levels.

## Database Support

This project now supports persistent storage using SQLite. All movie data is stored in a local SQLite database file (`movies.db`).

No additional dependencies are required as Python's built-in `sqlite3` module is used.

## Project Structure

```
Movie app/
├── main.py
├── requirements.txt
├── README.md
└── (other source files)
```

## Example: Using SQLite in Python

Below is a basic example of how to interact with the SQLite database in this project:

```python
import sqlite3

DB_NAME = 'movies.db'

conn = sqlite3.connect(DB_NAME)  # Open connection to DB
c = conn.cursor()                # Create a cursor object

c.execute('...')                 # Run SQL commands
results = c.fetchall()           # Get results (if SELECT)

conn.commit()                    # Commit changes (if needed)
conn.close()                     # Close connection
```

Replace `'...'` with your desired SQL statement (e.g., `SELECT * FROM movies`).