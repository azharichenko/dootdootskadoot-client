from django.urls import path
from manager import views

urlpatterns = [
    path('sms', views.receive_from_twilio),
    path('init', views.initiate_contact),
    path('call', views.start_call),
    path('response', views.call_response)
]