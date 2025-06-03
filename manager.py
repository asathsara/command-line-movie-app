from movie import Movie

class MovieManager:
    def __init__(self):
        self.movies = {}
     
    # Method to add a movie  
    def add_movie(self):
        movie_id = input("\nEnter movie ID: ")
        if movie_id in self.movies:
            print("\nMovie ID already exists.\n")
            return
        
        
        title = input("Enter movie title: ")
        director = input("Enter movie director: ")
        
        # Check entered year is a valid 
        try:
            release_year = int(input("Enter movie release year: "))
        except ValueError:
            print("\nInvalid year. Please enter a valid integer.\n")
            return
        
        genre = input("Enter movie genre: ")
        
        self.movies[movie_id] = Movie(movie_id, title, director, release_year, genre)
        print("\nMovie added successfully.\n")
        
    # Method to view all movies
    def view_movies(self):
        if not self.movies:
            print("\nNo movies available.\n")
            return
            
        print("\n", "-" * 20)
        print("|       Movies      |")
        for movie in self.movies.values():
            print("-" * 20, "\n")
            print(movie)
            print("-" * 20 + "\n")  # Separator
                
        # Method to search for a movie by title
    def search_movie(self):
        search_title = input("\nEnter movie title to search: ").lower()
        found = False
            
        for movie in self.movies.values():
            if search_title in movie.title.lower():
                print("\n" + str(movie))
                found = True
             
        if not found:
            print("\nNo movies found with that title.\n")   
                
    # Method to update a movie by ID
    def update_movie(self):
        movie_id = input("\nEnter movie ID to update: ")
            
        if movie_id not in self.movies:
            print("\nMovie ID not found.\n")
            return
            
        movie = self.movies[movie_id]
        print("\nLeave input blank to keep current value.")
            
        title = input(f"\nEnter new title (current: {movie.title}): ") or movie.title
        director = input(f"Enter new director (current: {movie.director}): ") or movie.director
            
        try:
            year_input = input(f"Enter new release year (current: {movie.release_year}): ")
            release_year = int(year_input) if year_input else movie.release_year
        except ValueError:
            print("Error: Release year must be a number.")
            return
        genre = input(f"Enter new genre (current: {movie.genre}): ") or movie.genre
            
        self.movies[movie_id] = Movie(movie_id, title, director, release_year, genre)
        print("\nMovie updated successfully.\n")
            
    # Method to delete a movie by ID
    def delete_movie(self):
        movie_id = input("\nEnter movie ID to delete: ")
        if movie_id in self.movies:
            del self.movies[movie_id]
            print("\nMovie deleted successfully.\n")
        else:
            print("\nMovie ID not found.\n")





