from django.urls import path

from .views import greetings,list_item, detail_item

urlpatterns = [
    path('',greetings, name = 'greetings'),
    path('shop/<int:id>/detail_item', detail_item, name = 'detail_item'),
    path('shop/', list_item, name = 'items')
]