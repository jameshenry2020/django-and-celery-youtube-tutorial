from django.urls import path
from main.views import home_page, display_customers



urlpatterns = [
    path('', home_page, name="scraper"),
    path('customers-list/', display_customers, name="customers"),
    
]
