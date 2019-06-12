import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'firstproject.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec =AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

def populate_users(N=10):
    for  entry in range(N):
        fake_name = fakegen.name().split()[0]
        fake_surname = fakegen.name().split()[1]
        fake_email = fakegen.email()

        add_user = User.objects.get_or_create(first_name=fake_name, last_name=fake_surname, email=fake_email)[0]


if __name__ == "__main__":
    print("populating script")
    # populate(20)
    populate_users(20)
    print("populating complete")


