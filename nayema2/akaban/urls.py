from django.urls import path
from . import views

urlpatterns = [
    path('', views.an),
    path('home/', views.An_Home, name='home'), 
    path('account/', views.An_Account, name='account'), 
    path('offers/', views.An_Offers, name='offers'), 
    #Categories:
    path('bs/', views.Best_sellers, name='bestsellers'), 
    
    

]
