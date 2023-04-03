# -------------------------------------------------
# Function of the Main Menu File in this Programme.
# -------------------------------------------------

class MainMenu:
    @staticmethod
    def input1():
        print("=========================================")
        print("Welcome to OUSL Library System!")
        print("OUSL පුස්තකාල පද්ධතියට සාදරයෙන් පිළිගනිමු!")
        print("OUSL நூலக அமைப்புக்கு வரவேற்கிறோம்!")
        print("=========================================")
        print("""Main Menu | ප්‍රධාන මෙනුව | முதன்மை பட்டியல்
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Books| පොත් | புத்தகங்கள்.
2. Magazines | සඟරා |  இதழ்கள்.
3. Educational DVDs | අධ්‍යාපනික DVD තැටි | கல்வி டிவிடிகள்.
4. Lecture CDs | දේශන CD තැටි | விரிவுரை குறுந்தகடுகள்.
5. View all resources (any type) filtered by subject | විෂය අනුව පෙරන ලද සියලුම සම්පත් (ඕනෑම වර්ගයක්) බලන්න. | பொருள் மூலம் வடிகட்டப்பட்ட அனைத்து ஆதாரங்களையும் (எந்த வகையையும்) காண்க.
6. Exit | පිටවීම |  வெளியேறு.
    """)

    @staticmethod
    def menue():
        MainMenu.input1()
        select = 0  # Initialize the variable with a default value
        while select < 1 or select > 7:
            try:
                select = int(input("• Select what you want to do? "))
# Books selection
                if select == 1:
                    Books.intro()
                    menu1()
# Magazines selection
                elif select == 2:
                    Magazines.intro1()
                    menu2()
# DVD selection
                elif select == 3:
                    educational_DVD1.intro2()
                    menu3()
# CD selection
                elif select == 4:
                    lecture_CDs1.intro3()
                    menu4()
# View all resources (any type) filtered by subject
                elif select == 5:
                    print("Sorry Currently this function is not available.Sorry for the inconvenience.")
                    print("*****************************************")
                    choice = input("-> Do yo Need to Continue (Y/N)").upper()
                    if choice == "Y":
                        MainMenu.menue()
                    else:
                        print("\n | Thank You! 🙏 |")
# Exit Programme
                elif select == 6:
                    print("\n | Thank You! 🙏 |")
                else:
                    print("Please enter a valid option...")
            except ValueError:
                print("Please enter a valid option...")


# --------------------------
# This is the Class function.
# --------------------------

class Books:
    def __init__(self, isbn_number, title, format, subject, rental_price_per_day, number_of_copies):
        self.isbn_number = isbn_number
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.number_of_copies = number_of_copies

    @staticmethod
    def intro():
        print("********************************")
        print("""• 1. View all the books
• 2. Add a new resource to the system.
• 3. Remove a resource from the system.
• 4. View currently available resources.
• 5. View currently unavailable resources.
• 6. Lend a resource.
• 7. Update resource.
• 8. Go to menu
• 9. Exit""")
        print("********************************")


class book_list1(Books):
    def __init__(self):
        self.book_L = []
        self.append1()

# Add the books early
    def append1(self):

        book_1 = Books(isbn_number='ISBN1234', title='The Solar System', format='Hardcover', subject='Science',
                       rental_price_per_day=15.00, number_of_copies=5)
        self.book_L.append(book_1)
        book_2 = Books(isbn_number='ISBN9876', title='Types of Animal Species', format='Paperback', subject='Science',
                       rental_price_per_day=10.00, number_of_copies=8)
        self.book_L.append(book_2)
        book_3 = Books(isbn_number='ISBN1290', title='Second World War', format='Hardcover', subject='History',
                       rental_price_per_day=12.50, number_of_copies=0)
        self.book_L.append(book_3)

# Display all list function
    def all_list(self):
        for l in self.book_L:
            print(
                f"ISBN Number:{l.isbn_number}, Title:{l.title}, Format:{l.format}, Subject:{l.subject}, Rental price per day:{l.rental_price_per_day}, Number of copies:{l.number_of_copies} ")

