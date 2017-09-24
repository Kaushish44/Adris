from django.conf.urls import url
from . import views

app_name = 'sales'

urlpatterns = [
    #user login
    url(r'^$',views.login_user, name='login'),
    #Main after login window
    url(r'^index/$',views.IndexView, name='index'),
    #Adding customer to db
    url(r'^customer/add$',views.CustomerView, name='customer_add'),
    #Customer Add form
    url(r'^customer/$',views.CustomerForm, name='customer'),
    #Orders Window
    url(r'^orders/$',views.OrdersView, name='orders'),
    #Getting Item Price from DB
    url(r'^orders/submitBill/$', views.submitBill, name='submitBill'),
    #url(r'^customer/autocomplete_cus/$', views.autocomplete_cus, name = 'ac_cus'),
]
