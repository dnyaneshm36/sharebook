
from . import views

from django.urls import path,include

urlpatterns = [
    # path('books/', include('books.urls')),
    path("", views.Bookshows,name="bookshow"),
]
