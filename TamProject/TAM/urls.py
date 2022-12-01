from django.urls import path
from . import views

app_name = 'TAM'

urlpatterns = [
    path('', views.ContactList, name='home'),
    path('Contact/<str:pk>/', views.ContactDetials, name='ContactD'),
    path('create_contact/', views.createContact, name='create_contact'),
    path('update_contact/<str:pk>/', views.updateContact, name='update_contact'),
    path('delete_contact/<str:pk>/', views.updateContact, name='delete_contact'),

]
