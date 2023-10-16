from datetime import date

# define first class
class Library_Item:
    def __init__(self, title, status, condition, due_date):
        self.title = title
        self.status = status
        self.condition = condition
        self.due_date = due_date

# first subclass
class Movies(Library_Item):
    def __init__(self, title, status, condition, due_date, director, run_time):
        super().__init__(title, status, condition, due_date)
        self.director = director
        self.run_time = run_time

# second subclass
class Books(Library_Item):
    def __init__(self, title, status, condition, due_date):
        super().__init__(title, status, condition, due_date)


# third subclass
class Media(Library_Item):
    def __init__(self, title, status, condition, due_date, artist):
        super().__init__(title=title, status=status, condition=condition, due_date=due_date)
        self.artist = artist

# creating list of all item titles
books_catalog = [Books(title ='Wool', status='on shelf', condition='good', due_date='Oct 16 23'),
                 Books(title ='Wicked', status='on shelf', condition='good', due_date='Oct 16 23'),
                 Books(title = 'Moon_Palace', status='on shelf', condition='good', due_date='Oct 16 23'),
                 Books(title ='Cats', status='on shelf', condition='good', due_date='Oct 16 23')]

# Finish adding items to movies list
movies_catalog = [Media(title='Footloose' status = 'checked_out'), Media('Braveheart'), Media('Starman')]

# finish adding items to media list
media_catalog = [Media(title ='Load'),
           Media(title ='Aqualung'), Media(title='Cocky'), Media(title='Dark_Side_of_the_Moon'), Media(title= 'Thriller'),]