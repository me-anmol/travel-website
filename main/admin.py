from django.contrib import admin
from .models import destinations, messages, news, subscribers

# Register your models here.

admin.site.register(destinations)
admin.site.register(messages)
admin.site.register(news)
admin.site.register(subscribers)
