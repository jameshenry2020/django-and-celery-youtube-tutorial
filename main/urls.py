from django.urls import path
from main.views import generate_random_customers, display_customers, post_read_view



urlpatterns = [
    path('', generate_random_customers, name="create-customer"),
    path('customers-list/', display_customers, name="customers"),
    path('post-detail/<slug:slug>/', post_read_view, name='post_detail')
]
