import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animal_blog.settings')

app = Celery('animal_blog')

app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)
app.autodiscover_tasks()
