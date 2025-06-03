from movie import Movie
import database

class MovieManager:
    def __init__(self):
        database.init_db()
    
    # Method to add a movie  
    def add_movie(self):
        movie_id = input("\nEnter movie ID: ")
        title = input("Enter movie title: ")
        director = input("Enter movie director: ")
        try:
            release_year = int(input("Enter movie release year: "))
        except ValueError:
            print("\nInvalid year. Please enter a valid integer.\n")
            return
        genre = input("Enter movie genre: ")
        success = database.add_movie_db(movie_id, title, director, release_year, genre)
        if success:
            print("\nMovie added successfully.\n")
        else:
            print("\nMovie ID already exists.\n")

    # Method to view all movies
    def view_movies(self):
        movies = database.get_all_movies_db()
        if not movies:
            print("\nNo movies available.\n")
            return
        print("\n", "-" * 20)
        print("|       Movies      |")
        for m in movies:
            print("-" * 20, "\n")
            print(f"ID: {m[0]}\nTitle: {m[1]}\nDirector: {m[2]}\nRelease Year: {m[3]}\nGenre: {m[4]}")
            print("-" * 20 + "\n")

    # Method to search for a movie by title
    def search_movie(self):
        search_title = input("\nEnter movie title to search: ").lower()
        results = database.search_movies_db(search_title)
        if not results:
            print("\nNo movies found with that title.\n")
            return
        for m in results:
            print(f"\nID: {m[0]}\nTitle: {m[1]}\nDirector: {m[2]}\nRelease Year: {m[3]}\nGenre: {m[4]}")

    # Method to update a movie by ID
    def update_movie(self):
        movie_id = input("\nEnter movie ID to update: ")
        movies = database.get_all_movies_db()
        movie = next((m for m in movies if m[0] == movie_id), None)
        if not movie:
            print("\nMovie ID not found.\n")
            return
        print("\nLeave input blank to keep current value.")
        title = input(f"\nEnter new title (current: {movie[1]}): ") or movie[1]
        director = input(f"Enter new director (current: {movie[2]}): ") or movie[2]
        try:
            year_input = input(f"Enter new release year (current: {movie[3]}): ")
            release_year = int(year_input) if year_input else movie[3]
        except ValueError:
            print("Error: Release year must be a number.")
            return
        genre = input(f"Enter new genre (current: {movie[4]}): ") or movie[4]
        updated = database.update_movie_db(movie_id, title, director, release_year, genre)
        if updated:
            print("\nMovie updated successfully.\n")
        else:
            print("\nMovie update failed.\n")

    # Method to delete a movie by ID
    def delete_movie(self):
        movie_id = input("\nEnter movie ID to delete: ")
        deleted = database.delete_movie_db(movie_id)
        if deleted:
            print("\nMovie deleted successfully.\n")
        else:
            print("\nMovie ID not found.\n")





