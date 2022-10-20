
from django.urls import path,include
from hospitalapp.views import about,index,booking,department,contact,doctors

urlpatterns = [

    path('',index,name='home'),
    path('about/',about,name='about'),
    path('booking/',booking,name='booking'),
    path('doctors/',doctors,name='doctors'),
    path('contact/',contact,name='contact'),
    path('department/',department,name='department'),
    
]