# Adding books function
    def add(self):
        isbn_number1 = input("• ISBN Number: ").strip().upper()
        title1 = input("• Title of the book: ").strip().capitalize()
        format1 = input("• Format of the book: ").strip().capitalize()
        subject1 = input("• Subject Name: ").strip().capitalize()
        rental_price_per_day1 = float(input("• Rental price per day: "))
        number_of_copies1 = int(input("• Number of Copies: "))
        
# create an instance of the Books class with the user inputs
        books1 = Books(isbn_number=isbn_number1, title=title1, format=format1, subject=subject1,
                       rental_price_per_day=rental_price_per_day1, number_of_copies=number_of_copies1)

# append the Books instance to the book_L list
        self.book_L.append(books1)

# Remove books function
    def remove(self):
        delete = input("Enter the ISBN number: ").upper()
        y = [l for l in self.book_L if l.isbn_number == delete]
        for l in y:
            self.book_L.remove(l)
        self.all_list()

# Lending books function
    def lend(self):
        isbmn1 = input("• Enter the ISBN number: ").upper()
        copy = int(input("• Enter number of copies need to lend: "))
        y = list(l for l in self.book_L if l.isbn_number == isbmn1)
        for l in y:
            l.number_of_copies -= copy
        self.all_list()

# Getting books function
    def give(self):
        isbmn2 = input("• Enter the ISBN number: ").upper()
        copy = int(input("• Enter number of copies need to Update: "))
        y = list(l for l in self.book_L if l.isbn_number == isbmn2)
        for z in y:
            z.number_of_copies += copy
        self.all_list()

# Display not available books
    def zero(self):
        y = [l for l in self.book_L if l.number_of_copies == 0]
        for z in y:
            print(
                f"ISBN Number:{z.isbn_number}, Title:{z.title}, Format:{z.format}, Subject:{z.subject}, Rental price per day:{z.rental_price_per_day}, Number of copies:{z.number_of_copies} ")

# Display available books
    def available(self):
        y = [l for l in self.book_L if l.number_of_copies > 0]
        for z in y:
            print(
                f"ISBN Number:{z.isbn_number}, Title:{z.title}, Format:{z.format}, Subject:{z.subject}, Rental price per day:{z.rental_price_per_day}, Number of copies:{z.number_of_copies} ")

# Continue function
    def continue_p(self):
        print("*****************************************")
        choice = input("-> Do yo Need to Continue (Y/N)").upper()
        if choice == "Y":
            Books.intro()
            menu1()
        else:
            quit()

# Books main menu function
def menu1():
    select2 = 0  # Initialize the variable with a default value
    while select2 < 1 or select2 > 10:
        try:
            select2 = int(input("• Select what you want to do? "))
            if select2 == 1:
                print("*****************************************")
                book_list1().all_list()
                book_list1().continue_p()

            elif select2 == 2:
                book_list = book_list1()
                book_list.add()
                print("*****************************************")
                choice1 = input("Do you need to view the all details (y/n)").upper()
                if choice1 == "Y":
                    book_list.all_list()
                    book_list1().continue_p()
                else:
                    book_list1().continue_p()

            elif select2 == 3:
                book_list1().remove()
                book_list1().continue_p()

            elif select2 == 4:
                book_list1().available()
                book_list1().continue_p()

            elif select2 == 5:
                book_list1().zero()
                book_list1().continue_p()

            elif select2 == 6:
                book_list1().lend()
                book_list1().continue_p()

            elif select2 == 7:
                book_list1().give()
                book_list1().continue_p()

            elif select2 == 8:
                MainMenu.menue()

            elif select2 == 9:
                print("\n | Thank You! 🙏 |")
            else:
                print("Please enter a valid option...")
        except ValueError:
            print("Please enter a valid option...")


# -------------------------------
# This is the Magazines Function.
# -------------------------------

class Magazines:
    def __init__(self, magazine_number, title, color_or_black_and_white_print, subject, rental_price, number_of_copies):
        self.magazine_number = magazine_number
        self.title = title
        self.color_or_black_and_white_print = color_or_black_and_white_print
        self.subject = subject
        self.rental_price = rental_price
        self.number_of_copies = number_of_copies

# Displaying the menu
    @staticmethod
    def intro1():
        print("********************************")
        print("""• 1. View all the Magazines
• 2. Add a new resource to the system.
• 3. Remove a resource from the system.
• 4. View currently available resources.
• 5. View currently unavailable resources.
• 6. Lend a resource.
• 7. Update resource.
• 8. Go to menu
• 9. Exit""")
        print("********************************")


