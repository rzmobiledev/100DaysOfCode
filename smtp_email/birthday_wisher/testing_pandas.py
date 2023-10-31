import pandas as pd
import datetime as dt
import random

data = pd.read_csv("birthdays.csv")
date = dt.datetime.now()
date_tuple = (date.month, date.day)

birthday_dict = {(row['month'], row['day']): row for (index, row) in data.iterrows()}

print(random.randint(1,3))