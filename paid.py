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

def paid(start, number_of_rows):
    return [{
        'id': x + 1,
        'booking_id': random.randint(1, 2000)
              } for x in range(start, start + number_of_rows, 1)
            ]
    

pd.DataFrame(paid(0, 1000)).to_csv('paid.csv', index=False)