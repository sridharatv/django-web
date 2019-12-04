import  os, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

import django
from faker import Faker, Factory
django.setup()

from cbvs.models import Book, Library

fakegen = Faker()

def populate_Book(n=1):
    for i in range(n):
        title = fakegen.company()
        author = fakegen.name()
        publisher = fakegen.name()
        year = random.randint(1900,2019)
        pages = random.randint(500,2500)

        b = Book.objects.get_or_create(
            title=title,
            author = author,
            publisher = publisher,
            year = year,
            pages = pages
        )[0]
        b.save()
    return b


def populate_Library():
    name = fakegen.company()
    b = populate_Book()
    location = fakegen.address()

    l = Library.objects.get_or_create(
        name = name,
        location = location
    )[0]
    l.save()


def populate_All(n=10):
    for i in range(n):
        print(f"Populating {i} ", end="")
        b = populate_Library()
        print("... Done")


if __name__ == "__main__":
    print("POPULATING DATA!!!")
    #populate_Book(10)
    populate_All(10)
    print("COMPLETED POPULATING!!!!!!!!!!!")

