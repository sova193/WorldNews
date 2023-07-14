from django.apps import AppConfig
import redis

class SimpleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpleapp'

    def ready(self):
        from .signals import send_notifications, notify_about_new_post

red = redis.Redis(
    host='redis-13131.c256.us-east-1-2.ec2.cloud.redislabs.com',
    port=13131,
    password='C5MkgzqO3h4UJB9JpQjeuRvM2CXBpQ7r',
)