class magazine_list1:
    def __init__(self):
        self.magazine_L = []
        self.append2()

# Add the magazine early
    def append2(self):
        magazine_1 = Magazines(magazine_number="01", title='History of Cricket', color_or_black_and_white_print='color',
                               subject='Sports',
                               rental_price=5.00, number_of_copies=0)
        self.magazine_L.append(magazine_1)
        magazine_2 = Magazines(magazine_number="02", title='Evolution of the Computer',
                               color_or_black_and_white_print='black&white', subject='Technology',
                               rental_price=3.00, number_of_copies=21)
        self.magazine_L.append(magazine_2)

# Display all list function
    def all_list1(self):
        for lm in self.magazine_L:
            print(
                f"Magazine Number:{lm.magazine_number}, Title:{lm.title}, Print:{lm.color_or_black_and_white_print}, Subject:{lm.subject}, Rental price per day:{lm.rental_price}, Number of copies:{lm.number_of_copies} ")

# Adding magazine function
    def add1(self):
        magazine_number = input("• Magazine Number: ").strip().upper()
        title = input("• Title of the Magazine: ").strip().capitalize()
        color_or_black_and_white_print = input(
            "• Print of the Magazine (Color or Black & White): ").strip().capitalize()
        subject = input("• Subject Name: ").strip().capitalize()
        rental_price = float(input("• Rental price per day: "))
        number_of_copies = int(input("• Number of Copies: "))

# create an instance of the Magazines class with the user inputs
        magazine = Magazines(magazine_number=magazine_number, title=title,
                             color_or_black_and_white_print=color_or_black_and_white_print,
                             subject=subject, rental_price=rental_price, number_of_copies=number_of_copies)

# append the magazine instance to the magazine_L list
        self.magazine_L.append(magazine)

# Remove magazine function
    def remove1(self):
        delete1 = input("• Enter the Magazine number: ").upper()
        y1 = [lm for lm in self.magazine_L if lm.magazine_number == delete1]
        for lm in y1:
            self.magazine_L.remove(lm)
        self.all_list1()

# Lending magazine function
    def lend1(self):
        Maga1 = input("• Enter the Magazine number: ").upper()
        copy1 = int(input("• Enter number of copies need to lend: "))
        y1 = list(lm for lm in self.magazine_L if lm.magazine_number == Maga1)
        for lm in y1:
            lm.number_of_copies -= copy1
        self.all_list1()

# Getting magazine function
    def give1(self):
        Maga = input("• Enter the Magazine number: ").upper()
        copy1 = int(input("• Enter number of copies need to Update: "))
        y1 = list(lm for lm in self.magazine_L if lm.magazine_number == Maga)
        for lm in y1:
            lm.number_of_copies += copy1
        self.all_list1()

# Display not available magazine
    def zero1(self):
        y1 = [lm for lm in self.magazine_L if lm.number_of_copies == 0]
        for lm in y1:
            print(
                f"Magazine Number:{lm.magazine_number}, Title:{lm.title}, Print:{lm.color_or_black_and_white_print}, Subject:{lm.subject}, Rental price per day:{lm.rental_price}, Number of copies:{lm.number_of_copies} ")

# Display available magazine
    def available1(self):
        y1 = [lm for lm in self.magazine_L if lm.number_of_copies > 0]
        for lm in y1:
            print(
                f"Magazine Number:{lm.magazine_number}, Title:{lm.title}, Print:{lm.color_or_black_and_white_print}, Subject:{lm.subject}, Rental price per day:{lm.rental_price}, Number of copies:{lm.number_of_copies} ")

# Continue function
    def continue_p1(self):
        print("*****************************************")
        choicem = input("-> Do yo Need to Continue (Y/N)").upper()
        if choicem == "Y":
            Magazines.intro1()
            menu2()
        else:
            quit()

