# TODO Найдите количество книг, которое можно разместить на дискете
FLOPPY_VOLUME = 1.44  # MBytes
PAGES_IN_BOOK = 100
STRINGS_IN_PAGE = 50
CHARS_IN_STRING = 25
CHAR_SIZE = 4  # Bytes

floppy_volume_in_bytes = FLOPPY_VOLUME * 1024 ** 2
book_size_in_bytes = PAGES_IN_BOOK * STRINGS_IN_PAGE * CHARS_IN_STRING * CHAR_SIZE
books_in_floppy = int(floppy_volume_in_bytes) // book_size_in_bytes

print("Количество книг, помещающихся на дискету:", books_in_floppy)