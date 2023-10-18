from datetime import date, timedelta

import Library_Item

# creating list of all book information
books_catalog = [Library_Item.Books('Wool', 'on shelf', 1, 'null', 'Hugh Howey'),
                 Library_Item.Books('Wicked', 'on shelf', 10, 'null', 'Gregory Maguire'),
                 Library_Item.Books('Moon Palace', 'on shelf', 3, 'null', 'Paul Auster'),
                 Library_Item.Books('Cats', 'on shelf', 10, 'null', 'Lisa Covey')]

# creating list of all movie information
movies_catalog = [Library_Item.Movies('Footloose', 'on shelf', 10, 'null', 'Herbert Ross', '90min'),
                  Library_Item.Movies('Braveheart', 'on shelf', 10, 'null', 'Mel Gibson', '178min'),
                  Library_Item.Movies('Starman', 'on shelf', 7, 'null', 'John Carpenter', '135min'),
                  Library_Item.Movies('Suicide Squad', 'on shelf', 4, 'null', 'David Ayer', '120min')]

# creating list of all media information
media_catalog = [Library_Item.Media('Load', 'on shelf', 10, 'null', 'Metallica'),
                 Library_Item.Media('Aqualung', 'on shelf', 8, 'null', 'Jethro Tull'),
                 Library_Item.Media('Cocky', 'on shelf', 2, 'null', 'Kid Rock'),
                 Library_Item.Media('Dark Side of the Moon', 'on shelf', 6, 'null', 'Pink Floyd')]

inventory = [books_catalog, movies_catalog, media_catalog]


# viewing inventory function

def view_inventory(prompt):
    if prompt not in (1, 2, 3, 4):
        print("Please enter a valid number (1-4)")
    elif prompt == 1:
        for book in books_catalog:
            print(str(book))
    elif prompt == 2:
        for movie in movies_catalog:
            print(str(movie))
    elif prompt == 3:
        for media in media_catalog:
            print(str(media))
    elif prompt == 4:
        for item in inventory:
            for i in item:
                print(str(i))


# searching author funct
def search_author():
    author = input("Enter the name of the author: ")
    books_by_author = []
    for book in books_catalog:
        if book.author.lower() == author.lower():
            books_by_author.append(book)
    for book in books_by_author:
        print()
        print(str(book))
    if len(books_by_author) < 1:
        print("No books by that author were found.")


# searching title function ## currently printing string instead of f string
def search_title():
    search_key = input("Enter keyword: ")
    works_by_keyword = []

    for item in inventory:
        for i in item:
            if search_key.lower() in i.title.lower():
                works_by_keyword.append(str(i))
    print(str(works_by_keyword))
    return works_by_keyword


# check status function
def check_status(item):
    return item.status


# adding new inventory function
def add_inventory():
    """Will prompt the user for the title and creator for a new item, then create that item
     with default status of 'on shelf' and condition of 10"""
    while True:
        add_item = int(input("1. Book, 2. Movie, or 3. Media\n>>>"))
        if add_item == 1:
            new_title = input("Enter the title of the book: ")
            new_author = input("Enter the Author of the book: ")
            books_catalog.append(Library_Item.Books(new_title, "on shelf", 10, "null", new_author))
            break
        elif add_item == 2:
            new_title = input("Enter the title of the movie: ")
            new_director = input("Enter the director of the movie: ")
            new_runtime = int(input("Enter the runtime of the movie: "))
            movies_catalog.append(Library_Item.Movies(new_title, "on shelf", 10, "null", new_director, new_runtime))
            break
        elif add_item == 3:
            new_title = input("Enter the title of the media: ")
            new_artist = input("Enter the artist's name: ")
            media_catalog.append(Library_Item.Media(new_title, "on shelf", 10, "null", new_artist))
            break
        else:
            print("Enter a valid number 1, 2, or 3: ")


