import os
import django
import csv
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '11-HYUNLANEIGE-BACKEND.settings')
django.setup()

from product.models import (
    MainCategory,
    TypeCategory,
    WorryCategory,
    LineCategory,
    Product,
    Image,
    Video,
    Description,
    Precaution,
    Size,
    Ingredient,
    Tag,
    Review,
)



CSV_PATH = "./product.csv"

with open(CSV_PATH_PROUDCT) as in_file:
    data_render = csv.reader(in_file)
    for row in data_render:
        print(row)
        # row[0] : MainCategory
        # try: 
        #     MainCategory.objects.get(name = row[1])
        # except:
        #     MainCategory.objects.create(name = row[1])

        #row[2] : SubCategory
        #try:
         #   SubCategory.objects.get(name = row[1])

