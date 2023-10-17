# define first class
class Library_Item:
    def __init__(self, title, status, condition, due_date):
        self.title = title
        self.status = status
        self.condition = condition
        self.due_date = due_date
    def __str__(self):
        return f"Title: {self.title} \n Status: {self.status} \n Condition: {self.condition} \n Due Date: {self.due_date} \n"


# define first class

# first subclass
class Movies(Library_Item):
    def __init__(self, title, status, condition, due_date, director, run_time):
        super().__init__(title=title, status=status, condition=condition, due_date=due_date)
        self.director = director
        self.run_time = run_time

    def __str__(self):
        return f"Title: {self.title}\n Director: {self.director}\n Runtime: {self.run_time}\n Status: {self.status}\n Condition: {self.condition}\n Due Date: {self.due_date}\n"

# second subclass
class Books(Library_Item):
    def __init__(self, title, status, condition, due_date, author):
        super().__init__(title=title, status=status, condition=condition, due_date=due_date)
        self.author = author
    def __str__(self):
        return f"Title: {self.title}\n Author: {self.author}\n Status: {self.status}\n Condition: {self.condition}\n Due Date: {self.due_date}\n"


# third subclass
class Media(Library_Item):
    def __init__(self, title, status, condition, due_date, artist):
        super().__init__(title=title, status=status, condition=condition, due_date=due_date)
        self.artist = artist
    def __str__(self):
        return f"Title: {self.title}\n Artist: {self.artist}\n Status: {self.status}\n Condition: {self.condition}\n Due Date: {self.due_date}\n"