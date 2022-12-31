from django.contrib import admin
from .models import Post 
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['title', 'date']	
    search_fields = ['title','date']

admin.site.register(Post, PostAdmin)