# Magazine main menu function
def menu2():
    select2 = 0  # Initialize the variable with a default value
    while select2 < 1 or select2 > 10:
        try:
            select2 = int(input("• Select what you want to do? "))
            if select2 == 1:
                print("*****************************************")
                magazine_list1().all_list1()
                magazine_list1().continue_p1()

            elif select2 == 2:
                magazine_list = magazine_list1()
                magazine_list.add1()
                print("*****************************************")
                choice1 = input("-> Do you need to view the all details (Y/N)").upper()
                if choice1 == "Y":
                    magazine_list.all_list1()
                    magazine_list1().continue_p1()
                else:
                    magazine_list1().continue_p1()

            elif select2 == 3:
                magazine_list1().remove1()
                magazine_list1().continue_p1()

            elif select2 == 4:
                magazine_list1().available1()
                magazine_list1().continue_p1()

            elif select2 == 5:
                magazine_list1().zero1()
                magazine_list1().continue_p1()

            elif select2 == 6:
                magazine_list1().lend1()
                magazine_list1().continue_p1()

            elif select2 == 7:
                magazine_list1().give1()
                magazine_list1().continue_p1()

            elif select2 == 8:
                MainMenu.menue()

            elif select2 == 9:
                print("\n | Thank You! 🙏 |")
            else:
                print("Please enter a valid option...")
        except ValueError:
            print("Please enter a valid option...")


# ------------------------
# This is the DVD Function
# ------------------------

class educational_DVD:

    def __init__(self, dvd_number, title, subject, rental_price_per_day, number_of_copies):
        self.dvd_number = dvd_number
        self.title = title
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.number_of_copies = number_of_copies

# Displaying the DVD
    @staticmethod
    def intro2():
        print("********************************")
        print("""• 1. View all the DVDs.
• 2. Add a new resource to the system.
• 3. Remove a resource from the system.
• 4. View currently available resources.
• 5. View currently unavailable resources.
• 6. Lend a resource.
• 7. Update resource.
• 8. Go to menu
• 9. Exit""")
        print("********************************")


class educational_DVD1(educational_DVD):
    def __init__(self):
        self.educational_DVD_L = []
        self.append2()

# Add the DVD early
    def append2(self):

        educational_1 = educational_DVD(dvd_number="10", title='Birth of the Solar System', subject='Astronomy',
                                        rental_price_per_day=2.50, number_of_copies=10)
        self.educational_DVD_L.append(educational_1)
        educational_2 = educational_DVD(dvd_number="11", title='Pythagoras Theorem', subject='Math',
                                        rental_price_per_day=1.00, number_of_copies=0)
        self.educational_DVD_L.append(educational_2)

# Display all list function
    def all_list2(self):
        for ld in self.educational_DVD_L:
            print(
                f"DVD Number:{ld.dvd_number}, Title:{ld.title}, Subject:{ld.subject}, Rental price per day:{ld.rental_price_per_day}, Number of copies:{ld.number_of_copies} ")

# Adding DVD function
    def add2(self):
        dvd_number1 = input("• DVD Number: ").strip().upper()
        title2 = input("• Title of the DVD: ").strip().capitalize()
        subject2 = input("• Subject Name: ").strip().capitalize()
        rental_price_per_day2 = float(input("• Rental price per day: "))
        number_of_copies2 = int(input("• Number of Copies: "))
# create an instance of the educational_DVD class with the user inputs
        educational_DVD1 = educational_DVD(dvd_number=dvd_number1, title=title2, subject=subject2,
                                           rental_price_per_day=rental_price_per_day2,
                                           number_of_copies=number_of_copies2)
# append the educational_DVD instance to the educational_DVD_L list
        self.educational_DVD_L.append(educational_DVD1)

# Remove DVD function
    def remove2(self):
        delete2 = input("• Enter the Magazine number: ").upper()
        y2 = [ld for ld in self.educational_DVD_L if ld.dvd_number == delete2]
        for ld in y2:
            self.educational_DVD_L.remove(ld)
        self.all_list2()

# Lending DVD function
    def lend2(self):
        Dvd1 = input("• Enter the DVD number: ").upper()
        copy2 = int(input("• Enter number of copies need to lend: "))
        y2 = list(ld for ld in self.educational_DVD_L if ld.dvd_number == Dvd1)
        for ld in y2:
            ld.number_of_copies -= copy2
        self.all_list2()

