#!/usr/bin/env python3
from typing import List, Any

import book

python_book = book.Book('Practical Programming', ['Campbell', 'Gries', 'Montojo'], 'Pragmatic Bookshelf', '978-1-6805026-8-8', 25.0)
print(python_book.title)
print(python_book.authors)
print(python_book.publisher)
print(python_book.ISBN)
print(python_book.price)
print()
print(python_book)

python_book_1 = book.Book('Practical Programming',['Campbell', 'Gries', 'Montojo'],'Pragmatic Bookshelf','978-1-6805026-8-8',25.0)
python_book_2 = book.Book('Practical Programming',['Campbell', 'Gries', 'Montojo'],'Pragmatic Bookshelf','978-1-6805026-8-8',25.0)

print(python_book_1 == python_book_2)
print(python_book_1 == python_book_1)
print(python_book_2 == python_book_2)

print(python_book.__dict__)