from django.urls import path

from . import views

urlpatterns = [
    path('', views.other, name="index"),
    path('book', views.book, name="book"),
    path('whale', views.index, name="other"),
    path('book/<int:book_id>', views.book_by_id, name="book_by_id")
]