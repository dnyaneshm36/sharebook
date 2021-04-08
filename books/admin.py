from django.contrib import admin

# Register your models here.
from .models import Book
class Bookadmin(admin.ModelAdmin):
    list_display= [
            'id',
            'name',
            'icon',
            'description',
            'book',
        ]
    # class Meta:
    #     model = Myfrienddetail

admin.site.register(Book,Bookadmin)