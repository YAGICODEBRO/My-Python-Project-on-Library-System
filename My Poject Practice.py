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
5. Exit | පිටවීම |  வெளியேறு.
    """)

    @staticmethod
    def menue():
        MainMenu.input1()
        try:
            select = int(input("Which resource details you want to find?"))
        except ValueError:
            print("An exception occurred")
        while select < 0 or select > 5:
            MainMenu.input1()
            try:
                select = int(input("Which resource details you want to find?"))
            except ValueError:
                print("An exception occurred")
        if select == 5:
            print("\n | Thank You! 🙏 |")
        elif select == 1:
            Books.intro()
            menu1()
        elif select == 2:
            Magazines.intro1()
            menu2()
        elif select == 3:
            educational_DVD1.intro2()
            menu3()
        elif select == 4:
            lecture_CDs1.intro3()
            menu4()


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

    def all_list(self):
        for l in self.book_L:
            print(
                f"ISBN Number:{l.isbn_number}, Title:{l.title}, Format:{l.format}, Subject:{l.subject}, Rental price per day:{l.rental_price_per_day}, Number of copies:{l.number_of_copies} ")

    def add(self):
        isbn_number1 = input("• ISBN Number: ").strip().upper()
        title1 = input("• Title of the book: ").strip().capitalize()
        format1 = input("• Format of the book: ").strip().capitalize()
        subject1 = input("• Subject Name: ").strip().capitalize()
        rental_price_per_day1 = float(input("• Rental price per day: "))
        number_of_copies1 = int(input("• Number of Copies: "))
        books1 = Books(isbn_number=isbn_number1, title=title1, format=format1, subject=subject1,
                       rental_price_per_day=rental_price_per_day1, number_of_copies=number_of_copies1)
        self.book_L.append(books1)

    def remove(self):
        delete = input("Enter the ISBN number: ").upper()
        y = [l for l in self.book_L if l.isbn_number == delete]
        for l in y:
            self.book_L.remove(l)
        self.all_list()

    def lend(self):
        isbmn1 = input("• Enter the ISBN number: ").upper()
        copy = int(input("• Enter number of copies need to lend: "))
        y = list(l for l in self.book_L if l.isbn_number == isbmn1)
        for l in y:
            l.number_of_copies -= copy
        self.all_list()

    def give(self):
        isbmn2 = input("• Enter the ISBN number: ").upper()
        copy = int(input("• Enter number of copies need to Update: "))
        y = list(l for l in self.book_L if l.isbn_number == isbmn2)
        for z in y:
            z.number_of_copies += copy
        self.all_list()

    def zero(self):
        y = [l for l in self.book_L if l.number_of_copies == 0]
        for z in y:
            print(
                f"ISBN Number:{z.isbn_number}, Title:{z.title}, Format:{z.format}, Subject:{z.subject}, Rental price per day:{z.rental_price_per_day}, Number of copies:{z.number_of_copies} ")

    def available(self):
        y = [l for l in self.book_L if l.number_of_copies > 0]
        for z in y:
            print(
                f"ISBN Number:{z.isbn_number}, Title:{z.title}, Format:{z.format}, Subject:{z.subject}, Rental price per day:{z.rental_price_per_day}, Number of copies:{z.number_of_copies} ")

    def continue_p(self):
        print("*****************************************")
        choice = input("-> Do yo Need to Continue (Y/N)").upper()
        if choice == "Y":
            Books.intro()
            menu1()
        else:
            quit()


def menu1():
    try:
        select2 = int(input("• Select what  you want to do?"))
    except ValueError:
        print("An exception occurred")
    while select2 < 0 or select2 > 9:
        MainMenu.input1()
        try:
            select2 = int(input("• Select what  you want to do?"))
        except ValueError:
            print("An exception occurred")

    if select2 == 1:
        book_list1().all_list()
        print("*****************************************")
        book_list1().continue_p()

    elif select2 == 2:
        book_list = book_list1()
        book_list.add()
        print("*****************************************")
        choice1 = input("-> Do you need to view the all details (Y/N)").upper()
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

    def append2(self):
        magazine_1 = Magazines(magazine_number="01", title='History of Cricket', color_or_black_and_white_print='color',
                               subject='Sports',
                               rental_price=5.00, number_of_copies=0)
        self.magazine_L.append(magazine_1)
        magazine_2 = Magazines(magazine_number="02", title='Evolution of the Computer',
                               color_or_black_and_white_print='black&white', subject='Technology',
                               rental_price=3.00, number_of_copies=21)
        self.magazine_L.append(magazine_2)

    def all_list1(self):
        for lm in self.magazine_L:
            print(
                f"Magazine Number:{lm.magazine_number}, Title:{lm.title}, Print:{lm.color_or_black_and_white_print}, Subject:{lm.subject}, Rental price per day:{lm.rental_price}, Number of copies:{lm.number_of_copies} ")

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

    # create an instance of the magazine_list1 class and call its methods

    def remove1(self):
        delete1 = input("• Enter the Magazine number: ").upper()
        y1 = [lm for lm in self.magazine_L if lm.magazine_number == delete1]
        for lm in y1:
            self.magazine_L.remove(lm)
        self.all_list1()

    def lend1(self):
        Maga1 = input("• Enter the Magazine number: ").upper()
        copy1 = int(input("• Enter number of copies need to lend: "))
        y1 = list(lm for lm in self.magazine_L if lm.magazine_number == Maga1)
        for lm in y1:
            lm.number_of_copies -= copy1
        self.all_list1()

    def give1(self):
        Maga = input("• Enter the Magazine number: ").upper()
        copy1 = int(input("• Enter number of copies need to Update: "))
        y1 = list(lm for lm in self.magazine_L if lm.magazine_number == Maga)
        for lm in y1:
            lm.number_of_copies += copy1
        self.all_list1()

    def zero1(self):
        y1 = [lm for lm in self.magazine_L if lm.number_of_copies == 0]
        for lm in y1:
            print(
                f"Magazine Number:{lm.magazine_number}, Title:{lm.title}, Print:{lm.color_or_black_and_white_print}, Subject:{lm.subject}, Rental price per day:{lm.rental_price}, Number of copies:{lm.number_of_copies} ")

    def available1(self):
        y1 = [lm for lm in self.magazine_L if lm.number_of_copies > 0]
        for lm in y1:
            print(
                f"Magazine Number:{lm.magazine_number}, Title:{lm.title}, Print:{lm.color_or_black_and_white_print}, Subject:{lm.subject}, Rental price per day:{lm.rental_price}, Number of copies:{lm.number_of_copies} ")

    def continue_p1(self):
        print("*****************************************")
        choicem = input("-> Do yo Need to Continue (Y/N)").upper()
        if choicem == "Y":
            Magazines.intro1()
            menu1()
        else:
            quit()


def menu2():
    try:
        select2 = int(input("• Select what  you want to do?"))
    except ValueError:
        print("An exception occurred")
    while select2 < 0 or select2 > 9:
        MainMenu.input1()
        try:
            select2 = int(input("• Select what  you want to do?"))
        except ValueError:
            print("An exception occurred")

    if select2 == 1:
        magazine_list1().all_list1()
        print("*****************************************")
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

    def append2(self):

        educational_1 = educational_DVD(dvd_number="10", title='Birth of the Solar System', subject='Astronomy',
                                        rental_price_per_day=2.50, number_of_copies=10)
        self.educational_DVD_L.append(educational_1)
        educational_2 = educational_DVD(dvd_number="11", title='Pythagoras Theorem', subject='Math',
                                        rental_price_per_day=1.00, number_of_copies=0)
        self.educational_DVD_L.append(educational_2)

    def all_list2(self):
        for ld in self.educational_DVD_L:
            print(
                f"DVD Number:{ld.dvd_number}, Title:{ld.title}, Subject:{ld.subject}, Rental price per day:{ld.rental_price_per_day}, Number of copies:{ld.number_of_copies} ")

    def add2(self):
        dvd_number1 = input("• DVD Number: ").strip().upper()
        title2 = input("• Title of the DVD: ").strip().capitalize()
        subject2 = input("• Subject Name: ").strip().capitalize()
        rental_price_per_day2 = float(input("• Rental price per day: "))
        number_of_copies2 = int(input("• Number of Copies: "))
        educational_DVD1 = educational_DVD(dvd_number=dvd_number1, title=title2, subject=subject2,
                                           rental_price_per_day=rental_price_per_day2,
                                           number_of_copies=number_of_copies2)
        self.educational_DVD_L.append(educational_DVD1)

    def remove2(self):
        delete2 = input("• Enter the Magazine number: ").upper()
        y2 = [ld for ld in self.educational_DVD_L if ld.dvd_number == delete2]
        for ld in y2:
            self.educational_DVD_L.remove(ld)
        self.all_list2()

    def lend2(self):
        Dvd1 = input("• Enter the DVD number: ").upper()
        copy2 = int(input("• Enter number of copies need to lend: "))
        y2 = list(ld for ld in self.educational_DVD_L if ld.dvd_number == Dvd1)
        for ld in y2:
            ld.number_of_copies -= copy2
        self.all_list2()

    def give2(self):
        Dvd1 = input("• Enter the DVD number: ").upper()
        copy2 = int(input("• Enter number of copies need to Update: "))
        y2 = list(ld for ld in self.educational_DVD_L if ld.dvd_number == Dvd1)
        for ld in y2:
            ld.number_of_copies += copy2
        self.all_list2()

    def zero2(self):
        y2 = [ld for ld in self.educational_DVD_L if ld.number_of_copies == 0]
        for ld in y2:
            print(
                f"DVD Number:{ld.dvd_number}, Title:{ld.title}, Subject:{ld.subject}, Rental price per day:{ld.rental_price_per_day}, Number of copies:{ld.number_of_copies} ")

    def available2(self):
        y2 = [ld for ld in self.educational_DVD_L if ld.number_of_copies > 0]
        for ld in y2:
            print(
                f"DVD Number:{ld.dvd_number}, Title:{ld.title}, Subject:{ld.subject}, Rental price per day:{ld.rental_price_per_day}, Number of copies:{ld.number_of_copies} ")

    def continue_p2(self):
        print("*****************************************")
        choicem = input("-> Do yo Need to Continue (Y/N)").upper()
        if choicem == "Y":
            educational_DVD.intro2()
            menu1()
        else:
            quit()


def menu3():
    try:
        select2 = int(input("• Select what  you want to do?"))
    except ValueError:
        print("An exception occurred")
    while select2 < 0 or select2 > 9:
        MainMenu.input1()
        try:
            select2 = int(input("•Select what  you want to do?"))
        except ValueError:
            print("An exception occurred")

    if select2 == 1:
        educational_DVD1().all_list2()
        print("*****************************************")
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

    def append3(self):

        lecture_1 = lecture_CDs(cd_number="21", title='Basics of Western Music', subject='Music',
                                rental_price=1.50, number_of_copies=0)
        self.lecture_CD_L.append(lecture_1)
        lecture_2 = lecture_CDs(cd_number="22", title='Japanese Language', subject='Foreign Languages',
                                rental_price=2.00, number_of_copies=3)
        self.lecture_CD_L.append(lecture_2)

    def all_list3(self):
        for lc in self.lecture_CD_L:
            print(
                f"Lecture CD Number:{lc.cd_number}, Title:{lc.title}, Subject:{lc.subject}, Rental price per day:{lc.rental_price}, Number of copies:{lc.number_of_copies} ")

    def add3(self):
        cd_number1 = input("• Lecture CD Number: ").strip().upper()
        title3 = input("• Title of the Lecture CD: ").strip().capitalize()
        subject3 = input("• Subject Name: ").strip().capitalize()
        rental_price_per_day3 = float(input("• Rental price per day: "))
        number_of_copies3 = int(input("• Number of Copies: "))
        lecture_CD1 = lecture_CDs(cd_number=cd_number1, title=title3, subject=subject3,
                                  rental_price=rental_price_per_day3, number_of_copies=number_of_copies3)
        self.lecture_CD_L.append(lecture_CD1)

    def remove3(self):
        delete3 = input("• Enter the Magazine number: ").upper()
        y3 = [lc for lc in self.lecture_CD_L if lc.cd_number == delete3]
        for lc in y3:
            self.lecture_CD_L.remove(lc)
        self.all_list3()

    def lend3(self):
        Cd1 = input("• Enter the Lecture CD number: ").upper()
        copy3 = int(input("• Enter number of copies need to lend: "))
        y3 = list(lc for lc in self.lecture_CD_L if lc.cd_number == Cd1)
        for lc in y3:
            lc.number_of_copies -= copy3
        self.all_list3()

    def give3(self):
        Cd1 = input("• Enter the DVD number: ").upper()
        copy3 = int(input("• Enter number of copies need to Update: "))
        y3 = list(lc for lc in self.lecture_CD_L if lc.cd_number == Cd1)
        for lc in y3:
            lc.number_of_copies += copy3
        self.all_list3()

    def zero3(self):
        y3 = [lc for lc in self.lecture_CD_L if lc.number_of_copies == 0]
        for lc in y3:
            print(
                f"Lecture CD Number:{lc.cd_number}, Title:{lc.title}, Subject:{lc.subject}, Rental price per day:{lc.rental_price}, Number of copies:{lc.number_of_copies} ")

    def available3(self):
        y2 = [lc for lc in self.lecture_CD_L if lc.number_of_copies > 0]
        for lc in y2:
            print(
                f"Lecture CD Number:{lc.cd_number}, Title:{lc.title}, Subject:{lc.subject}, Rental price per day:{lc.rental_price}, Number of copies:{lc.number_of_copies}")

    def continue_p3(self):
        print("*****************************************")
        choicem = input("-> Do yo Need to Continue (Y/N)").upper()
        if choicem == "Y":
            educational_DVD.intro2()
            menu1()
        else:
            print("\n | Thank You! 🙏 |")


def menu4():
    try:
        select2 = int(input("• Select what  you want to do?"))
    except ValueError:
        print("An exception occurred")
    while select2 < 0 or select2 > 9:
        MainMenu.input1()
        try:
            select2 = int(input("• Select what  you want to do?"))
        except ValueError:
            print("An exception occurred")

    if select2 == 1:
        lecture_CDs1().all_list3()
        print("*****************************************")
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


# ---------------------------
# Initializing the programme.
# ---------------------------

MainMenu.input1()
MainMenu.menue()
