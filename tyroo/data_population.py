''' Script to populate the table with random user activity data'''

# setting up the django environment
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'tyroo.settings')
django.setup()

# Importing required libraries
from rule_based_engine.models import camp_data
import random
import datetime
import time

campaign_choice = ['zomato','flipkart','amazon','swiggy','grofer']
metric_choice = ['clicks','spends','impressions','installs']

def populate(N):
    ''' Iterate for N times and inserts the random data into table '''
    
    for i in range(N):
        now = datetime.datetime.now()
        random_time = now + datetime.timedelta(seconds=i)
        
        random_campaign = random.choice(campaign_choice)
        random_metric = random.choice(metric_choice)
        random_value = random.randint(1,10000)
        random_datetime = random_time.strftime("%Y-%m-%d %H:%M:%S")
        
        camp_data.objects.get_or_create(campaign=random_campaign, metric=random_metric, value=random_value, created_time=random_datetime)
        time.sleep(5)


if __name__=='__main__':
    print('populating with data')
    populate(10)
    print('completed')