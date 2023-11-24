from django.contrib import admin
from server.service.tags.models import *

admin.site.register(TopicTag)
admin.site.register(UserTag)
admin.site.register(WorkTag)
admin.site.register(DefaultTopicTag)
admin.site.register(DefaultUserTag)
admin.site.register(DefaultWorkTag)
