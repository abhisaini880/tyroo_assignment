from django.contrib import admin
from rule_based_engine.models import camp_rules,camp_data
# Register your models here.

admin.site.register(camp_rules)
admin.site.register(camp_data)
