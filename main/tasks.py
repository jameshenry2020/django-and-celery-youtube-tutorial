import string
import requests
import lxml
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List
from django.utils.crypto import get_random_string
from celery import shared_task
from main.models import Customer, News
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
    
@shared_task(serializer='json')
def send_article_to_db(articles_list):
    count = 0
    for article in articles_list:
        try:
            News.objects.create(
                title = article['title'],
                link = article['link'],
                published = article['published'],
            )
            count +=1
        except Exception as e:
            print(e)
            print('task failed an error occured')


@shared_task(name='scrape_hacker_new_rss_feed')
def scrape_hacker_new_rss_feed():
    articles_list=[]
    try:
        res=requests.get('https://news.ycombinator.com/rss')
        soup=BeautifulSoup(res.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published_date = a.find('pubDate').text
            published = datetime.strptime(published_date, '%a, %d %b %Y %H:%M:%S %z')

            article={
                'title': title,
                'link': link,
                'published': published,
            }
            articles_list.append(article)
        return send_article_to_db.delay(articles_list)
    except Exception as e:
        print(e)
        print('task failed an error occured')
