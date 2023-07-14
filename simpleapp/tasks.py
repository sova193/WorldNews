from celery import shared_task
import datetime
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import NewsPortal, NewsPortalCategory, NewsCategory


@shared_task
def week_send_task():
    #  Your job processing logic here...
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    news = NewsPortal.objects.filter(sort_date_of_publication__gte=last_week)
    categories = set(news.values_list('news_category__article_title', flat=True))
    subscribers = set(NewsCategory.objects.filter(article_title__in=categories).values_list('subscribers__email',
                                                                                            flat=True))
    html_context = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'news': news,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()

@shared_task
def send_email_task(pk):
    new = NewsPortal.objects.get(pk=pk)
    categories = new.news_category.all()
    title = new.article_title
    subscribers_emails = []
    for category in categories:
        subscribers_users = category.subscribers.all()
        for subscriber_user in subscribers_users:
            subscribers_emails.append(subscriber_user.email)
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': new.preview,
            'link': f'{settings.SITE_URL}/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()