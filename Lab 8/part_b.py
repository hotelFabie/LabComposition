#Part B

#1
movie = {
    "title" : "Noroi: The Curse",
    "director" : "Kōji Shiraishi",
    "rating" : 6.8
}

#2
class Movie:
    def __init__(self, title : str, director : str, rating : float):
        self.title = title,
        self.director = director,
        self.rating = rating

    #3
    def is_highly_rated(self) -> bool:
        if self.rating >= 7.5:
            return True
        return False

movie_instance = Movie("Noroi: The Curse", "Kōji Shiraishi", 6.8)


#4
#I would choose a class where we want to quickly/mass produce related objects. E.g. a customer has personal information, and there are usually more than a handful.
#Dictionary would, however, be more beneficial when we want to store related information that stays universal but can be changed,
#like a configuration.