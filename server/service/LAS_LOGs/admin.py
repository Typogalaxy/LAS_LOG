from django.contrib import admin
from server.service.LAS_LOGs.models import Topic, Entry, Work

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Work)