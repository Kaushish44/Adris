from django.shortcuts import render
from django.contrib.auth import authenticate, login
from . import forms
from django.urls.base import reverse_lazy
from .models import customers, menu, orders
from django.http.response import JsonResponse

#user login validations
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'sales/index.html' , {'user':user} )
            else:
                return render(request, 'sales/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'sales/login.html', {'error_message': 'Invalid login'})
    return render(request, 'sales/login.html')

#Adding customer data in the database            
def CustomerView(request):
    if not request.user.is_authenticated():
        return render(request, 'sales/login.html')
    else:
        form = forms.CustomerForm(request.POST)
        if form.is_valid():
            try:
                cus = form.save(commit=False)
                cus.user = request.user
                cus.save()
                form = forms.CustomerForm()# Reseting the form after completion
                context = { 'message' : 'Customer details added successfully', "form": form}
                return render(request, 'sales/customer_form.html', context)
            except:
                form = forms.CustomerForm()
                context = { 'message' : 'Customer already added', "form": form}
                return render(request, 'sales/customer_form.html', context)
        context = {
            "form": form,
        }
        return render(request, 'sales/customer_form.html', context)
    
#Initial form display    
def CustomerForm(request):
    form = forms.CustomerForm()
    context = {
            "form": form,
        }
    return render(request, 'sales/customer_form.html', context)

#Main Login window
def IndexView(request):
    if request.user.is_authenticated():
        return render(request,'sales/index.html')
    
#Orders window
def OrdersView(request):
    m = menu.objects.all().order_by('description')
    context = {'menu':m}
    return render(request,'sales/orders.html', context)

#Submittng the Bill in database
def submitBill(request):
    desc=[]
    if request.is_ajax():
        billAmount=request.GET.get('billAmount',None)
        ids=request.GET.get('ids',None)
    
    cus = customers.objects.get(id=8).id
    order_entry = orders.objects.create(customer_id = cus, food_ordered = ids , bill=billAmount, owner=request.user.username)
    order_entry.save()
    idos = 'done'
    data={'id':idos}
    return JsonResponse(data)
# def autocomplete_cus(request):
#     if request.is_ajax():
#         search_qs = customers.objects.filter(Phone__startswith=request.GET.get('q',None))
#         results = []
#         for r in search_qs:
#             results.append(r.name)
#         data = {'results':results}
#         return JsonResponse(data)