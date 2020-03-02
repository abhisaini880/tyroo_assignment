from django.urls import re_path,path
from rule_based_engine import views

app_name = 'rule_based_engine'

urlpatterns = [
    re_path(r'^$', views.rules_display, name='rule_display'),
    re_path(r'^rule_form', views.rules_add,name='rule_add'),
    re_path(r'^rule_update/(?P<id>\d+)/$', views.rule_update, name='rule_update'),
]