
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('thread/<int:thread_id>',views.thread,name='thread'),
    path('delete_reply/<int:reply_id>/', views.delete_reply, name='delete_reply'),
]
