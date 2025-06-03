from manager import MovieManager

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
