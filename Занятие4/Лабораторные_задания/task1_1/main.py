import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"#### (?P<position>\d\d+)-(?P<book>.*?)-(?P<book_url>^(https?:\/\/)?)
m.groupdict(BOOK_REGEX)

def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '_

    r'#### (?P<position>\w+)\. \[(?P<book>.*?)]\((?P<book_url>.*?)\) by (?P<author>.*?) \((?P<recommended>.*?)\%.*(?P<cover_url>https.*?)\)'