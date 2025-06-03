class Movie:
    def __init__(self, movie_id: int, title: str, director: str, release_year: int, genre: str):
        
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre

    def __str__(self):
        return (f"ID: {self.movie_id}, Title: {self.title}, Director: {self.director}, "
                f"Year: {self.release_year}, Genre: {self.genre}")
    