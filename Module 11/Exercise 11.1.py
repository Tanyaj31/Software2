class Publication:                      #base class Publication
    def __init__(self, name):           #initializing the base class with a name
        self.name = name

    def print_information(self):        #method to print data about the base class
        print(f"Publication Name: {self.name}")


class Book(Publication):                 #Book subclass inherits from Publication class
    def __init__(self, name, author, page_count):
        super().__init__(name)           #to call Publication class's data members
        self.author = author
        self.page_count = page_count

    def print_information(self):         #method to print data about the Book class
        super().print_information()       #to call Publication class's method
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count} pages")


class Magazine(Publication):              #Magazine subclass inherits data from Publication class
    def __init__(self, name, chief_editor):
        super().__init__(name)           #to call Publication class's data members
        self.chief_editor = chief_editor

    def print_information(self):             #method to print data about the Book class
        super().print_information()          #to call Publication class's method
        print(f"Chief Editor: {self.chief_editor}")


#main program
#object of Magazine class for Donald Duck
donald_duck = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")

#object of Book class for Compartment No. 6
compartment_no_6 = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)

#print info for Donald Duck
donald_duck.print_information()
print("\n------\n")                           #adding extra line space to avoid confusion
compartment_no_6.print_information()              #print info for Compartment No. 6
