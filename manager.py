from movie import Movie

class MovieManager:
    def __init__(self):
        self.movies ={}
     
     # Method to add a movie  
    def add_movie(self):
        movie_id = input("Enter movie ID: ")
        if movie_id in self.movies:
            print("Movie ID already exists.")
            return
        
        
        title = input("Enter movie title: ")
        director = input("Enter movie director: ")
        
        # Check entered year is a valid 
        try:
            release_year = int(input("Enter movie release year: "))
        except ValueError:
            print("Invalid year. Please enter a valid integer.")
            return
        
        genre = input("Enter movie genre: ")
        
        self.movies[movie_id] = Movie(movie_id, title, director, release_year, genre)
        print("Movie added successfully.")
        
        # Method to view all movies
    def view_movies(self):
        if not self.movies:
            print("No movies available.")
            return
            
        for movie in self.movies.values():
            print(f"\nID: {movie.movie_id}")
            print(f"Title: {movie.title}")
            print(f"Director: {movie.director}")
            print(f"Release Year: {movie.release_year}")
            print(f"Genre: {movie.genre}")
            print("\n","-" * 20, "\n")
                
        # Method to search for a movie by title
    def search_movie(self):
        search_title = input("Enter movie title to search: ").lower()
        found = False
            
        for movie in self.movies.values():
            if search_title in movie.title.lower():
                print(movie)
                found = True
             
        if not found:
            print("No movies found with that title.")   
                
        # Method to update a movie by ID
    def update_movie(self):
        movie_id = input("Enter movie ID to update: ")
            
        if movie_id not in self.movies:
            print("Movie ID not found.")
            return
            
        movie = self.movies[movie_id]
        print("Leave input blank to keep current value.")
            
        title = input(f"Enter new title (current: {movie.title}): ") or movie.title
        director = input(f"Enter new director (current: {movie.director}): ") or movie.director
            
        try:
            year_input = input(f"Enter new release year (current: {movie.release_year}): ")
            release_year = int(year_input) if year_input else movie.release_year
        except ValueError:
            print("Error: Release year must be a number.")
            return
        genre = input(f"Enter new genre (current: {movie.genre}): ") or movie.genre
            
        self.movies[movie_id] = Movie(movie_id, title, director, release_year, genre)
        print("Movie updated successfully.")
            
        # Method to delete a movie by ID
    def delete_movie(self):
        movie_id = input("Enter movie ID to delete: ")
        if movie_id in self.movies:
            del self.movies[movie_id]
            print("Movie deleted successfully.")
        else:
            print("Error: Movie ID not found.")
                
            
            
        
        
        