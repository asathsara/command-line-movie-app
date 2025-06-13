class Movie:
    def __init__(self, movie_id: int, title: str, director: str, release_year: int, genre: str):
        
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre

    def __str__(self):
        return (
            f"\nID: {self.movie_id}\n"
            f"Title: {self.title}\n"
            f"Director: {self.director}\n"
            f"Year: {self.release_year}\n"
            f"Genre: {self.genre}\n"
        )
    

class MovieManager:
    def __init__(self):
        self.movies = {}
     
    # Method to add a movie  
    def add_movie(self):
        movie_id = input("\nEnter movie ID: ")
        if movie_id in self.movies:
            print("\nMovie ID already exists.\n")
            return
        
        
        title = input("Enter movie title: ").strip()
        director = input("Enter movie director: ").strip()
        
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




def main():
    manager = MovieManager()
    while True:
        print("\n", "-" * 20)
        print("|   Movie Manager   |")
        print("-" * 20, "\n")
        print("1. Add a new movie")
        print("2. View all movies")
        print("3. Search for a movie by title")
        print("4. Update a movie")
        print("5. Delete a movie")
        print("6. Exit\n")

        choice = input("Choose an option (1-6): ")
        if choice == '1':
            manager.add_movie()
        elif choice == '2':
            manager.view_movies()
        elif choice == '3':
            manager.search_movie()
        elif choice == '4':
            manager.update_movie()
        elif choice == '5':
            manager.delete_movie()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
