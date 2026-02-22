from django.urls import path
from .views import HomeView, submit_contact_message

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/submit/', submit_contact_message, name='submit_contact_message'),
]