# Getting DVD function
    def give2(self):
        Dvd1 = input("• Enter the DVD number: ").upper()
        copy2 = int(input("• Enter number of copies need to Update: "))
        y2 = list(ld for ld in self.educational_DVD_L if ld.dvd_number == Dvd1)
        for ld in y2:
            ld.number_of_copies += copy2
        self.all_list2()

# Display not available DVD
    def zero2(self):
        y2 = [ld for ld in self.educational_DVD_L if ld.number_of_copies == 0]
        for ld in y2:
            print(
                f"DVD Number:{ld.dvd_number}, Title:{ld.title}, Subject:{ld.subject}, Rental price per day:{ld.rental_price_per_day}, Number of copies:{ld.number_of_copies} ")

# Display available DVD
    def available2(self):
        y2 = [ld for ld in self.educational_DVD_L if ld.number_of_copies > 0]
        for ld in y2:
            print(
                f"DVD Number:{ld.dvd_number}, Title:{ld.title}, Subject:{ld.subject}, Rental price per day:{ld.rental_price_per_day}, Number of copies:{ld.number_of_copies} ")

# Continue function
    def continue_p2(self):
        print("*****************************************")
        choicem = input("-> Do yo Need to Continue (Y/N)").upper()
        if choicem == "Y":
            educational_DVD.intro2()
            menu3()
        else:
            quit()

# DVD main menu function
def menu3():
    select2 = 0  # Initialize the variable with a default value
    while select2 < 1 or select2 > 10:
        try:
            select2 = int(input("• Select what you want to do? "))
            if select2 == 1:
                print("*****************************************")
                educational_DVD1().all_list2()
                educational_DVD1().continue_p2()

            elif select2 == 2:
                educataion_list = educational_DVD1()
                educataion_list.add2()

                print("*****************************************")
                choice1 = input("-> Do you need to view the all details (Y/N) ").upper()
                if choice1 == "Y":
                    educataion_list.all_list2()
                    educational_DVD1().continue_p2()
                else:
                    educational_DVD1().continue_p2()

            elif select2 == 3:
                educational_DVD1().remove2()
                educational_DVD1().continue_p2()

            elif select2 == 4:
                educational_DVD1().available2()
                educational_DVD1().continue_p2()

            elif select2 == 5:
                educational_DVD1().zero2()
                educational_DVD1().continue_p2()

            elif select2 == 6:
                educational_DVD1().lend2()
                educational_DVD1().continue_p2()

            elif select2 == 7:
                educational_DVD1().give2()
                educational_DVD1().continue_p2()

            elif select2 == 8:
                MainMenu.menue()

            elif select2 == 9:
                print("\n | Thank You! 🙏 |")
            else:
                print("Please enter a valid option...")
        except ValueError:
            print("Please enter a valid option...")


# -----------------------
# This is the CD Function
# -----------------------

class lecture_CDs:
    def __init__(self, cd_number, title, subject, rental_price, number_of_copies):
        self.cd_number = cd_number
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.number_of_copies = number_of_copies

# Displaying the CD
    @staticmethod
    def intro3():
        print("********************************")
        print("""• 1. View all the Lecture CDs.
• 2. Add a new resource to the system.
• 3. Remove a resource from the system.
• 4. View currently available resources.
• 5. View currently unavailable resources.
• 6. Lend a resource.
• 7. Update resource.
• 8. Go to menu
• 9. Exit""")
        print("********************************")


class lecture_CDs1(lecture_CDs):
    def __init__(self):
        self.lecture_CD_L = []
        self.append3()

# Add the CD early
    def append3(self):

        lecture_1 = lecture_CDs(cd_number="21", title='Basics of Western Music', subject='Music',
                                rental_price=1.50, number_of_copies=0)
        self.lecture_CD_L.append(lecture_1)
        lecture_2 = lecture_CDs(cd_number="22", title='Japanese Language', subject='Foreign Languages',
                                rental_price=2.00, number_of_copies=3)
        self.lecture_CD_L.append(lecture_2)

# Display all list function
    def all_list3(self):
        for lc in self.lecture_CD_L:
            print(
                f"Lecture CD Number:{lc.cd_number}, Title:{lc.title}, Subject:{lc.subject}, Rental price per day:{lc.rental_price}, Number of copies:{lc.number_of_copies} ")

