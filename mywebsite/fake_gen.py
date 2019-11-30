import  os, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

import django
from faker import Faker, Factory
django.setup()

from myapp1.models import Publisher, Author, Book

fakegen = Faker()

def populate_Publisher():
    name = fakegen.name()
    fadr = fakegen.address()
    ad1 = fadr.split('\n')
    address = ad1[0]
    provnc = ad1[1]
    city = fakegen.city()
    country = fakegen.country()
    web = fakegen.url()

    p = Publisher.objects.get_or_create(
        name = name,
        address = address,
        city = city,
        state_province = provnc,
        country = country,
        website = web
    )[0]
    p.save()
    return p

def populate_Author():
    fn = fakegen.first_name()
    ln = fakegen.last_name()
    email = fakegen.email()

    a = Author.objects.get_or_create(
        first_name = fn,
        last_name = ln,
        email = email
    )[0]
    a.save()
    return a

def populate_Book():
    title = fakegen.company()
    date = fakegen.date()
    p = populate_Publisher()
    a = populate_Author()

    b = Book.objects.get_or_create(
        title=title,
        publisher = p,
        authors = a,
        publication_date = date
    )[0]
    b.save()
    print(b.title, b.authors, b.publisher, b.publication_date)
    return b


def populate_All(n=10):
    for i in range(n):
        print(f"Populating {i} ", end="")
        b = populate_Book()
        print("... Done")


if __name__ == "__main__":
    print("POPULATING DATA!!!")
    populate_All(25)
    print("COMPLETED POPULATING!!!!!!!!!!!")