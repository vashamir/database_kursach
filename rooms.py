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

def rooms(start, number_of_rows):
    return [{
        'id': x + 1,
        'number': random.randint(1, 999999),
        'type': random.choices(roles)[0],
        'price': random.randint(1000, 20000)
              } for x in range(start, start + number_of_rows, 1)
            ]
    

pd.DataFrame(rooms(0, 100001)).to_csv('rooms.csv', index=False)