import string
from django.utils.crypto import get_random_string
from celery import shared_task
from main.models import Customer



@shared_task
def create_multiple_customer(number_of_customer):
    for cust in range(number_of_customer):
        name="customer{}".format(get_random_string(5, string.ascii_letters))
        email="{}@mysite.com".format(name)
        Customer.objects.create(name=name, email=email)
    return '{} random customer created successfully'.format(number_of_customer)