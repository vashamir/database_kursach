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

def turbooking(start, number_of_rows):
    return [{
        'id': x + 1,
        'number': random.randint(1, 100000),
        'company_id': random.randint(1, 10),
        'food_type': random.randint(1, 3),
        'date_booking': faker.date(),
        'date_start': faker.date(),
        'date_end': faker.date()
              } for x in range(start, start + number_of_rows, 1)
            ]
    

pd.DataFrame(turbooking(5000, 7000)).to_csv('turbooking.csv', index=False)