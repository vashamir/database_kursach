from mimesis import Person
from mimesis import Text
from faker import Faker
import pandas as pd
import random
import json


person = Person('ru')
rand_text = Text()
faker = Faker()


roles = ['econom', 'standard', 'luxe']

def booking(start, number_of_rows):
    return [{
        'id': x + 1,
        'number': random.randint(1, 100000),
        'date_booking': faker.date(),
        'date_start': faker.date(),
        'date_end': faker.date(),
        'name': person.first_name() + ' ' + person.last_name()
              } for x in range(start, start + number_of_rows, 1)
            ]
    

pd.DataFrame(booking(0, 2000)).to_csv('booking.csv', index=False)