# Parent class
class Media:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def show_info(self):
        print(f"{self.title} ({self.year})")
        

# Child class (inherits from Media)
class Movie(Media):
    def __init__(self, title, year, director, genre):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre

    def play(self):
        print(f"Now playing '{self.title}' directed by {self.director} ")

    def get_genre(self):
        print(f"Genre: {self.genre}")


# create objects
m1 = Movie("Inception", 2010, "Christopher Nolan", "Sci-Fi")
m2 = Movie("Black Panther", 2018, "Ryan Coogler", "Action")

# test methods
m1.show_info()
m1.play()
m1.get_genre()

m2.show_info()
m2.play()
m2.get_genre()
