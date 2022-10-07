from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from main.models import Post
from django.template.loader import render_to_string
from .tasks import send_background_email


@receiver(post_save, sender=Post)
def send_notification_email(sender, instance, **kwargs):
    email_template=render_to_string('email_template.html', {'url':instance.get_absolute_url, 'title':instance.title})
    subject="Notification for a new post"
    email_from=settings.DEFAULT_FROM_EMAIL
    recipient_list=[ u.email for u in User.objects.filter(is_staff=False) ]
    send_background_email.delay(
        subject=subject,
        message=email_template,
        email_sender=email_from, 
        recievers_list=recipient_list
        )
    
