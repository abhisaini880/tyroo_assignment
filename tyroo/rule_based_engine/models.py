from django.db import models
from datetime import datetime

rule_choices = (
    ('`eCPM` >= $5.00 AND `Impressions` >= 1000000','`eCPM` >= $5.00 AND `Impressions` >= 1000000'),
    ('`Spend` >= $1000.00 AND `eCPC` <=  $0.20','`Spend` >= $1000.00 AND `eCPC` <=  $0.20'),
    ('`Clicks` >= 50000 AND `Installs` <= 100','`Clicks` >= 50000 AND `Installs` <= 100'),
    ('`eCPI` >= $2.00 AND `Installs` >= 100','`eCPI` >= $2.00 AND `Installs` >= 100'),
)

campaign = (
    ('zomato','zomato'),
    ('flipkart','flipkart'),
    ('amazon','amazon'),
    ('swiggy','swiggy'),
    ('grofer','grofer'),
)

schedule_time_choices = (
    ('every 15 min','every 15 min'),
    ('every hour','every hour'),
    ('every day','every day'),
)

class camp_rules(models.Model):
    rule_name = models.CharField(max_length=15)
    campaign = models.CharField(max_length=20, choices=campaign)
    condition = models.CharField(max_length=50, choices=rule_choices)
    action = models.CharField(max_length=10, default='notify')
    status = models.BooleanField()
    schedule_time = models.CharField(max_length=20,choices=schedule_time_choices)



class camp_data(models.Model):
    campaign = models.CharField(max_length=20)
    metric = models.CharField(max_length=15)
    value = models.DecimalField(max_digits=15,decimal_places=2)
    created_time = models.DateTimeField()