# search director function (add into search author)
def search_director():
    director = input("Enter the name of the director: ")
    movies_by_director = []
    for movie in movies_catalog:
        if movie.director.lower() == director.lower():
            movies_by_director.append(movie)
    for movie in movies_by_director:
        print()
        print(str(movie))
    if len(movies_by_director) < 1:
        print("No movies by that director were found.")


# search artist function (add into search author)
def search_artist():
    artist = input("Enter the name of the artist: ")
    media_by_artist = []
    for media in media_catalog:
        if media.artist.lower() == artist.lower():
            media_by_artist.append(media)
    for media in media_by_artist:
        print()
        print(str(media))
    if len(media_by_artist) < 1:
        print("No media by that artist was found.")


# check condition of items in catalog/recycle and replace if condition is poor
def check_condition(returned_item):
    if returned_item.condition <= 1:
        print(f"{returned_item.title} was recycled due to poor condition. Consider replacing.\n")
        for item in inventory:
            for i in item:
                if i.title == returned_item.title:
                    item.remove(returned_item)
    else:
        returned_item.status = "on shelf"
        returned_item.due_date = "null"
        print(f"{returned_item.title} returned successfully.\n")


# return item to inventory
def return_item(item):
    if item.status.lower() == "out":
        check_condition(item)
    else:
        print("\nItem is already returned to library.\n")


# final checkout set return date/loop to ask if more than 1 item
def checkout(item):
    if item.status.lower() == "on shelf":
        item.due_date = date.today() + timedelta(days=14)
        item.status = "out"
        item.condition -= 1
        print("\nYour item was checked out.")
        print(str(item))

    else:
        print("This item is already checked out.")


# silly shush function
def quiet_down():
    print("\nBryce says: Quiet down!\n")


# printing menu options
def main():
    while True:
        prompt = int(input("Welcome to The Final Four Library! What would you like to do? \n1. View Books \n2. View "
                           "Movies \n3. View Media \n4. View All \n5. Search by Keyword \n6. Search by "
                           "Author/Director/Artist\n7. Checkout Item \n8. Return Item \n9. "
                           "Quit \n10.Add Inventory(Employees Only!)\n>>> "))
        # view books
        if prompt == 1:
            view_inventory(1)
        # view movies
        elif prompt == 2:
            view_inventory(2)
        # view media
        elif prompt == 3:
            view_inventory(3)
        # view all items
        elif prompt == 4:
            view_inventory(4)
        # search by keyword
        elif prompt == 5:
            search_title()
        # secret hidden function
        elif prompt == 0:
            quiet_down()
        # search by author/director/artist functions
        elif prompt == 6:
            while True:
                user_ask = input("Are you looking for an Author, Director, or Artist? ")
                if user_ask.lower() == "artist":
                    search_artist()
                    break
                elif user_ask.lower() == "director":
                    search_director()
                    break
                elif user_ask.lower() == "author":
                    search_author()
                    break
                else:
                    print("Improper input. Please choose between: Artist, Director, or Author")
        # checkout item function - lower condition
        elif prompt == 7:
            while True:
                checkout_title = input('Enter the title of the item you would like to check out: ')
                checkout_item = None
                for item in inventory:
                    for i in item:
                        if i.title.lower() == checkout_title.lower():
                            checkout_item = i

                if checkout_item != None:
                    checkout(checkout_item)
                    break
                else:
                    print("Please make sure you entered a valid title")
        # return item function
        elif prompt == 8:
            while True:
                return_title = input('Enter the title of the item you are returning: ')
                item_to_return = ""
                for item in inventory:
                    for i in item:
                        if i.title.lower() == return_title.lower():
                            item_to_return = i

                if item_to_return != "":
                    return_item(item_to_return)
                    break
                else:
                    print("Please make sure you entered a valid title \n")
        elif prompt == 10:
            add_inventory()
        # quit
        elif prompt == 9:
            print("Goodbye!")
            break
        else:
            print("Improper input. Please choose from the list (1,2,3,4,5,6,7,8,9)")


if __name__ == "__main__":
    main()
