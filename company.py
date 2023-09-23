from mimesis import Person
from mimesis import Text
from mimesis import Finance
from faker import Faker
import pandas as pd
import random
import json


finance = Finance('ru')
person = Person('ru')
rand_text = Text()
faker = Faker()


roles = ['econom', 'standard', 'luxe']

def company(start, number_of_rows):
    return [{
        'id': x + 1,
        'name': finance.company()
              } for x in range(start, start + number_of_rows, 1)
            ]
    

pd.DataFrame(company(0, 10)).to_csv('company.csv', index=False)