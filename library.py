
#---------08/04/2026--------------

#-------Project---------------
"""Library Management"""

#database
books = []
issued_books = []

def add_book():
    name = input('Enter the Book Name:')
    books.append(name)
    print(name, ' is added')

def show_books():
    if len(books) == 0:
         print('No Books Avaliable')
    else:
        print('Avaliable Books')
        for book in books:
            print(book)

        print('-----------') 


def issue_book():
    if len(books) == 0:
         print('No Books Avaliable')
    else:
        show_books()
        name = input('Enter the book name:')
        if name in books:
            books.remove(name)
            issued_books.append(name)
        else:
            print(name, ' is not avaliable')
def return_book():
    name = input('Enter book name you want to return:')
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name, ' book returned')
    else:
        print(name, ' book was not issued')    


def library():
    while True:       #element True hoga to loop infite woork karega isliye while ture ka use hua haiii
        print('\n menu')
        print('1.Add Book')
        print('2. Show Books')
        print('3.Issue Books')
        print('4.Return Book')
        print('5.Exit')

        choice = int(input('Enter your choice:'))

        if choice == 1:
           add_book()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()  
        elif choice == 5:
            print('Thank You')
            break
        else:
            print('Invalid choice')


library()
