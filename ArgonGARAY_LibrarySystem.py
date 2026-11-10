
# Parent Class
class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


# Child Class: Book
class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        if isinstance(number_pages, int) and not isinstance(number_pages, bool) and number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_of_pages)


# Child Class: Magazine
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and not isinstance(issue_number, bool) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue_number)


# Creating two objects of each class
pub1 = Publication("Journal of Experimental Psychology",
                   "Ratcliff, R. & Van Dongen, H.")
pub2 = Publication("Philippine Journal of Science",
                   "DOST")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 350)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("TIME Magazine", "Various Authors", 150)


# Displaying Publication Information
print("Publication Information:")
pub1.display_info()

print("\nSecond Publication:")
pub2.display_info()


# Displaying Book Information
print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print("Number of Pages:", book1.get_number_of_pages())

print("\nSecond Book:")
book2.display_info()


# Displaying Magazine Information
print("\nMagazine Information:")
mag1.set_issue_number(0)
mag1.display_info()
print("Issue Number:", mag1.get_issue_number())

print("\nSecond Magazine:")
mag2.display_info()
