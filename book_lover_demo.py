from booklovers import booklover

person = booklover.BookLover("Jon", "jonbrandin@gmail.com", "fiction")

person.add_book("The Tempest", 4)

print(person.num_books_read())