# Adding CD function
    def add3(self):
        cd_number1 = input("• Lecture CD Number: ").strip().upper()
        title3 = input("• Title of the Lecture CD: ").strip().capitalize()
        subject3 = input("• Subject Name: ").strip().capitalize()
        rental_price_per_day3 = float(input("• Rental price per day: "))
        number_of_copies3 = int(input("• Number of Copies: "))
        
# create an instance of the lecture_CDs class with the user inputs
        lecture_CD1 = lecture_CDs(cd_number=cd_number1, title=title3, subject=subject3,
                                  rental_price=rental_price_per_day3, number_of_copies=number_of_copies3)

# append the lecture_CDs instance to the lecture_CD_L list
        self.lecture_CD_L.append(lecture_CD1)

# Remove CD function
    def remove3(self):
        delete3 = input("• Enter the Magazine number: ").upper()
        y3 = [lc for lc in self.lecture_CD_L if lc.cd_number == delete3]
        for lc in y3:
            self.lecture_CD_L.remove(lc)
        self.all_list3()

# Lending CD function
    def lend3(self):
        Cd1 = input("• Enter the Lecture CD number: ").upper()
        copy3 = int(input("• Enter number of copies need to lend: "))
        y3 = list(lc for lc in self.lecture_CD_L if lc.cd_number == Cd1)
        for lc in y3:
            lc.number_of_copies -= copy3
        self.all_list3()

# Getting CD function
    def give3(self):
        Cd1 = input("• Enter the DVD number: ").upper()
        copy3 = int(input("• Enter number of copies need to Update: "))
        y3 = list(lc for lc in self.lecture_CD_L if lc.cd_number == Cd1)
        for lc in y3:
            lc.number_of_copies += copy3
        self.all_list3()

# Display not available CD
    def zero3(self):
        y3 = [lc for lc in self.lecture_CD_L if lc.number_of_copies == 0]
        for lc in y3:
            print(
                f"Lecture CD Number:{lc.cd_number}, Title:{lc.title}, Subject:{lc.subject}, Rental price per day:{lc.rental_price}, Number of copies:{lc.number_of_copies} ")

# Display available CD
    def available3(self):
        y2 = [lc for lc in self.lecture_CD_L if lc.number_of_copies > 0]
        for lc in y2:
            print(
                f"Lecture CD Number:{lc.cd_number}, Title:{lc.title}, Subject:{lc.subject}, Rental price per day:{lc.rental_price}, Number of copies:{lc.number_of_copies}")

# Continue function
    def continue_p3(self):
        print("*****************************************")
        choicem = input("-> Do yo Need to Continue (Y/N)").upper()
        if choicem == "Y":
            educational_DVD.intro2()
            menu4()
        else:
            print("\n | Thank You! 🙏 |")

# CD main menu function
def menu4():
    select2 = 0  # Initialize the variable with a default value
    while select2 < 1 or select2 > 10:
        try:
            select2 = int(input("• Select what you want to do? "))
            if select2 == 1:
                print("*****************************************")
                lecture_CDs1().all_list3()
                lecture_CDs1().continue_p3()

            elif select2 == 2:
                CD_list = lecture_CDs1()
                CD_list.add3()

                print("*****************************************")
                choice1 = input("-> Do you need to view the all details (Y/N)").upper()
                if choice1 == "Y":
                    CD_list.all_list3()
                    lecture_CDs1().continue_p3()
                else:
                    lecture_CDs1().continue_p3()

            elif select2 == 3:
                lecture_CDs1().remove3()
                lecture_CDs1().continue_p3()

            elif select2 == 4:
                lecture_CDs1().available3()
                lecture_CDs1().continue_p3()

            elif select2 == 5:
                lecture_CDs1().zero3()
                lecture_CDs1().continue_p3()

            elif select2 == 6:
                lecture_CDs1().lend3()
                lecture_CDs1().continue_p3()

            elif select2 == 7:
                lecture_CDs1().give3()
                lecture_CDs1().continue_p3()

            elif select2 == 8:
                MainMenu.menue()

            elif select2 == 9:
                print("\n | Thank You! 🙏 |")
            else:
                print("Please enter a valid option...")
        except ValueError:
            print("Please enter a valid option...")


# ---------------------------
# Initializing the programme.
# ---------------------------
MainMenu.menue()
