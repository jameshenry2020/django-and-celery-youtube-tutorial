import string
from typing import List
from django.utils.crypto import get_random_string
from celery import shared_task
from main.models import Customer
from django.core.mail import EmailMessage



@shared_task
def create_multiple_customer(number_of_customer):
    for cust in range(number_of_customer):
        name="customer{}".format(get_random_string(5, string.ascii_letters))
        email="{}@mysite.com".format(name)
        Customer.objects.create(name=name, email=email)
    return '{} random customer created successfully'.format(number_of_customer)


@shared_task
def send_background_email(subject, message, email_sender, recievers_list):
    email_message=EmailMessage(
        subject=subject,
        body=message,
        from_email=email_sender,
        to=recievers_list
    )
    email_message.content_subtype='html'
    email_message.send()
    return "notification email sent successful"
    
