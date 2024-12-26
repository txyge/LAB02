from django.urls import path
from .views import home, add_client, client_detail
urlpatterns =[
    path('', home, name='home'),
    path('add/', add_client, name='add_client'),
    path('client/<int:client_id>/', client_detail, name='client_detail'),
]