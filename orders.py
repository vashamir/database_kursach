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

def orders(start, number_of_rows):
    return [{
        'id': x + 1,
        'service_id': random.randint(1,10),
        'residence_id': random.randint(1,5000),
        'date': faker.date() 
              } for x in range(start, start + number_of_rows, 1)
            ]
    

pd.DataFrame(orders(0, 2000)).to_csv('orders.csv', index=False)