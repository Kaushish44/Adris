from django.conf.urls import url
from . import views

app_name = 'ragnal'

urlpatterns = [
    url(r'^$',views.Index ,name='index'),
    #city
    url(r'^city/$', views.city, name='city'),
    #autocomplete
    url(r'^autocomplete/$', views.autocomplete, name='auto')
    #city    
#     url(r'^city/$',views.IndexView.as_view(),name='city'),
]
