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
        super().__init__(title=title, status=status, condition=condition, due_date=due_date)
        self.director = director
        self.run_time = run_time


# second subclass
class Books(Library_Item):
    def __init__(self, title, status, condition, due_date):
        super().__init__(title=title, status=status, condition=condition, due_date=due_date)


# third subclass
class Media(Library_Item):
    def __init__(self, title, status, condition, due_date, artist):
        super().__init__(title=title, status=status, condition=condition, due_date=due_date)
        self.artist = artist


# creating list of all item titles
books_catalog = [Books('Wool', 'on shelf', 'good', 'null'),
                 Books('Wicked', 'on shelf', 'good', 'null'),
                 Books('Moon_Palace', 'on shelf', 'good', 'null'),
                 Books('Cats', 'on shelf', 'good', 'null')]

# Finish adding items to movies list
movies_catalog = [Movies('Footloose', 'on shelf', 'good', 'null', 'Herbert Ross', '90min'),
                  Movies('Braveheart', 'on shelf', 'good', 'null', 'Mel Gibson', '178min'),
                  Movies('Starman', 'on shelf', 'good', 'null', 'John Carpenter', '135min'),
                  Movies('Suicide Squad', 'on shelf', 'good', 'null', 'David Ayer', '120min')]

# finish adding items to media list
media_catalog = [Media('Load', 'on shelf', 'good', 'null', 'Metallica'),
                 Media('Aqualung', 'on shelf', 'good', 'null', 'Jethro Tull'),
                 Media('Cocky', 'on shelf', 'good', 'null', 'Kid Rock'),
                 Media('Dark_Side_of_the_Moon', 'on shelf', 'good', 'null', 'Pink Floyd')]

inventory = [books_catalog, movies_catalog, media_catalog]
# viewing inventory function
def view_inventory():
# searching author function
def search_author():
# searching title function
def search_title():
# check status function
def check_status():
# adding new inventory function
def add_inventory():
# search director function (add into search author)
def search_director():
# check condition of items in catalog/recycle and replace if condition is poor
def check_condition():
# return item to inventory
def return_item():
# final checkout set return date/loop to ask if more than 1 item
def checkout():
# silly shush function
def quiet_down():
