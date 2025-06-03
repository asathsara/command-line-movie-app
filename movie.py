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
    