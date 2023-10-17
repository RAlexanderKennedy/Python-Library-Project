from datetime import date, timedelta

import Library_Item

# creating list of all item titles
books_catalog = [Library_Item.Books('Wool', 'on shelf', 1, 'null', 'Hugh Howey'),
                 Library_Item.Books('Wicked', 'on shelf', 10, 'null', 'Gregory Maguire'),
                 Library_Item.Books('Moon Palace', 'on shelf', 3, 'null', 'Paul Auster'),
                 Library_Item.Books('Cats', 'on shelf', 10, 'null', 'Lisa Covey')]

# Finish adding items to movies list
movies_catalog = [Library_Item.Movies('Footloose', 'on shelf', 10, 'null', 'Herbert Ross', '90min'),
                  Library_Item.Movies('Braveheart', 'on shelf', 10, 'null', 'Mel Gibson', '178min'),
                  Library_Item.Movies('Starman', 'on shelf', 7, 'null', 'John Carpenter', '135min'),
                  Library_Item.Movies('Suicide Squad', 'on shelf', 4, 'null', 'David Ayer', '120min')]

# finish adding items to media list
media_catalog = [Library_Item.Media('Load', 'on shelf', 10, 'null', 'Metallica'),
                 Library_Item.Media('Aqualung', 'on shelf', 8, 'null', 'Jethro Tull'),
                 Library_Item.Media('Cocky', 'on shelf', 2, 'null', 'Kid Rock'),
                 Library_Item.Media('Dark_Side_of_the_Moon', 'on shelf', 6, 'null', 'Pink Floyd')]

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
        # for book in books_catalog:
        #     print(str(book))
        # for movie in movies_catalog:
        #     print(str(movie))
        # for media in media_catalog:
        #     print(str(media))


# searching author funct
def search_author():
    author = input("Enter the name of the author: ")
    books_by_author = []
    for book in books_catalog:
        if book.author.lower() == author.lower():
            books_by_author.append(book)
    for book in books_by_author:
        print(str(book))
    if len(books_by_author) < 1:
        print("No books by that author were found.")


# searching title function
def search_title():
    search_key = input("Enter keyword: ")
    works_by_keyword = []

    # for book in books_catalog:
    #     if search_key.lower() in (book.title.lower()):
    #         works_by_keyword.append(book)
    # for movie in movies_catalog:
    #     if search_key.lower() in (movie.title.lower()):
    #         works_by_keyword.append(movie)
    # for media in media_catalog:
    #     if search_key.lower() in (media.title.lower()):
    #         works_by_keyword.append(media)
    # for work in works_by_keyword:
    #     print(str(work))
    # if len(works_by_keyword) < 1:
    #     print("No books by that author were found.")
    for item in inventory:
        for i in item:
            if search_key.lower() in i.title.lower():
                works_by_keyword.append(str(i))
    print(works_by_keyword)
    return works_by_keyword


# check status function
def check_status(item):
    return item.status


# adding new inventory function
def add_inventory():
    while True:
        add_item = int(input("1. Book, 2. Movie, or 3. Media"))
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
        print(f"{returned_item.title} returned successfully.")


# return item to inventory
def return_item(item):
    if item.status.lower() == "out":
        check_condition(item)
    else:
        print("Item is already returned to library.")


# final checkout set return date/loop to ask if more than 1 item
def checkout(item):
    if item.status.lower() == "on shelf":
        item.due_date = date.today() + timedelta(days=14)
        item.status = "out"
        item.condition -= 1
        print("Your item was checked out.")
        print(str(item))

    else:
        print("This item is already checked out.")


# silly shush function
def quiet_down():
    print("Bryce says: Quiet down!")


# search_title()
# view_inventory(prompt)
# search_author()
# print(check_status(inventory[1][1]))

def main():
    while True:
        prompt = int(input("Welcome to The Final Four library! What would you like to do? (\n1. View Books \n2. View "
                           "Movies \n3. View Media \n4. View All \n5. Search by Keyword \n6. Search by "
                           "Author/Director/Artist\n"))
        if prompt == 1:
            view_inventory(1)

        elif prompt == 2:
            view_inventory(2)

        elif prompt == 3:
            view_inventory(3)

        elif prompt == 4:
            view_inventory(4)

        elif prompt == 5:
            search_title()

        elif prompt == 6:
            while True:
                user_ask = input("Are you looking for an Author, Director, or Artist? ")
                if user_ask.lower() == "artist":
                    search_artist()
                elif user_ask.lower() == "director":
                    search_director()
                elif user_ask.lower() == "author":
                    search_author()
                else:
                    print("Improper input. Please choose between: Artist, Director, or Author")
                    
        else:
            print("Improper input. Please choose from the list (1,2,3,4,5,6)")
        break


if __name__ == "__main__":
    main()
