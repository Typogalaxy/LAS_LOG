from django.urls import path
from . import views

urlpatterns = [
    path('edit_topic_tag/(<topic_id>)/', views.edit_topic_tag, name='edit_topic_tag'),
    path('edit_user_tag/(<user_id>)/', views.edit_user_tag, name='edit_user_tag'),
    path('edit_work_tag/(<work_id>)/', views.edit_work_tag, name='edit_work_tag'),
]
