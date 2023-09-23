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

def guests(start, number_of_rows):
    return [{
        'id': x + 1,
        'name_id': person.first_name() + ' ' + person.last_name() 
              } for x in range(start, start + number_of_rows, 1)
            ]
    

pd.DataFrame(guests(0, 5000)).to_csv('guests.csv', index=False)