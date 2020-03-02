from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms
from rule_based_engine.models import camp_rules

# Home page view containing details about project.
def home(request):
    return render(request, 'rbe/index.html')

# Login view for admin user
def user_login(request):
    return render(request, 'rbe/login.html')

# Logout view for admin user
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# Rules add view
@login_required
def rules_add(request):
    form = forms.create_rule_form()

    if request.method == 'POST':
        form = forms.create_rule_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return rules_display(request)
            
    return render(request, 'rbe/rule_form.html',{'form':form})


# Rules display view
@login_required
def rules_display(request):
    rules_list = camp_rules.objects.order_by('id')
    rule_dict = {'rule_record':rules_list}
    return render(request, 'rbe/rules_display.html', context=rule_dict)


# Rules updation view

@login_required
def rule_update(request, id):
    rule = get_object_or_404(camp_rules, id=id)

    if request.method == 'POST':
        form = forms.create_rule_form(request.POST, instance=rule)
        if form.is_valid():
            rule = form.save(commit=False)
            rule.save()
            return HttpResponseRedirect(reverse('rule_based_engine:rule_display'))
    else:
        form = forms.create_rule_form(instance=rule)

    return render(request,'rbe/rule_form.html',context={'form':form}) 

# View for User authentication

def user_auth(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('rules_display')
            else:
                return HttpResponse('account not active')
        else:
            messages.warning(request,'username or password not correct')
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request,'rbe/login.html')

