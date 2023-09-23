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

def residence(start, number_of_rows):
    return [{
        'id': x + 1,
        'guest_id': random.randint(1,5000),
        'date_start': faker.date(),
        'date_end': faker.date(),
        'room_id': random.randint(1,100001) 
              } for x in range(start, start + number_of_rows, 1)
            ]
    

pd.DataFrame(residence(0, 5000)).to_csv('residence.csv', index=False)