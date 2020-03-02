from django import forms
from rule_based_engine.models import  camp_rules

class create_rule_form(forms.ModelForm):
    class Meta:
        model = camp_rules
        fields = '__all__'