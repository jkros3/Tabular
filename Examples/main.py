from tabular import table

book1 = ["Brave New World", "Aldous Huxley", 1932]
book2 = ["The Lord of the Rings", "J.R.R. Tolkien", 1954]
book3 = ["The Alchemist", "Paulo Coelho", 1988]
book4 = ["The Chronicles of Narnia", "C.S. Lewis", 1950]
book5 = ["Crime and Punishment", "Fyodor Dostoevsky", 1866]

book_list = []

book_list.append(book1)
book_list.append(book2)
book_list.append(book3)
book_list.append(book4)
book_list.append(book5)

header = ["Title", "Author", "Publication Year"]
table1 = table(header)
table1.center_alignment = True

for book in book_list:
    table1.new_row(book)

table1.display_table()